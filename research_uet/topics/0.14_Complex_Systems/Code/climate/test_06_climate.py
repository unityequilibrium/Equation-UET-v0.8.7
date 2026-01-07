"""
🌍 UET Test 06: Climate Forced Equilibrium
==========================================

Tests: Forced system far from equilibrium

Uses real NASA/NOAA climate data.

Updated for UET V3.0
"""

import numpy as np
import pandas as pd

# Import from UET V3.0 Master Equation
import sys
from pathlib import Path

_root = Path(__file__).parent
while _root.name != "research_uet" and _root.parent != _root:
    _root = _root.parent
sys.path.insert(0, str(_root.parent))
try:
    from research_uet.core.uet_master_equation import (
        UETParameters,
        SIGMA_CRIT,
        strategic_boost,
        potential_V,
        KAPPA_BEKENSTEIN,
    )
except ImportError:
    pass  # Use local definitions if not available

import os

TOPIC_DIR = Path(__file__).resolve().parent.parent.parent
DATA_PATH = TOPIC_DIR / "Data"
DATA_DIR = str(DATA_PATH)


def load_climate_data():
    """Load climate data."""
    data = {}
    climate_dir = os.path.join(DATA_DIR, "climate")

    # CO2
    co2_path = os.path.join(climate_dir, "noaa_co2_mauna_loa.csv")
    if os.path.exists(co2_path):
        df = pd.read_csv(co2_path, comment="#")
        data["co2"] = df

    # Sea level
    sea_path = os.path.join(climate_dir, "noaa_sea_level.csv")
    if os.path.exists(sea_path):
        try:
            df = pd.read_csv(sea_path, comment="#")
            data["sea_level"] = df
        except:
            pass

    return data


def analyze_equilibrium_distance(time_series, name):
    """
    Analyze how far system is from equilibrium.

    UET Interpretation:
    - dC/dt = 0: Equilibrium
    - dC/dt > 0 (accelerating): Forcing overpowers stabilization
    - Climate is being FORCED (CO2 injection) → dΩ/dt > 0
    """
    if len(time_series) < 10:
        return None

    values = time_series.values if hasattr(time_series, "values") else time_series
    values = values[np.isfinite(values)]

    if len(values) < 10:
        return None

    # Rate of change
    rate = np.diff(values)
    avg_rate = np.mean(rate[-12:])  # Recent rate

    # Acceleration (derivative of rate)
    accel = np.diff(rate)
    avg_accel = np.mean(accel[-12:]) if len(accel) > 0 else 0

    # Equilibrium distance
    # 0 = equilibrium, higher = farther
    eq_distance = abs(avg_rate) / (np.std(values) + 0.001)

    # Classify
    if avg_rate > 0 and avg_accel > 0:
        status = "ACCELERATING AWAY (far from equilibrium)"
    elif avg_rate > 0:
        status = "INCREASING (not at equilibrium)"
    elif abs(avg_rate) < 0.01 * np.std(values):
        status = "STABLE (near equilibrium)"
    else:
        status = "DECREASING (returning to equilibrium)"

    return {
        "name": name,
        "current_value": values[-1],
        "avg_rate": avg_rate,
        "avg_accel": avg_accel,
        "eq_distance": eq_distance,
        "status": status,
        "data_points": len(values),
    }


def run_test():
    """Run climate equilibrium test."""
    print("\n" + "=" * 60)
    print("🌍 UET TEST 06: Climate Forced Equilibrium")
    print("=" * 60)
    print("\nEquation: dΩ/dt = Forcing - Stabilization")
    print("UET Interpretation: Climate is FORCED system")

    data = load_climate_data()

    if not data:
        print("❌ No climate data found!")
        return {"status": "FAIL", "error": "No data"}

    print(f"\nLoaded {len(data)} climate datasets\n")

    results = []

    # Analyze CO2
    if "co2" in data:
        df = data["co2"]
        # Find CO2 column
        co2_col = None
        for col in df.columns:
            if "average" in col.lower() or "co2" in col.lower() or "trend" in col.lower():
                co2_col = col
                break

        if co2_col is None and len(df.columns) > 1:
            co2_col = df.columns[1]  # Usually second column

        if co2_col:
            metrics = analyze_equilibrium_distance(df[co2_col], "CO2 (ppm)")
            if metrics:
                results.append(metrics)
                print(f"   CO2:")
                print(f"      Current: {metrics['current_value']:.1f} ppm")
                print(f"      Rate: +{metrics['avg_rate']:.2f} ppm/month")
                print(f"      Status: {metrics['status']}")
                print()

    # Analyze sea level
    if "sea_level" in data:
        df = data["sea_level"]
        # Find sea level column
        sl_col = None
        for col in df.columns:
            if "gmsl" in col.lower() or "sea" in col.lower() or "level" in col.lower():
                sl_col = col
                break

        if sl_col is None and len(df.columns) > 1:
            sl_col = df.columns[1]

        if sl_col:
            metrics = analyze_equilibrium_distance(df[sl_col], "Sea Level (mm)")
            if metrics:
                results.append(metrics)
                print(f"   Sea Level:")
                print(f"      Current: {metrics['current_value']:.1f} mm")
                print(f"      Rate: +{metrics['avg_rate']:.2f} mm/period")
                print(f"      Status: {metrics['status']}")
                print()

    if not results:
        print("❌ Could not analyze climate data")
        return {"status": "FAIL", "error": "Analysis failed"}

    # Summary
    print("=" * 40)
    print("UET Analysis:")
    print("=" * 40)

    accelerating = [r for r in results if "ACCELERATING" in r["status"]]
    increasing = [r for r in results if "INCREASING" in r["status"]]

    if accelerating:
        status = "WARN"
        grade = "⚠️ FORCED DISEQUILIBRIUM"
        print("\n⚠️ Climate system is being FORCED away from equilibrium")
        print("   CO2 injection > Natural absorption")
        print("   dΩ/dt > 0 (system stress increasing)")
    elif increasing:
        status = "WARN"
        grade = "⚡ TRANSITIONAL"
        print("\n⚡ Climate system in transition")
    else:
        status = "PASS"
        grade = "✅ STABLE"

    print(f"\nGrade: {grade}")

    print("\nUET Interpretation:")
    print("   I (Information) = CO2 concentration")
    print("   C (Capacity) = Temperature, Sea Level")
    print("   β·C·I coupling = Greenhouse effect")
    print("   Current state: Far from pre-industrial equilibrium")

    # --- VISUALIZATION ---
    try:
        from research_uet.core import uet_viz

        result_dir = Path(__file__).resolve().parent.parent.parent / "Result" / "climate"
        result_dir.mkdir(parents=True, exist_ok=True)

        fig = uet_viz.go.Figure()

        # Plot CO2
        if "co2" in data:
            df = data["co2"]
            # Try to grab relevant columns
            if len(df.columns) >= 2:
                # Assuming index or year/month is implicit or 1st column
                # Just plot simple sequence if no proper time index found
                vals = df.iloc[:, 1].values  # 2nd column usually data
                vals = vals[vals > 0]  # Filter invalid

                fig.add_trace(
                    uet_viz.go.Scatter(
                        y=vals, mode="lines", name="CO2 Concentration", line=dict(color="red")
                    )
                )

        # Plot Sea Level (on secondary axis potentially, or normalized)
        # For simplicity, just CO2 helps visualize "Forcing"

        fig.update_layout(
            title="Climate Forcing (CO2): Information Injection",
            xaxis_title="Time Steps",
            yaxis_title="CO2 (ppm)",
        )
        uet_viz.save_plot(fig, "climate_viz.png", result_dir)
        print("  [Viz] Generated 'climate_viz.png'")

    except Exception as e:
        print(f"Viz Error: {e}")

    return {
        "status": status,
        "grade": grade,
        "datasets_analyzed": len(results),
        "accelerating": len(accelerating),
        "results": results,
    }


if __name__ == "__main__":
    result = run_test()
    print(f"\n✅ Test complete: {result['status']}")
