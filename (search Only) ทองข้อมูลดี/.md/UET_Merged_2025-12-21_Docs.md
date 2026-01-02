

# 🔹 Source: file_0.md

# UET Bridge Program (Layer E)

**Version:** 0.9  
**Purpose:** เชื่อม UET กับทฤษฎีจากสาขาอื่น

---

## 🌉 Bridge Program คืออะไร?

Bridge Program คือการแสดงว่า UET "พูดภาษาเดียวกับ" ทฤษฎีอื่นๆ ได้อย่างไร ทำให้:
1. คนจากสาขาอื่นเข้าใจ UET ได้เร็วขึ้น
2. ใช้ผลลัพธ์จาก UET ตีความในบริบทอื่นได้
3. นำเทคนิคจากสาขาอื่นมาปรับใช้กับ UET ได้

---

## 🔥 E1: Thermodynamics Bridge

### แนวคิดหลัก

| UET | Thermodynamics |
|-----|----------------|
| Ω (Energy Functional) | Free Energy (F) |
| $\frac{d\Omega}{dt} \leq 0$ | Second Law: $dS \geq 0$ |
| Equilibrium Phase | Thermodynamic Equilibrium |
| T (simulation time) | Relaxation Time |

### การตีความ

**Ω as Free Energy:**
$$\Omega = U - TS$$
- $U$ = Internal energy (potential + coupling)
- $T$ = Temperature (noise level)
- $S$ = Entropy (disorder)

ใน UET เราใช้ $T = 0$ (deterministic) ดังนั้น $\Omega = U$

**Energy Minimization = Entropy Maximization (at fixed U):**
- UET minimizes Ω
- ≈ System finding lowest free energy state
- ≈ Maximizing entropy subject to constraints

### Decomposition Mapping

| UET Component | Thermo Interpretation |
|---------------|----------------------|
| $\Omega_{pot}$ | Bulk internal energy |
| $\Omega_{coup}$ | Interaction energy |
| $\Omega_{grad}$ | Surface/interface energy |

### สมการ Dynamics

**UET:** 
$$\frac{\partial C}{\partial t} = -M \frac{\delta\Omega}{\delta C}$$

**Thermo (Relaxation):**
$$\frac{\partial \phi}{\partial t} = -\Gamma \frac{\delta F}{\delta \phi}$$

เหมือนกันทุกประการ! (Allen-Cahn / Model A dynamics)

---

## 📊 E2: Information Theory Bridge

### แนวคิดหลัก

| UET | Information Theory |
|-----|-------------------|
| Field C(x) | Probability distribution |
| Ω | Negative log-likelihood |
| Equilibrium | Maximum likelihood state |
| Gradient flow | Gradient descent optimization |

### Shannon Entropy ของ Field

**นิยาม Spatial Entropy:**
$$H[C] = -\sum_{i,j} p(C_{ij}) \log p(C_{ij})$$

ถ้า normalize field เป็น distribution

**Phase Entropy:**
| Phase | Entropy |
|-------|---------|
| SYM | High (uncertain) |
| BIAS_C | Low (certain C-dominant) |
| BIAS_I | Low (certain I-dominant) |

### Mutual Information

**C-I Mutual Information:**
$$I(C; I) = H[C] + H[I] - H[C, I]$$

- High $I(C;I)$: Fields strongly correlated → high coupling
- Low $I(C;I)$: Fields independent → weak coupling

### KL Divergence Interpretation

**Distance from uniform:**
$$D_{KL}(C || U) = \sum p_C \log \frac{p_C}{1/N^2}$$

Greater divergence = more ordered/biased structure

---

## ⚛️ E3: Quantum Analogy Bridge

### ⚠️ ข้อควรระวัง

**UET ไม่ใช่ Quantum Mechanics!** นี่คือ "analogy" ไม่ใช่ equivalence

### Mapping Table

| UET | Quantum (Analogy) |
|-----|------------------|
| C(x) field | Wave function amplitude |
| Ω functional | Energy expectation ⟨H⟩ |
| Gradient flow | Imaginary-time Schrödinger |
| Equilibrium | Ground state |
| Phase transition | Quantum phase transition (T=0) |

### Imaginary-Time Correspondence

**Schrödinger (imaginary time τ = it):**
$$\frac{\partial \psi}{\partial \tau} = -\hat{H} \psi$$

**UET (gradient flow):**
$$\frac{\partial C}{\partial t} = -\frac{\delta\Omega}{\delta C}$$

ทั้งสองให้ ground state ที่ $t \to \infty$

### อะไรที่ไม่เหมือน

| Feature | UET | QM |
|---------|-----|-----|
| Superposition | ❌ No | ✅ Yes |
| Measurement problem | ❌ No | ✅ Yes |
| Entanglement | ❌ No | ✅ Yes |
| Complex amplitude | ❌ Real only | ✅ Complex |
| Probabilistic | ❌ Deterministic | ✅ Intrinsic |

---

## 🎮 E4: Game Dynamics Bridge

### แนวคิดหลัก

| UET | Game Theory |
|-----|-------------|
| C_i, I_i values | Player strategies |
| Ω | Potential function |
| Equilibrium | Nash Equilibrium |
| Gradient flow | Best-response dynamics |
| Phase | Coordination outcome |

### Potential Game Interpretation

**Definition:** A game is a potential game if there exists Φ such that:
$$u_i(s_i', s_{-i}) - u_i(s_i, s_{-i}) = \Phi(s_i', s_{-i}) - \Phi(s_i, s_{-i})$$

**UET as Potential Game:**
- $\Phi = -\Omega$ (negated energy)
- Each "site" is a player
- Strategy = field value at that site
- Utility = local energy contribution

### Coordination vs Anti-coordination

| β value | Game Type | Outcome |
|---------|-----------|---------|
| β > 0 | Coordination (C wants I to match) | Aligned phases |
| β < 0 | Anti-coordination | Opposite phases |
| β = 0 | Independent games | No interaction |

### Nash Equilibrium ↔ UET Equilibrium

**Theorem:** Stationary points of Ω in UET correspond to Nash equilibria of the induced potential game.

**Proof sketch:** At equilibrium, $\frac{\delta\Omega}{\delta C_i} = 0$ for all i. This means no player can improve their utility by unilateral deviation → Nash equilibrium. □

---

## 🌌 E5: Einstein/Lambda Bridge

### Cosmological Analogy

| UET | Cosmology |
|-----|-----------|
| Ω | Dark energy density |
| a (quartic parameter) | Curvature term |
| δ (quartic parameter) | Self-interaction |
| s (tilt) | Cosmological constant Λ |
| Phase transition | Cosmic phase transition |

### Lambda (Λ) Mapping

**In UET:**
- s = external tilt = external "pressure"
- When s ≠ 0, symmetry is explicitly broken

**In Cosmology:**
- Λ = cosmological constant = constant energy density
- Causes accelerated expansion

**Analogy:** Both represent "external bias" that shifts equilibrium

### Scalar Field Analogy

**Cosmological scalar field (inflaton):**
$$\mathcal{L} = \frac{1}{2}(\partial\phi)^2 - V(\phi)$$

**UET energy:**
$$\Omega = \int \left[\frac{\kappa}{2}|\nabla C|^2 + V(C)\right] dx$$

เหมือนกันทุกประการ!

### Phase Transitions in Early Universe

| UET Phase | Cosmic Analogy |
|-----------|---------------|
| SYM → BIAS | Symmetry breaking (electroweak) |
| Domain walls | Cosmic strings/defects |
| Gradient energy | Tension in defects |

### Scale Mapping

| UET Parameter | Physical Scale |
|---------------|---------------|
| L (domain size) | Hubble radius |
| ξ (correlation length) | Horizon scale |
| τ (relaxation time) | Hubble time |

**หมายเหตุ:** นี่คือ analogy สำหรับ intuition ไม่ใช่ physical model ของเอกภพจริง

---

## 🔗 Cross-Bridge Summary

### Universal Patterns

ทุก bridge มีโครงสร้างเดียวกัน:

1. **Energy Functional → Objective Function**
   - Thermo: Free energy
   - Info: Negative log-likelihood
   - QM: Expectation Hamiltonian
   - Game: Potential function
   - Cosmo: Action

2. **Gradient Flow → Optimization**
   - Thermo: Relaxation
   - Info: ML training
   - QM: Imaginary-time evolution
   - Game: Best-response
   - Cosmo: Classical dynamics

3. **Equilibrium → Solution**
   - Thermo: Thermal equilibrium
   - Info: MLE/MAP
   - QM: Ground state
   - Game: Nash equilibrium
   - Cosmo: Vacuum state

### When to Use Each Bridge

| ถ้าคนฟังมาจาก... | ใช้ Bridge... |
|-----------------|--------------|
| Physics background | E1 (Thermo) |
| ML/CS background | E2 (Info) |
| Theoretical physics | E3 (Quantum) |
| Economics/Social science | E4 (Game) |
| Cosmology/HEP | E5 (Einstein) |

---

## 📚 References

### E1: Thermodynamics
- Landau, L.D. "Statistical Physics"
- Callen, H.B. "Thermodynamics and an Introduction to Thermostatistics"

### E2: Information Theory
- Cover, T.M. & Thomas, J.A. "Elements of Information Theory"
- MacKay, D.J.C. "Information Theory, Inference, and Learning Algorithms"

### E3: Quantum
- Sachdev, S. "Quantum Phase Transitions"
- Fradkin, E. "Field Theories of Condensed Matter Physics"

### E4: Game Theory
- Sandholm, W.H. "Population Games and Evolutionary Dynamics"
- Monderer, D. & Shapley, L.S. "Potential Games"

### E5: Cosmology
- Weinberg, S. "Cosmology"
- Mukhanov, V. "Physical Foundations of Cosmology"

---

**เกณฑ์ผ่าน:** อธิบายได้ว่า UET มาจาก/ไปสู่ แต่ละสาขาอย่างไร


---


# 🔹 Source: file_1.md

# Cross Sweeps Walkthrough

## Quick Start

```powershell
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run all cross-sweeps (matrix → simulate → aggregate)
powershell -ExecutionPolicy Bypass -File .\run_all_cross_sweep.ps1

# 3. Or just re-aggregate existing results
powershell -ExecutionPolicy Bypass -File .\run_all_cross_sweep.ps1 -Mode aggregate_only
```

---

## Sweep Summary (seed10)

| Sweep | Axes | Runs Dir | Summary File |
|-------|------|----------|--------------|
| β × k_ratio | beta=[0.1,0.5,1,2,5], k_ratio=[0.1,0.5,1,2,10] | `runs_cross_beta_k_ratio_seed10/` | `UET_final_summary_v2.csv` |
| β × δ | beta=[0.1,0.5,1,2,5], delta=[0.01,0.1,0.3,1,3,10] | `runs_cross_beta_delta_seed10/` | `UET_final_summary_v2.csv` |
| s × δ | s=[-2,-1,0,1,2], delta=[0.01,0.1,0.3,1,3,10] | `runs_cross_s_delta_seed10/` | `UET_final_summary_v2.csv` |

---

## Key Output Columns

| Column | Description |
|--------|-------------|
| `delta`, `delta_C`, `delta_I` | Λ (cosmological constant) from potC/potI |
| `s_C`, `s_I`, `s_tilt` | Tilt parameter |
| `k_ratio` | kC/kI ratio |
| `grade_bias` | SYM / BIAS_C / BIAS_I |
| `t_relax` | Relaxation time (5% band) |
| `t_relax_flag` | OK / NOT_INFORMATIVE |

---

## Regression Check

To verify results match previous runs:
1. Pick one baseline case (e.g., `param_CI_sd_sp2_d1_seed0`)
2. Re-run with same seed
3. Compare `Omega`, `bias_CI` values (should match within floating-point tolerance)


---


# 🔹 Source: file_10.md

# UET Modeling Interface Card (MI Card) Template

**Version:** 0.9  
**Purpose:** ใช้แปลงโจทย์โดเมนใหม่ให้เข้ากับ UET Framework

---

## ⚠️ ก่อนเริ่ม

**MI Card คือ "แบบฟอร์ม" ที่บังคับให้คุณคิดให้ครบก่อนรัน simulation**

หลักการ:
1. ตอบคำถามทุกข้อให้ครบก่อน
2. ถ้าตอบไม่ได้ = ยังไม่พร้อมทำ UET
3. ถ้าตอบได้ = สามารถแปลงเป็น config และ matrix ได้ทันที

---

## 📋 MI Card Template

### Section A: Entity (Introvert View - สิ่งหนึ่ง)

**A1. สิ่งหนึ่งคืออะไรในโดเมนนี้?**
> _ตัวอย่าง: "ความคิดเห็นสาธารณะ", "อุณหภูมิในห้อง", "ราคาหุ้น"_

```
คำตอบ: _______________________________________________
```

**A2. State ของมันคืออะไร?**
> _แนะนำ: เลือก 1-2 field ก่อน (C และ/หรือ I)_

```
C แทน: _______________________________________________
I แทน: _______________________________________________
```

**A3. Constraints ที่จริงในโลกคืออะไร?**
> _ห้าม sweep หลุดข้อจำกัดเหล่านี้_

```
ข้อจำกัด 1: _______________________________________________
ข้อจำกัด 2: _______________________________________________
ข้อจำกัด 3: _______________________________________________
```

---

### Section B: World (Extrovert View - ระบบรวม)

**B4. สนาม/สิ่งแวดล้อมคืออะไร?**
> _สิ่งที่ "บังคับ" ให้ระบบต้องจัดรูป_

```
คำตอบ: _______________________________________________
```

**B5. มี "แรง" อะไรบ้าง?**
> _ผลัก/ดึง/ต้าน ในโดเมนนี้_

```
แรงผลัก: _______________________________________________
แรงดึง: _______________________________________________
แรงต้าน: _______________________________________________
```

---

### Section C: Map เข้า UET

**C6. C กับ I แปลว่าอะไรในโดเมนนี้?**
> _หรือใช้ C-only ถ้าไม่มี coupling_

```
C = _______________________________________________
I = _______________________________________________
(หรือ C-only เพราะ: _______________________________)
```

**C7. Potential (P) มาจากอะไร?**
> _อะไรคือ "แรงขับ" ที่ทำให้ระบบอยากเปลี่ยน?_

```
แรงขับ: _______________________________________________
→ แมพกับ parameter: a = ___, delta = ___, s = ___
```

**C8. Conflict/Resistance (R) มาจากอะไร?**
> _อะไรคือ "ต้นทุน/รอยต่อ/การต้าน"?_

```
ต้นทุน: _______________________________________________
→ แมพกับ parameter: kappa/kC/kI = ___
```

**C9. Flow (J) - timescale คืออะไร?**
> _dynamics/เวลาในโดเมนนี้เทียบกับ dt ยังไง?_

```
Timescale: _______________________________________________
→ แมพกับ parameter: M/MC/MI = ___
```

---

### Section D: Observables

**D10. ผลลัพธ์ที่อยากได้คืออะไร?**
> _phase? value? conflict? pattern?_

```
□ Phase (BIAS_C / BIAS_I / SYM)
□ Value (Ω reduction)
□ Conflict (Ω_grad)
□ Pattern (spatial structure)
□ อื่นๆ: _______________________________________________
```

**D11. จะทำ demo ยังไงให้คนเห็นภาพ?**
> _ต้อง export อะไร?_

```
□ Snapshots (C, I fields)
□ Animation (evolution.gif)
□ Terrain plot (3D surface)
□ Omega decomposition (Ω_pot, Ω_coup, Ω_grad)
□ อื่นๆ: _______________________________________________
```

---

### Section E: Sweep Plan

**E12. เลือก sweep แค่ 2 แกนก่อน + เหตุผล**
> _เพราะต้องทำ phase map ไม่ใช่สุ่ม 10 มิติ_

```
แกน 1: _______________ (เหตุผล: _______________________)
แกน 2: _______________ (เหตุผล: _______________________)

Range แกน 1: [___, ___] step ___
Range แกน 2: [___, ___] step ___
```

---

## 🔄 แปลง MI Card → UET Config

### เมื่อกรอก MI Card ครบแล้ว ใช้ข้อมูลนี้สร้าง config:

```python
config = {
    "case_id": "YOUR_CASE_ID",
    "model": "C_I",  # หรือ "C_only"
    "domain": {"L": 10.0, "dim": 2, "bc": "periodic"},
    "grid": {"N": 64},
    "time": {"dt": 0.01, "T": 10.0, "max_steps": 2000},
    "params": {
        # จาก C7 (Potential)
        "potC": {"type": "quartic", "a": -1.0, "delta": 1.0, "s": YOUR_S},
        "potI": {"type": "quartic", "a": -1.0, "delta": 1.0, "s": YOUR_S},
        
        # จาก C8 (Conflict/Resistance)
        "kC": YOUR_KC,
        "kI": YOUR_KI,
        
        # Coupling (จาก C6)
        "beta": YOUR_BETA,
        
        # จาก C9 (Flow)
        "MC": 1.0,
        "MI": 1.0,
    }
}
```

---

## 📖 ตัวอย่าง MI Card ที่กรอกแล้ว

### ตัวอย่าง: "Conscience vs Instinct"

**A1. สิ่งหนึ่ง:** การตัดสินใจของมนุษย์

**A2. State:**
- C = ความแข็งแกร่งของ Conscience (จิตสำนึก)
- I = ความแข็งแกร่งของ Instinct (สัญชาตญาณ)

**A3. Constraints:**
- ค่าต้องมีขอบเขต (ไม่ระเบิด)
- ต้องมี coupling (C กับ I มีปฏิสัมพันธ์)

**B4. สนาม:** สิ่งแวดล้อมทางสังคม/จริยธรรม

**B5. แรง:**
- แรงผลัก: แรงจูงใจภายนอก (s tilt)
- แรงดึง: coupling ระหว่าง C และ I (beta)
- แรงต้าน: gradient penalty (kappa)

**C6. C กับ I:**
- C = Conscience field
- I = Instinct field

**C7. Potential:** 
- แรงขับคือ "ความพอใจ" ในการเลือกข้าง
- a = -1 (double-well), delta = 1, s = tilt

**C8. Conflict:**
- ต้นทุนคือการเปลี่ยนใจ (gradient)
- kC = kI = 0.5

**C9. Flow:**
- Timescale = หน่วยเวลาสมมติ
- MC = MI = 1.0

**D10. ผลลัพธ์:** Phase (BIAS_C / BIAS_I / SYM)

**D11. Demo:** Snapshots + Animation + Terrain

**E12. Sweep:**
- แกน 1: s (tilt) - เพราะควบคุมทิศทาง
- แกน 2: beta (coupling) - เพราะควบคุม interaction strength

---

## ✅ Checklist ก่อน Run

- [ ] กรอก MI Card ครบทุกข้อ
- [ ] ตรวจสอบ constraints ไม่หลุด
- [ ] สร้าง config.json
- [ ] สร้าง matrix.csv สำหรับ sweep
- [ ] พร้อม run!

---

**เกณฑ์ผ่าน:** คนทำ matrix ได้โดยไม่ต้องถามกลับว่า "จะใส่อะไร"


---


# 🔹 Source: file_11.md

# UET Framework - Comprehensive Analysis
## Complete Strategic Assessment

*Last Updated: 2025-12-21*

---

# Executive Summary

**UET (Unified Excitable Theory) is a meta-framework for modeling coupled dynamics across domains.**

- **NOT:** New fundamental physics
- **IS:** Common mathematical language for complex systems
- **GOAL:** Become the "Python of mathematical modeling"

---

# 1. What UET Actually Is

## 1.1 Core Identity

```
UET = Reaction-Diffusion Framework + Cross-Domain Vocabulary

Mathematical Core:
∂C/∂t = κ∇²C - ∂V/∂C - β(C-I) + s
∂I/∂t = κ∇²I - ∂V/∂I - β(I-C)

Where V(φ) = (φ²-1)²/4 (double-well potential)
```

**Classification:**
- Mathematical: Two-field reaction-diffusion system
- Computational: PDE solver framework
- Conceptual: Meta-language for coupled dynamics

## 1.2 What UET Is NOT

| ❌ Common Misconception | ✅ Reality |
|------------------------|-----------|
| Theory of Everything | Modeling framework |
| New fundamental physics | Organized existing math |
| Replacement for GR/QFT | Phenomenological tool |
| Proven scientific theory | Exploratory framework |
| Production-ready software | Research/education tool |

---

# 2. Strategic Position

## 2.1 Market Position

```
Established Physics  ←→  UET  ←→  Computational Models
   (Fundamental)              (Phenomenological)
```

**UET occupies the BRIDGE position:**
- Left: Connects to established theories (Thermodynamics, GR, StatMech)
- Right: Connects to practical applications (simulations, data fitting)
- Center: Provides translation layer

## 2.2 Competitive Landscape

| Tool/Framework | Domain | UET Comparison |
|----------------|--------|----------------|
| **NumPy/SciPy** | General numerics | UET: Higher-level, domain-specific |
| **FEniCS** | General PDE | UET: Specialized for C-I coupling |
| **Brian2** | Neuroscience | UET: Continuous fields vs spikes |
| **Mesa** | Agent-based | UET: Field-based vs agents |
| **TensorFlow** | ML/AI | UET: Physics-based vs data-driven |
| **Turing.jl** | Pattern formation | **Most similar!** Different philosophy |

**Unique Value Proposition:**
1. Cross-domain vocabulary (C, I, β, κ)
2. Built-in duality (observable + hidden)
3. Gallery of 50+ examples
4. Honest scope and limitations
5. Falsifiable framework

---

# 3. Strengths Analysis

## 3.1 Technical Strengths

| Strength | Description | Impact |
|----------|-------------|--------|
| **Simplicity** | 2 equations, 5 parameters | ⭐⭐⭐⭐⭐ |
| **Flexibility** | Works across many domains | ⭐⭐⭐⭐⭐ |
| **Duality** | C-I structure natural for hidden states | ⭐⭐⭐⭐ |
| **Visualization** | 50+ gallery demos | ⭐⭐⭐⭐⭐ |
| **Documentation** | Clear scope, honest limitations | ⭐⭐⭐⭐ |

## 3.2 Strategic Strengths

1. **Cross-Domain Communication**
   - Physicist + Biologist speak same language
   - Reduces translation overhead
   - Enables interdisciplinary collaboration

2. **Educational Value**
   - Simple enough to teach
   - Rich enough to explore
   - Visual demos aid understanding

3. **Falsifiability**
   - Clear boundaries
   - Testable predictions
   - Scientific integrity

4. **Extensibility**
   - Can add features without breaking core
   - Plugin architecture possible
   - Community contributions enabled

---

# 4. Weaknesses Analysis

## 4.1 Technical Weaknesses

| Weakness | Impact | Mitigation Strategy |
|----------|--------|---------------------|
| **Limited scope** | Can't do quantum, discrete, stochastic | ⭐⭐⭐ | Extensions module |
| **Performance** | Python, no GPU, basic solver | ⭐⭐⭐ | Numba JIT, CuPy |
| **Maturity** | New, limited testing | ⭐⭐⭐⭐ | Time + community |
| **Learning curve** | Must map domain → C,I | ⭐⭐⭐⭐ | Domain templates |
| **Community** | Small, no ecosystem | ⭐⭐⭐⭐⭐ | Outreach, examples |

## 4.2 Strategic Weaknesses

1. **Adoption Barriers**
   - Unknown framework
   - No established user base
   - Competing with mature tools

2. **Credibility Gap**
   - Not from established institution
   - No peer-reviewed publications
   - "Unified" name sounds grandiose

3. **Resource Constraints**
   - Limited development capacity
   - No funding
   - Solo/small team effort

---

# 5. Opportunities

## 5.1 Market Opportunities

| Opportunity | Potential | Difficulty |
|-------------|-----------|------------|
| **Education** | ⭐⭐⭐⭐⭐ | Low |
| **Cross-domain research** | ⭐⭐⭐⭐ | Medium |
| **Rapid prototyping** | ⭐⭐⭐⭐ | Low |
| **Visualization tool** | ⭐⭐⭐⭐⭐ | Low |
| **Production simulation** | ⭐⭐ | High |

## 5.2 Growth Strategies

1. **Education-First Approach**
   - Target universities
   - Create course materials
   - Workshops and tutorials

2. **Community Building**
   - GitHub presence
   - User-contributed examples
   - Plugin ecosystem

3. **Integration**
   - Export to other tools
   - Import from standard formats
   - Interoperability focus

4. **Niche Domination**
   - Own "coupled dynamics modeling"
   - Be THE tool for C-I systems
   - Don't try to do everything

---

# 6. Threats

## 6.1 External Threats

| Threat | Likelihood | Impact |
|--------|------------|--------|
| **Established tools improve** | High | ⭐⭐⭐⭐ |
| **Competing framework emerges** | Medium | ⭐⭐⭐ |
| **Lack of adoption** | High | ⭐⭐⭐⭐⭐ |
| **Credibility challenges** | Medium | ⭐⭐⭐ |

## 6.2 Internal Threats

1. **Scope Creep**
   - Trying to do too much
   - Losing focus on core value

2. **Over-claiming**
   - Promising more than delivered
   - Damaging credibility

3. **Maintenance Burden**
   - Code becomes unmaintainable
   - Documentation falls behind

---

# 7. Improvement Roadmap

## 7.1 Phase 1: Foundation (Months 1-2)

**Goal: Make UET easy to use**

| Feature | Priority | Effort |
|---------|----------|--------|
| Domain templates | P0 | Medium |
| Quick start guide | P0 | Low |
| Tutorial notebooks | P0 | Medium |
| Better error messages | P1 | Low |
| API documentation | P1 | Medium |

**Success Metrics:**
- Time to first simulation: 30 min → 5 min
- Lines of code (hello world): 20 → 3
- Documentation pages: 5 → 30

## 7.2 Phase 2: Features (Months 3-4)

**Goal: Add essential features**

| Feature | Priority | Effort |
|---------|----------|--------|
| Adaptive timestep | P0 | Medium |
| Checkpointing | P1 | Low |
| Error control | P1 | Medium |
| Multi-field extension | P2 | High |
| Stochastic extension | P2 | High |

**Success Metrics:**
- Simulation stability: 80% → 95%
- User-reported issues: Track and fix
- Feature requests: Prioritize top 5

## 7.3 Phase 3: Performance (Months 5-6)

**Goal: Make UET fast enough**

| Feature | Priority | Effort |
|---------|----------|--------|
| Numba JIT compilation | P0 | Medium |
| Vectorization | P0 | Low |
| Parallel solver | P1 | High |
| GPU support (CuPy) | P2 | Very High |

**Success Metrics:**
- Speed improvement: 10x with Numba
- Memory efficiency: 2x better
- Scalability: Handle 256³ grids

## 7.4 Phase 4: Ecosystem (Months 7-12)

**Goal: Build community and ecosystem**

| Feature | Priority | Effort |
|---------|----------|--------|
| Plugin system | P0 | High |
| Example gallery expansion | P0 | Medium |
| Export to other tools | P1 | Medium |
| Web interface | P2 | Very High |
| Package on PyPI | P0 | Low |

**Success Metrics:**
- GitHub stars: 0 → 100
- Active users: 1 → 50
- User-contributed examples: 0 → 20
- PyPI downloads: 0 → 500/month

---

# 8. Target Audiences

## 8.1 Primary Audiences

### 1. Educators (⭐⭐⭐⭐⭐ Best fit)

**Why UET:**
- Simple enough to teach
- Visual demos
- Cross-domain examples

**Needs:**
- Course materials
- Jupyter notebooks
- Student exercises

**Adoption Strategy:**
- Create teaching pack
- Offer workshops
- Free for education

### 2. Researchers (Exploratory) (⭐⭐⭐⭐ Good fit)

**Why UET:**
- Quick prototyping
- Pattern exploration
- Cross-domain insights

**Needs:**
- Flexibility
- Performance (moderate)
- Documentation

**Adoption Strategy:**
- Publish examples
- Academic outreach
- Conference presentations

### 3. Students (⭐⭐⭐⭐⭐ Best fit)

**Why UET:**
- Learning tool
- Project platform
- Portfolio building

**Needs:**
- Tutorials
- Examples
- Support

**Adoption Strategy:**
- University partnerships
- Student competitions
- Thesis projects

## 8.2 Secondary Audiences

### 4. Cross-Domain Teams (⭐⭐⭐⭐ Good fit)

**Why UET:**
- Common vocabulary
- Shared framework
- Collaboration tool

**Needs:**
- Stability
- Documentation
- Integration

### 5. Industry (Prototyping) (⭐⭐⭐ Maybe)

**Why UET:**
- Rapid prototyping
- Concept validation
- Exploration

**Needs:**
- Performance
- Reliability
- Support

**Note:** Not for production use

---

# 9. Success Criteria

## 9.1 Technical Success

| Metric | Current | 6 Months | 12 Months |
|--------|---------|----------|-----------|
| **Code quality** | Basic | Good | Excellent |
| **Performance** | 1x | 10x | 50x |
| **Features** | Core only | + Adaptive | + Extensions |
| **Documentation** | 5 pages | 50 pages | 100 pages |
| **Test coverage** | 0% | 50% | 80% |

## 9.2 Adoption Success

| Metric | Current | 6 Months | 12 Months |
|--------|---------|----------|-----------|
| **GitHub stars** | 0 | 100 | 500 |
| **Active users** | 1 | 50 | 200 |
| **PyPI downloads** | 0 | 500/mo | 2000/mo |
| **Examples** | 50 | 100 | 200 |
| **Contributors** | 1 | 5 | 15 |

## 9.3 Impact Success

| Metric | Target |
|--------|--------|
| **Papers using UET** | 5+ |
| **Courses using UET** | 3+ |
| **Domains applied** | 10+ |
| **User testimonials** | 20+ |

---

# 10. Risk Assessment

## 10.1 Critical Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **No adoption** | High | Fatal | Education focus |
| **Credibility loss** | Medium | High | Honest claims |
| **Maintenance burden** | Medium | High | Keep simple |
| **Competition** | Medium | Medium | Niche focus |

## 10.2 Risk Mitigation

1. **No Adoption Risk**
   - Focus on education (guaranteed users)
   - Make it easy to try (5-minute start)
   - Show value immediately (gallery)

2. **Credibility Risk**
   - Never over-claim
   - Be transparent about limitations
   - Welcome criticism

3. **Maintenance Risk**
   - Keep core simple
   - Good documentation
   - Automated testing

---

# 11. Strategic Recommendations

## 11.1 Immediate Actions (Next 30 Days)

1. ✅ **Create domain templates**
   - NeuralTemplate, EconomicsTemplate, BiologyTemplate
   - Reduce learning curve dramatically

2. ✅ **Write quick start guide**
   - 5-minute tutorial
   - Copy-paste examples
   - Immediate gratification

3. ✅ **Package on PyPI**
   - `pip install uet`
   - Lower barrier to entry

4. ✅ **Create tutorial notebooks**
   - Jupyter notebooks
   - Interactive learning
   - Binder integration

## 11.2 Medium-Term Actions (3-6 Months)

1. **Performance improvements**
   - Numba JIT
   - Vectorization
   - 10x speedup target

2. **Feature additions**
   - Adaptive timestep
   - Checkpointing
   - Error control

3. **Community building**
   - GitHub presence
   - User examples
   - Documentation expansion

## 11.3 Long-Term Vision (12+ Months)

**UET becomes:**
- The standard tool for teaching coupled dynamics
- A common language for cross-domain research
- A bridge between theory and computation

**Success looks like:**
- 200+ active users
- 10+ courses using UET
- 5+ papers citing UET
- Self-sustaining community

---

# 12. Conclusion

## 12.1 Core Thesis

> **UET is not trying to be the BEST tool.**
> **UET is trying to be the EASIEST tool that WORKS.**

Like Python:
- Not the fastest (C++ is faster)
- Not the most powerful (Lisp is more powerful)
- But: Easy to learn, good enough, widely adopted

UET:
- Not the most accurate (specialized tools better)
- Not the fastest (optimized solvers faster)
- But: Easy to learn, flexible enough, cross-domain

## 12.2 Value Proposition

**For educators:** Best tool to teach coupled dynamics
**For researchers:** Best tool to explore patterns
**For students:** Best tool to learn modeling
**For teams:** Best tool to communicate across domains

## 12.3 Final Assessment

**Strengths:**
- ⭐⭐⭐⭐⭐ Simplicity
- ⭐⭐⭐⭐⭐ Cross-domain applicability
- ⭐⭐⭐⭐⭐ Educational value
- ⭐⭐⭐⭐ Visualization

**Weaknesses:**
- ⭐⭐ Performance
- ⭐⭐ Maturity
- ⭐ Community
- ⭐⭐ Scope limitations

**Overall Viability:** ⭐⭐⭐⭐ (4/5)

**Recommendation:** **PROCEED with education-first strategy**

---

# Appendix A: Comparison Matrix

## A.1 Feature Comparison

| Feature | UET | NumPy | FEniCS | Brian2 | Mesa |
|---------|-----|-------|--------|--------|------|
| Ease of use | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Performance | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Flexibility | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| Documentation | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| Community | ⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Cross-domain | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐ | ⭐⭐ |

---

*End of Comprehensive Analysis*

**Next Steps:** Implement Phase 1 improvements (Domain Templates + Documentation)


---


# 🔹 Source: file_12.md

# UET Framework - Language Reference

## 🎯 What is UET?

**UET is NOT new physics. UET is a COMMON LANGUAGE.**

A universal framework for modeling coupled dynamics across ANY domain.
Like math is a language for science, UET is a language for complex systems.

---

## 📐 Core Equations

```
∂C/∂t = κ∇²C - ∂V/∂C - β(C - I) + s
∂I/∂t = κ∇²I - ∂V/∂I - β(I - C)
```

Where:
- **V(φ) = (φ² - 1)² / 4** (Double-well potential)

---

## 🔤 Symbol Dictionary

| Symbol | Name | Meaning | Units |
|--------|------|---------|-------|
| **C** | Conscious Field | Observable/Visible state | domain-dependent |
| **I** | Instinctive Field | Hidden/Latent state | domain-dependent |
| **κ** | Kappa | Diffusion/Spreading rate | length²/time |
| **β** | Beta | Coupling strength | 1/time |
| **s** | Source | External drive/bias | field/time |
| **V(φ)** | Potential | Energy landscape | energy/volume |
| **Ω** | Omega | Total energy | energy |

---

## 🗺️ Domain Mapping Guide

### Physics
| UET | Maps to |
|-----|---------|
| C | Visible matter / Observable fields |
| I | Dark matter / Hidden sectors |
| β | Gravitational coupling |
| κ | Speed of propagation |
| V | Potential energy |

### Neuroscience  
| UET | Maps to |
|-----|---------|
| C | Excitatory neural activity |
| I | Inhibitory neural state |
| β | E-I balance |
| κ | Axonal connectivity |
| V | Attractor landscape |

### Economics
| UET | Maps to |
|-----|---------|
| C | Market price |
| I | Intrinsic/Fundamental value |
| β | Market efficiency |
| κ | Information spreading |
| s | External shocks (news) |

### Biology
| UET | Maps to |
|-----|---------|
| C | Activator (morphogen A) |
| I | Inhibitor (morphogen B) |
| β | Reaction rate |
| κ | Diffusion coefficient |
| V | Chemical potential |

### Machine Learning
| UET | Maps to |
|-----|---------|
| C | Observable features |
| I | Latent representation |
| β | Learning rate |
| κ | Weight sharing/convolution |
| V | Loss landscape |

---

## ⚙️ Key Parameters

### Double-Well Potential V(φ)
```
V(φ) = (φ² - 1)² / 4

Properties:
- Minima at φ = ±1
- Maximum at φ = 0
- Barrier height = 1/4
```

This creates **bistable dynamics**:
- Two stable states (φ = ±1)
- Energy barrier between them
- Spontaneous symmetry breaking

### Coupling β
```
β controls how strongly C and I interact:
- β → 0: C and I evolve independently
- β → ∞: C ≈ I (locked together)
- β moderate: Rich coupled dynamics
```

### Diffusion κ
```
κ controls spatial spreading:
- κ → 0: Local dynamics only
- κ large: Global/smooth patterns
- κ moderate: Pattern formation
```

---

## 📊 Observable Quantities

| Quantity | Formula | Meaning |
|----------|---------|---------|
| **Energy Ω** | ∫[κ(∇C)²/2 + V(C) + κ(∇I)²/2 + V(I) + β(C-I)²/2]dx | Total system energy |
| **Order Parameter** | ⟨C⟩ | Average field value |
| **Coherence** | 1 - Var(C)/Max | Spatial uniformity |
| **Entropy** | -∫P(C)log(P(C))dC | Disorder measure |
| **C-I Gap** | ⟨(C-I)²⟩ | Hidden-visible mismatch |

---

## 🧪 Simulation Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `grid_size` | 32 | Spatial resolution (NxN) |
| `dt` | 0.01 | Time step |
| `T` | 10.0 | Total simulation time |
| `kappa` | 0.3 | Diffusion coefficient |
| `beta` | 0.5 | Coupling strength |
| `s` | 0.0 | External bias |
| `V_type` | quartic | Potential type |

---

## 🎬 Gallery Categories

| Category | Demos | Purpose |
|----------|-------|---------|
| **Archetypes** | BIAS_C, BIAS_I, SYM | Basic dynamics |
| **Physics** | Einstein, NR, GR | Field equations |
| **Neural** | Seizure, Sleep | Brain dynamics |
| **Finance** | Stock, Bubble | Market dynamics |
| **Traffic** | Rush hour, Smart | Flow dynamics |
| **Biology** | Physarum, Coffee | Pattern formation |
| **3D** | Galaxy, Shell | Volumetric |

---

## 🔧 How to Use

### 1. Identify your domain
What are you trying to model?

### 2. Map variables
- What's your "observable" → C
- What's your "hidden state" → I
- How do they interact → β
- How do they spread → κ

### 3. Choose initial conditions
- Symmetric? Biased? Random?

### 4. Run simulation
```bash
python scripts/run_case.py --kappa 0.3 --beta 0.5 --s 0.1
```

### 5. Analyze results
- Energy evolution
- Pattern formation
- Equilibrium states

---

## 📖 Philosophy

> **"UET doesn't explain everything. UET provides a language TO explain things."**

Like:
- Math doesn't create physics, but describes it
- Programming languages don't solve problems, but express solutions
- UET doesn't discover phenomena, but models them

**You bring the domain knowledge.**
**UET provides the vocabulary.**

---

## 🔗 Resources

- Gallery: `runs_gallery/gallery.html`
- Scripts: `scripts/`
- Docs: `docs/`
- Examples: `runs_demo/`

---

*UET Framework v0.1 - A Common Language for Complex Systems*


---


# 🔹 Source: file_13.md

# UET Framework - Limitations & Non-Claims

## ⚠️ What UET Does NOT Claim

This document defines clear boundaries. UET is honest about what it is and isn't.

---

## ❌ UET Does NOT:

| Non-Claim | Explanation |
|-----------|-------------|
| ❌ **Discover new physics** | UET uses existing mathematics. No new particles, forces, or laws. |
| ❌ **Replace established theories** | GR, QFT, SM are correct. UET doesn't compete with them. |
| ❌ **Prove anything** | UET is a modeling language, not a proof. |
| ❌ **Explain fundamentally** | UET describes patterns, doesn't explain "why". |
| ❌ **Predict the future** | UET simulates dynamics, not prophecy. |
| ❌ **Solve the cosmological constant** | λ problem needs real QFT, not toy models. |
| ❌ **Unify all physics** | The name "Unified" is aspirational, not factual. |

---

## 🚫 Forbidden Claims

**Do NOT use UET to claim:**

1. ❌ "UET explains dark matter"
   - ✅ Say: "UET models hidden-visible coupling, similar to dark-visible matter interaction"

2. ❌ "UET solves quantum gravity"
   - ✅ Say: "UET provides visualization tools for field dynamics"

3. ❌ "UET predicts [specific physical value]"
   - ✅ Say: "UET fits parameters to match observed behavior"

4. ❌ "UET is the theory of everything"
   - ✅ Say: "UET is a common language for modeling coupled systems"

5. ❌ "UET is scientifically proven"
   - ✅ Say: "UET is a mathematical framework with useful applications"

---

## ✅ UET IS:

| What UET Is | Description |
|-------------|-------------|
| ✅ **A modeling language** | Vocabulary for complex systems |
| ✅ **A simulation framework** | Tools to run coupled dynamics |
| ✅ **An educational resource** | Gallery of demos for teaching |
| ✅ **A bridge between domains** | Same equations, different interpretations |
| ✅ **Simple and accessible** | 2 PDEs, 5 parameters, infinite applications |

---

## 📏 Scope Boundaries

### UET CAN model:
- Coupled two-field dynamics
- Pattern formation
- Phase transitions
- Equilibrium-seeking behavior
- Diffusion + reaction + coupling

### UET CANNOT model:
- Quantum superposition (no ℏ)
- Relativistic effects (no c, except as analogy)
- Discrete/particle systems (continuous fields only)
- Non-Markovian dynamics (no memory)
- Stochastic processes (deterministic PDEs)

---

## 🎯 Philosophy Summary

```
UET doesn't claim to be the BIGGEST.
UET claims to be the SIMPLEST that WORKS.

Not: "This is the truth"
But: "This is a useful way to think"

Not: "We discovered something new"
But: "We organized what's known"

Not: "Theory of Everything"
But: "Language for Anything"
```

---

## 📝 How to Cite

When using UET, always acknowledge:

> "UET is a phenomenological framework for coupled field dynamics.
> It does not claim fundamental physics validity but provides
> a common language for modeling complex systems across domains."

---

## 🤝 Honest Collaboration

UET is designed for:
- **Domain experts** to bring real data
- **Researchers** to test hypotheses
- **Educators** to visualize concepts
- **Engineers** to prototype models

UET provides the framework. **You** provide the expertise.

---

## 🔬 Falsifiability (How to Prove UET Wrong)

**UET welcomes criticism. We WANT to be proven wrong.**

### One Counterexample is Enough

Like Einstein said about Relativity:
> "No amount of experimentation can ever prove me right;
> a single experiment can prove me wrong."

**Same for UET.**

---

### ❌ How to Falsify UET:

Show **ONE** of these:

1. **Mathematical inconsistency**
   - Find internal contradiction in equations
   - Show that ∂C/∂t + ∂I/∂t equations violate conservation when they should conserve
   - Prove numerical solver gives wrong results for known analytical solutions

2. **Domain where it fundamentally fails**
   - Find coupled system where UET framework CANNOT be applied at all
   - Not "hard to fit" but "impossible in principle"
   - Example: "Quantum entanglement cannot be modeled by C-I coupling even approximately"

3. **Better alternative exists**
   - Show simpler equations that do the same thing
   - Prove UET adds unnecessary complexity
   - Demonstrate that standard methods always outperform UET

4. **Prediction failure**
   - UET predicts X, observation shows NOT-X
   - Example: "UET says β>0 always stabilizes, but here's a case where it destabilizes"

---

### ✅ What Would NOT Falsify UET:

- ❌ "UET doesn't explain quantum gravity" → We never claimed it does
- ❌ "UET is just reaction-diffusion" → Yes, we know. That's the point.
- ❌ "UET doesn't predict Higgs mass" → Not in scope
- ❌ "I don't like the name" → Not a scientific criticism

---

### 🎯 Challenge to Critics:

**We actively seek falsification.**

If you can show:
1. Internal mathematical contradiction
2. Fundamental domain where framework breaks
3. Simpler alternative that works better
4. Specific prediction that fails

**We will acknowledge it immediately and either:**
- Fix the framework
- Narrow the scope
- Abandon it entirely

**This is how science works.**

---

### 💭 Why We Want to Be Wrong:

```
Being wrong = Learning opportunity
Being right = Dangerous (overconfidence)

"I want to be proven wrong because I want to LEARN,
not because I want to be RIGHT."
```

**Criticism welcome. Bring your best counterexample.** 🔥

---

*UET: Simple equations, honest limitations, broad applications, open to falsification.*


---


# 🔹 Source: file_14.md

# UET Position Statement

## 🎯 What UET Is

**UET is a Meta-Framework, not a New Theory.**

UET does not invent new physics. UET **unifies existing knowledge** into a common language.

---

## 🌉 UET as a Bridge

```
Established Physics  ←→  UET  ←→  Computational Models
   (Fundamental)              (Phenomenological)
```

### Left Side: Established Theories
- Thermodynamics
- Einstein's Field Equations
- Statistical Mechanics
- Quantum Field Theory

### Right Side: Practical Applications
- Computational dynamics
- Agent-based models
- Data-driven simulations
- Phenomenological descriptions

### UET in the Middle:
**Translation layer that connects both sides**

---

## 💪 UET's Potential

UET has the potential to:

1. **Extend Thermodynamics**
   - From equilibrium → non-equilibrium
   - From isolated → coupled systems
   - From objective → subjective dynamics

2. **Augment Einstein's Framework**
   - From pure GR → phenomenological field models
   - From spacetime → general coupled fields
   - From fundamental → effective theories

3. **Bridge Statistical Mechanics**
   - From microscopic → mesoscopic
   - From ensemble averages → individual trajectories
   - From physics → computation

---

## 🔗 Not Replacement, But Extension

| Theory | UET's Role |
|--------|------------|
| **Thermodynamics** | Extend to non-equilibrium, coupled systems |
| **Einstein's GR** | Provide phenomenological field framework |
| **Statistical Mechanics** | Bridge to computational/agent models |
| **Reaction-Diffusion** | Unify under common C-I language |

**UET doesn't compete. UET complements.**

---

## 📐 Core Philosophy

> **"UET is not new knowledge. UET is a new way to ORGANIZE knowledge."**

Like:
- Calculus didn't invent physics, but organized it
- Linear algebra didn't create transformations, but described them
- UET doesn't discover phenomena, but **connects** them

---

## 🎯 The Vision

**From fragmented knowledge → Unified language**

Different fields use different equations for similar phenomena:
- Physics: Field equations
- Biology: Reaction-diffusion
- Economics: Price dynamics
- Neuroscience: Neural field theory

**UET says:** "These are all the same structure"

```
∂C/∂t = κ∇²C - ∂V/∂C - β(C-I) + s
∂I/∂t = κ∇²I - ∂V/∂I - β(I-C)
```

One language. Many interpretations.

---

## 🚀 Potential Impact

If successful, UET could:

1. **Enable cross-domain collaboration**
   - Physicists ↔ Biologists speak same language
   - Economists ↔ Neuroscientists share models

2. **Accelerate understanding**
   - Solution in one domain → applies to another
   - Pattern in physics → insight for biology

3. **Simplify complexity**
   - Reduce many equations → one framework
   - Universal parameters (C, I, β, κ)

---

## ⚠️ Honest Limitations

UET is NOT:
- ❌ Fundamental physics
- ❌ Theory of everything
- ❌ Replacement for established theories

UET IS:
- ✅ Meta-framework
- ✅ Common language
- ✅ Bridge between domains
- ✅ Extension/augmentation tool

---

*UET: Not new physics. New perspective.*


---


# 🔹 Source: file_15.md

# UET R0-E10 — Band Stability + Richer Run Metrics v0.1
**Goal:** ทำให้ band/presets “นิ่ง” ภายใต้หลาย seed และวัดความ “ตึง/ใกล้ fail” จาก run artifacts

## 1) Expand dt ladder to multiple seeds
```bash
python scripts/expand_dt_ladder_matrix_seeds.py \
  --matrix_in dt_ladder_matrix.csv \
  --matrix_out dt_ladder_matrix_seeds.csv \
  --seeds 0;1;2;3;4
```

## 2) Run ladder
```bash
python scripts/run_dt_ladder.py --matrix dt_ladder_matrix_seeds.csv --out dt_ladder_runs_seeds --overwrite
```

## 3) Compute metrics from timeseries/summary
```bash
python scripts/compute_run_metrics.py --ledger dt_ladder_runs_seeds/dt_ladder_ledger.csv
```
Outputs `dt_ladder_runs_seeds/run_metrics.csv` with:
- `dOmega_max, dOmega_median`
- `tight_frac` (fraction of accepted steps with dΩ > -eps)
- `dt_collapse_ratio = dt_min/dt`
- `backtracks_density = dt_backtracks_total/steps_accepted`

## 4) Band stability check (per seed → mode)
```bash
python scripts/band_stability_check.py \
  --ledger dt_ladder_runs_seeds/dt_ladder_ledger.csv \
  --write_band_map
```
Outputs:
- `band_by_seed.csv`
- `band_stability_by_case.csv`
- `band_map_mode.csv`


---


# 🔹 Source: file_16.md

# UET R0-E11 — Strict Robustness + Data-Driven Bands v0.1
**Goal:** ทำให้ “ผ่านจริง” = PASS ทุก seed และ downgrade band ถ้า “ผ่านแบบตึง” ตาม metrics

## Strict dt_max per case
```bash
python scripts/strict_dt_max_pass_by_case.py \
  --ledger dt_ladder_runs_seeds/dt_ladder_ledger.csv \
  --require_seed_coverage
```

## Band map from metrics
```bash
python scripts/band_map_from_metrics.py \
  --ledger dt_ladder_runs_seeds/dt_ladder_ledger.csv \
  --run_metrics dt_ladder_runs_seeds/run_metrics.csv \
  --out band_map_metrics.csv \
  --strict_all_seeds --require_seed_coverage
```
Metric gates (defaults):
- tight_frac_max=0.2
- dt_collapse_ratio_min=0.5
- backtracks_density_max=0.5


---


# 🔹 Source: file_17.md

# UET R0-E12 — Seed-Robust dt Presets + Threshold Calibration v0.1
**Goal:** สร้าง dt presets ที่ “ล็อกแล้วนิ่ง” โดย
1) ต้อง PASS ทุก seed (strict)
2) ไม่ “ผ่านแบบตึง” (ใช้ run_metrics + thresholds)

---

## 1) Calibrate thresholds from run_metrics
```bash
python scripts/calibrate_metric_thresholds.py \
  --run_metrics dt_ladder_runs_seeds/run_metrics.csv \
  --use_only_pass
```
Output: `metric_thresholds.json` (quantile-based)

---

## 2) Extract strict global dt presets (model × integrator)
```bash
python scripts/extract_dt_presets_strict.py \
  --ledger dt_ladder_runs_seeds/dt_ladder_ledger.csv \
  --strict_all_seeds --require_seed_coverage \
  --metrics dt_ladder_runs_seeds/run_metrics.csv \
  --thresholds_json dt_ladder_runs_seeds/metric_thresholds.json
```
Output folder: `dt_presets_strict/` with
- `dt_presets_strict.json`
- `dt_presets_strict_selected.csv`

---

## 3) Extract strict band-aware dt presets (band × model × integrator)
ต้องมี `band_map.csv` ก่อน (จาก R0-E9/R0-E10/R0-E11)
```bash
python scripts/extract_band_dt_presets_strict.py \
  --ledger dt_ladder_runs_seeds/dt_ladder_ledger.csv \
  --band_map band_map_metrics.csv \
  --strict_all_seeds --require_seed_coverage \
  --metrics dt_ladder_runs_seeds/run_metrics.csv \
  --thresholds_json dt_ladder_runs_seeds/metric_thresholds.json
```
Output folder: `band_dt_presets_strict/` with
- `band_dt_presets_strict.json`
- `band_dt_presets_strict_selected.csv`

---

## 4) Freeze into baseline manifest (audit)
`freeze_baseline_manifest.py` รองรับ `--metric_thresholds` และ `--band_stability` แล้ว

```bash
python scripts/freeze_baseline_manifest.py \
  --out baseline/baseline_manifest.json \
  --ledger dt_ladder_runs_seeds/dt_ladder_ledger.csv \
  --band_map band_map_metrics.csv \
  --metric_thresholds dt_ladder_runs_seeds/metric_thresholds.json \
  --overwrite
```

---

## Next step (R0-E13)
- ทำ “preset stress test”: ใช้ dt presets แล้วสุ่มเคสใหม่ใน band เดิมเพื่อวัด generalization
- ทำ threshold tuning แบบ multi-objective (speed vs margin)


---


# 🔹 Source: file_18.md

# UET R0-E13 — Preset Stress Test + Generalization Gate v0.1
**Goal:** ตรวจว่า dt presets (strict/global/band-aware) “generalize” ได้จริง  
ไม่ใช่แค่รอดกับชุด ladder/atlas ที่เราตั้งใจเลือก

> หลักคิด: ถ้า preset ใช้จริงได้ ต้อง “รอด” ภายใต้ perturbation ของพารามิเตอร์ + หลาย seed ของ init

---

## 1) Stress Spec
ใช้ `stress_spec.json` กำหนด:
- anchor cases (base_case_id, model, params)
- band label (DEMO/MID/BOUNDARY/HARD)
- perturbation distributions ของพารามิเตอร์ (top-level และ quartic coefficients)
- meta (N,L,T,seeds,integrators,n_per_case)

---

## 2) Generate stress matrix (พร้อม dt จาก presets)
```bash
python scripts/generate_stress_matrix.py \
  --spec stress_spec.json \
  --band_dt_presets dt_ladder_runs_seeds/band_dt_presets_strict/band_dt_presets_strict.json \
  --dt_presets dt_ladder_runs_seeds/dt_presets_strict/dt_presets_strict.json \
  --out stress_matrix.csv
```

Output:
- `stress_matrix.csv` (พร้อม `dt_list` แบบ single dt ต่อ integrator)
- ถ้ามี preset ขาด จะได้ `stress_missing_presets.csv`

> หมายเหตุ: matrix นี้ compatible กับ `run_dt_ladder.py`

---

## 3) Run stress test
```bash
python scripts/run_dt_ladder.py --matrix stress_matrix.csv --out stress_runs --overwrite
```

---

## 4) Summarize
```bash
python scripts/summarize_stress_test.py --ledger stress_runs/dt_ladder_ledger.csv
```
Outputs `stress_runs/stress_summary/stress_summary.csv` (pass rate + Wilson CI + fail code histogram)

---

## 5) Generalization Gate (fail-fast)
```bash
python scripts/gate_stress_results.py \
  --summary_csv stress_runs/stress_summary/stress_summary.csv \
  --min_pass_rate 0.95 \
  --min_ci_lo 0.90
```
Outputs `stress_gate_report.json` and exit code 2 on FAIL.

**Interpretation**
- ถ้า FAIL: presets/thresholds/bands ยังไม่ robust → ต้องลด dt หรือปรับ threshold (tight/collapse/btden) หรือปรับ band rule

---

## 6) Freeze evidence to baseline manifest
```bash
python scripts/freeze_baseline_manifest.py \
  --out baseline/baseline_manifest.json \
  --stress_spec stress_spec.json \
  --stress_report stress_runs/stress_summary/stress_gate_report.json \
  --overwrite
```

---

## Recommended default (เริ่มต้น)
- n_per_case: 20
- seeds: 0;1;2;3;4
- integrators: semiimplicit;stabilized
- Gate: min_pass_rate=0.95, min_ci_lo=0.90

---

## Next step (R0-E14)
- ทำ “adaptive stress”: ถ้า FAIL ให้ auto-focus ไปที่พารามิเตอร์/ย่านที่พังบ่อย แล้ว refine dt/band rule เฉพาะจุด


---


# 🔹 Source: file_19.md

# UET R0-E14 — Adaptive Stress + Failure-Mode Targeting v0.1
**Goal:** ถ้า stress gate (R0-E13) FAIL → ไม่วนมั่ว  
ให้สร้าง stress รอบถัดไปที่ “ยิงตรงจุด” โดยอัตโนมัติ:
- โฟกัสกลุ่มที่ fail เยอะสุด (band×model×integrator×fail_code)
- jitter รอบตัวอย่างที่ fail จริง (local neighborhood)
- ทำ A/B test ด้วย dt scaling เพื่อแยก “dt issue” vs “model/constraint issue”

> ใช้เพื่อปรับ dt presets / band rule / metric thresholds แบบ evidence-driven

---

## 1) Make failure-mode report (เร็ว)
```bash
python scripts/failure_mode_report.py \
  --ledger stress_runs/dt_ladder_ledger.csv
```
Output: `stress_runs/failure_mode_report.json`

---

## 2) Generate adaptive stress matrix (focus on failures)
ต้องมี `stress_matrix.csv` ที่ใช้รันรอบแรก และ `dt_ladder_ledger.csv` ของผล
```bash
python scripts/make_adaptive_stress_matrix.py \
  --stress_matrix_in stress_matrix.csv \
  --stress_ledger stress_runs/dt_ladder_ledger.csv \
  --out adaptive_stress_matrix.csv \
  --top_groups 5 \
  --cases_per_group 5 \
  --jitters_per_case 3 \
  --dt_scales 1.0;0.5
```

สิ่งที่มันทำ:
- เลือก top fail groups
- เลือกเคสที่ fail หลาย seed ก่อน
- สุ่มพารามิเตอร์ใหม่แบบ “ใกล้เคียง” (log jitter)
- สร้าง variant 2 แบบ:
  - dt×1.0 (ดูว่ามันยัง fail ไหม)
  - dt×0.5 (ถ้าหาย fail แปลว่า dt ยังใหญ่ไป)

> Matrix ที่สร้างจะใส่คอลัมน์เพิ่ม: `variant, origin_case_id, origin_fail_code`  
และ `run_dt_ladder.py` จะ carry ลง ledger แล้ว

---

## 3) Run adaptive stress
```bash
python scripts/run_dt_ladder.py --matrix adaptive_stress_matrix.csv --out adaptive_runs --overwrite
python scripts/summarize_stress_test.py --ledger adaptive_runs/dt_ladder_ledger.csv --group band_model_integrator_variant
```

ดูผลแบบ A/B:
- compare `variant` ที่ dt=1 vs dt=0.5
- ถ้า dt=0.5 ผ่านเยอะขึ้น → ปรับ dt preset หรือ cap rule
- ถ้า dt=0.5 ยัง fail → ไปดู fail_code และ constraints/terms ที่เกี่ยวข้อง (ไม่ใช่ dt ล้วน)

---

## 4) Gate (optional)
ใช้ gate เดิมได้:
```bash
python scripts/gate_stress_results.py \
  --summary_csv adaptive_runs/stress_summary/stress_summary.csv \
  --min_pass_rate 0.95 --min_ci_lo 0.90
```

---

## 5) What to change after adaptive
Checklist:
- ถ้า fail เฉพาะ stabilized: ปรับ `stab_scale/margin` หรือ tighten metric thresholds
- ถ้า fail เฉพาะ boundary band: ลด dt preset เฉพาะ band (ไม่ลดทั้งระบบ)
- ถ้า fail_code บอก NaN/overflow: เพิ่ม clamp/regularize ใน solver (audit ก่อน)
- ถ้า fail เพราะ coercivity: กลับไป R0-B2 (เงื่อนไข coercive) แล้ว fix param domain

---

## Next step (R0-E15)
- ทำ “auto-fix proposals”:
  - เสนอ dt scale ใหม่ต่อ band
  - เสนอ threshold ใหม่จากผล A/B
  - ทำ PR checklist เพื่อ lock baseline รอบใหม่


---


# 🔹 Source: file_20.md

# UET R0-E15 — Auto-fix Proposals + Baseline Refresh Loop v0.1
**Goal:** ปิด loop จาก R0-E13/R0-E14 ให้กลายเป็น “ระบบปรับปรุงแบบ evidence-driven”  
โดยไม่ต้องเดา: ใช้ผล A/B (dt scaling variants) → สร้างข้อเสนอปรับ dt presets → apply → re-run → freeze baseline

---

## 1) Inputs
- Adaptive run summary (จาก R0-E14):
  - `adaptive_runs/stress_summary/stress_summary.csv` **(ต้อง group = band_model_integrator_variant)**
- (optional) current presets:
  - `band_dt_presets_strict.json` (หรือ band_dt_presets.json)
- (optional) gate report:
  - `adaptive_runs/stress_summary/stress_gate_report.json`

---

## 2) Generate preset update proposals (from variants)
> เลือก “dt scale ที่เล็กสุดที่ผ่าน gate” ต่อ (band×model×integrator)

```bash
python scripts/propose_preset_updates_from_variant_summary.py \
  --variant_summary_csv adaptive_runs/stress_summary/stress_summary.csv \
  --band_presets_json dt_ladder_runs_seeds/band_dt_presets_strict/band_dt_presets_strict.json \
  --min_pass_rate 0.95 --min_ci_lo 0.90 \
  --out preset_update_proposals.csv
```

Output:
- `preset_update_proposals.csv`

**Interpretation**
- `gate_pass_at_recommended_scale=1` → scale นี้ควร “พอ” (ตาม evidence)
- ถ้าเป็น 0 → ไม่มี variant ไหนผ่าน; เลือก scale ที่เล็กสุดที่มี → ชี้ว่า “ต้องแก้เชิงโมเดล/constraint หรือเพิ่ม scale ต่ำกว่าเดิม”

---

## 3) Render report (อ่านง่าย)
```bash
python scripts/render_preset_update_report.py \
  --updates_csv preset_update_proposals.csv \
  --out_md preset_update_report.md \
  --only_changes
```

---

## 4) Apply proposals to presets
### 4.1 band-aware presets
```bash
python scripts/apply_preset_updates.py \
  --presets_in dt_ladder_runs_seeds/band_dt_presets_strict/band_dt_presets_strict.json \
  --updates_csv preset_update_proposals.csv \
  --presets_out band_dt_presets_strict_updated.json \
  --mode band \
  --apply_only_gate_pass
```

### 4.2 global presets (ถ้าต้องการ)
```bash
python scripts/apply_preset_updates.py \
  --presets_in dt_ladder_runs_seeds/dt_presets_strict/dt_presets_strict.json \
  --updates_csv preset_update_proposals.csv \
  --presets_out dt_presets_strict_updated.json \
  --mode global \
  --apply_only_gate_pass
```

---

## 5) Re-run stress with updated presets (sanity loop)
1) Generate new stress matrix from spec (R0-E13) แต่ใช้ presets_updated  
2) Run + gate  
3) ถ้าผ่าน → freeze baseline

---

## 6) Freeze baseline (lock evidence)
ใช้ `freeze_baseline_manifest.py` บันทึก:
- presets updated
- stress_spec + stress_report
- metric_thresholds + band_map + stability (ถ้ามี)

> แนวคิด: baseline คือ “ชุด configuration + evidence hash” ที่ repeatable

---

## 7) When proposals are not enough
ถ้า adaptive A/B dt scaling (1.0 vs 0.5) ยัง FAIL ทั้งคู่:
- นี่คือสัญญาณว่า “ไม่ใช่ dt อย่างเดียว”
- ต้องไปดู fail_code และกลับไปแก้:
  - coercivity/domain constraints (R0-B2)
  - solver numerical guards (clamps, NaN detection, boundary conditions)
  - band rule / thresholds (R0-E11/E12)

---

## Next step (R0-E16)
- ทำ “auto-run loop driver” (single command):
  - run adaptive → summarize → propose → apply → rerun → freeze
- เพิ่ม dt_scales grid (1.0, 0.7, 0.5, 0.35, 0.25) แบบ adaptive


---


# 🔹 Source: file_22.md

# UET R0-E16 — One-Command Loop Driver + Adaptive dt Grid v0.1
**Goal:** รวม R0-E13→E15 ให้ “สั่งครั้งเดียว” แล้วระบบทำ:
1) stress test (generalization)
2) gate
3) ถ้า FAIL → adaptive stress targeting + A/B dt scales
4) propose dt preset updates
5) apply updates
6) วนซ้ำจน PASS หรือถึง max_iters
7) freeze baseline manifest พร้อม evidence hashes

> มุ่งให้ pipeline “repeatable + audit-able” มากกว่าทำ manual ทีละคำสั่ง

---

## 1) New
- `scripts/loop_driver.py`
- `freeze_baseline_manifest.py` เพิ่ม `--extra_files` (semicolon-separated) เพื่อ hash artifacts เพิ่ม

---

## 2) Config template
ใช้ `loop_config.json` (ดู template ที่ให้)

**paths**
- `stress_spec`
- `band_dt_presets`
- `dt_presets` (optional)
- `baseline_manifest`
- `work_dir`
- `scripts_dir` (default: `scripts`)

**params**
- `max_iters`
- `min_pass_rate`, `min_ci_lo`
- `dt_scales_grid` เช่น `1.0;0.7;0.5;0.35;0.25`
- `top_groups`, `cases_per_group`, `jitters_per_case`
- `prefer_keep_if_pass` (dt×1 ผ่านแล้วไม่ลด)
- `apply_only_gate_pass` (apply เฉพาะ proposal ที่ gate ผ่าน)
- `freeze_extra_files` (optional)

---

## 3) Run (one command)
```bash
python scripts/loop_driver.py --config loop_config.json
```

**Dry-run (ดู command plan)**
```bash
python scripts/loop_driver.py --config loop_config.json --dry
```

---

## 4) How it decides dt scale
Adaptive stress สร้าง variant ตาม `dt_scales_grid`:
- ถ้า dt×1 ยัง FAIL แต่ dt×0.5 ผ่าน → proposal จะเลือก 0.5
- ถ้าผ่านหลาย scale → default เลือก scale เล็กสุดที่ผ่าน (robust)
- ถ้า `prefer_keep_if_pass=true` → ถ้า dt×1 ผ่าน จะไม่ลด (คง efficiency)

---

## 5) Evidence + Baseline
ทุก iteration จะบันทึก evidence hash ลง `baseline_manifest.json` (best-effort) เช่น:
- stress gate report
- adaptive summary
- proposals
- updated presets
- และไฟล์ extra ที่กำหนดเพิ่ม

---

## Next step (R0-E17)
- ทำ dt_scales “adaptive search” (binary/zoom) แทน grid คงที่
- ทำ auto “band-aware scale” (บาง band ลด, บาง band คง)


---


# 🔹 Source: file_23.md

# UET R0-E17 — Adaptive dt Search (Zoom/Binary) + Band-Aware Scaling v0.1
**Goal:** ลดจำนวน dt variants ที่ต้องทดลอง (เร็วขึ้น) แต่ยังหาค่า dt “พอดี” ได้  
แทนที่จะยิง grid หนาๆ ทุกครั้ง → ใช้ zoom (binary search ใน log-scale) ต่อกลุ่มที่พังจริง

---

## 1) New scripts
- `scripts/suggest_zoom_scales.py`
  - อ่าน summary ที่ group = `band_model_integrator_variant`
  - จัดกลุ่มด้วย key: `band|model|integrator|code`
  - หา bracket (fail vs pass) แล้วเสนอ scale ใหม่ (geometric mid) จน bracket “แคบพอ”
  - Output: `zoom_scale_plan.json` (field `dt_scales_plan`)

- `scripts/merge_variant_summaries.py`
  - merge summary หลายรอบโดยรวม `n/pass/fail_codes` แล้วคำนวณ Wilson CI ใหม่
  - ใช้รวม evidence จากหลาย zoom rounds

> NOTE: `code` ถูกดึงจาก `variant` (pattern `_code..._dt...`) ที่ adaptive matrix สร้างไว้

---

## 2) make_adaptive_stress_matrix รองรับ plan
`make_adaptive_stress_matrix.py` เพิ่ม `--dt_scales_plan`
- ถ้ามี plan จะใช้ scales เฉพาะกลุ่มนั้น
- ถ้าไม่มี จะ fallback ไป `--dt_scales`

---

## 3) loop_driver รองรับ adaptive_mode=zoom
`loop_driver.py` อ่าน params เพิ่ม:
- `adaptive_mode`: `"grid"` หรือ `"zoom"`
- `zoom_rounds`: จำนวนรอบ zoom (default 2)
- `zoom_eps_ratio`: หยุดเมื่อ `s_hi_pass / s_lo_fail <= eps_ratio` (default 1.15)
- `zoom_min_scale`
- `zoom_max_new_scales_per_group`

**Behavior**
- ทำ adaptive รอบแรกด้วย grid (`dt_scales_grid`)
- ถ้า zoom mode:
  - สร้าง merged variant summary
  - วน `suggest_zoom_scales` → ได้ plan
  - รัน adaptive “เฉพาะ scale ใหม่” (targeted)
  - merge summary เพิ่ม evidence
  - ทำซ้ำจนหมด zoom_rounds หรือไม่มี scale ใหม่

สุดท้ายใช้ `adaptive_summary` ที่ merge แล้วไปทำ proposals (R0-E15)

---

## 4) Manual usage (ถ้าจะลอง zoom ทีละรอบ)
```bash
python scripts/suggest_zoom_scales.py \
  --variant_summary_csv adaptive_runs/stress_summary/stress_summary.csv \
  --out_plan zoom_scale_plan.json \
  --min_pass_rate 0.95 --min_ci_lo 0.90 \
  --eps_ratio 1.15

python scripts/make_adaptive_stress_matrix.py \
  --stress_matrix_in stress_matrix.csv \
  --stress_ledger stress_runs/dt_ladder_ledger.csv \
  --out adaptive_zoom_matrix.csv \
  --dt_scales_plan zoom_scale_plan.json
```

---

## Next step (R0-E18)
- ทำ zoom ที่ “aware ของ band” จริงๆ:
  - ถ้า FAIL ใน HARD band → zoom ลดเยอะกว่า
  - ถ้า FAIL ใน DEMO band → zoom ลดน้อย
- ทำ monotonic smoothing / Bayesian estimate ของ pass probability ต่อ scale


---


# 🔹 Source: file_25.md

# UET R0-E18 — Band-Priority Zoom Policy + Monotonic Smoothing v0.1
**Goal:** ทำให้ zoom dt search (R0-E17) “ฉลาดขึ้น + เสถียรขึ้น”
1) **Band-priority policy**: band ต่างกันควร zoom ต่างกัน (HARD ต้อง conservative กว่า DEMO)
2) **Monotonic smoothing**: ในเชิงตรรกะ เมื่อ dt เล็กลงควร “ไม่แย่ลง” แต่ข้อมูลจริงมี noise  
   → ใช้ isotonic regression (PAVA) บังคับให้ `pass_rate` และ/หรือ `ci_lo` เป็น monotone กับ `-log(dt_scale)`

---

## 1) New script
### `scripts/monotonic_smooth_variant_summary.py`
Input: merged variant summary CSV  
Output: CSV เดิม + เพิ่มคอลัมน์:
- `smoothed_pass_rate`
- `smoothed_ci_lo`

วิธี: ทำ PAVA ต่อกลุ่ม `band|model|integrator|code` โดย x = `-log(scale)` (scale เล็ก → x ใหญ่) แล้วบังคับ y(x) ไม่ลดลง

> ใช้เพื่อ “ตัด noise” ตอนตัดสิน bracket ใน zoom, ไม่ใช่แทน gate หลักของ stress

---

## 2) Update: `scripts/suggest_zoom_scales.py`
เพิ่มความสามารถ:
- `--band_policy_json` : กำหนด policy ต่อ band เช่น min_scale/eps_ratio/step_down/mid_weight
- `--use_smoothed` : ใช้ `smoothed_pass_rate/smoothed_ci_lo` ถ้ามี

**mid_weight (สำคัญ)**
- 0.0 = เลือกใกล้ fail (scale เล็กกว่า → conservative)
- 1.0 = เลือกใกล้ pass (scale ใหญ่กว่า → aggressive)

---

## 3) Template policy
ไฟล์: `UET_R0-E18_band_zoom_policy_template.json`  
ตัวอย่าง:
- DEMO: aggressive (step_down 0.7, mid_weight 0.65, min_scale 0.2)
- HARD: conservative (step_down 0.4, mid_weight 0.35, min_scale 0.05, max_new_scales_per_group 2)

---

## 4) loop_driver รองรับ smoothing + policy
เพิ่ม params ใน `loop_config.json`:
- `zoom_use_smoothing`: true/false (default true)
- `zoom_band_policy_json`: path to policy json (optional)

ใน zoom round:
1) merge summary
2) (ถ้าเปิด smoothing) run `monotonic_smooth_variant_summary.py`
3) run `suggest_zoom_scales.py --use_smoothed --band_policy_json ...`

---

## 5) Recommended defaults
- `zoom_use_smoothing: true`
- ใช้ policy template แล้วปรับตามผลจริง
- `zoom_rounds: 2` เริ่มต้น

---

## Next step (R0-E19)
- ทำ “band-aware proposal” ต่อ dt presets: ลดเฉพาะ band ที่ fail และคง band ที่ผ่าน
- เพิ่ม monotonic check ว่า “scale ลดแล้วไม่ควร fail มากขึ้น” ถ้าผิด → flag ว่า stochastic/metric issue


---


# 🔹 Source: file_28.md

# UET R0-E19 — Band-aware dt Proposals + Monotonic Consistency Guard v0.1
**Goal:** ทำให้การ “อัปเดต presets” ปลอดภัยขึ้นและไม่ลด dt เกินจำเป็น
1) **Band-aware proposals**: ปรับ dt เฉพาะ (band×model×integrator) ที่ “fail จริง” จาก stress gate
2) **Monotonic consistency guard**: ถ้า dt เล็กลงแต่ผล “แย่ลงอย่างมีนัย” → ถือว่า evidence ยังไม่เสถียร  
   → block การ apply อัตโนมัติสำหรับกลุ่มนั้น (ต้องเพิ่ม sample/ปรับ metric ก่อน)

---

## 1) New scripts
### 1.1 `scripts/failing_groups_from_gate_report.py`
- Input: `stress_gate_report.json`
- Output: `failing_groups.json` มี `groups: ["band|model|integrator", ...]`
- ใช้เป็น filter ให้ proposal script แนะนำ update เฉพาะกลุ่มที่ fail ใน stress gate

### 1.2 `scripts/monotonic_consistency_check.py`
- Input: variant summary (group = `band_model_integrator_variant`) ซึ่งอาจ merge มาหลาย zoom rounds
- ตรวจว่าเมื่อ `dt_scale` ลดลง (dt เล็กลง) **pass_rate ไม่ควรลดลง**
- Flag **violation** เมื่อ:
  - `pass_rate_lo + delta < pass_rate_hi` และทั้งคู่มี `n >= min_n`
  - ถ้า “มีนัย” โดย `ci_hi_lo < ci_lo_hi` → ใส่ลง `blocklist_band_model_integrator`

Output: `monotonic_report.json`
- `status`: OK/BLOCK
- `blocklist_band_model_integrator`: รายชื่อ group ที่ควร “หยุด apply อัตโนมัติ”
- `violations`: รายละเอียด pair ที่ผิด monotonic

---

## 2) Update scripts
### 2.1 `propose_preset_updates_from_variant_summary.py`
เพิ่ม `--only_groups_json failing_groups.json`
- ถ้าให้มา จะ output proposals เฉพาะ group ที่อยู่ใน list

### 2.2 `apply_preset_updates.py`
เพิ่ม `--blocklist_json monotonic_report.json`
- ถ้า group อยู่ใน blocklist จะ skip update

---

## 3) loop_driver behavior (อัตโนมัติ)
เพิ่ม params:
- `band_aware_updates` (default true)
- `monotonic_check` (default true)
- `monotonic_min_n` (default 50)
- `monotonic_delta` (default 0.05)

ในลูป:
1) หลัง stress gate FAIL → สร้าง `failing_groups.json`
2) หลังได้ `adaptive_summary` → สร้าง `monotonic_report.json`
3) proposal จะ filter ด้วย failing_groups (ถ้าเปิด band_aware_updates)
4) apply จะใช้ blocklist (ถ้าเปิด monotonic_check)

---

## 4) Recommended defaults
- `band_aware_updates: true` (กันลด dt ทั้งระบบ)
- `monotonic_check: true`
- `monotonic_min_n: 50` (ถ้า n น้อยอาจไม่เสถียร)
- `monotonic_delta: 0.05`

---

## Next step (R0-E20)
- Auto “resample policy”: ถ้าโดน blocklist ให้เพิ่ม `jitters_per_case` หรือเพิ่ม seeds / n_per_case อัตโนมัติ แล้ว rerun เฉพาะกลุ่มนั้น
- Add metric-level diagnosis mapping: violation ที่เกิดมักสัมพันธ์กับ fail_code ใด → แนะนำแก้ metric/threshold เฉพาะจุด


---


# 🔹 Source: file_3.md

# UET Extensions - Stochastic Dynamics

## 🎲 Stochastic Noise in UET

**Why Noise Matters:**

Real systems have **random fluctuations**:
- **Neural:** Synaptic noise, ion channel stochasticity
- **Economics:** Random market shocks, unexpected news
- **Biology:** Molecular noise, genetic mutations
- **Climate:** Weather variability, volcanic eruptions

**Deterministic models miss this!**

---

## 📐 Mathematical Formulation

### Standard UET (Deterministic):
```
∂C/∂t = κ∇²C - ∂V/∂C - β(C-I) + s
∂I/∂t = κ∇²I - ∂V/∂I - β(I-C)
```

### Stochastic UET (with Noise):
```
∂C/∂t = κ∇²C - ∂V/∂C - β(C-I) + s + σ_C·ξ_C(x,t)
∂I/∂t = κ∇²I - ∂V/∂I - β(I-C) + σ_I·ξ_I(x,t)
```

**New Parameters:**
- `σ_C`: Noise strength for C field
- `σ_I`: Noise strength for I field
- `ξ(x,t)`: White noise (Gaussian, mean=0, variance=1)

**Properties of ξ:**
```
⟨ξ(x,t)⟩ = 0                           (zero mean)
⟨ξ(x,t)ξ(x',t')⟩ = δ(x-x')δ(t-t')     (uncorrelated)
```

---

## 🔧 Implementation Strategy

### 1. Euler-Maruyama Method

**Stochastic differential equations need special treatment:**

```python
# Deterministic Euler:
C_new = C + dt * f(C)

# Stochastic Euler-Maruyama:
C_new = C + dt * f(C) + sqrt(dt) * σ * ξ
                                  ↑
                              Important!
```

**Why `sqrt(dt)`?**
- Noise scales with √dt (Wiener process)
- Ensures correct variance in limit dt→0

---

### 2. Implementation

```python
class UETWithNoise:
    """UET model with stochastic noise."""
    
    def __init__(self, N=32, kappa=0.1, beta=0.5, s=0.0,
                 sigma_C=0.0, sigma_I=0.0, dt=0.01):
        self.N = N
        self.kappa = kappa
        self.beta = beta
        self.s = s
        self.sigma_C = sigma_C
        self.sigma_I = sigma_I
        self.dt = dt
        
        # Initialize fields
        self.C = np.random.randn(N, N) * 0.1 + 1.0
        self.I = np.random.randn(N, N) * 0.1 - 1.0
    
    def step(self):
        """Evolve one timestep with noise (Euler-Maruyama)."""
        C, I = self.C, self.I
        dt = self.dt
        
        # Deterministic part
        dC_det = (
            self.kappa * laplacian_2d(C) -
            dV_dphi(C) -
            self.beta * (C - I) +
            self.s
        )
        
        dI_det = (
            self.kappa * laplacian_2d(I) -
            dV_dphi(I) -
            self.beta * (I - C)
        )
        
        # Stochastic part (white noise)
        noise_C = np.random.randn(self.N, self.N)
        noise_I = np.random.randn(self.N, self.N)
        
        # Euler-Maruyama update
        self.C = C + dt * dC_det + np.sqrt(dt) * self.sigma_C * noise_C
        self.I = I + dt * dI_det + np.sqrt(dt) * self.sigma_I * noise_I
```

---

## 🎯 Use Cases

### 1. Neural Noise (Ion Channel Stochasticity)

**Neurons are noisy!**

```python
# Neural model with synaptic noise
model = UETWithNoise(
    sigma_C=0.1,  # Excitatory noise
    sigma_I=0.05, # Inhibitory noise (less noisy)
    beta=1.0
)

# Result: Irregular spiking, realistic neural activity
```

**Physical meaning:**
- σ_C: Random opening/closing of ion channels
- σ_I: Spontaneous neurotransmitter release
- Noise → Variability in spike timing

---

### 2. Market Volatility

**Markets have random shocks:**

```python
# Economics: Random news/events
model = UETWithNoise(
    sigma_C=0.2,  # Price volatility
    sigma_I=0.05, # Value is more stable
    beta=0.5
)

# Result: Realistic price fluctuations, volatility clustering
```

**Examples:**
- Unexpected earnings reports
- Political events
- Natural disasters

---

### 3. Molecular Noise (Gene Expression)

**Small numbers → Big fluctuations:**

```python
# Biology: Stochastic gene expression
model = UETWithNoise(
    sigma_C=0.3,  # mRNA noise (low copy number)
    sigma_I=0.1,  # Protein noise (higher copy)
    beta=0.3
)

# Result: Cell-to-cell variability, phenotypic diversity
```

---

### 4. Climate Variability

**Weather is chaotic:**

```python
# Climate: Random weather fluctuations
model = UETWithNoise(
    sigma_C=0.05, # Temperature noise
    sigma_I=0.02, # Ocean is less noisy
    beta=0.1
)

# Result: Year-to-year variability, extreme events
```

---

## 📊 Noise Effects

### Effect 1: Noise-Induced Transitions

**Noise can push system over barriers!**

```
Without noise:
  System stuck in local minimum

With noise:
  System can escape → explore other states
```

**Example:** Genetic switches, decision-making

---

### Effect 2: Stochastic Resonance

**Noise + Signal = Enhanced detection!**

```
Weak signal alone: Not detected
Noise alone: Random
Signal + Noise: Signal amplified!
```

**Example:** Sensory neurons, climate cycles

---

### Effect 3: Noise-Induced Oscillations

**Noise can create oscillations in stable systems:**

```
Deterministic: Stable equilibrium
+ Noise: Fluctuations around equilibrium
+ Nonlinearity: Coherent oscillations!
```

**Example:** Circadian rhythms, business cycles

---

## ⚠️ Numerical Considerations

### 1. Timestep Constraint

**Noise requires smaller dt:**

```
Deterministic: dt ≈ 0.01 OK
Stochastic: dt ≈ 0.001 better

Rule: dt << 1/σ²
```

### 2. Ensemble Averaging

**Single trajectory is noisy → Average many:**

```python
# Run N_ensemble simulations
trajectories = []
for _ in range(N_ensemble):
    model = UETWithNoise(sigma_C=0.1)
    model.run()
    trajectories.append(model.C)

# Average
C_mean = np.mean(trajectories, axis=0)
C_std = np.std(trajectories, axis=0)
```

### 3. Noise Types

**Different noise models:**

```python
# 1. White noise (current)
ξ(t) ~ N(0,1), uncorrelated

# 2. Colored noise (future extension)
ξ(t) has correlation time τ_corr

# 3. Multiplicative noise (future)
dC/dt = ... + σ·C·ξ(t)  # Noise ∝ C
```

---

## 🔬 Demo: Noise-Induced Escape

```python
def demo_noise_escape():
    """Show how noise helps escape local minimum."""
    
    # Setup: Double-well potential
    # Two minima at C = ±1
    
    # 1. No noise: Stuck in one well
    model_no_noise = UETWithNoise(sigma_C=0.0)
    model_no_noise.C[:] = -1.0  # Start at C=-1
    
    for _ in range(1000):
        model_no_noise.step()
    
    # Result: Still at C ≈ -1 (stuck!)
    
    # 2. With noise: Can escape
    model_with_noise = UETWithNoise(sigma_C=0.5)
    model_with_noise.C[:] = -1.0
    
    for _ in range(1000):
        model_with_noise.step()
    
    # Result: Sometimes jumps to C ≈ +1 (escaped!)
```

---

## 📈 Expected Behaviors

| Noise σ | Effect |
|---------|--------|
| 0 | Deterministic (smooth) |
| Small (0.01-0.1) | Small fluctuations |
| Medium (0.1-0.5) | Significant variability |
| Large (>0.5) | Dominated by noise |

---

## 🎓 Domain Interpretations

### Neural:
```
σ_C = Ion channel noise
σ_I = Synaptic noise

Typical: σ ≈ 0.05-0.2
```

### Economics:
```
σ_C = Market volatility
σ_I = Fundamental uncertainty

Typical: σ ≈ 0.1-0.5
```

### Biology:
```
σ_C = Molecular noise (mRNA)
σ_I = Protein noise

Typical: σ ≈ 0.1-0.3
```

---

## 🔗 Combination with Other Extensions

### Noise + Delays:
```
∂C/∂t = ... - β(C(t) - I(t-τ)) + σξ(t)
```
→ Delayed stochastic oscillator (realistic neural)

### Noise + Multi-field:
```
∂Cᵢ/∂t = ... - Σⱼ βᵢⱼ(Cᵢ-Cⱼ) + σᵢξᵢ(t)
```
→ Noisy network dynamics

---

## 🚀 Next Steps

1. **Implement in core**
   - Add `sigma_C`, `sigma_I` parameters
   - Euler-Maruyama solver
   - Ensemble averaging tools

2. **Create demos**
   - Noise-induced escape
   - Stochastic resonance
   - Ensemble statistics

3. **Documentation**
   - When to use noise
   - How to choose σ
   - Numerical stability

---

*Noise: From nuisance to feature!*


---


# 🔹 Source: file_30.md

# UET R0-E20 — Auto-Resample for Blocked Groups + Targeted Rerun v0.1
**Goal:** ถ้า monotonic guard (R0-E19) ตัดสินว่า evidence “ไม่นิ่ง” (BLOCK)  
อย่าหยุดนิ่ง — ให้ระบบเพิ่มหลักฐาน (n) อัตโนมัติ โดย rerun เฉพาะกลุ่มที่โดน blocklist

---

## 1) New script
### `scripts/resample_blocked_groups.py`
สร้าง matrix เพิ่มเติมจาก matrix ที่ใช้สร้าง adaptive variants แล้ว:
- เลือกเฉพาะ rows ในกลุ่มที่อยู่ใน `blocklist_band_model_integrator`
- clone rows พร้อมสร้าง seed ใหม่เพิ่ม `extra_seeds` ต่อ row
- เลี่ยง duplicate seeds ถ้าให้ `--dedupe_ledger`

Output: `resample_matrix.csv`

---

## 2) loop_driver behavior
เพิ่ม params:
- `resample_on_block` (default true)
- `resample_rounds` (default 2)
- `resample_extra_seeds` (default 10)
- `resample_seed_start` (default 200000)
- `resample_max_rows` (default 20000)

Workflow:
1) ทำ adaptive (grid/zoom) ตามเดิม → ได้ `adaptive_summary` (merged)
2) ทำ monotonic check → ได้ `monotonic_report.json`
3) ถ้า `status == "BLOCK"` และเปิด resample:
   - สร้าง `resample_matrix_roundXX.csv`
   - รัน `run_dt_ladder.py`
   - สรุปเป็น summary (variant grouping)
   - merge เข้า `adaptive_summary`
   - rerun monotonic check
   - วนซ้ำจน `OK` หรือครบ `resample_rounds`

**ผลลัพธ์**: ลด false block จาก noise และทำให้การ apply presets ปลอดภัยขึ้น

---

## 3) Recommended defaults
- `resample_rounds: 2`
- `resample_extra_seeds: 10`
- ถ้า model stochastic มาก → เพิ่ม extra_seeds เป็น 20

---

## Next step (R0-E21)
- Auto “escalation”: ถ้ายัง BLOCK หลัง resample
  - เพิ่ม jitters_per_case / เพิ่ม cases_per_group เฉพาะกลุ่มนั้น
  - หรือสลับไปตรวจ metric thresholds / solver determinism


---


# 🔹 Source: file_32.md

# UET R0-E21 — Auto-Escalation Policy (Persistent BLOCK) + Determinism Probe v0.1
**Goal:** ถ้า monotonic guard (R0-E19) ยัง `BLOCK` แม้ผ่าน resample (R0-E20) แล้ว  
ระบบต้อง “ยกระดับ” การตรวจสอบให้ชัดว่า:
- เป็น **noise (ยัง sample ไม่พอ)** → เพิ่ม evidence แบบหนักขึ้น
- เป็น **solver non-determinism / stochastic bug** → ต้องแก้ระบบก่อน (ห้าม auto-apply presets)
- หรือเป็น **metric/threshold artifact** → ต้องกลับไปปรับ metric/threshold

---

## 1) Fix (สำคัญ)
### `scripts/run_dt_ladder.py`
- แก้เรียก `init_run_folder(...)` ให้ตรง signature: `init_run_folder(out_root, model, case_id, config)`
- เพิ่มรองรับ `probe_tag` (column ใน matrix) → ใส่ใน `config["probe"]` เพื่อให้ run_id แตกต่าง (ใช้กับ determinism probe)

---

## 2) New scripts
### 2.1 `scripts/determinism_probe_matrix.py`
สร้าง matrix สำหรับ “replay” config เดิมด้วย seed เดิมหลายครั้ง:
- input: matrices ที่ใช้รัน adaptive
- groups_json: ใช้ `monotonic_report.json` (เอา blocklist)
- output: `determinism_probe_matrix.csv` ที่เพิ่มคอลัมน์ `probe_tag=rep01..`

### 2.2 `scripts/determinism_report.py`
อ่าน `dt_ladder_ledger.csv` จาก determinism probe runs แล้วสรุปว่า
- กลุ่มเดียวกัน (base_case_id, model, integrator, dt, seed) ให้ผล pass/fail/fail_code “เหมือนกัน” ไหม
- ถ้ามีผลต่างกัน → `status=UNSTABLE`

---

## 3) loop_driver escalation
เพิ่ม params:
- `determinism_probe` (default true)
- `determinism_repeats` (default 5)
- `determinism_max_base_rows` (default 200)
- `escalate_on_persistent_block` (default true)
- `escalate_extra_seeds_multiplier` (default 2)
- `escalate_additional_resample_rounds` (default 1)

Behavior:
1) ทำ adaptive + zoom + resample ตามเดิม
2) ถ้ายัง `BLOCK`:
   - รัน determinism probe → ได้ `determinism_report.json`
   - ทำ “heavier resample” เพิ่ม seeds มากขึ้น (extra_seeds × multiplier) อีก 1–N รอบ
   - merge summary + rerun monotonic check


---


# 🔹 Source: file_36.md

# UET R0-E22 — Metric Triage (Blocklist ↔ Fail Codes ↔ Metrics) v0.1
Goal: ระบุ “BLOCK มาจากอะไร” โดยเชื่อม 3 ชั้น:
1) monotonic_report (BLOCK + violations)
2) fail_codes_json (จาก summarize_stress_test)
3) run-level metrics (จาก run_dir/summary.json)

Outputs:
- metric_triage_report.json
- metric_triage_report.md

Patch:
- run_case.py + run_dt_ladder.py เติม summary['fail_code'] จาก fail_reasons[0] เพื่อให้ fail_codes_json ใช้งานได้จริง

Integration:
- loop_driver รัน metric_triage อัตโนมัติก่อน propose/apply presets

Optional thresholds template:
- docs/UET_R0-E22_metric_thresholds_optional_template.json


---


# 🔹 Source: file_37.md

R0-E23: Action router reads metric_triage + monotonic/determinism reports and emits action_plan.*; can enforce hold_apply.


---


# 🔹 Source: file_38.md

R0-E24: Targeted evidence executor: if action_plan requests INCREASE_EVIDENCE, expand seeds for those groups via resample_blocked_groups + rerun dt ladder, then re-check monotonic.


---


# 🔹 Source: file_39.md

# UET R0-E25 — Auto-Evidence Budgeter + Stop Rules v0.1

## Goal
เมื่อ action_router แนะนำ `INCREASE_EVIDENCE` เราไม่อยาก “เพิ่ม seed ไปเรื่อย ๆ” แบบไร้เพดาน
R0-E25 เพิ่มตัว **budgeter** เพื่อ:
- กำหนดจำนวน evidence ที่เหมาะสมต่อกลุ่ม (band|model|integrator)
- มี **stop rules** ชัดเจนว่าเมื่อไร “ควรหยุดเพิ่มหลักฐาน” แล้วหันไปแก้ solver/สมการ/พารามิเตอร์แทน

---

## New script
### `scripts/evidence_budgeter.py`

**Inputs**
- `--action_plan_json` (required): `action_plan.json` จาก R0-E23
- `--variant_summary_csv` (required): `adaptive_variant_summary_merged.csv` หรือไฟล์ merged ล่าสุด
- `--triage_json` (optional): `metric_triage_report.json`
- `--monotonic_report_json` (optional): `monotonic_report.json`
- `--determinism_report_json` (optional): `determinism_report.json`

**Outputs**
- `evidence_budget.json`
- `evidence_budget.md`

---

## Stop rules (conservative defaults)
- STOP ถ้า determinism report = `UNSTABLE` (optional flag)
- STOP ถ้า n_total ของกลุ่ม >= `max_n_for_evidence` (default 500) แล้วยัง BLOCK → “ไม่ใช่เรื่อง sample แล้ว”
- STOP ถ้า blowup/nan_inf rate สูง (default >= 0.02) → ต้องลด dt/แก้ stability ไม่ใช่เพิ่มหลักฐาน
- มี **global cap** ของ extra seeds รวมทั้งระบบ (`max_total_extra_seeds`)

---

## loop_driver integration
เพิ่ม stage:
- **7.65 Evidence budgeter** → สร้าง evidence_budget.*
- Evidence executor (7.7) จะ:
  - ถ้า evidence_budget มี → ทำ evidence แบบ **per-group schedule**
  - ถ้าไม่มี → fallback ไป schedule เดิม (global)

เพิ่ม params:
- `evidence_budgeter` (default true)
- `evidence_budget_max_n` (default 500)
- `evidence_budget_total_extra_seeds` (default 200)
- `evidence_budget_max_rounds` (default 3)
- `evidence_budget_stop_on_unstable` (default true)

---

## Why it matters
- ทำให้ loop “ไม่เผา compute” แบบไร้เพดาน
- ทำให้เรารู้ว่าจุดไหนต้องแก้ **สมการ/solver** จริง ๆ ไม่ใช่เพิ่ม sample
- ลดโอกาส drift ของ baseline เพราะ evidence บางกลุ่มไม่คุ้มค่า

---

## Next step (R0-E26)
- “Executor for actions” ขั้นต่อไป: ถ้า budgeter บอก STOP เพราะ blowup/nan_inf → ออก proposal ลด dt preset/เพิ่ม stability caps แบบ targeted


---


# 🔹 Source: file_4.md

# UET Extensions - Time Delays

## 🕐 Time Delays in UET

**Why Time Delays Matter:**

Many real systems have **delayed responses**:
- **Neural:** Action potential takes time to propagate
- **Economics:** Market reactions lag behind news
- **Biology:** Gene expression has transcription delays
- **Climate:** Ocean temperature responds slowly to atmosphere

---

## 📐 Mathematical Formulation

### Standard UET (No Delay):
```
∂C/∂t = κ∇²C - ∂V/∂C - β(C(t) - I(t)) + s
∂I/∂t = κ∇²I - ∂V/∂I - β(I(t) - C(t))
```

### UET with Time Delays:
```
∂C/∂t = κ∇²C - ∂V/∂C - β(C(t) - I(t-τ_CI)) + s
∂I/∂t = κ∇²I - ∂V/∂I - β(I(t) - C(t-τ_IC))
```

**Parameters:**
- `τ_CI`: Delay from I → C (how long C waits for I's signal)
- `τ_IC`: Delay from C → I (how long I waits for C's signal)

---

## 🔧 Implementation Strategy

### 1. History Buffer

**Need to store past values:**

```python
class UETModelWithDelay:
    def __init__(self, tau_CI=0.0, tau_IC=0.0, dt=0.01):
        self.tau_CI = tau_CI
        self.tau_IC = tau_IC
        self.dt = dt
        
        # Calculate buffer size
        self.buffer_size_CI = int(tau_CI / dt) + 1
        self.buffer_size_IC = int(tau_IC / dt) + 1
        
        # History buffers (circular)
        self.C_history = deque(maxlen=self.buffer_size_CI)
        self.I_history = deque(maxlen=self.buffer_size_IC)
    
    def step(self, C, I):
        # Store current values
        self.C_history.append(C.copy())
        self.I_history.append(I.copy())
        
        # Get delayed values
        if len(self.I_history) >= self.buffer_size_CI:
            I_delayed = self.I_history[0]  # Oldest value
        else:
            I_delayed = I  # Not enough history, use current
        
        if len(self.C_history) >= self.buffer_size_IC:
            C_delayed = self.C_history[0]
        else:
            C_delayed = C
        
        # Compute derivatives with delays
        dC_dt = (self.kappa * laplacian(C) 
                 - dV_dC(C) 
                 - self.beta * (C - I_delayed)  # ← Delayed I
                 + self.s)
        
        dI_dt = (self.kappa * laplacian(I)
                 - dV_dI(I)
                 - self.beta * (I - C_delayed))  # ← Delayed C
        
        # Update
        C_new = C + self.dt * dC_dt
        I_new = I + self.dt * dI_dt
        
        return C_new, I_new
```

---

## 🎯 Use Cases

### 1. Neural Oscillations

**Without delay:** Stable equilibrium
**With delay:** Oscillations!

```python
# Neural model with synaptic delay
model = UETModelWithDelay(
    tau_CI=0.5,  # Inhibition delayed by 0.5 time units
    tau_IC=0.1,  # Excitation delayed by 0.1
    beta=1.0
)

# Result: Oscillatory neural activity (alpha waves, etc.)
```

**Physical meaning:**
- τ_CI: Time for inhibitory signal to reach excitatory neurons
- τ_IC: Time for excitatory signal to reach inhibitory neurons
- Different delays → different oscillation frequencies

---

### 2. Economic Cycles

**Market price C lags behind fundamental value I:**

```python
# Economics: Price adjusts slowly to value
model = UETModelWithDelay(
    tau_CI=2.0,  # Price takes 2 time units to respond to value
    tau_IC=0.1,  # Value responds quickly to price
    beta=0.5
)

# Result: Boom-bust cycles, overshooting
```

---

### 3. Predator-Prey Dynamics

**Predator population I lags behind prey C:**

```python
# Biology: Predator growth delayed by reproduction time
model = UETModelWithDelay(
    tau_CI=0.0,   # Prey responds immediately to predators
    tau_IC=5.0,   # Predators take time to reproduce
    beta=0.3
)

# Result: Classic Lotka-Volterra oscillations
```

---

## ⚠️ Stability Considerations

**Time delays can destabilize systems!**

### Stability Criterion (Linear Analysis):

For small delays:
```
System stable if: β·τ < π/2
```

**Intuition:**
- Small delay (τ → 0): Stable
- Large delay (τ → ∞): Unstable (oscillations or chaos)
- Critical delay: τ_crit ≈ π/(2β)

---

## 🔬 Demo: Delayed Neural Oscillator

```python
import numpy as np
from collections import deque

def demo_delayed_oscillator():
    """Show how delay creates oscillations."""
    
    # Setup
    N = 64
    C = np.random.randn(N, N) * 0.1 + 1.0
    I = np.random.randn(N, N) * 0.1 - 1.0
    
    # Parameters
    tau = 1.0  # Delay time
    dt = 0.01
    beta = 1.0
    kappa = 0.1
    
    # History buffer
    buffer_size = int(tau / dt)
    I_history = deque([I.copy() for _ in range(buffer_size)], 
                      maxlen=buffer_size)
    
    # Simulate
    for step in range(1000):
        # Get delayed I
        I_delayed = I_history[0]
        
        # Update C with delayed I
        dC = (kappa * laplacian(C) 
              - dV_dC(C) 
              - beta * (C - I_delayed))
        C += dt * dC
        
        # Update I with current C
        dI = (kappa * laplacian(I)
              - dV_dI(I)
              - beta * (I - C))
        I += dt * dI
        
        # Store current I
        I_history.append(I.copy())
        
        # Plot every 10 steps
        if step % 10 == 0:
            plot_fields(C, I, step)
    
    # Result: Oscillations in C and I!
```

---

## 📊 Expected Behaviors

| Delay τ | β | Behavior |
|---------|---|----------|
| 0 | Any | Stable equilibrium |
| Small | Small | Damped oscillations |
| Medium | Medium | Sustained oscillations |
| Large | Large | Chaos / instability |

---

## 🎓 Domain Interpretations

### Neural:
```
τ_CI = Synaptic delay (inhibitory → excitatory)
τ_IC = Synaptic delay (excitatory → inhibitory)

Typical values: 1-10 ms
```

### Economics:
```
τ_CI = Information processing time
τ_IC = Market reaction time

Typical values: days to months
```

### Climate:
```
τ_CI = Ocean thermal inertia
τ_IC = Atmosphere response time

Typical values: years to decades
```

---

## 🚀 Next Steps

1. **Implement in core UET**
   - Add `tau_CI`, `tau_IC` parameters
   - Add history buffers
   - Update solver

2. **Create demo**
   - Neural oscillator
   - Economic cycles
   - Show stability transition

3. **Documentation**
   - When to use delays
   - How to choose τ values
   - Stability guidelines

---

## 🔗 Connection to Other Extensions

**Delays + Stochastic:**
```
∂C/∂t = ... - β(C(t) - I(t-τ)) + σξ(t)
```
→ Delayed stochastic oscillator (realistic neural noise)

**Delays + Multi-field:**
```
∂Cᵢ/∂t = ... - Σⱼ βᵢⱼ(Cᵢ(t) - Cⱼ(t-τᵢⱼ))
```
→ Network with heterogeneous delays

---

*Time delays: Simple addition, profound consequences!*


---


# 🔹 Source: file_41.md

# UET R0-E26 — Targeted Action Executor (Non-evidence) v0.1
**Goal:** เมื่อ triage/action_plan บอกว่า “ต้องลด dt” หรือ “ต้องทำ determinism diagnose”
ให้มีตัว executor ที่ทำงานได้จริงและบันทึก audit trail ชัดเจน โดยไม่ต้องรอ manual edit

## What it does (v0.1)
- อ่าน `action_plan.json`
- สำหรับแต่ละ group ที่มี action `DECREASE_DT_PRESET`:
  - เลือก multiplier ที่ **เข้มที่สุด** (min multiplier ใน actions)
  - พยายาม apply กับ:
    - `band_dt_presets` (per band|model|integrator)
    - `dt_presets` (per model|integrator)
  - รองรับ schema หลายแบบ (nested dict หรือ list of rows)
  - ถ้า `--apply` จะ:
    - สร้าง backup `.bak.<timestamp>`
    - เขียน preset ที่ถูกปรับแล้วกลับไปที่ไฟล์

Outputs ใน run_dir:
- `targeted_actions_applied.json`
- `targeted_actions_applied.md`

## loop_driver integration
Stage 7.62 เรียก executor หลัง action_router และก่อน propose/apply อื่น ๆ

Params:
- `targeted_action_executor` (default true)
- `targeted_action_allow_when_hold` (default false)
  - ถ้า action_router บอก `hold_apply=true` จะไม่ apply โดย default
  - เปิด option นี้เมื่อคุณต้องการ “ลด dt เพื่อความปลอดภัย” แม้ยัง hold
- `targeted_action_min_multiplier` (default 0.1)

## Next step (R0-E27)
- เพิ่ม action type อื่น ๆ: ปรับ backtracking policy / tolerance / caps
- เพิ่ม rule “do-not-touch list” สำหรับ presets ที่ถูก baseline lock แล้ว


---


# 🔹 Source: file_42.md

# UET R0-E27 — Action Types Expansion + Lock/Do-Not-Touch Guard v0.1

## Goal
1) ขยาย “ชนิด action” ที่ action_router สามารถแนะนำได้ (ยังไม่บังคับ apply ทุกอย่าง)
2) เพิ่ม **Lock Guard** + **Do-not-touch** เพื่อกันการแก้ presets ที่ถูกล็อกเป็น baseline แล้ว

---

## 1) Action types ที่เพิ่มใน `action_router.py`
- `TUNE_BACKTRACKING`  
  ใช้เมื่อ ENERGY_INCREASE เด่น หรือ backtracking density สูง
- `ENABLE_NUMERIC_GUARDS`  
  ใช้เมื่อ BLOWUP / NAN_INF เด่น (ชี้ว่าควรใช้ caps / safe exp/log / clamp)
> หมายเหตุ: ใน v0.1 executor จะ “บันทึก” actions เหล่านี้เป็น `unapplied_actions`
เพื่อให้มนุษย์ตัดสินใจ/หรือรอ executor รุ่นถัดไปที่รองรับการ apply จริง

---

## 2) Lock/Do-not-touch guard ใน `targeted_action_executor.py`
เพิ่ม args:
- `--baseline_manifest <path>` : ใช้ตรวจ best-effort ว่าไฟล์ presets ถูกล็อกหรือไม่
- `--do_not_touch_json <path>` : ไฟล์กำหนดรายการห้ามแตะ
- `--respect_lock` : เปิด lock guard
- `--allow_modify_locked` : override (อันตราย ใช้เมื่อรู้ว่ากำลังทำอะไร)

รูปแบบ do_not_touch_json (ตัวอย่าง):
```json
{
  "files": [
    "dt_ladder_runs_seeds/dt_presets_strict/dt_presets_strict.json"
  ],
  "groups": [
    "BAND_A|MODEL_X|rk4"
  ]
}
```

Behavior:
- ถ้า group อยู่ใน do-not-touch → `skipped=true`
- ถ้าไฟล์อยู่ใน do-not-touch หรือ baseline_manifest บอกว่าล็อก → จะไม่เขียนทับ (แม้มี --apply)

Outputs เพิ่ม:
- ใน `targeted_actions_applied.json` จะมี `skipped`, `skip_reasons`, `unapplied_actions`

---

## 3) loop_driver params
- `targeted_action_respect_lock` (default true)
- `targeted_action_allow_modify_locked` (default false)
- `targeted_action_do_not_touch_json` (default "")

---

## Next (R0-E28)
- เพิ่ม executor ที่ apply `TUNE_BACKTRACKING` และ `ENABLE_NUMERIC_GUARDS` อย่างปลอดภัย
  (ต้องนิยาม schema ของ solver-policy/caps ชัดก่อน)


---


# 🔹 Source: file_43.md

# UET R0-E3 — Dimensional & Scaling Checklist v0.1
**Goal:** checklist ตรวจหน่วย/สเกลทุกครั้งที่เพิ่มเทอมใน Ω หรือ PDE (กันพังเงียบ)

---

## A) Choose mode first
- [ ] Dimensionless mode (default)  
- [ ] Physical mode (provide L0,C0,I0,e0,t0)

---

## B) Ω integrand consistency
ทุกเทอมต้องเป็น energy density [E]/[L]^d (physical) หรือ order-1 (dimensionless).

- [ ] Potential term: V(C), V(I)
- [ ] Gradient term: +κ/2|∇u|²  (κ>0)
- [ ] Coupling: -βCI (หรือรูปอื่นที่ประกาศชัด)

---

## C) Variational derivative consistency
- [ ] μ_C has units ([E]/[L]^d)/[C]
- [ ] μ_I has units ([E]/[L]^d)/[I]
- [ ] sign rule: +κ/2|∇u|² ⇒ μ contains -κΔu

---

## D) Dynamics
Allen–Cahn:
- [ ] ∂t u = -M μ  (M>0)
Cahn–Hilliard (ถ้า conserved):
- [ ] ∂t u = ∇·(M ∇μ)  (units differ; re-derive)

---

## E) Scaling sanity (dimensionless mode)
- [ ] κ extremely small/large → stiffness marker
- [ ] β large → risk unboundedness unless coercivity conditions hold
- [ ] use backtracks_total / dt_min as objective stiffness signals

---

## F) Done criteria for “units solved”
- [ ] units table
- [ ] nondim recipe
- [ ] declare mode in demos/config
- [ ] coercivity/boundedness stated in scaled parameters


---


# 🔹 Source: file_44.md

# UET R0-E3 — Nondimensionalization Recipe v0.1
**Goal:** สูตรแปลง physical → dimensionless ที่ชัด เพื่อให้เทียบสากล/ทำ calibration ได้จริง  
(harness ปัจจุบันใช้ dimensionless mode อยู่แล้ว)

---

## 1) Choose reference scales
เลือกสเกล:
- \(L_0\) length scale
- \(C_0, I_0\) field scales
- \(e_0\) energy density scale ([E]/[L]^d)
- \(t_0\) time scale

Define:
\[
\tilde x=x/L_0,\quad \tilde t=t/t_0,\quad \tilde C=C/C_0,\quad \tilde I=I/I_0
\]
and \(dx=L_0^d d\tilde x\).

---

## 2) Scale Ω (C-only)
Assume \(V(C)=e_0 \tilde V(\tilde C)\).  
Then:
\[
\tilde\Omega := \frac{\Omega}{e_0 L_0^d}
= \int\Big(\tilde V(\tilde C)+\frac{\tilde\kappa}{2}|\tilde\nabla \tilde C|^2\Big)\,d\tilde x
\]
with:
\[
\boxed{\tilde\kappa=\frac{\kappa C_0^2}{e_0 L_0^2}}
\]

---

## 3) Scale coupling (C+I)
\[
-\beta CI = -\beta C_0 I_0\,\tilde C\tilde I
\quad\Rightarrow\quad
\boxed{\tilde\beta=\frac{\beta C_0 I_0}{e_0}}
\]
and:
\[
\tilde\kappa_C=\frac{\kappa_C C_0^2}{e_0 L_0^2},\quad
\tilde\kappa_I=\frac{\kappa_I I_0^2}{e_0 L_0^2}
\]

---

## 4) Quartic coefficients
If \(V(C)=aC^2/2+\delta C^4/4+sC\) then:
\[
\boxed{\tilde a=\frac{aC_0^2}{e_0}},\quad
\boxed{\tilde\delta=\frac{\delta C_0^4}{e_0}},\quad
\boxed{\tilde s=\frac{sC_0}{e_0}}
\]
(and similarly for I)

---

## 5) Scale dynamics (Allen–Cahn)
\[
\partial_t C=-M_C\mu_C
\]
leads to:
\[
\partial_{\tilde t}\tilde C = -\tilde M_C \tilde\mu_C,\quad
\boxed{\tilde M_C=\frac{t_0 M_C e_0}{C_0^2}}
\]
Similarly:
\[
\boxed{\tilde M_I=\frac{t_0 M_I e_0}{I_0^2}}
\]

**Convenient choice:** pick \(t_0=C_0^2/(M_C e_0)\) so \(\tilde M_C=1\).

---

## 6) How to use this in the project
- ถ้า “dimensionless mode”: ถือว่าพารามิเตอร์ในโค้ดคือ \(\tilde{\cdot}\) ทั้งหมด  
- ถ้าอยาก “โยงสากล/ของจริง”: กำหนด (L0,C0,I0,e0,t0) แล้วแปลงย้อนกลับ

Dimensional Gap ปิดเมื่อเราพูดได้ชัดว่า “ชุด demo นี้อยู่ในสเกลอะไร”


---


# 🔹 Source: file_45.md

# UET R0-E3 — Symbols & Units Table v0.1
**Goal:** ปิด “Dimensional Gap” โดยล็อกหน่วย/มิติของสัญลักษณ์หลักให้ชัด  
**โหมดที่รองรับ**
1) **Dimensionless mode (default ใน harness)**: ทุกอย่างเป็นไร้มิติ  
2) **Physical mode (optional)**: กำหนดสเกลอ้างอิง (L0,C0,I0,e0,t0) แล้วแปลงเป็นไร้มิติ

---

## 1) Base dimensions (symbolic)
- **[L]**: length  
- **[T]**: time  
- **[E]**: energy  
- **[C]**: unit of field C  
- **[I]**: unit of field I  

ใน d-dimensional domain:
- \(dx^d\): [L]^d
- energy density: [E]/[L]^d

> ใน harness ใช้ 2D (d=2) และ periodic BC (spectral).

---

## 2) Canonical Ω (continuous)
C-only:
\[
\Omega_C=\int\Big(V_C(C)+\frac{\kappa}{2}|\nabla C|^2\Big)\,dx
\]

C+I:
\[
\Omega_{CI}=\int\Big(V_C(C)+V_I(I)-\beta CI+\frac{\kappa_C}{2}|\nabla C|^2+\frac{\kappa_I}{2}|\nabla I|^2\Big)\,dx
\]

---

## 3) Units table (physical mode)
### 3.1 Fields & coordinates
| Symbol | Meaning | Units |
|---|---|---|
| x | position | [L] |
| t | time | [T] |
| C(x,t) | field C | [C] |
| I(x,t) | field I | [I] |

### 3.2 Potential & derivatives
| Symbol | Meaning | Units |
|---|---|---|
| V_C(C) | potential energy density | [E]/[L]^d |
| V_C'(C) | dV/dC | ([E]/[L]^d)/[C] |
| V_I(I), V_I'(I) | analogous | ([E]/[L]^d), ([E]/[L]^d)/[I] |

### 3.3 Gradient penalties
Because \(|\nabla C|^2\sim [C]^2/[L]^2\):
\[
[\kappa]=\frac{[E]/[L]^d}{[C]^2/[L]^2}=\frac{[E]\,[L]^{2-d}}{[C]^2}
\]
Similarly:
\[
[\kappa_C]=\frac{[E]\,[L]^{2-d}}{[C]^2},\quad
[\kappa_I]=\frac{[E]\,[L]^{2-d}}{[I]^2}
\]

### 3.4 Coupling β
From \(-\beta CI\) is energy density:
\[
[\beta]=\frac{[E]/[L]^d}{[C][I]}
\]

### 3.5 Mobility (Allen–Cahn form)
For \(\partial_t C=-M_C\mu_C\) and \([\mu_C]=([E]/[L]^d)/[C]\):
\[
[M_C]=\frac{[C]/[T]}{([E]/[L]^d)/[C]}=\frac{[C]^2[L]^d}{[E][T]}
\]
\[
[M_I]=\frac{[I]^2[L]^d}{[E][T]}
\]

---

## 4) Quartic coefficients (used in harness)
If:
\[
V(C)=\frac{a}{2}C^2+\frac{\delta}{4}C^4+sC
\]
then:
\[
[a]=\frac{[E]/[L]^d}{[C]^2},\quad
[\delta]=\frac{[E]/[L]^d}{[C]^4},\quad
[s]=\frac{[E]/[L]^d}{[C]}
\]
(analogous for I)

---

## 5) Dimensionless mode (default)
Declare:
- C, I are dimensionless order-1
- x, t are scaled already
- Ω is dimensionless energy-like functional (strict mode enforces monotone decrease)

In this mode: κ, β, a, δ, s, M are all dimensionless numbers.

---

## 6) What “Dimensional Gap closed” means in this project
ขั้นต่ำต้องมี:
- units table (ไฟล์นี้)
- nondimensionalization recipe (R0-E3_Nondimensionalization_Recipe)
- ระบุว่ารันงานนี้ใช้ mode ไหน (dimensionless/physical) ใน demo narratives หรือ config


---


# 🔹 Source: file_46.md

# UET R0-E6 — dt-Ladder Experiment Pack v0.1
**Goal:** เลือก dt “ใช้งานจริง” สำหรับ atlas/demos แบบ audit-friendly และเปรียบเทียบ semiimplicit vs stabilized

## Quickstart
1) Create matrix
```bash
python scripts/dt_ladder_matrix.py --out dt_ladder_matrix.csv --T 5 --N 128
```

2) Run ladder
```bash
python scripts/run_dt_ladder.py --matrix dt_ladder_matrix.csv --out dt_ladder_runs --overwrite
```

3) Summarize
```bash
python scripts/summarize_dt_ladder.py --ledger dt_ladder_runs/dt_ladder_ledger.csv
```

4) Plot
```bash
python scripts/plot_dt_ladder.py --summary_csv dt_ladder_runs/dt_ladder_summary/dt_ladder_summary.csv
```

## Recommended decision rule
- Use dt_max_pass per integrator (pass_threshold default=1.0)
- If tied, prefer lower median_backtracks and higher median_dt_min


---


# 🔹 Source: file_47.md

# UET R0-E7 — Atlas dt Presets from dt-Ladder v0.1
**Goal:** ทำให้ atlas sweep ใช้ dt ที่ “พิสูจน์แล้วว่ารอด” จาก dt-ladder  
โดยแยกตาม **(model × integrator)** และทำเป็น workflow ที่ audit-friendly

> แนวคิด: อย่าเดา dt. ให้ dt มาจาก evidence (ledger) แล้วค่อย freeze baseline

---

## 1) Inputs / Outputs
**Input**
- `dt_ladder_runs/dt_ladder_ledger.csv` (จาก R0-E6)

**Outputs**
- `dt_presets/dt_presets.json` : mapping `{model: {integrator: dt}}`
- `dt_presets/dt_presets_selected.csv` : ตารางเลือก dt
- `dt_presets/dt_presets_stats.csv` : pass-rate/backtracks ต่อ dt
- atlas matrix ใหม่ที่ถูก apply dt แล้ว

---

## 2) Extract dt presets (from ladder ledger)
```bash
python scripts/extract_dt_presets.py \
  --ledger dt_ladder_runs/dt_ladder_ledger.csv \
  --pass_threshold 1.0
```

จะได้ folder `dt_ladder_runs/dt_presets/` ที่มี `dt_presets.json`

> ถ้า boundary zones ทำให้ 1.0 เข้มเกิน: ใช้ 0.9 แต่ต้อง mark ว่า “boundary risk” (อย่า overclaim)

---

## 3) Apply dt presets to any matrix
ตัวอย่างกับ atlas stage1:
```bash
python scripts/apply_dt_presets_to_matrix.py \
  --matrix_in atlas_stage1.csv \
  --presets_json dt_ladder_runs/dt_presets/dt_presets.json \
  --matrix_out atlas_stage1_dt.csv \
  --mode overwrite
```

### Modes
- `overwrite` : เซ็ต dt ตาม preset ทุกแถวที่มี preset
- `fill_missing` : ใส่ dt เฉพาะแถวที่ dt ว่าง/0
- `cap_to_preset` : จำกัด dt ไม่ให้เกิน preset (dt = min(dt_old, dt_preset))

---

## 4) Recommended operational rule
- ใช้ `cap_to_preset` สำหรับ matrix ที่ dt ถูกตั้งไว้แล้ว (กัน “เผลอเพิ่ม dt”)
- ใช้ `overwrite` สำหรับ matrix generated ใหม่ที่อยากให้ “ทั้งชุด” ใช้ dt จาก evidence

---

## 5) Next step (R0-E8)
- ผูก dt presets เข้ากับ atlas band-map (บาง band อาจต้อง dt เล็กกว่า global)
- เพิ่ม “preset card” ลง baseline manifest (R0-D7) เพื่อ freeze baseline อย่างมีหลักฐาน

---


---


# 🔹 Source: file_48.md

# UET R0-E8 — Band-aware dt Presets + Baseline Manifest Integration v0.1
**Goal:** ยกระดับจาก dt preset แบบ global (model × integrator) → เป็น **band-aware**  
เพื่อให้ atlas sweep “เร็วแต่ไม่หลอก” โดยใช้ dt ตามความยากของ regime/band และล็อกหลักฐานลง baseline manifest

---

## 1) Why band-aware matters
ผล dt-ladder มักไม่สม่ำเสมอ:
- demo regimes ผ่าน dt ใหญ่ได้
- boundary regimes ต้อง dt เล็ก (ไม่งั้น backtrack แหลก หรือ fail)

ดังนั้นถ้าใช้ dt เดียวทั้ง atlas:
- ต้องเลือก dt เล็กสุดตาม boundary → เสียเวลามาก
- หรือเลือก dt ใหญ่ → boundary fail แล้ว map แตก

ทางออก: แยก dt ตาม band (หรือ regime class) แล้วใช้ **cap_to_preset** เป็น default

---

## 2) Inputs (minimum)
1) `dt_ladder_runs/dt_ladder_ledger.csv` (R0-E6)
2) `band_map.csv` mapping `base_case_id -> band`  
   (ทำเองจากความรู้ domain ของเรา: demo vs boundary หรือชื่อ band ใน atlas spec)

> วิธีง่ายสุด: ให้ band_map มีแค่ 2 band ก่อน: `DEMO` กับ `BOUNDARY`

---

## 3) Extract band dt presets
```bash
python scripts/extract_band_dt_presets.py \
  --ledger dt_ladder_runs/dt_ladder_ledger.csv \
  --band_map band_map.csv \
  --pass_threshold 1.0
```

Output:
- `dt_ladder_runs/band_dt_presets/band_dt_presets.json`
- `band_dt_presets_selected.csv`
- `band_dt_presets_stats.csv`

---

## 4) Apply band dt presets to atlas matrix
ต้องมีคอลัมน์ `band` ใน atlas matrix (หรือเปลี่ยนชื่อผ่าน `--band_col`)

```bash
python scripts/apply_band_dt_presets_to_matrix.py \
  --matrix_in atlas_stage1.csv \
  --matrix_out atlas_stage1_dt.csv \
  --band_presets_json dt_ladder_runs/band_dt_presets/band_dt_presets.json \
  --global_presets_json dt_ladder_runs/dt_presets/dt_presets.json \
  --mode cap_to_preset
```

**Fallback chain**
1) band preset (band × model × integrator)
2) global preset (model × integrator)
3) default_dt (ถ้ากำหนด)

---

## 5) Freeze evidence into baseline manifest
```bash
python scripts/freeze_baseline_manifest.py \
  --out baseline/baseline_manifest.json \
  --ledger dt_ladder_runs/dt_ladder_ledger.csv \
  --dt_presets dt_ladder_runs/dt_presets/dt_presets.json \
  --band_dt_presets dt_ladder_runs/band_dt_presets/band_dt_presets.json \
  --pass_threshold 1.0 \
  --note "dt presets frozen after ladder run 2025-xx-xx" \
  --overwrite
```

Manifest จะบันทึก:
- dt presets (global + band-aware)
- sha256 ของไฟล์หลักฐาน (ledger/presets) เพื่อ audit

---

## 6) Next step (R0-E9)
- ทำ “Band definition protocol” ที่ไม่อาศัย manual labeling:
  - band จาก metrics (เช่น backtracks density, ΔΩ margin, pattern metric)
- ผูกเข้ากับ Atlas Stage2 boundary refinement (R0-D3)


---


# 🔹 Source: file_49.md

# UET R0-E9 — Auto Band Definition from Metrics v0.1
**Goal:** ลดการกำหนด band ด้วยมือ โดยให้ band_map มาจาก “หลักฐานตัวเลข” ใน dt-ladder ledger  
แล้วนำไปใช้กับ R0-E8 (band-aware dt presets) และ baseline lock (manifest)

> บทนี้เป็น “protocol/engineering” ไม่ใช่การเพิ่มแก่นทฤษฎีฟิสิกส์

---

## 1) Input data (ขั้นต่ำ)
- `dt_ladder_runs/dt_ladder_ledger.csv` จาก R0-E6  
คีย์สำคัญที่ใช้:
- `base_case_id, integrator, dt, status, dt_backtracks_total, dt_min`

---

## 2) Core metric: dt_max_pass (per case)
สำหรับแต่ละ `base_case_id` และ integrator:
- หา `dt_max_pass` = dt ที่มากที่สุดที่ **PASS**

แล้ว collapse เป็น “robust_dt” ตาม policy:
- `max_over_integrators` (default): robust_dt = max(dt_max_pass_semi, dt_max_pass_stab)
- `min_over_integrators`: conservative (ต้องรอดทั้งคู่โดยนัย)
- `semiimplicit_only` / `stabilized_only`: ใช้ตัวเดียว

---

## 3) Band rule (default)
ให้ thresholds:
- DEMO: robust_dt ≥ 0.05 (และ backtracks ไม่สูงเกิน)
- MID: 0.02 ≤ robust_dt < 0.05
- BOUNDARY: 0.01 ≤ robust_dt < 0.02
- HARD: robust_dt < 0.01
- FAIL: ไม่มี dt ไหน PASS

**Safety tweak:** ถ้า band เป็น DEMO แต่ median backtracks@robust_dt > 1 → ลดเป็น MID (กัน “DEMO ที่จริง stiff”)

---

## 4) Generate band_map.csv (auto)
```bash
python scripts/auto_band_map_from_ledger.py \
  --ledger dt_ladder_runs/dt_ladder_ledger.csv \
  --out band_map.csv \
  --policy max_over_integrators \
  --demo_dt 0.05 --mid_dt 0.02 --hard_dt 0.01
```

Output `band_map.csv` มีคอลัมน์เพิ่ม:
- `robust_dt, dt_max_semi, dt_max_stab, chosen_integrator, median_backtracks_at_robust_dt, notes`

---

## 5) Apply band to atlas matrix
ถ้า atlas matrix ยังไม่มีคอลัมน์ band:
```bash
python scripts/add_band_to_matrix.py \
  --matrix_in atlas_stage1.csv \
  --band_map band_map.csv \
  --matrix_out atlas_stage1_with_band.csv \
  --key_col base_case_id \
  --band_col band
```

ถ้า matrix มีแต่ `case_id` ที่เป็นรูป `base__...`:
```bash
python scripts/add_band_to_matrix.py \
  --matrix_in atlas_stage1.csv \
  --band_map band_map.csv \
  --matrix_out atlas_stage1_with_band.csv \
  --extract_from_case_id
```

---

## 6) Plug into R0-E8 + baseline manifest
1) ใช้ `band_map.csv` ไป extract band_dt_presets (R0-E8)
2) freeze หลักฐานลง manifest:
```bash
python scripts/freeze_baseline_manifest.py \
  --out baseline/baseline_manifest.json \
  --ledger dt_ladder_runs/dt_ladder_ledger.csv \
  --dt_presets dt_ladder_runs/dt_presets/dt_presets.json \
  --band_dt_presets dt_ladder_runs/band_dt_presets/band_dt_presets.json \
  --band_map band_map.csv \
  --pass_threshold 1.0 \
  --overwrite
```

---

## 7) Next step (R0-E10)
- ปรับ auto-band ให้ robust ขึ้นด้วย additional metrics:
  - dt_min collapse ratio
  - ΔΩ margin (how close to violating gate)
  - pattern/structure metrics (ถ้าเพิ่มใน atlas)
- ทำ “band stability check” ว่า label ไม่สวิงง่ายเมื่อเปลี่ยน seed

---


---


# 🔹 Source: file_5.md

# UET Implementation Specification

**Version:** 0.9  
**Purpose:** Reproducible research, CI/CD, and deployment guide

---

## 1. Repository Structure

```
uet_harness_v0_1/
├── 📁 uet_min_pack/           # Core package (pip installable)
│   └── uet_core/
│       ├── __init__.py
│       ├── solver.py          # Main simulation loop
│       ├── energy.py          # Ω functional + decomposition
│       ├── potentials.py      # Quartic Landau potential
│       ├── operators.py       # Spectral operators
│       ├── variational.py     # Chemical potentials
│       ├── coercivity.py      # Stability checks
│       ├── snapshot_exporter.py   # Field export
│       └── demo_card_generator.py # Demo Card HTML
│
├── 📁 scripts/                # Command-line tools
│   ├── run_case.py           # Single case runner
│   ├── run_suite.py          # Batch runner
│   ├── run_atlas.py          # Parameter sweep
│   ├── run_with_snapshots.py # Demo runner
│   ├── generate_gallery.py   # Gallery generator
│   └── mi_card_generator.py  # MI Card tool
│
├── 📁 docs/                   # Documentation
│   ├── MATH_CORE.md          # Mathematical specification
│   ├── MI_CARD_TEMPLATE.md   # Modeling interface
│   └── example_mi_card.json  # Example MI Card
│
├── 📁 runs_*/                 # Output directories (gitignored)
│   ├── case_XXXX/
│   │   ├── config.json
│   │   ├── summary.json
│   │   ├── timeseries.csv
│   │   ├── snapshots/
│   │   └── demo_card/
│   └── ...
│
├── 📄 README.md               # Project overview
├── 📄 HANDOFF.md              # Status handoff document
├── 📄 requirements_frozen.txt # Locked dependencies
├── 📄 PYTHON_VERSION.txt      # Python version
├── 📄 setup.py                # Package setup
├── 📄 .gitignore              # Git exclusions
├── 📄 LICENSE                 # MIT License
└── 📄 run_all.ps1             # Master run script
```

---

## 2. Configuration Schema

### 2.1 Case Config (`config.json`)

```json
{
  "case_id": "case_0001",
  "run_id": "seed_42",
  "model": "C_I",
  "domain": {
    "L": 10.0,
    "dim": 2,
    "bc": "periodic"
  },
  "grid": {
    "N": 64
  },
  "time": {
    "dt": 0.01,
    "T": 10.0,
    "max_steps": 2000,
    "tol_abs": 1e-10,
    "tol_rel": 1e-10,
    "backtrack": {
      "factor": 0.5,
      "max_backtracks": 20
    }
  },
  "params": {
    "potC": {"type": "quartic", "a": -1.0, "delta": 1.0, "s": 0.3},
    "potI": {"type": "quartic", "a": -1.0, "delta": 1.0, "s": 0.3},
    "beta": 0.5,
    "kC": 0.5,
    "kI": 0.5,
    "MC": 1.0,
    "MI": 1.0
  }
}
```

### 2.2 Matrix Config (`matrix.csv`)

```csv
case_id,model,grid,dt,T,seed,params
case_0001,C_I,64,0.01,10.0,42,"{...}"
case_0002,C_I,64,0.01,10.0,43,"{...}"
...
```

---

## 3. Validators

### 3.1 Pre-run Validators

| Validator | Function | File |
|-----------|----------|------|
| Coercivity Check | `check_C_only()`, `check_CI()` | `coercivity.py` |
| Config Schema | Validate JSON structure | `run_case.py` |
| Parameter Bounds | Ensure physical validity | `coercivity.py` |

### 3.2 Runtime Validators

| Check | Condition | Action |
|-------|-----------|--------|
| NaN/Inf | `np.isfinite(C).all()` | FAIL immediately |
| Blowup | `max(abs(C)) > cap` | FAIL immediately |
| Energy Increase | `dΩ > tol` | Backtrack |
| Wall Timeout | `elapsed > limit` | FAIL with reason |

### 3.3 Post-run Validators

| Status | Conditions |
|--------|------------|
| **PASS** | Completed, Ω monotonic, no warnings |
| **WARN** | Completed but heavy backtracking (>100) |
| **FAIL** | Blowup, NaN, timeout, or energy increase |

---

## 4. Aggregators

### 4.1 Summary Aggregation

```python
# Collect all summary.json files
summaries = glob("runs_*/*/summary.json")

# Create master DataFrame
df = pd.DataFrame([json.load(open(f)) for f in summaries])

# Export
df.to_csv("master_summary.csv", index=False)
```

### 4.2 Phase Map Aggregation

```python
# Group by sweep parameters
phase_map = df.pivot_table(
    index="s",
    columns="beta",
    values="phase",
    aggfunc=lambda x: x.mode()[0]
)
```

---

## 5. Quality Gates

### 5.1 What Counts as PASS

A simulation **PASSES** if:

1. ✅ No NaN or Inf values detected
2. ✅ No blowup (max field value < cap)
3. ✅ Energy is monotonically decreasing (within tolerance)
4. ✅ Simulation completes within wall time
5. ✅ Backtracking count < 100 (otherwise WARN)

### 5.2 Why These Gates

| Gate | Rationale |
|------|-----------|
| **NaN/Inf** | Numerical instability, invalid results |
| **Blowup** | Physical solution unbounded, model failure |
| **Energy Monotone** | Gradient flow property, theory validation |
| **Wall Timeout** | Practical resource limit |
| **Backtracking** | Efficiency metric, stiff system indicator |

---

## 6. Reproducibility

### 6.1 Environment Lock

```bash
# Create environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\Activate.ps1

# Install locked deps
pip install -r requirements_frozen.txt
pip install -e ./uet_min_pack
```

### 6.2 Seed Management

```python
# Deterministic initialization
rng = np.random.default_rng(seed=42)
C = rng.normal(0.0, 0.1, size=(N, N))
```

### 6.3 Code Hash

```python
import hashlib

def compute_code_hash(files):
    h = hashlib.sha256()
    for f in sorted(files):
        h.update(open(f, "rb").read())
    return h.hexdigest()[:12]
```

---

## 7. CI/CD Configuration

### 7.1 GitHub Actions Workflow

Create `.github/workflows/test.yml`:

```yaml
name: UET Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements_frozen.txt
        pip install -e ./uet_min_pack
    
    - name: Run quick test
      run: |
        python scripts/run_with_snapshots.py \
          --case-id ci_test \
          --model C_I \
          --N 16 --T 1 \
          --out runs_ci
    
    - name: Verify output
      run: |
        test -f runs_ci/ci_test/summary.json
        python -c "import json; d=json.load(open('runs_ci/ci_test/summary.json')); assert d['status']=='PASS'"
```

### 7.2 Pre-commit Hooks

Create `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.2.0
    hooks:
      - id: black
        language_version: python3

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort

  - repo: https://github.com/pycqa/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
        args: [--max-line-length=120]
```

---

## 8. Release Checklist

### 8.1 Before Release

- [ ] All tests pass
- [ ] README updated
- [ ] HANDOFF.md current
- [ ] Version bumped
- [ ] CHANGELOG updated
- [ ] requirements_frozen.txt updated

### 8.2 Release Process

```bash
# 1. Create release branch
git checkout -b release/v0.9.0

# 2. Update version
echo "0.9.0" > VERSION

# 3. Build code-only pack
python scripts/pack_code_only.py

# 4. Tag and push
git tag -a v0.9.0 -m "Release 0.9.0"
git push origin v0.9.0

# 5. Create GitHub release with:
#    - uet_code_only_pack.zip (code)
#    - uet_reports_seed10.zip (artifacts, optional)
```

---

## 9. Troubleshooting

### 9.1 Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| `ModuleNotFoundError: uet_core` | Package not installed | `pip install -e ./uet_min_pack` |
| `FAIL: COERCIVITY_DELTA_NEG` | δ < 0 | Use δ > 0 for bounded potential |
| `FAIL: ENERGY_INCREASE` | Stiff system | Reduce dt, increase backtrack limit |
| `FAIL: BLOWUP` | Unbounded solution | Check coercivity conditions |
| Slow simulation | Large grid | Reduce N or use shorter T for testing |

### 9.2 Debug Mode

```bash
python scripts/run_case.py config.json \
  --progress-every-steps 10 \
  --wall-timeout 60
```

---

## 10. Performance Guidelines

### 10.1 Grid Size Recommendations

| Purpose | Grid N | Notes |
|---------|--------|-------|
| CI/Quick test | 16-32 | Fast, pattern visible |
| Development | 48-64 | Good balance |
| Production | 128-256 | High resolution |
| Publication | 256-512 | Maximum quality |

### 10.2 Typical Runtimes

| N | T=10 | T=100 |
|---|------|-------|
| 32 | ~2s | ~20s |
| 64 | ~8s | ~80s |
| 128 | ~30s | ~5min |
| 256 | ~2min | ~20min |

*(Times on modern CPU, single-threaded)*


---


# 🔹 Source: file_50.md

# UET Improvement Roadmap
## Making UET the "Python of Mathematical Modeling"

---

## 🎯 Vision

**Make UET as easy to use as Python is for programming**

```
Python: Easy to learn, hard to master, widely adopted
UET: Easy to learn, powerful enough, cross-domain
```

---

## 📈 Current Weaknesses → Improvements

### 1. ❌ Learning Curve (Mapping Domain → C, I, β)

**Problem:**
```
User must think: "What is my C? What is my I?"
This is cognitive overhead
```

**Solution: Domain Templates**

```python
# Instead of:
# "I need to figure out what C and I are..."

# Provide ready-made templates:
from uet.templates import NeuralTemplate, EconomicsTemplate, BiologyTemplate

# Neural modeling:
model = NeuralTemplate()
# Automatically sets:
# C = Excitatory activity
# I = Inhibitory state
# β = E-I balance
# κ = Connectivity

# Economics:
model = EconomicsTemplate()
# C = Price
# I = Fundamental value
# β = Market efficiency
```

**Implementation:**
- Create `uet/templates/` directory
- Pre-configured classes for each domain
- User just picks template + provides data

---

### 2. ❌ No Standard Features (Adaptive mesh, checkpointing, etc.)

**Problem:**
```
Basic Euler/RK4 only
Fixed grid
No error control
```

**Solution: Progressive Complexity**

```python
# Level 1: Beginner (current)
model = UETModel(grid_size=32, dt=0.01)
model.run(T=10)

# Level 2: Intermediate (add features)
model = UETModel(
    grid_size=32,
    adaptive_dt=True,      # Auto time-stepping
    error_tol=1e-6,        # Error control
    checkpoint_every=100   # Save progress
)

# Level 3: Advanced (full control)
model = UETModel(
    solver='RK45',         # Adaptive Runge-Kutta
    mesh='adaptive',       # Adaptive mesh refinement
    parallel=True,         # Multi-core
    gpu=True              # GPU acceleration (future)
)
```

**Implementation:**
- Add `adaptive_timestep.py`
- Add `checkpointing.py`
- Add `error_control.py`
- Keep simple API, add optional complexity

---

### 3. ❌ Performance (Python, no GPU, not optimized)

**Problem:**
```
Slow for large simulations
No parallelization
No GPU support
```

**Solution: Performance Tiers**

```python
# Tier 1: Pure Python (current) - for learning
from uet import UETModel

# Tier 2: NumPy optimized - for medium scale
from uet.fast import UETModelFast

# Tier 3: Numba JIT - for large scale
from uet.jit import UETModelJIT

# Tier 4: GPU (future) - for massive scale
from uet.gpu import UETModelGPU

# Same API, different backends!
```

**Implementation:**
- Optimize with Numba (JIT compilation)
- Add CuPy for GPU (optional dependency)
- Vectorize operations better
- Add parallel solver options

---

### 4. ❌ Limited Scope (only C-I coupling)

**Problem:**
```
Can't do:
- 3+ fields
- Discrete events
- Stochastic
```

**Solution: Extensions Module**

```python
# Core: 2 fields (C, I)
from uet import UETModel

# Extension: N fields
from uet.extensions import MultiFieldModel
model = MultiFieldModel(n_fields=5)  # C, I, J, K, L

# Extension: Stochastic
from uet.extensions import StochasticUET
model = StochasticUET(noise_level=0.1)

# Extension: Hybrid (continuous + discrete)
from uet.extensions import HybridUET
model = HybridUET(continuous=['C', 'I'], discrete=['events'])
```

**Implementation:**
- Keep core simple (C-I only)
- Add extensions for advanced users
- Maintain backward compatibility

---

### 5. ❌ Community & Ecosystem

**Problem:**
```
Small community
No plugins
No examples from others
```

**Solution: Ecosystem Building**

**A. Plugin System:**
```python
# Users can create plugins
from uet.plugin import UETPlugin

class MyCustomPotential(UETPlugin):
    def potential(self, phi):
        return phi**6  # Custom potential
    
# Register and use
model.register_plugin(MyCustomPotential())
```

**B. Example Gallery (already have!):**
- Expand to 100+ examples
- User-contributed examples
- "UET Cookbook" with recipes

**C. Integration with existing tools:**
```python
# Export to other formats
model.export_to_fenics()   # For FEM
model.export_to_pytorch()  # For ML
model.export_to_matlab()   # For MATLAB users
```

---

## 🎯 Priority Improvements (Next 6 Months)

### Phase 1: Ease of Use (Month 1-2)

| Feature | Impact | Effort |
|---------|--------|--------|
| **Domain Templates** | ⭐⭐⭐⭐⭐ Huge | Medium |
| **Better Documentation** | ⭐⭐⭐⭐⭐ Huge | Low |
| **Tutorial Notebooks** | ⭐⭐⭐⭐ High | Medium |
| **Error Messages** | ⭐⭐⭐⭐ High | Low |

### Phase 2: Features (Month 3-4)

| Feature | Impact | Effort |
|---------|--------|--------|
| **Adaptive Timestep** | ⭐⭐⭐⭐ High | Medium |
| **Checkpointing** | ⭐⭐⭐ Medium | Low |
| **Error Control** | ⭐⭐⭐ Medium | Medium |
| **Multi-field Extension** | ⭐⭐⭐ Medium | High |

### Phase 3: Performance (Month 5-6)

| Feature | Impact | Effort |
|---------|--------|--------|
| **Numba JIT** | ⭐⭐⭐⭐ High | Medium |
| **Vectorization** | ⭐⭐⭐ Medium | Low |
| **Parallel Solver** | ⭐⭐⭐ Medium | High |
| **GPU Support** | ⭐⭐ Low (niche) | Very High |

---

## 📚 Documentation Improvements

### Current: Basic docs
### Target: Python-level docs

**Add:**

1. **Quick Start (5 minutes)**
   ```python
   # Install
   pip install uet
   
   # Run first simulation
   from uet.templates import NeuralTemplate
   model = NeuralTemplate()
   model.run()
   model.plot()
   ```

2. **Tutorial Series**
   - Tutorial 1: Your first UET model (10 min)
   - Tutorial 2: Understanding C and I (15 min)
   - Tutorial 3: Parameter tuning (20 min)
   - Tutorial 4: Custom domains (30 min)

3. **API Reference**
   - Every function documented
   - Examples for each parameter
   - Type hints everywhere

4. **Cookbook**
   - Recipe: Fit to real data
   - Recipe: Custom potential
   - Recipe: 3D simulation
   - Recipe: Export results

---

## 🎓 Lower Learning Curve

### Strategy: "Pit of Success"

**Make the easy thing the right thing:**

```python
# BAD (current): User must know everything
model = UETModel(
    grid_size=32,
    dt=0.01,
    kappa=0.3,
    beta=0.5,
    s=0.0,
    pot_type='quartic',
    # ... 20 more parameters
)

# GOOD (improved): Sensible defaults
model = UETModel()  # Just works!

# BETTER: Domain-specific
model = NeuralModel()  # Optimized for neural
model.fit(eeg_data)    # Fits automatically
model.predict(steps=100)  # Predicts future
```

---

## 🔧 Implementation Priority

### Must Have (v0.2):
1. ✅ Domain templates (Neural, Economics, Biology)
2. ✅ Better error messages
3. ✅ Quick start guide
4. ✅ Tutorial notebooks

### Should Have (v0.3):
1. ⚠️ Adaptive timestep
2. ⚠️ Checkpointing
3. ⚠️ Numba optimization
4. ⚠️ Multi-field extension

### Nice to Have (v1.0):
1. 💡 GPU support
2. 💡 Plugin system
3. 💡 Export to other tools
4. 💡 Web interface

---

## 📊 Success Metrics

**How to measure if improvements work:**

| Metric | Current | Target (6 months) |
|--------|---------|-------------------|
| **Time to first simulation** | 30 min | 5 min |
| **Lines of code (hello world)** | 20 | 3 |
| **Documentation pages** | 5 | 50 |
| **Example gallery** | 50 | 100 |
| **GitHub stars** | 0 | 100 |
| **Users** | 1 | 50 |

---

## 🚀 Making UET the "Python of Math"

**Python succeeded because:**
1. Easy to learn (simple syntax)
2. Powerful enough (libraries)
3. Great documentation
4. Large community
5. "Batteries included"

**UET should:**
1. ✅ Easy to learn → Domain templates
2. ✅ Powerful enough → Extensions
3. ✅ Great docs → Tutorials + API ref
4. ⚠️ Community → Need to build
5. ✅ Batteries included → Gallery + templates

---

*Next: Implement Phase 1 (Domain Templates + Docs)*


---


# 🔹 Source: file_6.md

# UET Key Concepts (นิยามคำหลัก)

**Version:** 0.9  
**Purpose:** อธิบายแนวคิดหลักของ UET ให้คนทั่วไปเข้าใจ

---

## 🔑 4 คำหลักของ UET

### 1. สิ่งหนึ่ง (Entity)

**นิยาม:** สถานะ ณ จุดใดจุดหนึ่งในระบบ

**ในโค้ด:** ค่า `C[i,j]` หรือ `I[i,j]` ที่แต่ละจุด (pixel) ของ grid

**เปรียบเทียบ:**
- 🌡️ อุณหภูมิ ณ จุดหนึ่งในห้อง
- 💭 ความคิดเห็นของคนหนึ่งคน
- 📈 ราคาหุ้น ณ เวลาหนึ่ง
- ⚛️ ความหนาแน่นของอนุภาค ณ ตำแหน่งหนึ่ง

**หลักการ:**
> "สิ่งหนึ่ง" คือหน่วยที่เล็กที่สุดที่เราสนใจ  
> มันมี "สถานะ" ที่วัดได้เป็นตัวเลข

---

### 2. สนาม (Field)

**นิยาม:** กลุ่มของ "สิ่งหนึ่ง" ทั้งหมดที่กระจายอยู่ในพื้นที่

**ในโค้ด:** Array 2D ทั้งอัน เช่น `C[N,N]` ที่มี N×N จุด

**เปรียบเทียบ:**
- 🌊 แผนที่อุณหภูมิทั้งห้อง (temperature field)
- 🗳️ ความคิดเห็นของคนทั้งเมือง (opinion field)
- 📊 ราคาสินค้าทุกตัวในตลาด (price field)
- 🧠 การตัดสินใจของทุกส่วนในจิตใจ (C = Conscience, I = Instinct)

**หลักการ:**
> "สนาม" คือภาพรวมของ "สิ่งหนึ่ง" ทุกจุดรวมกัน  
> เราสนใจว่าสนามจะ "จัดรูป" ตัวเองอย่างไร

---

### 3. แรง (Force)

**นิยาม:** สิ่งที่ "ผลัก" ให้ระบบเปลี่ยนสถานะ

**ในโค้ด:** มาจาก `V'(C)` (อนุพันธ์ของ potential) และ coupling terms

**แรง 3 ประเภทใน UET:**

| แรง | สัญลักษณ์ | ความหมาย |
|-----|----------|----------|
| **แรงผลัก (Tilt)** | $s$ | แรงภายนอกที่ดึงให้เลือกข้าง |
| **แรงดึง (Coupling)** | $\beta$ | แรงระหว่าง C และ I ที่ดึงให้ไปด้วยกัน |
| **แรงต้าน (Gradient)** | $\kappa$ | ต้นทุนของการ "เปลี่ยนใจ" (surface tension) |

**เปรียบเทียบ:**
- 🧲 แรงผลัก = มีคนมาชวนให้เลือกข้าง A
- 🤝 แรงดึง = เพื่อนบ้านเลือกอะไร เราก็อยากเลือกตาม
- 🚧 แรงต้าน = ถ้าจะเปลี่ยนใจต้องใช้พลังงาน

**หลักการ:**
> "แรง" กำหนดว่าระบบจะเคลื่อนไปทางไหน  
> ผลรวมของแรงทั้งหมด = ทิศทางการเปลี่ยนแปลง

---

### 4. สมดุล (Equilibrium)

**นิยาม:** สถานะที่ระบบ "หยุด" เปลี่ยนแปลง (หรือเปลี่ยนช้ามาก)

**ในโค้ด:** เกิดเมื่อ $\frac{d\Omega}{dt} \approx 0$ (พลังงานไม่ลดต่อ)

**สมดุล 3 แบบใน UET:**

| สมดุล | Phase | ลักษณะ |
|-------|-------|--------|
| **BIAS_C** | C-dominant | สนามส่วนใหญ่ไป +1 (Conscience ชนะ) |
| **BIAS_I** | I-dominant | สนามส่วนใหญ่ไป +1 (Instinct ชนะ) |
| **SYM** | Symmetric | ไม่มีข้างไหนชนะชัด (สมดุลกลาง) |

**เปรียบเทียบ:**
- ⚖️ ลูกบอลหยุดนิ่งที่ก้นหลุม (local minimum)
- 🗳️ ผลเลือกตั้งที่ชัดเจน (BIAS) หรือ 50-50 (SYM)
- 💧 น้ำที่หยุดไหลเมื่อเต็มภาชนะ

**หลักการ:**
> "สมดุล" คือปลายทางของระบบ  
> ระบบจะลดพลังงานจนถึงจุดที่ลดต่อไม่ได้

---

## 🎭 การอ่านแบบ 2 แกน (Two-Axis Reading)

### แกน Introvert (มองจากข้างใน)

> "ฉันคือสิ่งหนึ่ง สถานะฉันเป็นอย่างไร?"

- สถานะปัจจุบัน: `C[i,j]` หรือ `I[i,j]`
- พลังงานที่นี่: `V(C[i,j])`
- แรงกดดันที่ฉันรู้สึก: จากเพื่อนบ้าน + แรงภายนอก

### แกน Extrovert (มองจากข้างนอก)

> "ระบบทั้งหมดเป็นอย่างไร?"

- ภาพรวมของสนาม: mean(C), mean(I)
- พลังงานรวม: Ω (Omega)
- Phase ของระบบ: BIAS_C / BIAS_I / SYM

---

## 📊 Value vs Conflict

### Value (คุณค่า)

**นิยาม:** สิ่งดีที่ระบบได้รับจากการถึงสมดุล

**วัดจาก:**
- พลังงานที่ลดได้: $V = \Omega_0 - \Omega_{final}$
- ความชัดเจนของ phase: ยิ่ง bias สูง ยิ่งมี value

**เปรียบเทียบ:**
- 💰 กำไรที่ได้จากการตัดสินใจ
- 🎯 ความชัดเจนของผลลัพธ์
- 😌 ความสบายใจที่ได้ตัดสินใจแล้ว

### Conflict (ความขัดแย้ง)

**นิยาม:** ต้นทุนหรืออุปสรรคที่ระบบต้องจ่ายเพื่อถึงสมดุล

**วัดจาก:**
- Gradient cost: $\Omega_{grad}$ สูง = มีเส้นแบ่งเขตมาก
- Backtracking: ระบบต้อง reject step บ่อย = ยากลำบาก
- Oscillation: ค่า bias สั่นไม่นิ่ง = ตัดสินใจลำบาก

**เปรียบเทียบ:**
- 💔 ต้นทุนทางจิตใจของการเลือก
- 🧗 ความยากของเส้นทาง
- ⚔️ การต่อสู้ระหว่างสองข้าง

---

## 🔄 วงจรของ UET

```
เริ่มต้น (Random Field)
    ↓
แรงผลักดัน (Forces)
    ↓
ระบบเปลี่ยนแปลง (Dynamics)
    ↓
พลังงานลด (Ω decreases)
    ↓
ถึงสมดุล (Equilibrium)
    ↓
ได้ Phase (BIAS_C / BIAS_I / SYM)
```

---

## 📝 สรุป 1 บรรทัด

| คำ | นิยาม 1 บรรทัด |
|----|----------------|
| **สิ่งหนึ่ง** | สถานะ ณ จุดหนึ่ง (C[i,j]) |
| **สนาม** | กลุ่มของสิ่งหนึ่งทั้งระบบ (C[N,N]) |
| **แรง** | สิ่งที่ผลักให้เปลี่ยน (s, β, κ) |
| **สมดุล** | จุดที่หยุดเปลี่ยน (BIAS_C/I/SYM) |
| **Value** | สิ่งดีที่ได้ (พลังงานที่ลด) |
| **Conflict** | ต้นทุนที่จ่าย (gradient, backtracks) |

---

**เกณฑ์ผ่าน:** คนทั่วไปอ่านแล้วอธิบายได้ว่า "BIAS_C คือภาพอะไร"


---


# 🔹 Source: file_7.md

# 🎯 UET KPI Dashboard - User Guide

## สารบัญ
1. [Dashboard คืออะไร](#dashboard-คืออะไร)
2. [วิธีใช้งาน](#วิธีใช้งาน)
3. [เข้าใจ Metrics](#เข้าใจ-metrics)
4. [UET Dynamics อธิบายยังไง](#uet-dynamics-อธิบายยังไง)
5. [ตัวอย่างการใช้งาน](#ตัวอย่างการใช้งาน)
6. [คำถามที่พบบ่อย](#คำถามที่พบบ่อย)

---

## Dashboard คืออะไร

**UET KPI Dashboard** คือเครื่องมือติดตาม KPI (Key Performance Indicators) ที่ใช้หลักการ **UET Field Dynamics** ในการวิเคราะห์และทำนายแนวโน้ม

### ต่างจาก Dashboard ปกติยังไง?

| Feature | Dashboard ปกติ | UET Dashboard |
|---------|---------------|---------------|
| แสดงตัวเลข | ✅ | ✅ |
| แสดงกราฟ | ✅ | ✅ |
| **ทำนายอนาคต** | ❌ | ✅ |
| **Balance Check** | ❌ | ✅ |
| **เห็น Dynamics** | ❌ | ✅ |

---

## วิธีใช้งาน

### 1. เตรียมข้อมูล KPI

สร้างไฟล์ CSV ตามรูปแบบนี้:

```csv
date,revenue,customer_sat,process_eff,innovation
2024-01-01,100,85,75,60
2024-02-01,120,83,78,65
2024-03-01,140,80,80,70
...
```

**คำอธิบายคอลัมน์:**
- `date` - วันที่ (YYYY-MM-DD)
- `revenue` - รายได้ (ตัวเลขใดก็ได้)
- `customer_sat` - ความพึงพอใจลูกค้า (0-100)
- `process_eff` - ประสิทธิภาพกระบวนการ (0-100)
- `innovation` - ดัชนีนวัตกรรม (0-100)

### 2. รัน Backend

```powershell
python scripts/run_kpi_dashboard.py --input data/your_kpi.csv --out my_dashboard
```

**Output:**
- `my_dashboard/kpi_evolution.gif` - Animation แสดง field dynamics
- `my_dashboard/dashboard_data.json` - ข้อมูลสำหรับ dashboard
- `my_dashboard/index.html` - Dashboard หน้าเว็บ

### 3. เปิด Dashboard

```powershell
Start-Process my_dashboard/index.html
```

---

## เข้าใจ Metrics

### 1. ⚖️ Balance Score (คะแนนความสมดุล)

**คืออะไร:** วัดความสมดุลระหว่าง Financial (C) กับ Customer (I)

**สูตร:** `Ω = mean((C - I)²)`

**การแปลผล:**
- **0.0 - 0.5** 🟢 ดีมาก - สมดุลดี
- **0.5 - 1.5** 🟡 ปานกลาง - ควรระวัง
- **> 1.5** 🔴 แย่ - ไม่สมดุล ต้องแก้ไข

**ตัวอย่าง:**
```
Balance = 0.2 → Revenue กับ Customer Sat สอดคล้องกัน
Balance = 2.5 → Revenue สูงแต่ Customer Sat ต่ำ (ไม่ sustainable)
```

---

### 2. 🎯 Health Score (คะแนนสุขภาพองค์กร)

**คืออะไร:** สุขภาพโดยรวมของ KPIs

**สูตร:** `Health = 100 × (1 - min(Balance, 1))`

**การแปลผล:**
- **80-100%** 🟢 แข็งแรง
- **50-80%** 🟡 พอใช้
- **< 50%** 🔴 อ่อนแอ

---

### 3. 🔗 Coupling (ความเชื่อมโยง)

**คืออะไร:** ความสัมพันธ์ระหว่าง Revenue กับ Customer Satisfaction

**สูตร:** `Coupling = correlation(C, I)`

**การแปลผล:**
- **0.7 - 1.0** 🟢 เชื่อมโยงแน่นแฟ้น (ดี)
- **0.3 - 0.7** 🟡 เชื่อมโยงปานกลาง
- **< 0.3** 🔴 ไม่เชื่อมโยง (อันตราย)

**ตัวอย่าง:**
```
Coupling = 0.9 → Revenue ขึ้นเพราะ Customer พอใจ (ดี)
Coupling = 0.2 → Revenue ขึ้นแต่ Customer ไม่พอใจ (ระวัง!)
```

---

## UET Dynamics อธิบายยังไง

### สมการพื้นฐาน

```
dC/dt = κ∇²C - C(C²-1) - β(C-I) + s
dI/dt = κ∇²I - I(I²-1) - β(I-C)
```

### แปลเป็นภาษาคน:

| Term | ความหมาย | ในบริบท KPI |
|------|----------|-------------|
| **C** | Financial field | Revenue, Profit |
| **I** | Customer field | Satisfaction, NPS |
| **κ∇²C** | Diffusion | การแพร่กระจายข้ามแผนก |
| **-C(C²-1)** | Self-regulation | แนวโน้มกลับสู่ปกติ |
| **-β(C-I)** | Coupling | Revenue ผูกกับ Customer |
| **s** | Forcing | Innovation, Marketing |

### ทำไมใช้ UET?

**1. Predictive (ทำนายได้)**
- ดู `dC/dt` รู้ว่า revenue กำลังจะขึ้นหรือลง
- ไม่ต้องรอเห็นผล

**2. Balance Check (เช็คสมดุล)**
- Ω ลดลง = ระบบมีเสถียรภาพ
- Ω ขึ้น = เตือนก่อนเกิดวิกฤต

**3. Spatial Understanding (เห็นภาพรวม)**
- Field 2D แสดงหลายแผนก/ภูมิภาค
- เห็นว่าปัญหาเริ่มจากไหน

---

## ตัวอย่างการใช้งาน

### Case 1: Startup Growth

**Scenario:** Startup กำลังเติบโต แต่ไม่แน่ใจว่า sustainable หรือไม่

**ข้อมูล:**
```csv
date,revenue,customer_sat,process_eff,innovation
2024-01,50,90,70,80
2024-02,100,85,75,85
2024-03,200,75,80,90
2024-04,350,65,85,95
```

**Dashboard แสดง:**
- Balance Score: 0.5 → 1.5 → 2.8 (เพิ่มขึ้น! 🔴)
- Health Score: 85% → 70% → 45% (ลดลง! 🔴)
- Coupling: 0.8 → 0.5 → 0.2 (อ่อนลง! 🔴)

**Prediction:**
> ⚠️ Revenue เติบโตเร็ว แต่ Customer Sat ลดลง → ไม่ sustainable!

**Action:**
- หยุด aggressive growth
- Focus on customer retention
- ปรับ product quality

---

### Case 2: Corporate Balance

**Scenario:** บริษัทใหญ่ต้องการ balanced scorecard

**ข้อมูล:**
```csv
date,revenue,customer_sat,process_eff,innovation
2024-Q1,1000,85,80,70
2024-Q2,1050,87,82,72
2024-Q3,1100,88,85,75
2024-Q4,1150,90,87,78
```

**Dashboard แสดง:**
- Balance Score: 0.3 (stable 🟢)
- Health Score: 92% (excellent 🟢)
- Coupling: 0.85 (strong 🟢)

**Prediction:**
> ✅ All metrics healthy - sustainable growth

---

### Case 3: Crisis Detection

**Scenario:** ตรวจจับวิกฤตก่อนเกิด

**ข้อมูล:**
```csv
date,revenue,customer_sat,process_eff,innovation
2024-01,500,80,85,75
2024-02,520,78,83,73
2024-03,540,75,80,70
2024-04,560,70,75,65
```

**Dashboard แสดง:**
- Balance Score: 0.5 → 0.8 → 1.2 (เพิ่มขึ้น 🟡)
- dC/dt > 0 แต่ dI/dt < 0 (ขาดสมดุล)

**Prediction:**
> ⚠️ Revenue ยังขึ้น แต่ Customer Sat ลดต่อเนื่อง → วิกฤตกำลังมา!

**Early Warning:** 2-3 เดือนก่อนเห็นผลกระทบ

---

## คำถามที่พบบ่อย

### Q1: ต้องมีข้อมูลย้อนหลังกี่เดือน?
**A:** อย่างน้อย 6-12 เดือน ยิ่งมากยิ่งดี

### Q2: ถ้า KPI ไม่ตรงกับ 4 คอลัมน์ล่ะ?
**A:** ปรับได้! แค่ map ให้ถูก:
- C = Financial metric ใดก็ได้
- I = Customer/Stakeholder metric
- s = Innovation/Forcing term

### Q3: Balance Score ควรเป็นเท่าไหร่?
**A:** ยิ่งต่ำยิ่งดี แต่:
- Startup: 0.5-1.0 ยอมรับได้ (growth phase)
- Corporate: < 0.5 ดีที่สุด (stable)

### Q4: Coupling ติดลบได้ไหม?
**A:** ได้! แปลว่า:
- Coupling < 0 = Revenue กับ Customer เคลื่อนตรงข้าม
- **อันตรายมาก!** ต้องแก้ด่วน

### Q5: ทำนายได้แม่นแค่ไหน?
**A:** ขึ้นกับ:
- คุณภาพข้อมูล
- ความสม่ำเสมอของ business
- External shocks (ทำนายไม่ได้)

---

## สรุป

**UET KPI Dashboard ให้อะไร:**
1. ✅ **Visualization** - เห็นภาพชัด
2. ✅ **Prediction** - ทำนายแนวโน้ม
3. ✅ **Balance Check** - เช็คความสมดุล
4. ✅ **Early Warning** - เตือนก่อนวิกฤต

**เหมาะกับ:**
- Startups (ติดตามการเติบโต)
- Corporates (balanced scorecard)
- Personal (life balance tracking)

**ไม่เหมาะกับ:**
- ธุรกิจที่ไม่มี pattern
- ข้อมูลน้อยเกินไป (< 6 เดือน)
- ต้องการ accuracy 100% (ไม่มี tool ไหนทำได้)

---

## ติดต่อ / Support

**Documentation:**
- [Implementation Plan](kpi_dashboard_plan.md)
- [UET Theory](../docs/KEY_CONCEPTS.md)

**Quick Start:**
```powershell
# 1. เตรียมข้อมูล
# 2. รัน
python scripts/run_kpi_dashboard.py --input data/my_kpi.csv

# 3. เปิด
Start-Process kpi_dashboard/index.html
```

**Happy Tracking! 🎯**


---


# 🔹 Source: file_8.md

# UET KPI Dashboard - Implementation Plan

## 🎯 Goal
สร้าง Balanced Scorecard & KPI Tracker ที่ใช้ UET dynamics แสดง:
- KPI evolution แบบ real-time
- Prediction & trends
- Balance score (Ω)
- Coupling between metrics

---

## 📊 Dashboard Layout

### **Main View:**
```
┌─────────────────────────────────────────────────────┐
│  🎯 UET KPI Dashboard - [Organization Name]        │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌──────────────┐  ┌──────────────┐               │
│  │ 💰 Financial │  │ 😊 Customer  │               │
│  │   Field      │  │   Field      │               │
│  │  (heatmap)   │  │  (heatmap)   │               │
│  └──────────────┘  └──────────────┘               │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │ 📈 KPI Trends Over Time                     │  │
│  │  - Revenue (green)                          │  │
│  │  - Customer Sat (blue)                      │  │
│  │  - Process Efficiency (orange)              │  │
│  └──────────────────────────────────────────────┘  │
│                                                     │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐   │
│  │ ⚖️ Balance │  │ 🔗 Coupling│  │ 🎯 Health  │   │
│  │   Score    │  │   Strength │  │   Score    │   │
│  │    Ω=2.3   │  │    β=0.7   │  │    85%     │   │
│  └────────────┘  └────────────┘  └────────────┘   │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │ 🔮 Predictions (Next 30 Days)               │  │
│  │  ⚠️ Revenue trend declining                 │  │
│  │  ✅ Customer sat improving                  │  │
│  │  ⚠️ Balance score increasing (risky)        │  │
│  └──────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

---

## 🔧 Technical Implementation

### **Phase 1: Backend (Python)**

**File:** `scripts/run_kpi_dashboard.py`

```python
# Input: CSV with KPI data
# Columns: date, revenue, customer_sat, process_eff, innovation

# Map to UET:
C = Revenue field (2D: departments × time)
I = Customer satisfaction field
s = Innovation/marketing forcing term

# Run simulation
history = run_kpi_simulation(data, config)

# Output:
- KPI evolution GIF
- Metrics JSON (Ω, coherence, predictions)
- Dashboard HTML
```

---

### **Phase 2: Frontend (HTML/JS)**

**File:** `kpi_dashboard.html`

**Features:**
- 📊 Interactive charts (Chart.js)
- 🎨 Field heatmaps (animated)
- 🔄 Real-time updates (load new data)
- 📱 Responsive (mobile-friendly)
- 🎯 Drill-down (click for details)

---

## 📈 KPI Mapping

### **Balanced Scorecard → UET:**

| Perspective | UET Field | Metric Example |
|-------------|-----------|----------------|
| **Financial** | C field | Revenue, Profit, Cash flow |
| **Customer** | I field | NPS, Satisfaction, Retention |
| **Internal** | β coupling | Efficiency, Quality, Cycle time |
| **Learning** | s forcing | Training hours, Innovation index |

---

## 🎨 Visualization Types

### **1. Field Heatmaps**
- Revenue field (C) - color: green (high) to red (low)
- Customer field (I) - color: blue (happy) to purple (unhappy)
- Animated over time

### **2. Time Series Charts**
- Multi-line chart: all KPIs
- Prediction overlay (dotted lines)
- Event markers (product launches, etc.)

### **3. Gauge Meters**
- Balance Score (Ω): 0-10 scale
- Health Score: 0-100%
- Coupling Strength (β): 0-1

### **4. Alert Panel**
- 🔴 Critical: Ω > 5 (imbalanced)
- 🟡 Warning: Revenue declining
- 🟢 Good: All metrics healthy

---

## 💼 Use Cases

### **A. Startup Dashboard**
**Metrics:**
- Monthly Recurring Revenue (MRR)
- Customer Acquisition Cost (CAC)
- Churn Rate
- Product Development Velocity

**Insight:**
- See if growth is sustainable (Ω check)
- Predict when to raise funding (trend analysis)

---

### **B. Corporate BSC**
**Metrics:**
- Quarterly Revenue
- Employee Satisfaction
- Process Efficiency
- Innovation Pipeline

**Insight:**
- Balance check across 4 perspectives
- Early warning for imbalance

---

### **C. Personal KPI Tracker**
**Metrics:**
- Income
- Health (exercise, sleep)
- Learning (courses completed)
- Relationships (quality time)

**Insight:**
- Life balance score
- Predict burnout

---

## 🚀 Implementation Steps

### **Day 1: Backend**
1. ✅ Copy `run_toy_stock.py` → `run_kpi_dashboard.py`
2. ✅ Modify to accept CSV input
3. ✅ Map columns to C, I fields
4. ✅ Generate metrics JSON
5. ✅ Test with sample data

### **Day 2: Frontend**
1. ✅ Create HTML template
2. ✅ Add Chart.js for time series
3. ✅ Add heatmap visualization
4. ✅ Add gauge meters
5. ✅ Style with modern CSS
6. ✅ Test responsiveness

### **Day 3: Integration & Polish**
1. ✅ Connect backend → frontend
2. ✅ Add data refresh button
3. ✅ Add export (PDF/PNG)
4. ✅ Write documentation
5. ✅ Create demo video

---

## 📦 Deliverables

### **1. Code**
- `scripts/run_kpi_dashboard.py` - Backend
- `kpi_dashboard.html` - Frontend
- `sample_kpi_data.csv` - Example data

### **2. Documentation**
- `README_KPI.md` - How to use
- `KPI_MAPPING.md` - How to map your KPIs

### **3. Demo**
- `demo_kpi.gif` - Animated demo
- `sample_dashboard.html` - Live example

---

## 💡 Selling Points

### **For Organizations:**
> "Dashboard ที่ไม่ใช่แค่แสดงตัวเลข แต่เข้าใจ dynamics และทำนายอนาคต"

**Features:**
- ✅ Predictive (ไม่ใช่แค่ retrospective)
- ✅ Balance check (Ω metric)
- ✅ Visual (เห็นภาพชัด)
- ✅ Scientific (based on physics)

### **Differentiation:**
| Feature | Normal Dashboard | UET Dashboard |
|---------|-----------------|---------------|
| Show current | ✅ | ✅ |
| Show trends | ✅ | ✅ |
| **Predict future** | ❌ | ✅ |
| **Balance score** | ❌ | ✅ |
| **Coupling analysis** | ❌ | ✅ |
| **Physics-based** | ❌ | ✅ |

---

## 🎯 Success Metrics

### **Technical:**
- ✅ Dashboard loads < 2 seconds
- ✅ Updates in real-time
- ✅ Works on mobile

### **Business:**
- ✅ 1 organization adopts
- ✅ Positive feedback
- ✅ Actual predictions come true

---

## ⏱️ Timeline

| Phase | Duration | Output |
|-------|----------|--------|
| Backend | 1 day | Python script working |
| Frontend | 1 day | HTML dashboard |
| Polish | 1 day | Production-ready |
| **Total** | **3 days** | **Deployable product** |

---

## 🔄 Future Enhancements

### **Phase 2 (Optional):**
- Real-time data integration (API)
- Multi-organization support
- Custom KPI definitions
- Mobile app
- AI recommendations

---

## 📝 Sample Data Format

```csv
date,revenue,customer_sat,process_eff,innovation
2024-01-01,100,85,75,60
2024-02-01,120,83,78,65
2024-03-01,140,80,80,70
...
```

**Output:**
- Animated GIF showing field evolution
- JSON with predictions
- HTML dashboard

---

## 🎨 Design Mockup

**Color Scheme:**
- Primary: #2563eb (blue)
- Success: #10b981 (green)
- Warning: #f59e0b (orange)
- Danger: #ef4444 (red)
- Background: #0f172a (dark)

**Typography:**
- Headers: Inter Bold
- Body: Inter Regular
- Metrics: JetBrains Mono

---

## ✅ Ready to Start?

**Next step:**
```powershell
# Create backend
python scripts/run_kpi_dashboard.py --input sample_kpi_data.csv

# View dashboard
Start-Process kpi_dashboard.html
```

**Timeline:** 3 days to working prototype! 🚀


---


# 🔹 Source: file_9.md

# UET Mathematical Core Specification

**Version:** 0.9  
**Status:** Paper-ready  
**Last Updated:** 2024-12

---

## Abstract

This document provides a complete mathematical specification of the Universal Evolution Thermodynamics (UET) framework. The framework models coupled field systems undergoing phase transitions and symmetry breaking through gradient flow dynamics on a Landau-Ginzburg free energy functional.

---

## 1. Energy Functional

### 1.1 Single Field (C-only Model)

For a single order parameter field $C(\mathbf{x}, t)$ on a periodic domain $\Omega = [0, L]^d$:

$$\Omega[C] = \int_\Omega \left[ V(C) + \frac{\kappa}{2}|\nabla C|^2 \right] d\mathbf{x}$$

where:
- $V(C)$ is the Landau potential (local bulk energy)
- $\frac{\kappa}{2}|\nabla C|^2$ is the gradient energy (surface tension)

### 1.2 Quartic Landau Potential

The quartic (double-well) potential:

$$V(u) = \frac{a}{2}u^2 + \frac{\delta}{4}u^4 - su$$

Parameters:
| Parameter | Physical Meaning | Typical Range |
|-----------|-----------------|---------------|
| $a$ | Quadratic coefficient | $a < 0$ for double-well |
| $\delta$ | Quartic coefficient | $\delta > 0$ for boundedness |
| $s$ | External field / tilt | Controls symmetry breaking |

**Critical Points:** For $s = 0$, the minima are at $u^* = \pm\sqrt{-a/\delta}$ when $a < 0$.

### 1.3 Coupled Fields (C-I Model)

For two coupled fields $C(\mathbf{x}, t)$ and $I(\mathbf{x}, t)$:

$$\Omega[C, I] = \int_\Omega \left[ V_C(C) + V_I(I) - \beta C \cdot I + \frac{\kappa_C}{2}|\nabla C|^2 + \frac{\kappa_I}{2}|\nabla I|^2 \right] d\mathbf{x}$$

where:
- $V_C(C)$, $V_I(I)$ are individual Landau potentials
- $-\beta C \cdot I$ is the coupling energy (negative = cooperative)
- $\beta > 0$ promotes alignment of fields

### 1.4 Energy Decomposition

The total energy decomposes as:

$$\Omega = \Omega_{\text{pot}} + \Omega_{\text{coup}} + \Omega_{\text{grad}}$$

| Component | Definition | Physical Meaning |
|-----------|------------|------------------|
| $\Omega_{\text{pot}}$ | $\int [V_C(C) + V_I(I)] d\mathbf{x}$ | Bulk potential energy |
| $\Omega_{\text{coup}}$ | $\int [-\beta C \cdot I] d\mathbf{x}$ | Coupling energy |
| $\Omega_{\text{grad}}$ | $\int \frac{1}{2}[\kappa_C|\nabla C|^2 + \kappa_I|\nabla I|^2] d\mathbf{x}$ | Gradient (surface) energy |

---

## 2. Dynamics

### 2.1 Gradient Flow (Model A / Allen-Cahn)

The dynamics follow $L^2$ gradient descent:

$$\frac{\partial C}{\partial t} = -M_C \frac{\delta\Omega}{\delta C} = -M_C \mu_C$$

$$\frac{\partial I}{\partial t} = -M_I \frac{\delta\Omega}{\delta I} = -M_I \mu_I$$

where the chemical potentials are:

$$\mu_C = V'_C(C) - \beta I - \kappa_C \nabla^2 C$$
$$\mu_I = V'_I(I) - \beta C - \kappa_I \nabla^2 I$$

### 2.2 Energy Dissipation (Lyapunov Property)

**Theorem 1 (Energy Monotonicity):** Along solutions of the gradient flow:

$$\frac{d\Omega}{dt} = -\int_\Omega \left[ M_C |\mu_C|^2 + M_I |\mu_I|^2 \right] d\mathbf{x} \leq 0$$

**Proof:** Direct computation using the chain rule and integration by parts with periodic boundary conditions. □

**Corollary:** $\Omega$ is a Lyapunov functional; stationary points are characterized by $\mu_C = \mu_I = 0$.

---

## 3. Discretization

### 3.1 Spatial Discretization

We use a uniform grid with $N$ points per dimension:
- Grid spacing: $\Delta x = L/N$
- Points: $x_j = j \cdot \Delta x$ for $j = 0, 1, \ldots, N-1$

**Spectral Laplacian (Periodic BC):**

$$(\nabla^2 u)_j = \mathcal{F}^{-1}[-|k|^2 \hat{u}_k]$$

where $k$ are the discrete wavenumbers: $k_j = \frac{2\pi}{L} \cdot \begin{cases} j & j < N/2 \\ j - N & j \geq N/2 \end{cases}$

**Spectral Gradient Energy:**

$$E_{\text{grad}} = \frac{\kappa}{2} \sum_k |k|^2 |\hat{u}_k|^2$$

### 3.2 Temporal Discretization (Semi-Implicit)

**Stiff Linear + Explicit Nonlinear:**

$$(1 - \alpha \Delta t \nabla^2) C^{n+1} = C^n + \Delta t \cdot R^n$$

where:
- Linear diffusion handled implicitly (Fourier space division)
- Nonlinear reaction term $R^n = -M[V'(C^n) - \beta I^n]$ explicit

**In Fourier Space:**

$$\hat{C}^{n+1}_k = \frac{\hat{C}^n_k + \Delta t \cdot \hat{R}^n_k}{1 + \alpha \Delta t |k|^2}$$

where $\alpha = M \kappa$.

---

## 4. Stability and Coercivity

### 4.1 Coercivity Condition

**Definition:** The energy functional is coercive if $\Omega[u] \to +\infty$ as $\|u\|_{H^1} \to \infty$.

**Theorem 2 (Coercivity):** For the quartic potential, $\Omega$ is coercive if and only if:
1. $\delta > 0$ (quartic term positive)
2. $\kappa > 0$ (gradient penalty positive)

**Coupled System Additional Condition:**
3. $|\beta| < \sqrt{\delta_C \delta_I}$ (coupling not too strong)

### 4.2 Numerical Stability

**CFL-type Condition:** For explicit treatment of reaction term:

$$\Delta t \leq \frac{C_{\text{CFL}}}{M \cdot L_V}$$

where $L_V = \sup_{u}|V''(u)| = |a| + 3\delta u_{\max}^2$ is the Lipschitz constant.

### 4.3 Energy Monitoring (Backtracking)

To preserve discrete energy monotonicity:

**Algorithm 1: Adaptive Backtracking**
```
1. Propose step: C_cand = step(C, dt)
2. Check: dΩ = Ω(C_cand) - Ω(C)
3. If dΩ > tol:
     dt ← dt × factor
     goto 1
4. Accept C_cand
```

Parameters:
- `tol`: tolerance for energy increase (default: $10^{-10}$)
- `factor`: backtrack factor (default: 0.5)
- `max_backtracks`: limit (default: 20)

---

## 5. Phase Classification

### 5.1 Order Parameter

Define the mean-field order parameter:

$$\langle C \rangle = \frac{1}{|\Omega|} \int_\Omega C(\mathbf{x}) d\mathbf{x}$$

### 5.2 Bias Metric

For coupled fields:

$$\text{bias}_{CI} = \langle C \rangle - \langle I \rangle$$

### 5.3 Phase Labels

| Phase | Condition | Physical Meaning |
|-------|-----------|------------------|
| **BIAS_C** | $\langle C \rangle > \theta$ and $\langle C \rangle > \langle I \rangle$ | C-dominant |
| **BIAS_I** | $\langle I \rangle > \theta$ and $\langle I \rangle > \langle C \rangle$ | I-dominant |
| **SYM** | Otherwise | Symmetric/disordered |

Default threshold: $\theta = 0.1$

---

## 6. Dimensional Analysis

### 6.1 Characteristic Scales

| Quantity | Scale | Expression |
|----------|-------|------------|
| Length | $\xi$ | $\xi = \sqrt{\kappa/|a|}$ (correlation length) |
| Energy | $\epsilon$ | $\epsilon = a^2/\delta$ (barrier height) |
| Time | $\tau$ | $\tau = 1/(M|a|)$ (relaxation time) |

### 6.2 Dimensionless Parameters

Rescaling $x \to x/\xi$, $t \to t/\tau$, $u \to u/u^*$:

$$\tilde{\Omega} = \int \left[ -\frac{1}{2}\tilde{u}^2 + \frac{1}{4}\tilde{u}^4 - \tilde{s}\tilde{u} + \frac{1}{2}|\tilde{\nabla}\tilde{u}|^2 \right] d\tilde{\mathbf{x}}$$

**Dimensionless tilt:** $\tilde{s} = s/(a u^*) = s \sqrt{\delta/|a|^3}$

### 6.3 Calibration

**Calibratable Parameters:**
- $s$: External field (maps to external bias/incentive)
- $\beta$: Coupling strength (maps to interaction intensity)
- $M$: Mobility (maps to timescale)

**Fixed Parameters (theory):**
- $a = -1$ (normalized)
- $\delta = 1$ (normalized)
- $\kappa = \xi^2$ (set by desired correlation length)

---

## 7. Implementation Reference

### 7.1 Core Functions

| Function | Location | Purpose |
|----------|----------|---------|
| `omega_C()` | `energy.py` | Total energy (C-only) |
| `omega_CI()` | `energy.py` | Total energy (coupled) |
| `omega_CI_decomposed()` | `energy.py` | Decomposed energy |
| `mu_CI()` | `variational.py` | Chemical potentials |
| `run_case()` | `solver.py` | Main simulation loop |

### 7.2 Validation

**Coercivity Check:** `check_C_only()`, `check_CI()` in `coercivity.py`

**Energy Monotonicity:** Tracked via `dt_backtracks_total` and `acceptance_ratio`

---

## 8. References

1. Landau, L.D. (1937). "On the theory of phase transitions."
2. Ginzburg, V.L. & Landau, L.D. (1950). "On the theory of superconductivity."
3. Allen, S.M. & Cahn, J.W. (1979). "A microscopic theory for antiphase boundary motion."
4. Chen, L.Q. (2002). "Phase-field models for microstructure evolution." *Annu. Rev. Mater. Res.*

---

## Appendix A: Full Energy Formula

**C-I Model (Discrete):**

$$\Omega = \Delta x^2 \sum_{i,j} \left[ V_C(C_{ij}) + V_I(I_{ij}) - \beta C_{ij} I_{ij} \right] + \frac{\kappa_C}{2} E_{\text{grad}}[C] + \frac{\kappa_I}{2} E_{\text{grad}}[I]$$

where $E_{\text{grad}}[u] = \sum_k |k|^2 |\hat{u}_k|^2$ (Parseval).

---

## Appendix B: Proof of Lyapunov Property

**Claim:** $\frac{d\Omega}{dt} \leq 0$ along gradient flow dynamics.

**Proof:**

$$\frac{d\Omega}{dt} = \int \frac{\delta\Omega}{\delta C} \frac{\partial C}{\partial t} + \frac{\delta\Omega}{\delta I} \frac{\partial I}{\partial t} d\mathbf{x}$$

Substituting $\partial_t C = -M_C \mu_C$ and $\partial_t I = -M_I \mu_I$:

$$= \int \mu_C (-M_C \mu_C) + \mu_I (-M_I \mu_I) d\mathbf{x}$$

$$= -\int M_C |\mu_C|^2 + M_I |\mu_I|^2 d\mathbf{x} \leq 0$$

Equality holds iff $\mu_C = \mu_I = 0$ (stationary point). □


---
