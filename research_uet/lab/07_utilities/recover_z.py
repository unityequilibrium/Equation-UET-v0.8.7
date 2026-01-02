from astropy.table import Table, Column
import os
import numpy as np


def recover_z():
    base_dir = r"c:\Users\santa\Desktop\lad\Lab_uet_harness_v0.8.7\research_uet\data\02_astrophysics\black_holes"
    full_path = os.path.join(base_dir, "shen2011_full.fits")
    sample_path = os.path.join(base_dir, "shen2011_sample.fits")
    output_path = os.path.join(base_dir, "shen2011_recovered.fits")

    print(f"Reading {full_path}...")
    t_full = Table.read(full_path)
    print(f"Reading {sample_path}...")
    t_sample = Table.read(sample_path)

    # Create lookup from full: logLbol -> z
    # Note: logLbol might not be unique.
    print("Building lookup map...")
    lbol_to_z = {}
    duplicates = 0
    for row in t_full:
        bol = float(row["logLbol"])
        z = row["z"]
        if bol in lbol_to_z:
            duplicates += 1
            # Keep first? Or mark ambiguous?
            # For now, keep first.
        else:
            lbol_to_z[bol] = z

    print(
        f"Lookup map built. {len(lbol_to_z)} unique logLbol values. {duplicates} duplicates ignored."
    )

    # Apply to sample
    print("Matching sample...")
    z_values = []
    matched_count = 0
    missed_count = 0

    for row in t_sample:
        bol = float(row["logLbol"])
        if bol in lbol_to_z:
            z_values.append(lbol_to_z[bol])
            matched_count += 1
        else:
            z_values.append(np.nan)
            missed_count += 1

    print(f"Matched: {matched_count}, Missed: {missed_count}")

    # Add column
    col_z = Column(name="z", data=z_values)
    t_sample.add_column(col_z)

    # Filter out non-matches if necessary?
    # The analysis script likely needs valid z.
    t_final = t_sample[~np.isnan(t_sample["z"])]
    print(f"Final rows after dropping NaN z: {len(t_final)}")

    t_final.write(output_path, overwrite=True)
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    recover_z()
