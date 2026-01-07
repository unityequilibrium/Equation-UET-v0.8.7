# After: UET Phase Transition: Spinodal Decomposition

## 1. Problem Definition: Spontaneous Unmixing
Why do mixtures distinct phases (e.g., Oil and Water, Alloys)?
- **Spinodal Region**: The region where $\frac{\partial^2 G}{\partial c^2} < 0$. The mixture is intrinsically unstable.
- **Cahn-Hilliard Equation**: Describes the time evolution of concentration $c$.

## 2. UET Solution: Information Sorting
UET derives the Cahn-Hilliard dynamics from the Master Equation:
- **Free Energy**: The Information Potential $V(C)$ has a "double well" shape.
- **Gradient Energy**: The term $\kappa |\nabla C|^2$ represents the energy cost of the interface (Information Friction).
- **Dynamics**: The system evolves to minimize total information, creating domains that coarsen over time ($L \sim t^{1/3}$).

## 3. Results Analysis

### Phase Separation Kinetics
![Phase Separation Viz](../../../Result/phase_separation/phase_separation_viz.png)
*Fig 1: Domain Growth. UET (Blue) accurately predicts the coarsening of domains, significantly outperforming Fick's Law (Dashed), which incorrectly predicts mixing.*

## 4. Conclusion
Phase separation is the sorting of information bits into ordered domains. UET naturally works for non-equilibrium thermodynamics.
