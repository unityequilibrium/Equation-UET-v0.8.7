"""
Hybrid MOND-UET Galaxy Rotation Test (Version 5: Multi-Component Halo)
====================================================================
Formula: g_final = (g_MOND * max(1, (rho/rho_ref)^kappa)) + (lambda_h * g_Newton)
"""

import numpy as np
import sys
import os

# CONSTANTS
c = 2.998e8
H0 = 2.2e-18
BETA_CI = 0.18
a0_SI = BETA_CI * c * H0
kpc_to_m = 3.086e19
G_astro = 4.302e-6
a0_astro = a0_SI * kpc_to_m / 1e6


def mu_simple(x):
    return x / (1 + x)


def mond_acceleration(g_newton, a0=a0_astro):
    if g_newton <= 0:
        return 0
    g = g_newton
    for _ in range(10):
        x = g / a0
        mu = mu_simple(x)
        g_new = g_newton / mu
        if abs(g_new - g) < 1e-5 * g:
            break
        g = g_new
    return g


def load_galaxies():
    try:
        sys.path.insert(0, os.path.dirname(__file__))
        from test_175_galaxies import SPARC_GALAXIES

        return [
            {
                "name": g[0],
                "R_max": g[1],
                "V_obs": g[2],
                "M_disk": g[3],
                "R_disk": g[4],
                "type": g[5],
            }
            for g in SPARC_GALAXIES
        ]
    except:
        return []


def optimize_hybrid_parameters():
    galaxies = load_galaxies()
    if not galaxies:
        return
    best_res = {"kappa": 0, "lambda_h": 0, "rho_ref": 0, "pass": 0, "err": 100}

    # Final Granular Parameters Search
    kappas = [-0.7, -0.65, -0.6, -0.55]
    lambda_hs = [0.6, 0.7, 0.8, 0.9, 1.0, 1.1]
    rho_refs = [2.0e7, 2.5e7, 3.0e7, 3.5e7, 4.0e7]

    print("\nStarting Final Granular Sweep...")
    print(f"{'KAPPA':<6} {'LAM_H':<6} {'RHO_REF':<10} {'PASS%':<8}")

    for kappa in kappas:
        for lam_h in lambda_hs:
            for rho_ref in rho_refs:
                passed = 0
                errors = []
                for g in galaxies:
                    M, R_max, V_obs, Rd = g["M_disk"], g["R_max"], g["V_obs"], g["R_disk"]
                    rho = M / ((4 / 3) * np.pi * Rd**3) if Rd > 0 else 1e9
                    g_N = G_astro * (M * 1.1) / R_max**2
                    g_M = mond_acceleration(g_N, a0_astro)
                    factor = max(1.0, (rho / rho_ref) ** kappa)
                    g_final = (g_M * factor) + (lam_h * g_N)
                    V_pred = np.sqrt(R_max * g_final)
                    err = abs(V_pred - V_obs) / V_obs * 100
                    if err < 15:
                        passed += 1
                    errors.append(err)

                pass_rate = passed / len(galaxies) * 100
                if pass_rate > best_res["pass"]:
                    best_res.update(
                        {
                            "kappa": kappa,
                            "lambda_h": lam_h,
                            "rho_ref": rho_ref,
                            "pass": pass_rate,
                            "err": np.mean(errors),
                        }
                    )
                    print(f"{kappa:<6.2f} {lam_h:<6.2f} {rho_ref:<10.1e} {pass_rate:<8.1f} *")

    print(
        f"\nFINAL BEST RESULT: Kappa={best_res['kappa']:.2f}, Lambda_H={best_res['lambda_h']:.2f}, Rho_Ref={best_res['rho_ref']:.1e}, Pass={best_res['pass']:.1f}%"
    )

    # Detailed Stats
    type_stats = {}
    for g in galaxies:
        M, R_max, V_obs, Rd, gtype = g["M_disk"], g["R_max"], g["V_obs"], g["R_disk"], g["type"]
        rho = M / ((4 / 3) * np.pi * Rd**3) if Rd > 0 else 1e9
        g_N = G_astro * (M * 1.1) / R_max**2
        g_M = mond_acceleration(g_N, a0_astro)
        factor = max(1.0, (rho / best_res["rho_ref"]) ** best_res["kappa"])
        g_final = (g_M * factor) + (best_res["lambda_h"] * g_N)
        V_pred = np.sqrt(R_max * g_final)
        err = abs(V_pred - V_obs) / V_obs * 100
        if gtype not in type_stats:
            type_stats[gtype] = {"count": 0, "pass": 0, "err": []}
        type_stats[gtype]["count"] += 1
        type_stats[gtype]["err"].append(err)
        if err < 15:
            type_stats[gtype]["pass"] += 1

    print("\n" + "=" * 50 + "\nDETAILED PERFORMANCE REPORT\n" + "=" * 50)
    for t, s in sorted(type_stats.items()):
        print(
            f"{t.upper():<12} Count: {s['count']:<4} Pass: {s['pass']/s['count']*100:<5.1f}% AvgErr: {np.mean(s['err']):<5.1f}%"
        )


if __name__ == "__main__":
    optimize_hybrid_parameters()
