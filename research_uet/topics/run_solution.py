"""
Solution Runner - Run all sections in a solution at once
=========================================================
Usage: python run_solution.py 0.1
       python run_solution.py 0.1_Galaxy_Rotation_Problem

Outputs results to Result/ folder and generates comparison report.
"""

import sys
import os
import subprocess
import json
from pathlib import Path
from datetime import datetime

# Find topics folder
TOPICS = Path(__file__).parent


def find_solution(query):
    """Find solution folder by number or name."""
    for folder in TOPICS.iterdir():
        if folder.is_dir() and folder.name.startswith(query):
            return folder
    return None


def get_test_files(solution_path):
    """Get all test files from Code/ subfolders."""
    code_path = solution_path / "Code"
    tests = []
    for section in code_path.iterdir():
        if section.is_dir():
            for f in section.glob("test_*.py"):
                tests.append((section.name, f))
    return tests


def run_tests(solution_path):
    """Run all tests and collect results."""
    tests = get_test_files(solution_path)
    results = {}

    # Add lab folder and solution Data folder to Python path
    research_uet = solution_path.parent.parent
    lab_path = research_uet / "lab"
    env = os.environ.copy()

    # Build PYTHONPATH with all potential data locations
    extra_paths = [
        str(lab_path),
        str(lab_path / "01_galaxy_dynamics"),
        str(lab_path / "02_gravitational"),
        str(lab_path / "03_electroweak"),
        str(lab_path / "04_neutrino"),
        str(lab_path / "05_qcd_hadrons"),
        str(lab_path / "06_motion_dynamics"),
        str(lab_path / "07_complex_systems"),
        str(lab_path / "00_thermodynamic_bridge"),
        str(solution_path / "Data"),
        str(research_uet),
    ]
    env["PYTHONPATH"] = os.pathsep.join(extra_paths)

    print(f"\n{'='*60}")
    print(f"Running Solution: {solution_path.name}")
    print(f"{'='*60}")

    for section_name, test_file in tests:
        print(f"\n[{section_name}] Running {test_file.name}...")

        try:
            result = subprocess.run(
                [sys.executable, str(test_file)],
                capture_output=True,
                text=True,
                timeout=300,
                cwd=str(test_file.parent),
                env=env,
            )

            success = result.returncode == 0
            results[section_name] = {
                "file": test_file.name,
                "success": success,
                "output": result.stdout[-2000:] if result.stdout else "",
                "error": result.stderr[-500:] if result.stderr else "",
            }

            status = "✅ PASS" if success else "❌ FAIL"
            print(f"  {status}")

        except subprocess.TimeoutExpired:
            results[section_name] = {"file": test_file.name, "success": False, "error": "Timeout"}
            print(f"  ⏱️ TIMEOUT")
        except Exception as e:
            results[section_name] = {"file": test_file.name, "success": False, "error": str(e)}
            print(f"  ❌ ERROR: {e}")

    return results


def generate_report(solution_path, results):
    """Generate markdown report."""
    result_path = solution_path / "Result"
    result_path.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = result_path / f"run_report_{timestamp}.md"

    passed = sum(1 for r in results.values() if r.get("success"))
    total = len(results)

    content = f"""# Solution Run Report: {solution_path.name}

**Date**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Result**: {passed}/{total} sections passed

## Summary

| Section | Test File | Status |
|:--------|:----------|:-------|
"""

    for section, data in results.items():
        status = "✅ PASS" if data.get("success") else "❌ FAIL"
        content += f"| {section} | {data['file']} | {status} |\n"

    content += "\n## Details\n\n"

    for section, data in results.items():
        content += f"### {section}\n\n"
        if data.get("output"):
            content += f"```\n{data['output'][:1000]}\n```\n\n"
        if data.get("error") and not data.get("success"):
            content += f"**Error**: {data['error']}\n\n"

    with open(report_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n📝 Report saved: {report_file}")

    # Also save JSON for programmatic access
    json_file = result_path / f"run_results_{timestamp}.json"
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    return report_file


def main():
    if len(sys.argv) < 2:
        print("Usage: python run_solution.py <solution_number_or_name>")
        print("Example: python run_solution.py 0.1")
        print("         python run_solution.py 0.1_Galaxy_Rotation_Problem")
        sys.exit(1)

    query = sys.argv[1]
    solution = find_solution(query)

    if not solution:
        print(f"Solution not found: {query}")
        print("\nAvailable solutions:")
        for folder in sorted(TOPICS.iterdir()):
            if folder.is_dir() and folder.name.startswith("0."):
                print(f"  - {folder.name}")
        sys.exit(1)

    results = run_tests(solution)
    report = generate_report(solution, results)

    passed = sum(1 for r in results.values() if r.get("success"))
    total = len(results)

    print(f"\n{'='*60}")
    print(f"FINAL: {passed}/{total} sections passed")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
