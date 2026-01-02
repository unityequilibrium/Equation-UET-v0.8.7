"""

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

Master References for UET Research
==================================
Complete bibliography of all data sources used.

Updated for UET V3.0
"""

# ================================================================
# PDG REFERENCES
# ================================================================

PDG_REFERENCES = {
    "PDG2024": {
        "title": "Review of Particle Physics",
        "authors": "Particle Data Group",
        "journal": "Phys. Rev. D",
        "volume": "110",
        "pages": "030001",
        "year": 2024,
        "doi": "10.1103/PhysRevD.110.030001",
        "url": "https://pdg.lbl.gov",
        "used_for": [
            "Quark masses",
            "Hadron masses",
            "QCD running coupling",
            "Electroweak parameters",
            "Neutrino oscillation parameters",
        ],
    },
    "PDG2025": {
        "title": "2025 Review of Particle Physics",
        "authors": "Particle Data Group",
        "year": 2025,
        "status": "Online update December 2025",
        "url": "https://pdg.lbl.gov",
    },
}

# ================================================================
# MUON G-2
# ================================================================

MUON_G2_REFERENCES = {
    "Fermilab2025": {
        "title": "Muon g-2 Final Result",
        "collaboration": "Muon g-2 Collaboration",
        "journal": "Phys. Rev. Lett.",
        "year": 2025,
        "month": "June",
        "result": "a_μ = 0.001165920705(114)",
        "precision": "127 ppb",
        "used_for": ["Muon g-2 experimental value"],
    },
    "TheoryInitiative2020": {
        "title": "The anomalous magnetic moment of the muon in the Standard Model",
        "authors": "Aoyama et al.",
        "journal": "Physics Reports",
        "volume": "887",
        "pages": "1-166",
        "year": 2020,
        "used_for": ["Standard Model prediction (data-driven)"],
    },
    "BMW2021": {
        "title": "Leading hadronic contribution to the muon magnetic moment from lattice QCD",
        "authors": "Borsanyi et al. (BMW Collaboration)",
        "journal": "Nature",
        "volume": "593",
        "pages": "51-55",
        "year": 2021,
        "used_for": ["Lattice QCD prediction"],
    },
}

# ================================================================
# ASTROPHYSICS
# ================================================================

ASTROPHYSICS_REFERENCES = {
    "SPARC2016": {
        "title": "SPARC: Mass Models for 175 Disk Galaxies",
        "authors": "Lelli, McGaugh, Schombert",
        "journal": "Astronomical Journal",
        "volume": "152",
        "pages": "157",
        "year": 2016,
        "doi": "10.3847/0004-6256/152/6/157",
        "data_url": "http://astroweb.cwru.edu/SPARC/",
        "used_for": ["Galaxy rotation curves", "Dark matter analysis"],
    },
    "THINGS2008": {
        "title": "The HI Nearby Galaxy Survey",
        "authors": "Walter et al.",
        "journal": "AJ",
        "year": 2008,
        "used_for": ["Dwarf galaxy rotation"],
    },
    "EHT2019": {
        "title": "First M87 Event Horizon Telescope Results",
        "collaboration": "Event Horizon Telescope",
        "journal": "ApJL",
        "volume": "875",
        "year": 2019,
        "used_for": ["Black hole mass, shadow"],
    },
}

# ================================================================
# CONDENSED MATTER
# ================================================================

CONDENSED_MATTER_REFERENCES = {
    "Lamoreaux1997": {
        "title": "Demonstration of the Casimir Force",
        "authors": "Lamoreaux, S.K.",
        "journal": "Phys. Rev. Lett.",
        "volume": "78",
        "pages": "5",
        "year": 1997,
        "used_for": ["Casimir force measurement"],
    },
    "Mohideen1998": {
        "title": "Precision Casimir Force Measurement",
        "authors": "Mohideen, Roy",
        "journal": "Phys. Rev. Lett.",
        "volume": "81",
        "pages": "4549",
        "year": 1998,
        "used_for": ["Casimir force at short distances"],
    },
    "Kittel": {
        "title": "Introduction to Solid State Physics",
        "authors": "Kittel, C.",
        "edition": "8th",
        "publisher": "Wiley",
        "year": 2004,
        "used_for": ["Superconductor critical temperatures"],
    },
}

# ================================================================
# QUANTUM FOUNDATIONS
# ================================================================

QUANTUM_REFERENCES = {
    "Aspect1982": {
        "title": "Experimental Realization of EPR Gedankenexperiment",
        "authors": "Aspect, Dalibard, Roger",
        "journal": "Phys. Rev. Lett.",
        "volume": "49",
        "pages": "1804",
        "year": 1982,
        "result": "S = 2.697 ± 0.015",
        "used_for": ["Bell inequality violation"],
    },
    "Hensen2015": {
        "title": "Loophole-free Bell inequality violation",
        "authors": "Hensen et al.",
        "journal": "Nature",
        "volume": "526",
        "pages": "682",
        "year": 2015,
        "result": "S = 2.42 ± 0.20",
        "used_for": ["Loophole-free Bell test"],
    },
    "Nobel2022": {
        "title": "Nobel Prize in Physics 2022",
        "laureates": ["Aspect", "Clauser", "Zeilinger"],
        "reason": "Experiments with entangled photons",
        "year": 2022,
    },
}

# ================================================================
# LATTICE QCD
# ================================================================

LATTICE_REFERENCES = {
    "FLAG2024": {
        "title": "FLAG Review 2024",
        "collaboration": "Flavour Lattice Averaging Group",
        "year": 2024,
        "arxiv": "2411.04268",
        "used_for": ["Quark condensate", "Lattice averages"],
    },
    "BMW_HVP": {
        "title": "BMW Collaboration Hadronic Vacuum Polarization",
        "collaboration": "Budapest-Marseille-Wuppertal",
        "year": 2021,
        "used_for": ["HVP for muon g-2"],
    },
}

# ================================================================
# NUCLEAR DATA
# ================================================================

NUCLEAR_REFERENCES = {
    "NNDC": {
        "title": "National Nuclear Data Center",
        "organization": "Brookhaven National Laboratory",
        "url": "https://www.nndc.bnl.gov/",
        "year": 2024,
        "used_for": ["Nuclear decay rates", "Neutrino data"],
    },
    "NuBase2020": {
        "title": "The NUBASE2020 evaluation",
        "journal": "Chinese Physics C",
        "year": 2021,
        "used_for": ["Nuclear properties"],
    },
}

# ================================================================
# HELPER FUNCTIONS
# ================================================================


def get_all_references():
    """Return all references as a single dictionary."""
    all_refs = {}
    all_refs.update(PDG_REFERENCES)
    all_refs.update(MUON_G2_REFERENCES)
    all_refs.update(ASTROPHYSICS_REFERENCES)
    all_refs.update(CONDENSED_MATTER_REFERENCES)
    all_refs.update(QUANTUM_REFERENCES)
    all_refs.update(LATTICE_REFERENCES)
    all_refs.update(NUCLEAR_REFERENCES)
    return all_refs


def print_reference(key):
    """Print a formatted reference."""
    all_refs = get_all_references()
    if key in all_refs:
        ref = all_refs[key]
        print(f"\n{key}:")
        for k, v in ref.items():
            print(f"  {k}: {v}")
    else:
        print(f"Reference '{key}' not found.")


if __name__ == "__main__":
    print("=" * 60)
    print("UET Research Master Reference List")
    print("=" * 60)

    refs = get_all_references()
    print(f"\nTotal references: {len(refs)}")

    print("\nCategories:")
    print(f"  PDG: {len(PDG_REFERENCES)}")
    print(f"  Muon g-2: {len(MUON_G2_REFERENCES)}")
    print(f"  Astrophysics: {len(ASTROPHYSICS_REFERENCES)}")
    print(f"  Condensed Matter: {len(CONDENSED_MATTER_REFERENCES)}")
    print(f"  Quantum: {len(QUANTUM_REFERENCES)}")
    print(f"  Lattice QCD: {len(LATTICE_REFERENCES)}")
    print(f"  Nuclear: {len(NUCLEAR_REFERENCES)}")
