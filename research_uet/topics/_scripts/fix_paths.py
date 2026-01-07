from pathlib import Path
import shutil

root = Path(r"c:\Users\santa\Desktop\lad\Lab_uet_harness_v0.8.7\research_uet\topics")


def fix_paths():
    # 1. Update Scripts
    for path in root.rglob("test_*.py"):
        try:
            content = path.read_text(encoding="utf-8")
            if 'parents[1] / "Result"' in content:
                new_content = content.replace('parents[1] / "Result"', 'parents[2] / "Result"')
                path.write_text(new_content, encoding="utf-8")
                print(f"Fixed path in {path.name}")
        except Exception as e:
            print(f"Error reading {path}: {e}")

    # 2. Move Files
    for code_res in root.rglob("Code/Result"):
        if code_res.is_dir():
            # Target is Topic/Result
            # Code/Result -> Code -> Topic -> Result
            topic_res = code_res.parents[1] / "Result"
            topic_res.mkdir(parents=True, exist_ok=True)

            for item in code_res.iterdir():
                if item.is_file():
                    target = topic_res / item.name
                    shutil.move(str(item), str(target))
                    print(f"Moved {item.name} to {topic_res}")

            # Remove empty Code/Result
            try:
                code_res.rmdir()
                print(f"Removed empty {code_res}")
            except:
                pass


if __name__ == "__main__":
    fix_paths()
