

# 🔹 Source: file_0.md

# UET Extensions - Custom Potentials

## 🎨 Custom Potentials in UET

**Why Custom Potentials?**

Different systems have **different energy landscapes**:
- **Double-well:** Bistability (current default)
- **Single-well:** Simple attractor
- **Triple-well:** Three stable states
- **Periodic:** Angular variables (phase, orientation)
- **Asymmetric:** Broken symmetry
- **Domain-specific:** Custom physics

**One potential doesn't fit all!**

---

## 📐 Mathematical Formulation

### Standard UET (Double-well):
```
V(φ) = (φ² - 1)² / 4

Minima at φ = ±1
Barrier at φ = 0
```

### Custom Potential:
```
V(φ) = user_defined_function(φ, params)

∂V/∂φ = user_defined_derivative(φ, params)
```

---

## 🎨 Potential Library

### 1. Double-Well (Current Default)
```python
def V_double_well(phi):
    return (phi**2 - 1)**2 / 4

def dV_double_well(phi):
    return phi * (phi**2 - 1)
```

**Properties:**
- 2 minima: φ = ±1
- Barrier height: 1/4
- Symmetric

**Use:** Bistable systems, binary states

---

### 2. Single-Well (Harmonic)
```python
def V_single_well(phi, k=1.0):
    return 0.5 * k * phi**2

def dV_single_well(phi, k=1.0):
    return k * phi
```

**Properties:**
- 1 minimum: φ = 0
- No barrier
- Restoring force

**Use:** Damped oscillators, relaxation

---

### 3. Triple-Well
```python
def V_triple_well(phi, a=1.0):
    return a * (phi**4 - 2*phi**2) + 1

def dV_triple_well(phi, a=1.0):
    return a * (4*phi**3 - 4*phi)
```

**Properties:**
- 3 minima: φ = 0, ±√2
- 2 barriers
- Central + two side wells

**Use:** Decision-making (3 choices), bifurcations

---

### 4. Periodic (Cosine)
```python
def V_periodic(phi, k=1.0):
    return -k * np.cos(phi)

def dV_periodic(phi, k=1.0):
    return k * np.sin(phi)
```

**Properties:**
- Periodic with period 2π
- Infinite minima
- Periodic boundary

**Use:** Angular variables (phase, rotation)

---

### 5. Asymmetric Double-Well
```python
def V_asymmetric(phi, a=0.2):
    return (phi**2 - 1)**2 / 4 + a * phi

def dV_asymmetric(phi, a=0.2):
    return phi * (phi**2 - 1) + a
```

**Properties:**
- 2 unequal minima
- Broken symmetry
- One well deeper

**Use:** Preferred states, hysteresis

---

### 6. Mexican Hat
```python
def V_mexican_hat(phi, r=1.0):
    r_sq = np.sum(phi**2, axis=-1)  # For 2D phi
    return (r_sq - r**2)**2 / 4

def dV_mexican_hat(phi, r=1.0):
    r_sq = np.sum(phi**2, axis=-1, keepdims=True)
    return phi * (r_sq - r**2)
```

**Properties:**
- Continuous circle of minima
- Central maximum
- Symmetry breaking

**Use:** Phase transitions, Higgs mechanism

---

### 7. Polynomial (General)
```python
def V_polynomial(phi, coeffs=[1, 0, -1, 0, 0.25]):
    """V(φ) = Σ cₙφⁿ"""
    return sum(c * phi**n for n, c in enumerate(coeffs))

def dV_polynomial(phi, coeffs=[1, 0, -1, 0, 0.25]):
    return sum(n * c * phi**(n-1) for n, c in enumerate(coeffs) if n > 0)
```

**Properties:**
- Arbitrary polynomial
- User-defined

**Use:** Fitting to experimental data

---

## 🔧 Implementation

```python
class UETWithCustomPotential:
    """UET with user-defined potential."""
    
    def __init__(self, N=32, kappa=0.1, beta=0.5, s=0.0,
                 potential_func=None, potential_deriv=None,
                 potential_params=None, dt=0.01):
        self.N = N
        self.kappa = kappa
        self.beta = beta
        self.s = s
        self.dt = dt
        
        # Potential functions
        if potential_func is None:
            # Default: double-well
            self.V = lambda phi: (phi**2 - 1)**2 / 4
            self.dV = lambda phi: phi * (phi**2 - 1)
        else:
            self.V = potential_func
            self.dV = potential_deriv
        
        # Potential parameters
        self.pot_params = potential_params or {}
        
        # Initialize fields
        self.C = np.random.randn(N, N) * 0.1 + 1.0
        self.I = np.random.randn(N, N) * 0.1 - 1.0
    
    def step(self):
        """Evolve with custom potential."""
        C, I = self.C, self.I
        
        # Use custom potential derivative
        if self.pot_params:
            dV_C = self.dV(C, **self.pot_params)
            dV_I = self.dV(I, **self.pot_params)
        else:
            dV_C = self.dV(C)
            dV_I = self.dV(I)
        
        # Compute derivatives
        dC_dt = (
            self.kappa * laplacian_2d(C) -
            dV_C -
            self.beta * (C - I) +
            self.s
        )
        
        dI_dt = (
            self.kappa * laplacian_2d(I) -
            dV_I -
            self.beta * (I - C)
        )
        
        # Update
        self.C = C + self.dt * dC_dt
        self.I = I + self.dt * dI_dt
```

---

## 🎯 Use Cases

### 1. Phase Oscillators (Neural)

**Use periodic potential:**

```python
# Neuroscience: Phase-coupled oscillators
model = UETWithCustomPotential(
    potential_func=lambda phi: -np.cos(phi),
    potential_deriv=lambda phi: np.sin(phi)
)

# C, I = Phase of oscillators
# Result: Phase synchronization (Kuramoto model)
```

---

### 2. Decision-Making (Triple-well)

**3 choices:**

```python
# Cognitive: Three-choice decision
model = UETWithCustomPotential(
    potential_func=lambda phi: phi**4 - 2*phi**2 + 1,
    potential_deriv=lambda phi: 4*phi**3 - 4*phi
)

# Result: System settles into one of 3 choices
```

---

### 3. Asymmetric Hysteresis

**Preferred state:**

```python
# Materials: Asymmetric ferromagnet
model = UETWithCustomPotential(
    potential_func=lambda phi, a: (phi**2-1)**2/4 + a*phi,
    potential_deriv=lambda phi, a: phi*(phi**2-1) + a,
    potential_params={'a': 0.2}
)

# Result: One magnetization direction preferred
```

---

### 4. Fitting to Data

**Learn potential from observations:**

```python
# Data-driven: Fit polynomial
coeffs = fit_potential_to_data(observed_dynamics)

model = UETWithCustomPotential(
    potential_func=lambda phi: sum(c*phi**n for n,c in enumerate(coeffs)),
    potential_deriv=lambda phi: sum(n*c*phi**(n-1) for n,c in enumerate(coeffs) if n>0)
)

# Result: Captures empirical dynamics
```

---

## 📊 Potential Comparison

| Potential | # Minima | Symmetry | Use Case |
|-----------|----------|----------|----------|
| **Double-well** | 2 | Symmetric | Binary states |
| **Single-well** | 1 | Symmetric | Relaxation |
| **Triple-well** | 3 | Symmetric | 3-state choice |
| **Periodic** | ∞ | Periodic | Phase/angle |
| **Asymmetric** | 2 | Broken | Preferred state |
| **Mexican hat** | ∞ (circle) | Radial | Phase transition |

---

## 🔬 Potential Design Guidelines

### 1. Stability

**Ensure minima exist:**

```python
# Check: dV/dφ = 0 has solutions
# Check: d²V/dφ² > 0 at minima
```

### 2. Boundedness

**Prevent blow-up:**

```python
# Ensure: V(φ) → ∞ as |φ| → ∞
# For stability
```

### 3. Smoothness

**Avoid discontinuities:**

```python
# Use smooth functions (C¹ or better)
# For numerical stability
```

---

## 🎨 Potential Visualization

```python
def plot_potential(V_func, phi_range=(-2, 2), params=None):
    """Visualize potential landscape."""
    phi = np.linspace(*phi_range, 200)
    
    if params:
        V_vals = V_func(phi, **params)
    else:
        V_vals = V_func(phi)
    
    plt.figure(figsize=(10, 4))
    plt.plot(phi, V_vals, 'b-', lw=2)
    plt.xlabel('φ', fontsize=14)
    plt.ylabel('V(φ)', fontsize=14)
    plt.title('Potential Landscape', fontsize=16, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.axhline(0, color='k', linestyle='--', alpha=0.3)
    
    # Mark minima
    from scipy.optimize import minimize_scalar
    # (find and plot minima)
```

---

## ⚠️ Numerical Considerations

### 1. Timestep Constraints

```
Steep potentials → Small dt required

Rule: dt < 1 / max(|d²V/dφ²|)
```

### 2. Initial Conditions

```
Start near minimum for stability

Or explore basin of attraction
```

### 3. Energy Conservation

```
Check: dΩ/dt ≤ 0 (energy decreases)

If violated: dt too large
```

---

## 🔗 Combination with Other Extensions

### Custom V + Stochastic:
```
∂C/∂t = ... - dV_custom/dC + σξ(t)
```
→ Noise-induced transitions in custom landscape

### Custom V + Memory:
```
∂C/∂t = ... - dV_custom/dC + ∫K(t-t')C(t')dt'
```
→ Path-dependent custom dynamics

### Custom V + Multi-field:
```
Different potentials for different fields:
∂Cᵢ/∂t = ... - dVᵢ/dCᵢ
```
→ Heterogeneous network

---

## 🚀 Implementation Tips

### 1. Potential Library

```python
POTENTIAL_LIBRARY = {
    'double_well': (V_double_well, dV_double_well),
    'single_well': (V_single_well, dV_single_well),
    'triple_well': (V_triple_well, dV_triple_well),
    'periodic': (V_periodic, dV_periodic),
    'asymmetric': (V_asymmetric, dV_asymmetric)
}

# Usage
V_func, dV_func = POTENTIAL_LIBRARY['triple_well']
```

### 2. Automatic Differentiation

```python
# Use autograd for derivatives
import autograd.numpy as np
from autograd import grad

V = lambda phi: (phi**2 - 1)**2 / 4
dV = grad(V)  # Automatic!
```

### 3. Parameter Fitting

```python
from scipy.optimize import curve_fit

def fit_potential(data, potential_func, p0):
    """Fit potential parameters to data."""
    # (fitting code)
    return optimal_params
```

---

## 📈 Expected Behaviors

| Potential Shape | Dynamics |
|-----------------|----------|
| Steep wells | Fast relaxation |
| Shallow wells | Slow dynamics |
| High barriers | Rare transitions |
| No barriers | Free diffusion |

---

*Custom potentials: Your landscape, your rules!*


---


# 🔹 Source: file_1.md

# UET Extensions - Memory & History

## 🧠 Memory/History in UET

**Why Memory Matters:**

Many real systems have **history-dependent behavior**:
- **Materials:** Hysteresis (magnets, shape-memory alloys)
- **Ecology:** Population depends on past dynamics
- **Economics:** Path-dependent markets (lock-in effects)
- **Neural:** Learning, adaptation, memory consolidation
- **Climate:** Ocean heat content affects future dynamics

**Markovian (no memory) models miss this!**

---

## 📐 Mathematical Formulation

### Standard UET (Markovian):
```
∂C/∂t = f(C(t), I(t))
         ↑
    Only depends on CURRENT state
```

### UET with Memory:
```
∂C/∂t = f(C(t), I(t)) + ∫₀ᵗ K(t-t') C(t') dt'
                        ↑
                   Depends on PAST states
```

**Memory Kernel K(τ):**
- `K(τ)`: Memory weight at lag τ
- `τ`: Time lag
- Normalized: ∫₀^∞ K(τ)dτ = finite

---

## 🔧 Memory Kernel Types

### 1. No Memory (Markovian)
```
K(τ) = 0

Result: Standard UET
```

### 2. Exponential Memory
```
K(τ) = (γ/τ_mem) exp(-τ/τ_mem)

Parameters:
- τ_mem: Memory timescale
- γ: Memory strength

Physical meaning: Recent past matters most
```

### 3. Power-Law Memory
```
K(τ) = γ / (1 + τ)^α

Parameters:
- α: Decay exponent
- γ: Strength

Physical meaning: Long-term memory (heavy tail)
```

### 4. Oscillatory Memory
```
K(τ) = γ exp(-τ/τ_mem) cos(ω₀τ)

Parameters:
- ω₀: Oscillation frequency
- τ_mem: Decay time

Physical meaning: Reverberation, echoes
```

---

## 🔧 Implementation Strategy

### Discrete Convolution with History Buffer:

```python
from collections import deque

class UETWithMemory:
    """UET model with memory/history effects."""
    
    def __init__(self, N=32, kappa=0.1, beta=0.5, s=0.0,
                 memory_type='exponential', tau_mem=5.0, 
                 gamma=0.1, dt=0.01):
        self.N = N
        self.kappa = kappa
        self.beta = beta
        self.s = s
        self.memory_type = memory_type
        self.tau_mem = tau_mem
        self.gamma = gamma
        self.dt = dt
        
        # Memory buffer size
        self.buffer_size = int(5 * tau_mem / dt)  # 5x memory time
        
        # History buffers
        self.C_history = deque(maxlen=self.buffer_size)
        self.I_history = deque(maxlen=self.buffer_size)
        
        # Pre-compute memory kernel
        self.K_mem = self._make_memory_kernel()
        
        # Initialize fields
        self.C = np.random.randn(N, N) * 0.1 + 1.0
        self.I = np.random.randn(N, N) * 0.1 - 1.0
        
        # Fill history with initial state
        for _ in range(self.buffer_size):
            self.C_history.append(self.C.copy())
            self.I_history.append(self.I.copy())
    
    def _make_memory_kernel(self):
        """Create discrete memory kernel."""
        # Time lags
        t_lags = np.arange(self.buffer_size) * self.dt
        
        if self.memory_type == 'exponential':
            K = (self.gamma / self.tau_mem) * np.exp(-t_lags / self.tau_mem)
        elif self.memory_type == 'power_law':
            alpha = 2.0
            K = self.gamma / (1 + t_lags)**alpha
        elif self.memory_type == 'oscillatory':
            omega = 2 * np.pi / self.tau_mem  # Oscillation frequency
            K = self.gamma * np.exp(-t_lags / self.tau_mem) * np.cos(omega * t_lags)
        else:  # 'none'
            K = np.zeros(self.buffer_size)
            if self.buffer_size > 0:
                K[0] = 0.0  # No memory
        
        # Normalize
        K = K * self.dt  # Discrete integral approximation
        
        return K
    
    def _memory_integral(self, history):
        """Compute memory integral: ∫K(t-t')·field(t')dt'."""
        if len(history) < self.buffer_size:
            # Not enough history yet
            return np.zeros_like(self.C)
        
        # Convert history to array (oldest to newest)
        history_array = np.array(list(history))
        
        # Convolution (weighted sum over past)
        # K[0] = current, K[-1] = oldest
        K_reversed = self.K_mem[::-1]
        
        memory_term = np.sum([
            K_reversed[i] * history_array[i]
            for i in range(len(history_array))
        ], axis=0)
        
        return memory_term
    
    def step(self):
        """Evolve one timestep with memory."""
        C, I = self.C, self.I
        
        # Compute memory integrals
        C_memory = self._memory_integral(self.C_history)
        I_memory = self._memory_integral(self.I_history)
        
        # Compute derivatives
        dC_dt = (
            self.kappa * laplacian_2d(C) -
            dV_dphi(C) -
            self.beta * (C - I) +
            self.s +
            C_memory  # ← Memory term
        )
        
        dI_dt = (
            self.kappa * laplacian_2d(I) -
            dV_dphi(I) -
            self.beta * (I - C) +
            I_memory  # ← Memory term
        )
        
        # Update
        self.C = C + self.dt * dC_dt
        self.I = I + self.dt * dI_dt
        
        # Store current state in history
        self.C_history.append(self.C.copy())
        self.I_history.append(self.I.copy())
```

---

## 🎯 Use Cases

### 1. Hysteresis (Materials)

**Path-dependent magnetization:**

```python
# Materials: Ferromagnetic hysteresis
model = UETWithMemory(
    memory_type='exponential',
    tau_mem=10.0,  # Relaxation time
    gamma=0.3,     # Hysteresis strength
    beta=0.5
)

# C = Magnetization
# I = Internal field
# Memory → Hysteresis loop

# Result: Different paths give different outcomes
```

**Physical meaning:**
- Memory of past magnetic states
- Remanence (residual magnetization)
- Coercivity (resistance to demagnetization)

---

### 2. Neural Adaptation

**Synaptic plasticity:**

```python
# Neuroscience: Spike-timing-dependent plasticity
model = UETWithMemory(
    memory_type='exponential',
    tau_mem=50.0,   # Adaptation timescale (ms)
    gamma=0.2,      # Plasticity strength
    beta=1.0
)

# C = Neural activity
# I = Adaptation current
# Memory → Learning

# Result: Response changes based on history
```

**Examples:**
- Long-term potentiation (LTP)
- Long-term depression (LTD)
- Habituation, sensitization

---

### 3. Economic Path Dependence

**Market lock-in effects:**

```python
# Economics: Technology lock-in
model = UETWithMemory(
    memory_type='power_law',  # Long-term effects
    tau_mem=100.0,  # Historical inertia
    gamma=0.15,
    beta=0.3
)

# C = Market share
# I = Intrinsic value
# Memory → Lock-in

# Result: QWERTY keyboard, VHS vs Betamax
```

---

### 4. Climate Ocean Memory

**Thermal inertia:**

```python
# Climate: Ocean heat storage
model = UETWithMemory(
    memory_type='exponential',
    tau_mem=1000.0,  # Decades (in timesteps)
    gamma=0.05,
    beta=0.1
)

# C = Atmosphere temperature
# I = Ocean temperature
# Memory → Committed warming

# Result: Delayed response to emissions
```

---

## 📊 Memory Effects

### Effect 1: Hysteresis

**Different paths → Different outcomes:**

```
Path A: C↑ then C↓ → Final state 1
Path B: C↓ then C↑ → Final state 2

State 1 ≠ State 2  (history matters!)
```

### Effect 2: Adaptation

**Response weakens with repeated stimulation:**

```
First stimulus: Large response
Repeated stimuli: Smaller response (adaptation)
```

### Effect 3: Reverberation

**Oscillatory memory → Echoes:**

```
Impulse → Decaying oscillations
(like ringing a bell)
```

---

## ⚠️ Computational Considerations

### 1. Memory Cost

```
Memory buffer: O(N² × buffer_size)

Large τ_mem → Large buffer → More RAM

Solution: Truncate old history
```

### 2. Computational Cost

```
Memory integral: O(N² × buffer_size) per timestep

Solution: Use FFT for long kernels (if applicable)
```

### 3. Numerical Stability

```
Long memory can accumulate errors

Solution:
- Periodic reinitialization
- Error control
- Smaller dt
```

---

## 🎓 Domain Interpretations

### Materials Science:
```
τ_mem = Relaxation time
γ = Hysteresis strength

Typical: τ_mem ~ seconds to hours
```

### Neuroscience:
```
τ_mem = Synaptic time constant
γ = Plasticity rate

Typical: τ_mem ~ 10-1000 ms
```

### Economics:
```
τ_mem = Market memory
γ = Lock-in strength

Typical: τ_mem ~ years to decades
```

---

## 🔗 Combination with Other Extensions

### Memory + Delays:
```
∂C/∂t = ... - β(C(t) - I(t-τ)) + ∫K(t-t')C(t')dt'
```
→ Both feedforward delay AND feedback memory

### Memory + Stochastic:
```
∂C/∂t = ... + ∫K(t-t')C(t')dt' + σξ(t)
```
→ Noisy path-dependent dynamics

### Memory + Nonlocal:
```
∂C/∂t = ... + ∫∫K_time(t-t') K_space(x-x') C(x',t') dx'dt'
```
→ Spatiotemporal memory

---

## 🚀 Implementation Tips

### 1. Choose Buffer Size Wisely

```python
# Rule of thumb: 5x memory timescale
buffer_size = int(5 * tau_mem / dt)

# Too small: Truncated memory
# Too large: Wasted RAM
```

### 2. Efficient Storage

```python
# Use deque for automatic old-value removal
from collections import deque
history = deque(maxlen=buffer_size)
```

### 3. Kernel Visualization

```python
# Always plot your kernel!
plt.plot(t_lags, K_mem)
plt.xlabel('Time lag τ')
plt.ylabel('Memory weight K(τ)')
```

---

## 📈 Expected Behaviors

| Memory Type | Effect | Use Case |
|-------------|--------|----------|
| None | Markovian | Standard dynamics |
| Exponential | Recent bias | Adaptation, relaxation |
| Power-law | Long memory | Lock-in, path dependence |
| Oscillatory | Echoes | Reverberation, waves |

---

*Memory: The past shapes the future!*


---


# 🔹 Source: file_11.md

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


# 🔹 Source: file_14.md

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


# 🔹 Source: file_16.md

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


# 🔹 Source: file_18.md

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


# 🔹 Source: file_2.md

# UET Extensions - Multi-field Networks

## 🔗 Multi-field Networks in UET

**Why More Than 2 Fields?**

Real systems often have **multiple interacting components**:
- **Neural Networks:** Many brain regions, not just 2
- **Ecosystems:** Predator-prey-plant (3+ species)
- **Economics:** Multiple markets, sectors, currencies
- **Social Networks:** Many individuals/groups
- **Gene Networks:** Multiple genes regulating each other

**C and I alone are not enough!**

---

## 📐 Mathematical Formulation

### Standard UET (2 Fields):
```
∂C/∂t = κ∇²C - ∂V/∂C - β(C - I) + s
∂I/∂t = κ∇²I - ∂V/∂I - β(I - C)
```

### Multi-field UET (N Fields):
```
∂Cᵢ/∂t = κᵢ∇²Cᵢ - ∂V/∂Cᵢ - Σⱼ βᵢⱼ(Cᵢ - Cⱼ) + sᵢ

for i = 1, 2, ..., N
```

**Coupling Matrix β:**
- `βᵢⱼ`: Coupling strength from field j to field i
- Can be asymmetric: βᵢⱼ ≠ βⱼᵢ
- Diagonal: βᵢᵢ = 0 (no self-coupling)

---

## 🎯 Network Topologies

### 1. Fully Connected
```
βᵢⱼ = β for all i ≠ j

All fields interact with each other equally
```

### 2. Ring/Chain
```
βᵢⱼ = β if |i-j| = 1, else 0

Linear chain or circular ring
```

### 3. Star Network
```
β₀ⱼ = β for all j ≠ 0
βᵢⱼ = 0 for i,j ≠ 0

One central hub connected to all others
```

### 4. Hierarchical
```
βᵢⱼ = β if i is parent/child of j

Tree-like structure
```

### 5. Random Network
```
βᵢⱼ = β with probability p, else 0

Erdős-Rényi random graph
```

### 6. Scale-Free
```
βᵢⱼ follows power-law degree distribution

Hubs with many connections
```

---

## 🔧 Implementation Strategy

```python
class UETMultiField:
    """UET model with N fields."""
    
    def __init__(self, n_fields=3, N=32, kappa=0.1, 
                 coupling_matrix=None, s=None, dt=0.01):
        self.n_fields = n_fields
        self.N = N
        self.kappa = kappa
        self.dt = dt
        
        # Coupling matrix (n_fields x n_fields)
        if coupling_matrix is None:
            # Default: fully connected with β=0.5
            self.beta = np.ones((n_fields, n_fields)) * 0.5
            np.fill_diagonal(self.beta, 0)  # No self-coupling
        else:
            self.beta = coupling_matrix
        
        # External drives
        if s is None:
            self.s = np.zeros(n_fields)
        else:
            self.s = s
        
        # Initialize fields
        self.fields = [
            np.random.randn(N, N) * 0.1 + (1 if i % 2 == 0 else -1)
            for i in range(n_fields)
        ]
    
    def step(self):
        """Evolve all fields one timestep."""
        # Compute derivatives for all fields
        derivatives = []
        
        for i in range(self.n_fields):
            C_i = self.fields[i]
            
            # Diffusion
            diff_term = self.kappa * laplacian_2d(C_i)
            
            # Potential
            pot_term = -dV_dphi(C_i)
            
            # Coupling with other fields
            coupling_term = np.zeros_like(C_i)
            for j in range(self.n_fields):
                if i != j:
                    coupling_term -= self.beta[i, j] * (C_i - self.fields[j])
            
            # External drive
            drive_term = self.s[i]
            
            # Total
            dC_dt = diff_term + pot_term + coupling_term + drive_term
            derivatives.append(dC_dt)
        
        # Update all fields
        for i in range(self.n_fields):
            self.fields[i] = self.fields[i] + self.dt * derivatives[i]
    
    def get_mean_values(self):
        """Get spatial mean of all fields."""
        return [np.mean(f) for f in self.fields]
```

---

## 🎯 Use Cases

### 1. Ecological Food Web

**3 species: Plant, Herbivore, Predator**

```python
# Ecology: Food chain
model = UETMultiField(
    n_fields=3,
    coupling_matrix=np.array([
        [0,    0.2,  0],     # Plant eaten by herbivore
        [-0.3, 0,    0.4],   # Herbivore eats plant, eaten by predator
        [0,   -0.5,  0]      # Predator eats herbivore
    ])
)

# fields[0] = Plant density
# fields[1] = Herbivore density
# fields[2] = Predator density

# Result: Lotka-Volterra 3-species dynamics
```

**Asymmetric couplings:**
- Plant ← Herbivore (negative, plant eaten)
- Herbivore ← Plant (positive, food)
- Herbivore ← Predator (negative, eaten)
- Predator ← Herbivore (positive, food)

---

### 2. Brain Network

**Multiple brain regions:**

```python
# Neuroscience: Default mode network (DMN)
n_regions = 5  # PCC, mPFC, IPL, etc.

# Connectivity matrix from neuroimaging
beta_matrix = np.array([
    [0,   0.8, 0.5, 0.3, 0.2],
    [0.8, 0,   0.6, 0.4, 0.3],
    [0.5, 0.6, 0,   0.7, 0.4],
    [0.3, 0.4, 0.7, 0,   0.6],
    [0.2, 0.3, 0.4, 0.6, 0]
])

model = UETMultiField(
    n_fields=n_regions,
    coupling_matrix=beta_matrix
)

# Result: Synchronized network activity
```

---

### 3. Multi-Currency Market

**Exchange rate dynamics:**

```python
# Economics: USD, EUR, JPY, GBP
n_currencies = 4

# Trade network (symmetric)
beta_matrix = np.array([
    [0,   0.5, 0.3, 0.4],  # USD
    [0.5, 0,   0.4, 0.6],  # EUR
    [0.3, 0.4, 0,   0.2],  # JPY
    [0.4, 0.6, 0.2, 0]     # GBP
])

model = UETMultiField(
    n_fields=n_currencies,
    coupling_matrix=beta_matrix
)

# Result: Exchange rate fluctuations, arbitrage
```

---

### 4. Gene Regulatory Network

**Multiple genes:**

```python
# Biology: Gene regulation
n_genes = 6

# Regulation matrix (can be asymmetric)
# Positive = activation, Negative = repression
beta_matrix = np.array([
    [ 0,   0.5, -0.3,  0,    0,    0],   # Gene 1
    [-0.4, 0,    0.6,  0,    0,    0],   # Gene 2
    [ 0.3, 0,    0,   -0.5,  0,    0],   # Gene 3
    [ 0,   0,    0.4,  0,    0.7,  0],   # Gene 4
    [ 0,   0,    0,    0,    0,   -0.6], # Gene 5
    [ 0,   0,    0,    0,    0.5,  0]    # Gene 6
])

model = UETMultiField(
    n_fields=n_genes,
    coupling_matrix=beta_matrix
)

# Result: Gene expression oscillations, switches
```

---

## 📊 Network Analysis

### 1. Synchronization

**How synchronized are the fields?**

```python
def synchronization_index(fields):
    """Measure of synchronization (0=none, 1=perfect)."""
    n_fields = len(fields)
    pairwise_corr = []
    
    for i in range(n_fields):
        for j in range(i+1, n_fields):
            corr = np.corrcoef(fields[i].flatten(), fields[j].flatten())[0, 1]
            pairwise_corr.append(abs(corr))
    
    return np.mean(pairwise_corr)
```

### 2. Hub Detection

**Which fields are most connected?**

```python
def find_hubs(coupling_matrix):
    """Find highly connected fields."""
    degree = np.sum(np.abs(coupling_matrix), axis=1)
    hub_threshold = np.mean(degree) + np.std(degree)
    hubs = np.where(degree > hub_threshold)[0]
    return hubs
```

### 3. Community Detection

**Which fields form groups?**

```python
def detect_communities(coupling_matrix):
    """Simple community detection via spectral clustering."""
    from sklearn.cluster import SpectralClustering
    
    # Convert to similarity matrix
    similarity = np.abs(coupling_matrix)
    
    # Cluster
    clustering = SpectralClustering(n_clusters=2, affinity='precomputed')
    labels = clustering.fit_predict(similarity)
    
    return labels
```

---

## 🔬 Emergent Behaviors

### 1. Consensus

**All fields converge to same value:**

```
Strong coupling → All Cᵢ → C*
```

### 2. Clustering

**Fields form groups:**

```
Weak long-range coupling → Clusters
```

### 3. Waves

**Traveling patterns across network:**

```
Ring topology + delays → Traveling waves
```

### 4. Chimera States

**Coexistence of sync and async:**

```
Some fields synchronized, others not
```

---

## ⚠️ Computational Considerations

### 1. Scaling

```
2 fields: O(N²) per timestep
N fields: O(N² × n_fields²) per timestep

Large networks → Expensive!
```

### 2. Memory

```
Memory: n_fields × N² × sizeof(float)

Example: 100 fields, 64×64 grid
→ 100 × 4096 × 4 bytes ≈ 1.6 MB
```

### 3. Sparse Networks

**For large, sparse networks:**

```python
# Use sparse matrix for coupling
from scipy.sparse import csr_matrix

beta_sparse = csr_matrix(beta_matrix)

# Coupling computation
for i in range(n_fields):
    coupling = beta_sparse[i].dot(field_vector)
```

---

## 🎓 Domain Interpretations

### Neuroscience:
```
n_fields = Brain regions (10-100)
βᵢⱼ = Structural/functional connectivity

Typical: n_fields ~ 10-100
```

### Ecology:
```
n_fields = Species (3-20)
βᵢⱼ = Interaction matrix (predation, competition)

Typical: n_fields ~ 3-20
```

### Economics:
```
n_fields = Markets/sectors (5-50)
βᵢⱼ = Trade/correlation matrix

Typical: n_fields ~ 5-50
```

---

## 🔗 Combination with Other Extensions

### Multi-field + Delays:
```
∂Cᵢ/∂t = ... - Σⱼ βᵢⱼ(Cᵢ(t) - Cⱼ(t-τᵢⱼ))
```
→ Network with heterogeneous delays

### Multi-field + Nonlocal:
```
∂Cᵢ/∂t = ... - Σⱼ βᵢⱼ∫K(x-x')Cⱼ(x')dx'
```
→ Spatially extended network

### Multi-field + Stochastic:
```
∂Cᵢ/∂t = ... - Σⱼ βᵢⱼ(Cᵢ - Cⱼ) + σᵢξᵢ(t)
```
→ Noisy network dynamics

---

## 🚀 Implementation Tips

### 1. Coupling Matrix Design

```python
def make_coupling_matrix(n_fields, topology='fully_connected', strength=0.5):
    """Factory for coupling matrices."""
    beta = np.zeros((n_fields, n_fields))
    
    if topology == 'fully_connected':
        beta = np.ones((n_fields, n_fields)) * strength
        np.fill_diagonal(beta, 0)
    
    elif topology == 'ring':
        for i in range(n_fields):
            beta[i, (i+1) % n_fields] = strength
            beta[i, (i-1) % n_fields] = strength
    
    elif topology == 'star':
        beta[0, :] = strength
        beta[:, 0] = strength
        np.fill_diagonal(beta, 0)
    
    elif topology == 'random':
        prob = 0.3  # Connection probability
        beta = (np.random.rand(n_fields, n_fields) < prob) * strength
        np.fill_diagonal(beta, 0)
    
    return beta
```

### 2. Efficient Update

```python
# Vectorize field updates
fields_array = np.array(self.fields)  # Shape: (n_fields, N, N)

# Coupling term (vectorized)
coupling = np.einsum('ij,jkl->ikl', 
                     -self.beta, 
                     fields_array - fields_array[:, None])
```

### 3. Visualization

```python
def visualize_network(coupling_matrix):
    """Visualize network structure."""
    import networkx as nx
    
    # Create graph
    G = nx.from_numpy_array(coupling_matrix)
    
    # Draw
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, 
            node_color='lightblue', 
            node_size=500,
            font_size=10,
            width=[abs(coupling_matrix[u,v])*5 for u,v in G.edges()])
```

---

## 📈 Expected Behaviors

| Topology | Synchronization | Waves | Clusters |
|----------|-----------------|-------|----------|
| Fully connected | High | No | No |
| Ring | Medium | Yes | No |
| Star | High (hub) | No | Hub+spokes |
| Random | Medium | Maybe | Yes |
| Hierarchical | Layered | No | Yes |

---

*Multi-field: From pairs to networks!*


---


# 🔹 Source: file_22.md

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


# 🔹 Source: file_23.md

R0-E23: Action router reads metric_triage + monotonic/determinism reports and emits action_plan.*; can enforce hold_apply.


---


# 🔹 Source: file_24.md

R0-E24: Targeted evidence executor: if action_plan requests INCREASE_EVIDENCE, expand seeds for those groups via resample_blocked_groups + rerun dt ladder, then re-check monotonic.


---


# 🔹 Source: file_25.md

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


# 🔹 Source: file_27.md

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


# 🔹 Source: file_28.md

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


# 🔹 Source: file_29.md

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


# 🔹 Source: file_3.md

# UET Extensions - Nonlocal Coupling

## 🌐 Nonlocal Coupling in UET

**Why Nonlocal Matters:**

Many real systems have **long-range interactions**:
- **Social Networks:** Influence spreads beyond neighbors (viral trends, information cascades)
- **Brain:** Long-range connections between distant regions
- **Economics:** Global markets affect local prices
- **Ecology:** Migration connects distant populations

**Local diffusion (∇²) is not enough!**

---

## 📐 Mathematical Formulation

### Standard UET (Local Coupling):
```
∂C/∂t = κ∇²C - ∂V/∂C - β(C(x) - I(x)) + s
                              ↑
                        Same location only
```

### UET with Nonlocal Coupling:
```
∂C/∂t = κ∇²C - ∂V/∂C - β∫K(x-x') I(x') dx' + s
                              ↑
                    Weighted average over ALL x'
```

**Kernel K(r):**
- `K(r)`: Coupling strength at distance r
- Normalized: ∫K(r)dr = 1

---

## 🔧 Kernel Functions

### 1. Local (Dirac Delta)
```
K(r) = δ(r)

Result: Standard UET (no nonlocal)
```

### 2. Gaussian Kernel
```
K(r) = (1/√(2πσ²)) exp(-r²/2σ²)

Parameters:
- σ: Interaction range
- r: Distance

Physical meaning: Smooth decay with distance
```

### 3. Exponential Kernel
```
K(r) = (1/2λ) exp(-|r|/λ)

Parameters:
- λ: Characteristic length scale

Physical meaning: Slower decay than Gaussian
```

### 4. Power-Law Kernel
```
K(r) = C / (1 + r)^α

Parameters:
- α: Decay exponent (α>dim for normalization)

Physical meaning: Long-range interactions (heavy tail)
```

### 5. Top-Hat Kernel
```
K(r) = {  1/(πR²)  if r < R
       {  0         if r ≥ R

Parameters:
- R: Interaction radius

Physical meaning: All-or-nothing (neighbors within R)
```

---

## 🔧 Implementation Strategy

### Discrete Convolution:

```python
class UETWithNonlocal:
    """UET model with nonlocal coupling."""
    
    def __init__(self, N=32, kappa=0.1, beta=0.5, s=0.0,
                 kernel_type='gaussian', kernel_sigma=2.0):
        self.N = N
        self.kappa = kappa
        self.beta = beta
        self.s = s
        self.kernel_type = kernel_type
        self.kernel_sigma = kernel_sigma
        
        # Pre-compute coupling kernel
        self.K = self._make_kernel()
        
        # Initialize fields
        self.C = np.random.randn(N, N) * 0.1 + 1.0
        self.I = np.random.randn(N, N) * 0.1 - 1.0
    
    def _make_kernel(self):
        """Create 2D coupling kernel."""
        N = self.N
        sigma = self.kernel_sigma
        
        # Distance from center
        x = np.arange(N) - N//2
        y = np.arange(N) - N//2
        X, Y = np.meshgrid(x, y)
        R = np.sqrt(X**2 + Y**2)
        
        if self.kernel_type == 'gaussian':
            K = np.exp(-R**2 / (2 * sigma**2))
        elif self.kernel_type == 'exponential':
            K = np.exp(-R / sigma)
        elif self.kernel_type == 'power_law':
            alpha = 3.0
            K = 1.0 / (1 + R)**alpha
        elif self.kernel_type == 'tophat':
            K = (R < sigma).astype(float)
        else:
            # Default: local (delta function approximation)
            K = np.zeros((N, N))
            K[N//2, N//2] = 1.0
        
        # Normalize
        K = K / np.sum(K)
        
        return K
    
    def _nonlocal_coupling(self, field):
        """Compute nonlocal coupling: ∫K(x-x')·field(x')dx'."""
        from scipy.signal import fftconvolve
        
        # Use FFT convolution for efficiency
        result = fftconvolve(field, self.K, mode='same')
        
        return result
    
    def step(self):
        """Evolve one timestep with nonlocal coupling."""
        C, I = self.C, self.I
        dt = 0.01
        
        # Nonlocal coupling term
        I_nonlocal = self._nonlocal_coupling(I)
        C_nonlocal = self._nonlocal_coupling(C)
        
        # Compute derivatives
        dC_dt = (
            self.kappa * laplacian_2d(C) -
            dV_dphi(C) -
            self.beta * (C - I_nonlocal) +  # ← Nonlocal I
            self.s
        )
        
        dI_dt = (
            self.kappa * laplacian_2d(I) -
            dV_dphi(I) -
            self.beta * (I - C_nonlocal)  # ← Nonlocal C
        )
        
        # Update
        self.C = C + dt * dC_dt
        self.I = I + dt * dI_dt
```

---

## 🎯 Use Cases

### 1. Social Network Influence

**Opinion spreads through network:**

```python
# Social media: Viral spread
model = UETWithNonlocal(
    kernel_type='power_law',  # Long-range influence
    kernel_sigma=5.0,         # Reach
    beta=0.8
)

# C = Public opinion
# I = Private belief
# K(r) = Social network structure

# Result: Viral cascades, echo chambers
```

**Physical meaning:**
- Power-law: "Hubs" have wide influence
- β: Peer pressure strength
- Result: Opinion polarization, viral spreading

---

### 2. Neural Long-Range Connections

**Brain regions communicate across distance:**

```python
# Brain: Cortical networks
model = UETWithNonlocal(
    kernel_type='exponential',  # Long-range connections
    kernel_sigma=10.0,          # Axon reach
    beta=0.5
)

# C = Local excitation
# I = Distal inhibition
# K(r) = White matter connectivity

# Result: Synchronized activity, large-scale patterns
```

**Examples:**
- Default mode network
- Attention networks
- Memory consolidation

---

### 3. Global Economic Markets

**Local prices affected by global markets:**

```python
# Economics: Global trade
model = UETWithNonlocal(
    kernel_type='gaussian',  # Smooth global influence
    kernel_sigma=20.0,       # Trade network reach
    beta=0.3
)

# C = Local price
# I = Global price index
# K(r) = Trade network strength

# Result: Price synchronization, global shocks
```

---

### 4. Ecological Migration

**Species migrate between patches:**

```python
# Ecology: Meta-population
model = UETWithNonlocal(
    kernel_type='tophat',   # Migration radius
    kernel_sigma=5.0,       # Dispersal distance
    beta=0.2
)

# C = Prey density
# I = Predator density
# K(r) = Migration kernel

# Result: Spatial coexistence, traveling waves
```

---

## 📊 Kernel Comparison

| Kernel | Shape | Range | Use Case |
|--------|-------|-------|----------|
| **Delta** | Spike at r=0 | Local only | Standard UET |
| **Gaussian** | Bell curve | Medium | Neural, diffusion |
| **Exponential** | Smooth decay | Long | Physical interactions |
| **Power-law** | Heavy tail | Very long | Social networks |
| **Top-hat** | Flat then zero | Fixed radius | Migration, neighborhoods |

---

## 🔬 Effects of Nonlocal Coupling

### Effect 1: Pattern Formation

**Nonlocal → New patterns!**

```
Local coupling: Turing patterns (stripes, spots)
Nonlocal coupling: Complex patterns (labyrinths, hexagons)
```

### Effect 2: Synchronization

**Long-range → Sync distant regions:**

```
Local: Only neighbors sync
Nonlocal: Global synchronization possible
```

### Effect 3: Traveling Waves

**Nonlocal enables wave propagation:**

```
Wave speed depends on K(r) shape
Power-law K → Super-diffusion (fast waves)
```

---

## ⚠️ Computational Considerations

### 1. Complexity

```
Local coupling: O(N²) per timestep
Nonlocal (naive): O(N⁴) per timestep  ← Expensive!
Nonlocal (FFT): O(N² log N)  ← Much better!
```

**Use FFT convolution for efficiency!**

### 2. Boundary Conditions

```python
# Periodic boundaries (FFT default)
from scipy.signal import fftconvolve
result = fftconvolve(field, K, mode='same')

# Or: scipy.ndimage.convolve for other boundary conditions
from scipy.ndimage import convolve
result = convolve(field, K, mode='wrap')  # periodic
```

### 3. Kernel Size

```
Small kernel (σ ~ 1-2): Fast, local-like
Medium kernel (σ ~ 5-10): Balanced
Large kernel (σ > N/4): Slow, truly nonlocal
```

---

## 🎓 Domain Interpretations

### Neural:
```
K(r) = White matter connectivity matrix
σ = Axon length scale

Typical: σ ≈ 5-20 grid points
```

### Social Networks:
```
K(r) = Friendship/follower network
α = Network degree distribution exponent

Typical: α ≈ 2-3 (scale-free networks)
```

### Economics:
```
K(r) = Trade/information network
σ = Market integration scale

Typical: σ ≈ global (all markets connected)
```

---

## 🔗 Combination with Other Extensions

### Nonlocal + Delays:
```
∂C/∂t = ... - β∫K(x-x') I(x',t-τ) dx'
```
→ Delayed nonlocal coupling (realistic neural)

### Nonlocal + Stochastic:
```
∂C/∂t = ... - β∫K(x-x') I(x') dx' + σξ(t)
```
→ Noisy long-range interactions

### Nonlocal + Multi-field:
```
∂Cᵢ/∂t = ... - Σⱼ∫Kᵢⱼ(x-x') Cⱼ(x') dx'
```
→ Network of nonlocal fields

---

## 🚀 Implementation Tips

### 1. Kernel Design

```python
def make_kernel_2d(N, kernel_type, params):
    """Factory for 2D kernels."""
    # ... (see implementation above)
    return K
```

### 2. Efficient Convolution

```python
# Use scipy for FFT convolution
from scipy.signal import fftconvolve

def convolve_2d(field, kernel):
    return fftconvolve(field, kernel, mode='same')
```

### 3. Kernel Visualization

```python
# Always plot your kernel!
plt.imshow(K, cmap='hot')
plt.colorbar()
plt.title('Coupling Kernel K(r)')
```

---

## 📈 Expected Behaviors

| Kernel Range (σ) | Pattern | Sync |
|------------------|---------|------|
| Small (σ<2) | Local Turing | None |
| Medium (σ~5) | Complex patterns | Regional |
| Large (σ>10) | Global modes | Global |

---

*Nonlocal coupling: Think globally, act locally!*


---


# 🔹 Source: file_30.md

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


# 🔹 Source: file_31.md

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


# 🔹 Source: file_32.md

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


# 🔹 Source: file_33.md

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


# 🔹 Source: file_34.md

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


# 🔹 Source: file_35.md

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


# 🔹 Source: file_4.md

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


# 🔹 Source: file_5.md

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


# 🔹 Source: file_6.md

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


# 🔹 Source: file_8.md

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


# 🔹 Source: file_9.md

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
