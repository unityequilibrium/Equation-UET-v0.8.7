import os
import sys
import subprocess
from pathlib import Path
import time

TOPICS_DIR = Path(r"c:\Users\santa\Desktop\lad\Lab_uet_harness_v0.8.7\research_uet\topics")


def run_topic_tests(topic_path):
    code_dir = topic_path / "Code"
    if not code_dir.exists():
        print(f"Skipping {topic_path.name} (No Code dir)")
        return

    result_dir = topic_path / "Result"
    result_dir.mkdir(exist_ok=True)

    log_file = result_dir / "execution_v0.8.7.log"

    print(f"Processing {topic_path.name}...")

    with open(log_file, "w", encoding="utf-8") as log:
        log.write(f"Execution Log for {topic_path.name}\n")
        log.write(f"Date: {time.ctime()}\n")
        log.write("=" * 60 + "\n\n")

        # Find test files
        test_files = list(code_dir.rglob("test_*.py"))

        if not test_files:
            log.write("No test files found.\n")
            return

        for test_file in sorted(test_files):
            log.write(f"Running {test_file.name}...\n")
            log.write("-" * 40 + "\n")
            log.flush()

            try:
                # Run test and capture output using sub-process
                # We interpret standard tests
                result = subprocess.run(
                    [sys.executable, str(test_file)],
                    cwd=test_file.parent,
                    capture_output=True,
                    text=True,
                    timeout=30,  # 30s timeout per test to be safe
                )

                log.write(result.stdout)
                if result.stderr:
                    log.write("\nSTDERR:\n")
                    log.write(result.stderr)

                status = "PASS" if result.returncode == 0 else "FAIL"
                log.write(f"\nResult: {status} (Exit Code: {result.returncode})\n")

            except subprocess.TimeoutExpired:
                log.write("\nTIMEOUT reached (30s).\n")
            except Exception as e:
                log.write(f"\nExecution Error: {e}\n")

            log.write("\n" + "=" * 60 + "\n\n")
            print(f"  - {test_file.name}: Done")

    print(f"  > Output saved to {log_file}")


def main():
    if not TOPICS_DIR.exists():
        print("Topics dir not found")
        return

    count = 0
    for item in sorted(TOPICS_DIR.iterdir()):
        if item.is_dir() and item.name[0].isdigit():  # 0.1, 0.2 etc
            run_topic_tests(item)
            count += 1

    print(f"\nFinished processing {count} topics.")


if __name__ == "__main__":
    main()
