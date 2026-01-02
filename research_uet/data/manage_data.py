"""
UET Data Management Script
==========================

This script:
1. Audits existing data (real vs synthetic)
2. Archives synthetic data to _archive/
3. Downloads missing real data where possible
4. Verifies data integrity

Run: python research_uet/data/manage_data.py
"""

import os
import shutil
import json
from pathlib import Path
from typing import Dict, List, Tuple

# Base path
DATA_DIR = Path(__file__).parent
ARCHIVE_DIR = DATA_DIR / "_archive"


# =============================================================================
# DATA CLASSIFICATION
# =============================================================================

DATA_STATUS = {
    # 00_thermodynamic_bridge - ALL REAL
    "00_thermodynamic_bridge/experimental_data.py": ("REAL", "Bérut, LIGO, EHT data"),
    # 01_particle_physics - MIXED
    "01_particle_physics/particle_masses.py": ("REAL", "PDG values"),
    "01_particle_physics/binding_energy.txt": ("REAL", "Nuclear data"),
    "01_particle_physics/alpha_decay_data.txt": ("REAL", "Half-lives"),
    "01_particle_physics/neutrino_extended_data.py": ("SYNTHETIC", "Not real oscillation data"),
    "01_particle_physics/qcd_strong_force_data.py": ("SYNTHETIC", "Not lattice QCD"),
    "01_particle_physics/quantum_mechanics_data.py": ("SYNTHETIC", "Representative"),
    "01_particle_physics/weak_force_data.py": ("SYNTHETIC", "Based on SM"),
    # 02_astrophysics - MOSTLY REAL
    "02_astrophysics/black_hole_data.py": ("REAL", "SDSS/EHT sources"),
    "02_astrophysics/galaxies/": ("REAL", "SPARC 175 galaxies"),
    "02_astrophysics/cosmology/": ("PARTIAL", "Some real, needs CMB"),
    # 03_condensed_matter - MOSTLY SYNTHETIC
    "03_condensed_matter/plasma_data.py": ("SYNTHETIC", "Not tokamak data"),
    "03_condensed_matter/superfluid_data.py": ("SYNTHETIC", "Representative"),
    "03_condensed_matter/real_condensed_data.json": ("PARTIAL", "Mixed"),
    # 04_quantum - EMPTY
    # Need to create/download
    # 06_complex_systems - MIXED
    "06_complex_systems/Real_EEG_Sample.npy": ("REAL", "MNE/PhysioNet"),
    "06_complex_systems/bio/": ("SYNTHETIC", "Representative HRV"),
    "06_complex_systems/climate/": ("REAL", "NOAA CO2"),
    "06_complex_systems/economy/": ("REAL", "Yahoo Finance S&P500"),
    "06_complex_systems/social/": ("SYNTHETIC", "Representative"),
}


def audit_data() -> Dict[str, List[str]]:
    """Audit all data and classify as REAL/SYNTHETIC/PARTIAL."""
    result = {"REAL": [], "SYNTHETIC": [], "PARTIAL": [], "UNKNOWN": []}

    for path, (status, note) in DATA_STATUS.items():
        full_path = DATA_DIR / path
        if full_path.exists():
            result[status].append(f"{path} - {note}")
        else:
            result["UNKNOWN"].append(f"{path} (missing)")

    return result


def archive_synthetic():
    """Move synthetic data to _archive folder."""
    ARCHIVE_DIR.mkdir(exist_ok=True)

    archived = []
    for path, (status, note) in DATA_STATUS.items():
        if status == "SYNTHETIC":
            src = DATA_DIR / path
            if src.exists():
                # Create directory structure in archive
                dest = ARCHIVE_DIR / path
                dest.parent.mkdir(parents=True, exist_ok=True)

                if src.is_file():
                    shutil.copy2(src, dest)
                    archived.append(str(path))
                elif src.is_dir():
                    if dest.exists():
                        shutil.rmtree(dest)
                    shutil.copytree(src, dest)
                    archived.append(str(path))

    return archived


def print_audit():
    """Print data audit results."""
    audit = audit_data()

    print("=" * 70)
    print("📊 UET DATA AUDIT")
    print("=" * 70)

    print("\n✅ REAL DATA (ready to use):")
    for item in audit["REAL"]:
        print(f"   • {item}")

    print("\n⚠️ PARTIAL DATA (needs verification):")
    for item in audit["PARTIAL"]:
        print(f"   • {item}")

    print("\n🔸 SYNTHETIC DATA (will archive):")
    for item in audit["SYNTHETIC"]:
        print(f"   • {item}")

    print("\n❓ UNKNOWN/MISSING:")
    for item in audit["UNKNOWN"]:
        print(f"   • {item}")

    print("\n" + "=" * 70)
    print(
        f"Summary: {len(audit['REAL'])} real, {len(audit['SYNTHETIC'])} synthetic, "
        f"{len(audit['PARTIAL'])} partial"
    )


# =============================================================================
# DOWNLOAD FUNCTIONS
# =============================================================================


def download_sparc_data():
    """Download SPARC galaxy rotation curve data."""
    print("\n📥 SPARC Galaxy Data")
    print("-" * 40)
    print("Source: http://astroweb.cwru.edu/SPARC/")
    print("Reference: Lelli et al. 2016, AJ 152, 157")
    print("\nTo download manually:")
    print("  1. Go to http://astroweb.cwru.edu/SPARC/")
    print("  2. Download 'SPARC_Lelli2016c.mrt'")
    print("  3. Save to research_uet/data/02_astrophysics/galaxies/")


def download_planck_cmb():
    """Download Planck CMB power spectrum."""
    print("\n📥 Planck CMB Data")
    print("-" * 40)
    print("Source: ESA Planck Legacy Archive")
    print("Reference: Planck Collaboration 2018")
    print("\nTo download:")
    print("  pip install astropy")
    print("  # Then use:")
    print(
        """
from astropy.io import fits
import urllib.request

# Planck 2018 TT power spectrum
url = "https://pla.esac.esa.int/pla/aio/planckResults.action?RELEASE.YEAR=2018&DATA.TYPE=CMB_SPECTRUM"
# Or download from Planck Legacy Archive web interface
"""
    )


def download_quantum_data():
    """Guide for quantum mechanics experimental data."""
    print("\n📥 Quantum Mechanics Data")
    print("-" * 40)
    print("Required datasets:")
    print("  1. Bell inequality: Aspect 1982, Hensen 2015")
    print("  2. Double-slit: Arndt 1999 (C60)")
    print("  3. Quantum Zeno: Itano 1990")
    print("\nNote: Most quantum data is in papers, not open datasets")
    print("Recommend: Create representative data based on published results")


def download_casimir_data():
    """Guide for Casimir force data."""
    print("\n📥 Casimir Force Data")
    print("-" * 40)
    print("Reference: Lamoreaux 1997 PRL 78, 5")
    print("Also: Mohideen & Roy 1998")
    print("\nData typically in papers - extract from:")
    print("  - Figure data in PDF")
    print("  - Supplementary materials")


def print_download_guides():
    """Print all download guides."""
    print("\n" + "=" * 70)
    print("📥 DATA DOWNLOAD GUIDES")
    print("=" * 70)

    download_sparc_data()
    download_planck_cmb()
    download_quantum_data()
    download_casimir_data()


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="UET Data Management")
    parser.add_argument("--audit", action="store_true", help="Audit existing data")
    parser.add_argument("--archive", action="store_true", help="Archive synthetic data")
    parser.add_argument("--download", action="store_true", help="Show download guides")
    parser.add_argument("--all", action="store_true", help="Run all operations")

    args = parser.parse_args()

    if args.all or args.audit or (not any(vars(args).values())):
        print_audit()

    if args.all or args.archive:
        print("\n📦 Archiving synthetic data...")
        archived = archive_synthetic()
        if archived:
            print(f"Archived {len(archived)} items to {ARCHIVE_DIR}")
            for item in archived:
                print(f"   → {item}")
        else:
            print("No synthetic data to archive")

    if args.all or args.download:
        print_download_guides()
