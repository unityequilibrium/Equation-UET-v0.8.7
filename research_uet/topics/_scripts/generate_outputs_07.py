import os
import sys
import subprocess
from pathlib import Path
import time

TOPIC_PATH = Path(
    r"c:\Users\santa\Desktop\lad\Lab_uet_harness_v0.8.7\research_uet\topics\0.7_Neutrino_Physics"
)


def run_tests():
    code_dir = TOPIC_PATH / "Code"
    result_dir = TOPIC_PATH / "Result"
    result_dir.mkdir(exist_ok=True)

    log_file = result_dir / "execution_v0.8.7.log"

    print(f"Processing {TOPIC_PATH.name}...")

    with open(log_file, "w", encoding="utf-8") as log:
        log.write(f"Execution Log for {TOPIC_PATH.name}\n")
        log.write(f"Date: {time.ctime()}\n")
        log.write("=" * 60 + "\n\n")

        test_files = list(code_dir.rglob("test_*.py"))

        for test_file in sorted(test_files):
            log.write(f"Running {test_file.name}...\n")
            log.write("-" * 40 + "\n")
            log.flush()

            try:
                # Force UTF-8 capture
                result = subprocess.run(
                    [sys.executable, str(test_file)],
                    cwd=test_file.parent,
                    capture_output=True,
                    encoding="utf-8",  # FIX: Explicitly interpret output as UTF-8
                    errors="replace",  # Safety
                    timeout=30,
                )

                log.write(result.stdout)
                if result.stderr:
                    log.write("\nSTDERR:\n")
                    log.write(result.stderr)

                status = "PASS" if result.returncode == 0 else "FAIL"
                log.write(f"\nResult: {status} (Exit Code: {result.returncode})\n")

            except Exception as e:
                log.write(f"\nExecution Error: {e}\n")

            log.write("\n" + "=" * 60 + "\n\n")
            print(f"  - {test_file.name}: Done")

    print(f"  > Output saved to {log_file}")


if __name__ == "__main__":
    run_tests()
