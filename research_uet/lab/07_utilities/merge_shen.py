from astropy.table import Table, hstack
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



def merge_shen_data():
    base_dir = r"c:\Users\santa\Desktop\lad\Lab_uet_harness_v0.8.7\research_uet\data\02_astrophysics\black_holes"
    full_path = os.path.join(base_dir, "shen2011_full.fits")
    sample_path = os.path.join(base_dir, "shen2011_sample.fits")
    output_path = os.path.join(base_dir, "shen2011_merged.fits")

    print(f"Reading {full_path}...")
    try:
        t_full = Table.read(full_path)
    except Exception as e:
        print(f"Error reading full: {e}")
        return

    print(f"Reading {sample_path}...")
    try:
        t_sample = Table.read(sample_path)
    except Exception as e:
        print(f"Error reading sample: {e}")
        return

    print(f"Full rows: {len(t_full)}")
    print(f"Sample rows: {len(t_sample)}")

    if len(t_full) != len(t_sample):
        print("Warning: Lengths differ! Cannot simply merge columns.")
        return

    # Check for desired columns
    has_z = "z" in t_full.colnames
    has_logBH = "logBH" in t_sample.colnames

    if has_z and has_logBH:
        print("Merging 'logBH' from sample into full...")
        t_full["logBH"] = t_sample["logBH"]
        t_full.write(output_path, overwrite=True)
        print(f"Saved merged file to {output_path}")
    else:
        print(f"Missing columns. Full has z: {has_z}, Sample has logBH: {has_logBH}")


if __name__ == "__main__":
    merge_shen_data()
