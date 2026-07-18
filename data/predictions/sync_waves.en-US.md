# Sync Waves — Collective Modes of the W-field Correlation Structure

## Definitions

### Sync Field ≠ Quantum Field

The sync field $A(r) = \varepsilon(r/\xi)^\beta$ is **not** an independent quantum field separate from the W-field. It is the W-field's **non-local two-point correlation function**:

$$A(r) \equiv \langle W(x) W^\dagger(x+r) \rangle_{\text{render}}$$

It describes the correlation strength of the W-field rendering across spatial scale $r$. It is not a dynamical field that can be independently quantised — it is the large-scale collective structure of the W-field itself.

### Sync Waves ≠ Particles

Sync waves are the time-evolution modes of the W-field correlation structure $A(r)$. They **do not correspond to any particle** — no spin, no mass, cannot be created or annihilated.

Physical analogy:

| System | Collective Mode | Particle | Sync wave analogy |
|:-------|:---------------|:---------|:------------------|
| Crystal lattice | Phonon | Atom | W-field particles (radial/phase) |
| Electron gas | Plasmon | Electron | W-field particles |
| **W-field correlation** | **Sync wave** | — | Perturbation of W-field correlation |

### Sync Waves vs W-field Waves

| Property | W-field Waves | Sync Waves |
|:---------|:--------------|:-----------|
| Object | W-field field $\phi, \eta$ | Correlation function $A(r)$ |
| Quantisable | ✅ Yes → particles | ❌ No → collective mode |
| Mass | $m_\phi \approx 174$ GeV | None |
| Wave speed | $c$ | $c$ |
| Physical counterpart | Top quark, Higgs, photon | BAO correlation evolution |

---

## Part One: Mathematical Structure of the Sync Field

### 1.1 Definition

The sync field $A(r)$ is the non-local rendering correlation function of the W-field:

$$A(r) = \varepsilon \left(\frac{r}{\xi}\right)^\beta$$

where:
- $\varepsilon = \varphi^{-1}/4 \approx 0.1545$ (injection strength)
- $\beta = \varphi^{-1}/2 \approx 0.3090$ (power-law index)
- $\xi = 105$ Mpc (sync correlation length)

### 1.2 Laplace Operator

In spherical coordinates:

$$\nabla^2 A = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial A}{\partial r}\right)$$

$$\frac{\partial A}{\partial r} = \frac{\beta A}{r}$$

$$\nabla^2 A = \frac{\beta(\beta+1)A}{r^2}$$

where $\beta(\beta+1) = 0.4045...$.

---

## Part Two: Wave Equation

### 2.1 Static Equation

The sync field $A(r)$ satisfies the static equation:

$$\nabla^2 A - \frac{\beta(\beta+1)}{r^2} A = 0$$

This is an Euler-Cauchy equation with solutions $A(r) \propto r^\beta$ (regular) and $A(r) \propto r^{-\beta-1}$ (singular).

### 2.2 Perturbation Equation

Introducing a time-dependent perturbation $\delta A(r,t)$:

$$A(r,t) = \varepsilon\left(\frac{r}{\xi}\right)^\beta + \delta A(r,t)$$

The perturbation satisfies the wave equation:

$$\frac{\partial^2 \delta A}{\partial t^2} - c^2 \nabla^2 \delta A + \frac{c^2 \beta(\beta+1)}{r^2} \delta A = 0$$

where $c$ is the speed of light, derived by IDCM:

$$c = \frac{16}{(\varphi^{-1})^2} \cdot H_0 \cdot \xi$$

### 2.3 Separation of Variables

Let $\delta A(r,t) = R(r) T(t)$, substituting into the wave equation:

$$\frac{T''}{T} = c^2 \left[ \frac{R''}{R} + \frac{2R'}{rR} - \frac{\beta(\beta+1)}{r^2} \right] = -\omega^2$$

Time part:

$$T(t) = e^{\pm i\omega t}$$

Spatial part (spherical Bessel equation):

$$R'' + \frac{2}{r} R' + \left[ \frac{\omega^2}{c^2} - \frac{\beta(\beta+1)}{r^2} \right] R = 0$$

Let $k = \omega/c$ and $\nu = \beta + 1/2$, then:

$$R(r) = j_\nu(kr)$$

where $j_\nu$ is the $\nu$-th order spherical Bessel function.

---

## Part Three: Dispersion Relation and Mode Spectrum

### 3.1 Dispersion Relation

Sync waves are massless waves:

$$\omega^2 = k^2 c^2$$

The wave speed $c$ is the same as for W-field waves.

### 3.2 Fundamental Mode

The lowest mode is determined by the first zero of the spherical Bessel function:

$$j_\nu(k_1\xi) = 0, \quad k_1 = \frac{j_{\nu,1}}{\xi}$$

where $j_{\nu,1} \approx 2.751$ is the first zero of the $\nu = 0.809$ spherical Bessel function.

### 3.3 Characteristic Scales

| Quantity | Value | Interpretation |
|:---------|:-----:|:--------------|
| $\nu = \beta + 1/2$ | 0.809 | Spherical Bessel order |
| $j_{\nu,1}$ | 2.751 | First zero |
| $k_1 = j_{\nu,1}/\xi$ | 0.0262 Mpc$^{-1}$ | Fundamental wavenumber |
| $\lambda_1 = 2\pi/k_1$ | 240 Mpc | Fundamental wavelength |
| $T_1 = 2\pi\xi/(c \cdot j_{\nu,1})$ | 782 Myr | Oscillation period |
| $T_1 / H_0^{-1}$ | 0.055 | Fraction of Hubble time |

---

## Part Four: Cross-Validation with BAO

### 4.1 BAO Scale

The standard BAO sound horizon $r_s \approx 147$ Mpc projected to $z=0$:

$$r_s^{\text{proj}} = \frac{r_s}{1+z_{\text{rec}}} \cdot D(z_{\text{rec}}) \approx 105 \text{ Mpc}$$

This matches the sync field correlation length $\xi = 105$ Mpc.

### 4.2 Relation Between Sync Waves and BAO

Sync waves are **not** the BAO. The BAO is the acoustic oscillation of the baryon-photon fluid at recombination, while sync waves are W-field rendering correlation modes. Their relationship:

| Property | BAO | Sync Waves |
|:---------|:----|:-----------|
| Medium | Baryon-photon plasma | W-field rendering |
| Scale | $r_s \approx 147$ Mpc | $\xi = 105$ Mpc |
| Wave speed | $c_s \approx c/\sqrt{3}$ | $c$ |
| Origin | Recombination epoch | Recursion $C_{n+1}=1/(1+C_n)$ |

The BAO imprints on the sync field background, and both couple at the scale $\xi$.

### 4.3 Verification Summary

| Test | Prediction | Observation | Status |
|:-----|:-----------|:------------|:------:|
| $\xi = 105$ Mpc | Sync correlation length | BAO peak | ✅ Consistent |
| $A(r) \propto r^\beta$ | Power-law $\beta = 0.309$ | Not matter correlation | ✅ Independent |
| $c$ wave speed | Same as W-field waves | Causal structure | ✅ Self-consistent |

---

## Part Five: Conclusion

1. **Sync waves exist**: Perturbations of the sync field $A(r) = \varepsilon(r/\xi)^\beta$ satisfy a wave equation, propagating at the speed of light $c$
2. **Characteristic timescale**: Fundamental oscillation period $T \approx 782$ Myr, about 5.5% of the Hubble time
3. **Characteristic spatial scale**: Fundamental wavelength $\lambda \approx 240$ Mpc
4. **BAO consistency**: Sync field correlation length $\xi = 105$ Mpc matches the projected BAO scale
5. **Not matter correlation**: The sync field is a deeper rendering correlation, distinct from the baryon matter correlation function

---

## References

1. IDCM (2026). Nonlocal Anchor Model. `nonlocal_anchor_model.en-US.md`.
2. DESI Collaboration (2025). DESI DR2 BAO. *arXiv:2503.14745*.
3. Eisenstein, D.J. et al. (2005). Detection of the BAO peak in the SDSS. *ApJ*, 633, 560.
4. IDCM (2026). W-field Waves.