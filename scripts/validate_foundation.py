import os
import sys
import subprocess
import time

# Get project root
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

# List of critical validation scripts (paths relative to project root)
scripts = [
    # Phase 1: Particle Physics & Strong Force
    "research_uet/lab/01_particle_physics/standard_model/test_uet_sm_bridge.py",
    "research_uet/lab/01_particle_physics/strong_nuclear/test_strong_force.py",
    # Phase 2: Astrophysics (Galaxies)
    "research_uet/lab/02_astrophysics/galaxies/test_175_galaxies.py",
    # Phase 3: Astrophysics (Black Holes & Thermo)
    "research_uet/lab/ultimate_ccbh_analysis.py",
    # Phase 4: Condensed Matter (V-B Bridge)
    "research_uet/lab/03_condensed_matter/condensed_matter/test_superconductivity.py",
]


def run_script(path):
    print(f"\n{'='*60}")
    print(f"🚀 RUNNING: {path}")
    print(f"{'='*60}")

    full_path = os.path.join(project_root, path)
    if not os.path.exists(full_path):
        print(f"❌ ERROR: File not found: {full_path}")
        return False

    start_time = time.time()
    try:
        # Run the script and capture output
        # Ensure we run from project root
        result = subprocess.run(
            [sys.executable, os.path.join(project_root, path)],
            cwd=project_root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        duration = time.time() - start_time

        # Print Output
        print(result.stdout)

        if result.stderr:
            print("⚠️ STDERR:")
            print(result.stderr)

        if result.returncode == 0:
            print(f"\n✅ PASS ({duration:.2f}s)")
            return True
        else:
            print(f"\n❌ FAIL (Return Code: {result.returncode})")
            return False

    except Exception as e:
        print(f"\n❌ EXCEPTION: {e}")
        return False


def main():
    print("🌌 UET GRAND UNIFIED VALIDATION RUN 🌌")
    print("========================================")

    passed = 0
    failed = 0
    results = {}

    for script in scripts:
        success = run_script(script)
        results[script] = "PASS" if success else "FAIL"
        if success:
            passed += 1
        else:
            failed += 1

    print("\n" + "=" * 60)
    print("📊 FINAL SUMMARY")
    print("=" * 60)
    for script, status in results.items():
        icon = "✅" if status == "PASS" else "❌"
        print(f"{icon} {os.path.basename(script)}: {status}")

    print("-" * 30)
    print(f"Total Tests: {len(scripts)}")
    print(f"Passed:      {passed}")
    print(f"Failed:      {failed}")

    if failed == 0:
        print("\n✨ ALL SYSTEMS GREEN. THEORY IS STABLE. ✨")
        sys.exit(0)
    else:
        print("\n⚠️ WARNING: SOME SYSTEMS FAILED.")
        sys.exit(1)


if __name__ == "__main__":
    main()
