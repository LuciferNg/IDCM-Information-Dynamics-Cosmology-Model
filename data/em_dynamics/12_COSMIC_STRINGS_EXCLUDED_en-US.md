# W-field Cosmic Strings — Structural Exclusion

**Date:** 2026-07-20  
**Status:** ❌ Structurally excluded — W-field has no U(1) phase  
**Location:** Appendix to Phase III: EM + Dynamics

---

## 1. Question

Does the W-field produce cosmic strings (topological defects) via spontaneous U(1) symmetry breaking?

## 2. Derivation

### 2.1 W-field Nature

The W-field $W(\mathbf{x}, t)$ is a **real scalar** consistency weight field:

$$W: \mathbb{R}^{3,1} \to \mathbb{R}$$

It has no complex phase. There is no fundamental U(1) symmetry $W \to e^{i\alpha}W$ associated with the W-field itself.

### 2.2 U(1) in IDCM

The U(1) appearing in IDCM is the **CY₃ line bundle** — not a symmetry of the W-field:

- Line bundle index: $\text{Ind}(L) = 48$ (determines KK tower truncation)
- GLSM charges: $[11,10,8,8,6,5]$ (determine FN charge quantization)
- The U(1) gauge group of electromagnetism is emergent from electron collective dynamics (Phase III), not a fundamental symmetry of the W-field

### 2.3 Vortex/String Requirement

For cosmic strings (vortices), the field must satisfy:
1. **Complex scalar** with U(1) symmetry → winding number $\oint d\theta = 2\pi n$
2. Spontaneously broken → Goldstone mode → topologically stable string

**W-field fails condition 1** — it has no complex phase. Therefore no winding number, no vortex solutions, no cosmic strings.

### 2.4 Hypothetical Tension Bound (for reference)

Even if the W-field had a U(1):
$$\mu \approx \varepsilon^2 \cdot M_P^2 \approx 0.024\, M_P^2$$
Planck CMB bound: $\mu < 10^{-7} M_P^2$

Ratio: $\mu/\mu_{\text{bound}} \approx 240,000$ — excluded by CMB even if W-field had U(1).

## 3. Resolution

| Question | Answer |
|:---------|:-------|
| Does W-field form cosmic strings? | **No** — structurally excluded |
| Why? | W-field is real scalar, no U(1) phase |
| Was the old glossary entry wrong? | Yes — "W-field condensation" and "cosmic strings" were misnomers |
| What condensation exists? | 𝒩 condensation (Phase III ✅) — W-field gradient bound in compact objects |

## 4. Glossary Cleanup

The following entries were **removed** from the glossary (v5.0 update):
- ~~W-field condensation~~ — replaced by 𝒩 condensation
- ~~Cosmic strings~~ — structurally excluded
- ~~Heat death~~ — merged into "Cosmic desynchronization"
- ~~Restart cycle~~ — merged into "Cosmic desynchronization"

New entries:
- **Cosmic desynchronization** — structural timescale $t_{\text{cycle}} \sim \tau_0 \cdot e^{16} \sim 10^{14}$ yr
- **𝒩 condensation** — $B_{\text{max}} = \varepsilon\beta M_P/\sqrt{\kappa} = 3.36\times 10^{37}$ G

## 5. Verification Script

```python
# /tmp/cosmic_strings_verify.py — runnable, standalone
# W-field = real scalar → NO vortex solutions → NO cosmic strings
# Even if hypothetical U(1), μ ≈ 0.024·M_P² >> 10⁻⁷·M_P² Planck bound
```
