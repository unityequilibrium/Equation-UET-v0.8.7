# 📁 Core — UET Engine

> **Purpose**: Core mathematical foundations of Unity Equilibrium Theory

---

## 📄 Contents

| File | Description |
|:-----|:------------|
| [`uet_master_equation.py`](./uet_master_equation.py) | The UET master equation Ω[C, I] |
| [`uet_matrix_engine.py`](./uet_matrix_engine.py) | Matrix operations for UET |
| [`uet_matrix_toolkit.py`](./uet_matrix_toolkit.py) | Helper functions |
| [`test_matrix_proof.py`](./test_matrix_proof.py) | Unit tests for matrix operations |
| [`test_matrix_real_galaxy.py`](./test_matrix_real_galaxy.py) | Real galaxy validation |
| [`test_tensor_parity.py`](./test_tensor_parity.py) | Tensor parity tests |

---

## 🎯 Core Equation

```math
Ω[C, I] = ∫ [V(C) + (κ/2)|∇C|² + β·C·I] dx
```

| Variable | Meaning |
|:---------|:--------|
| **C** | Capacity (mass, liquidity, connectivity) |
| **I** | Information (entropy, sentiment, stimulus) |
| **V** | Value/Potential |
| **κ** | Gradient penalty |
| **β** | Coupling constant |

---

## 🔗 Related

- **Lab tests**: `../lab/`
- **Data sources**: `../data/`
- **Theory docs**: `../theory/`

---

*Core Engine v0.8.7*
