"""
UET Standard Fluid References (NIST Source)
===========================================
Source: NIST Chemistry WebBook & Engineering Toolbox
Verified: 2026-01-03

Purpose: Provide REAL physical constants for Navier-Stokes validation in UET.
"""

FLUID_PROPERTIES = {
    "water_20c": {
        "density": 998.2,  # kg/m^3
        "viscosity": 1.002e-3,  # Pa.s (Dynamic)
        "kinematic": 1.004e-6,  # m^2/s
        "source": "NIST, 1 atm, 20C",
    },
    "air_20c": {
        "density": 1.204,  # kg/m^3
        "viscosity": 1.81e-5,  # Pa.s
        "kinematic": 1.516e-5,  # m^2/s
        "source": "NIST, 1 atm, 20C",
    },
    "honey_20c": {
        "density": 1420.0,  # kg/m^3
        "viscosity": 10.0,  # Pa.s (Approx 10,000x water)
        "kinematic": 7.04e-3,  # m^2/s
        "source": "Engineering Toolbox (Grade A)",
    },
    "mercury_20c": {
        "density": 13546.0,  # kg/m^3
        "viscosity": 1.526e-3,  # Pa.s
        "kinematic": 1.126e-7,  # m^2/s
        "source": "NIST",
    },
}


def get_fluid(name: str) -> dict:
    """Returns fluid properties or raises error if not found."""
    if name not in FLUID_PROPERTIES:
        raise ValueError(f"Fluid '{name}' not found. Available: {list(FLUID_PROPERTIES.keys())}")
    return FLUID_PROPERTIES[name]


if __name__ == "__main__":
    print("UET Real Fluid Database (NIST Verified)")
    for name, props in FLUID_PROPERTIES.items():
        print(f"{name}: rho={props['density']} kg/m3, mu={props['viscosity']} Pa.s")
