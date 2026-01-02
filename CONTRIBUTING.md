# 🤝 Contributing to Unity Equilibrium Theory

**Standard for Contributions: Rigorous, Real-Data Validation.**

---

## � Physics Contribution Standards (STRICT)

We only accept physics contributions that are validated against **Independent Empirical Data**.

### 1. The Validation Matrix Requirement
Every PR adding a physics domain must update the **README Matrix** with:
1.  **Phenomenon:** What are you testing? (e.g., *Isotope Stability*)
2.  **Equation:** Derived from `Ω[C, I]` (e.g., $E = \int \nabla C ...$)
3.  **Data Source:** Must be a reputable catalog (e.g., *NNDC*, *CERN*, *NASA*).
4.  **Error Metric:** Quantitative result (e.g., *RMSE < 5%*, *$R^2 > 0.95$*).

### 2. Prohibited Content
-   ❌ **No Pure Theory:** We do not accept "philosophical" papers without data.
-   ❌ **No Ad-Hoc Fitting:** Constants ($\beta, \kappa$) must be consistent or explicitly derived.

---

## �️ Development Workflow

1.  **Fork & Clone**:
    ```bash
    git clone https://github.com/unityequilibrium/Equation-UET-v0.8.7.git
    cd Equation-UET-v0.8.7
    ```

2.  **Run the Validation Suite (Before Submitting)**:
    ```bash
    cd research_uet/lab/07_utilities
    python run_master_validation.py
    ```
    **PRs will be rejected if existing tests fail.**

3.  **Add Your Test**:
    -   Create a script in `lab/0X_domain/test_my_hypothesis.py`.
    -   Import real data (CSV/JSON/FITS).
    -   Calculate `predicted` vs `observed`.
    -   Assert `error < tolerance`.

---

## � Bug Reports

Please include:
1.  **Script Name**: Which laboratory script failed?
2.  **Error Log**: The full Python traceback.
3.  **Data Context**: Which dataset were you using?

---

## 🔍 Transparency

**AI-Assisted Framework:**
This codebase was generated using agentic AI workflows.
-   **Review Process:** Code is reviewed for *mathematical consistency*, not *authorship intent*.
-   **Verification:** The ultimate arbiter is the **Data**.

---

## 📜 Legal
By contributing, you agree that your code will be licensed under the project's **MIT License**.
