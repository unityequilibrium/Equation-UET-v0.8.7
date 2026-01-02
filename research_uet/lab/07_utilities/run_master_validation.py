"""
🔬 UET Master Validation Runner (v2026)
=====================================
Runs all key validation scripts across the UET Lab structure and aggregates results.

Usage:
    python lab/07_utilities/run_master_validation.py

Updated for UET V3.0
"""

import subprocess
import os

# Import from UET V3.0 Master Equation
import sys
from pathlib import Path
_root = Path(__file__).parent
while _root.name != "research_uet" and _root.parent != _root:
    _root = _root.parent
sys.path.insert(0, str(_root.parent))
try:
    from research_uet.core.uet_master_equation import (
        UETParameters, SIGMA_CRIT, strategic_boost, potential_V, KAPPA_BEKENSTEIN
    )
except ImportError:
    pass  # Use local definitions if not available

import sys
from datetime import datetime

# Setup Paths
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "research_uet", "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Define Tests (Name, Relative Path from Project Root)
TESTS = [
    # === 01. PARTICLE PHYSICS ===
    ("Proton/Hadron Masses", "research_uet/lab/01_particle_physics/qcd_fix/uet_hadron_model.py"),
    ("Strong Force (QCD)", "research_uet/lab/01_particle_physics/qcd_fix/uet_qcd_bridge.py"),
    ("Weak Force", "research_uet/lab/01_particle_physics/weak_nuclear/test_weak_force.py"),
    (
        "Alpha Decay (Real)",
        "research_uet/lab/01_particle_physics/weak_nuclear/test_real_alpha_decay.py",
    ),
    (
        "Binding Energy (Real)",
        "research_uet/lab/01_particle_physics/weak_nuclear/test_real_binding_energy.py",
    ),
    # === 02. ASTROPHYSICS ===
    ("Galaxies (SPARC)", "research_uet/lab/02_astrophysics/galaxies/test_175_galaxies.py"),
    ("Black Holes", "research_uet/lab/02_astrophysics/black_holes/test_black_holes.py"),
    ("Cosmology (Real Data)", "research_uet/lab/02_astrophysics/cosmology/test_real_cosmology.py"),
    ("Cosmic History Sim", "research_uet/lab/02_astrophysics/cosmology/run_cosmic_history.py"),
    # === 03. CONDENSED MATTER ===
    ("Casimir Effect", "research_uet/lab/03_condensed_matter/electromagnetic/casimir_test.py"),
    (
        "Josephson Junction",
        "research_uet/lab/03_condensed_matter/condensed_matter/test_josephson_tunneling.py",
    ),
    (
        "Superconductivity",
        "research_uet/lab/03_condensed_matter/condensed_matter/test_superconductivity.py",
    ),
    ("Plasma Physics", "research_uet/lab/03_condensed_matter/plasma/test_plasma_physics.py"),
    # === 04. QUANTUM ===
    ("Quantum Mechanics", "research_uet/lab/04_quantum/quantum/test_quantum_mechanics.py"),
    # === 05. UNIFIED THEORY ===
    ("Muon g-2", "research_uet/lab/05_unified_theory/action_transformer/test_muon_g2.py"),
    (
        "Action-Transformer",
        "research_uet/lab/05_unified_theory/action_transformer/test_attention_equilibrium.py",
    ),
    (
        "Brownian Motion",
        "research_uet/lab/05_unified_theory/effect_of_motion/test_brownian_effect.py",
    ),
    (
        "Phase Separation",
        "research_uet/lab/05_unified_theory/effect_of_motion/test_phase_separation.py",
    ),
]


def run_test(name, script_rel_path):
    """Run a single test script."""
    full_path = os.path.join(PROJECT_ROOT, script_rel_path)

    if not os.path.exists(full_path):
        return f"SKIP: File not found: {script_rel_path}"

    try:
        # Force UTF-8 for Windows
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"

        result = subprocess.run(
            [sys.executable, full_path],
            capture_output=True,
            text=True,
            timeout=300,  # 5 mins max
            cwd=PROJECT_ROOT,  # Run from root
            env=env,
            encoding="utf-8",
            errors="replace",
        )

        output = result.stdout + result.stderr
        if result.returncode == 0:
            return f"PASS\n{output}"
        else:
            return f"ERROR (code {result.returncode})\n{output}"

    except subprocess.TimeoutExpired:
        return "TIMEOUT"
    except Exception as e:
        return f"EXCEPTION: {e}"


def main():
    print("=" * 60)
    print("🔬 UET MASTER VALIDATION RUNNER (v2026)")
    print(f"📂 Root: {PROJECT_ROOT}")
    print("=" * 60)

    passed = 0
    failed = 0
    skipped = 0

    for name, path in TESTS:
        print(f"🔄 Running: {name}...")
        res = run_test(name, path)

        status = "FAIL"
        if res.startswith("PASS"):
            status = "PASS"
            passed += 1
        elif res.startswith("SKIP"):
            status = "SKIP"
            skipped += 1
        else:
            failed += 1

        print(f"   → {status}")

    print("\n" + "=" * 60)
    print(f"✅ PASSED: {passed} | ❌ FAILED: {failed} | ⏭️ SKIPPED: {skipped}")
    print("=" * 60)


if __name__ == "__main__":
    main()
