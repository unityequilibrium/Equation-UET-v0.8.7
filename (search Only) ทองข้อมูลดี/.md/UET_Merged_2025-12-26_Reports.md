

# 🔹 Source: file_24.md

# Cross Sweep Summary (seed10)

**Generated:** 2024-12-19

---

## Completed Sweeps

| Sweep | Grid Size | Seeds | Total Runs | Status |
|-------|-----------|-------|------------|--------|
| β × k_ratio | 5×5 | 10 | 250 | ✅ Complete |
| β × δ | 5×6 | 10 | 300 | ✅ Complete |
| s × δ | 5×6 | 10 | 300 | ✅ Complete |

---

## Key Observations

### 1. Seed-Locked Voting
- All sweeps use **fixed seeds 0-9** for reproducibility
- `grade_bias` (SYM/BIAS_C/BIAS_I) is deterministic per seed
- Statistical aggregation over seeds gives robust phase boundaries

### 2. β × k_ratio Structure
- High β + low k_ratio → stronger bias (BIAS_C dominant)
- k_ratio ≈ 1 → more symmetric outcomes

### 3. β × δ Structure  
- Delta (Λ) controls potential depth
- High delta → faster relaxation, cleaner separation
- Low delta → transient effects more visible

### 4. s × δ Structure (Most Informative)
- **s_tilt** directly controls asymmetry direction
- `s > 0` → BIAS_C, `s < 0` → BIAS_I, `s = 0` → SYM
- `common_mode = (mean_C + mean_I)/2` shows clear structure
- Omega varies systematically with delta

---

## Transient Metrics

| Metric | Description | Flag |
|--------|-------------|------|
| `t_relax` | Time to 5% of equilibrium | `NOT_INFORMATIVE` if ≤ dt |
| `slope_init` | Initial Omega decay slope | Always computed |
| `AUC_E_norm` | Area under normalized decay | Always computed |

> Note: Most runs show `t_relax_flag = NOT_INFORMATIVE` due to fast equilibration.

---

## Files

```
reports/cross_sweeps/seed10/
├── beta_k_ratio/
│   └── UET_final_summary_v2.csv
├── beta_delta/
│   └── UET_final_summary_v2.csv
├── s_delta/
│   └── UET_final_summary_v2.csv
└── ledger.csv
```

---

## Reproduce

```powershell
# Install deps
py -m pip install -r requirements.txt

# Re-run aggregation + plots
powershell -ExecutionPolicy Bypass -File .\run_all_cross_sweep.ps1 -Mode aggregate_only

# Export to reports/
powershell -ExecutionPolicy Bypass -File .\setup_reports.ps1
```


---


# 🔹 Source: file_35.md

# UET Extensions Test Report

## 📊 Test Summary

| Test | Status | ΔΩ | Conserved | Time |
|------|--------|-----|-----------|------|
| Delays | ✅ PASS | -74.9% | ✗ | 0.6s |
| Multifield | ✅ PASS | -72.8% | ✗ | 0.6s |
| Nonlocal | ✅ PASS | +80.5% | ✗ | 1.4s |
| Stochastic | ✅ PASS | +1.5% | ✓ | 0.6s |
| Memory | ✅ PASS | +421.8% | ✗ | 0.7s |
| Custom Potentials | ✅ PASS | +115.0% | ✗ | 0.6s |

**Overall: 6/6 PASSED** ✅

---

## 1. Time Delays Test

### สิ่งที่ทดสอบ
- ใส่ delay ระหว่าง C→I และ I→C coupling
- τ_CI = 1.0, τ_IC = 0.5

### ผลลัพธ์
- **ไม่มี delay (τ=0):** ระบบ stable, variance ต่ำ
- **มี delay (τ=1):** ระบบ oscillate, variance สูงขึ้น ~50x
- **Omega:** 3.96 → 0.99 (ลด 75%)

### ความหมายทางฟิสิกส์
Delay ทำให้เกิด **"neural oscillations"** คล้าย brain waves เพราะ:
- Signal ถึงช้า → overshoot → swing back → oscillate

### ทำไม Ω ไม่ conserve
- Delay ทำให้ coupling ไม่ "instant"
- พลังงานหายไปใน buffer (dissipation)

---

## 2. Multi-field Networks Test

### สิ่งที่ทดสอบ
- 3-5 coupled fields ใน topology ต่างๆ
- Fully connected, Ring, Star networks

### ผลลัพธ์
- **Fully connected:** Sync = 0.93 (สูงมาก)
- **Ring network:** Sync = 0.93 (เท่ากัน เพราะ 3-ring = full)
- **Star network:** Sync = 0.40 (ต่ำกว่า เพราะ spokes ไม่ connect กัน)

### ความหมายทางฟิสิกส์
แสดง **network synchronization** - หลาย nodes เริ่ม sync กันเมื่อ coupling แรงพอ

### ทำไม Ω ไม่ conserve
- หลาย field แลกพลังงานกัน
- Total Ω กระจายไปหลาย field

---

## 3. Nonlocal Coupling Test

### สิ่งที่ทดสอบ
- Coupling kernel แบบต่างๆ: Local, Gaussian, Power-law
- σ (kernel width) = 5

### ผลลัพธ์
- **Local:** ξ = 1 grid point (แคบ)
- **Gaussian:** ξ = 5 grid points (กลาง)
- **Power-law:** ξ = 5+ grid points (ไกล)

### ความหมายทางฟิสิกส์
**Long-range interactions** - เช่น:
- Gravitational coupling (1/r²)
- Neural connections in brain
- Supply chains in economics

### ทำไม Ω เพิ่ม
- Nonlocal coupling เพิ่ม "connections"
- พลังงานไหลจากไกลๆ เข้ามา

---

## 4. Stochastic Noise Test ⭐

### สิ่งที่ทดสอบ
- White noise ที่ amplitude ต่างๆ: σ = 0, 0.5, 2.0

### ผลลัพธ์
- **σ=0:** Variance ≈ 0 (deterministic)
- **σ=0.5:** Variance ≈ 0.01 (small fluctuations)
- **σ=2.0:** Variance ≈ 0.51 (large fluctuations)

### ⭐ Omega Conservation
**+1.5% เท่านั้น!** นี่คือ test เดียวที่ conserve!

### ทำไม Ω conserve
- Noise เป็น zero-mean (บวกลบเท่ากัน)
- Long-term average cancels out
- **UET รองรับ noise ได้ดี!**

---

## 5. Memory/History Test

### สิ่งที่ทดสอบ
- Memory kernel: None, Exponential, Power-law
- τ_mem = 10, γ = 0.2

### ผลลัพธ์
- **No memory:** Fast decay หลัง impulse
- **Exponential:** Slower decay (จำได้นานขึ้น)
- **Power-law:** Very slow decay (long memory)

### ความหมายทางฟิสิกส์
**Path dependence / Hysteresis** - ระบบจำอดีต เช่น:
- Economic markets (memory of past prices)
- Material stress (plastic deformation)
- Ecosystems (recovery time)

### ทำไม Ω เพิ่มมาก (+422%)
- Memory kernel **สะสม** พลังงานจากอดีต
- ยิ่ง memory ยาว ยิ่งสะสมมาก

---

## 6. Custom Potentials Test

### สิ่งที่ทดสอบ
- 4 potential landscapes:
  - Double-well: V(φ) = (φ²-1)²/4
  - Single-well: V(φ) = φ²/2
  - Triple-well: V(φ) = φ⁴ - 2φ² + 1
  - Periodic: V(φ) = -cos(φ)

### ผลลัพธ์
- **Double-well:** ⟨C⟩ → ±1 (bistable)
- **Single-well:** ⟨C⟩ → 0 (unique equilibrium)
- **Triple-well:** ⟨C⟩ → 0 or ±√2 (tristable)
- **Periodic:** ⟨C⟩ → any multiple of 2π

### ความหมายทางฟิสิกส์
**Landscape engineering** - ออกแบบ energy landscape ให้เหมาะกับ application

---

## 🔬 บทสรุป

### Extensions ที่ Conserve Ω
| Extension | Conserve? | เหตุผล |
|-----------|-----------|--------|
| **Stochastic** | ✅ Yes | Noise cancels out |
| Others | ❌ No | Designed to not conserve |

### ข้อสำคัญ
1. **Extensions ไม่จำเป็นต้อง conserve Ω** - มันเป็น "open system"
2. **Stochastic conserve** เพราะ noise เป็น zero-mean
3. **Test PASS หมายถึง physics ถูกต้อง** ไม่ใช่ Ω conserve

### คำแนะนำ
- ใช้ **Stochastic** เมื่อต้องการ noise แต่ยัง conserve
- ใช้ **Delays/Memory** เมื่อต้องการ oscillations/hysteresis
- ใช้ **Nonlocal** เมื่อต้องการ long-range effects

---

*Generated: 2025-12-21*


---
