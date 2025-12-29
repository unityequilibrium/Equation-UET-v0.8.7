# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.8.7] - 2025-12-29

### Added
- **Full Paper Draft** (`research/00_core_paper/PAPER_FULL.md`)
- **Physics Gap Tests**
  - Pauli Exclusion test (vortex repulsion)
  - Lorentz/Euclidean dispersion analysis
  - Gauge Symmetry (U(1) + SU(2)) verification
  - Planck constant emergence test
- **Code Verification**
  - Determinism test (hash-based)
  - Edge case coverage (negative delta, extreme ratios)
  - Time-stepping verification (SciPy vs UET)
- **Testable Prediction**: κ_p/κ_e = (m_p/m_e)^(2/3) ≈ 150.2
- **Credibility Audit** document with honest assessment
- **Long-term Roadmap** (Phase 1-3)

### Changed
- Improved Black Hole validation with Kormendy data
- Enhanced stress test suite (4/4 pass)
- Updated documentation structure

### Fixed
- CSV parsing for Black Hole data (comment handling)
- Light Speed test logic in torture suite
- Energy key names (Omega0/OmegaT)

## [0.8.6] - 2025-12-28

### Added
- Black Hole CCBH integration
- k=3.0 cosmological coupling validation

## [0.8.5] - 2025-12-27

### Added
- 39-test unified validation suite
- 17 physics domain tests

## [0.8.0] - 2025-12-26

### Added
- Initial public release candidate
- Core solver with semi-implicit spectral method
- C_only and C_I models
- Auto-scaling and coercivity checks

---

*For older versions, see git history.*
