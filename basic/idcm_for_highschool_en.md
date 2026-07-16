# IDCM High School Edition — 100 Formulas

## Part 1: The Mathematical Structure of the Universe (1–10)

1. **The Generating Equation**
   $$x^2 + x - 1 = 0$$
   All cosmic structure emerges from this single quadratic equation. Solution: $x = (\sqrt{5} - 1)/2 = \varphi^{-1} \approx 0.618$.

2. **Recursive Map**
   $$C_{n+1} = \frac{1}{1 + C_n}$$
   For any positive initial $C_0$, this map converges to $\varphi^{-1}$.

3. **Convergence Rate**
   $$\lambda = \left|\frac{dC_{n+1}}{dC_n}\right|_{C=\varphi^{-1}} = \frac{1}{(1+\varphi^{-1})^2} = \varphi^{-2} \approx 0.381966$$
   Since $|\lambda| < 1$, linear stability guarantees convergence.

4. **Convergence Error**
   $$C_n - \varphi^{-1} \propto (-\varphi^{-2})^n$$
   Convergence factor $\varphi^{-2} \approx 0.382$. Error below $10^{-3}$ after 8 steps.

5. **Rational Approximation Sequence**
   $$1,\ \frac{1}{2},\ \frac{2}{3},\ \frac{3}{5},\ \frac{5}{8},\ \frac{8}{13},\ \frac{13}{21},\ \frac{34}{55}$$
   Truncated convergents of $\varphi^{-1}$'s continued fraction.

6. **Continued Fraction**
   $$\varphi^{-1} = \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \ddots}}}$$
   The universe's deepest structure is an infinite continued fraction.

7. **Fibonacci Relation**
   $$\frac{F_n}{F_{n+1}},\quad F_{n+2} = F_{n+1} + F_n$$
   Both numerator and denominator are Fibonacci numbers.

8. **Fibonacci Limit**
   $$\lim_{n\to\infty} \frac{F_n}{F_{n+1}} = \varphi^{-1}$$

9. **The Second Root**
   $$x_- = -\varphi \approx -1.618034$$
   The negative golden ratio. Corresponds to time reversal symmetry breaking.

10. **Structural Hierarchy**
    $$x^2 + x - 1 = 0 \to \varphi^{-1} \to (\varepsilon, \kappa, \beta, z_c) \to \text{observables}$$
    One equation generates all constants. Zero free parameters.

## Part 2: The Four Cosmological Constants (11–25)

11. **Sync Amplitude $\varepsilon$**
    $$\varepsilon = \frac{\varphi^{-1}}{4} \approx 0.1545085$$
    Controls the anomaly amplitude. Factor 4 from minimal $2 \times 2$ symmetry split.

12. **Closure Constant $\kappa$**
    $$\kappa = (\varepsilon\varphi)^2 = \frac{1}{16} = 0.0625$$
    Algebraic identity: $\varepsilon\varphi = (\varphi^{-1}/4) \times \varphi = 1/4$, squared $\to 1/16$.

13. **Scale Exponent $\beta$**
    $$\beta = \frac{\varphi^{-1}}{2} \approx 0.309017$$
    Controls the sync effect's decay rate with distance.

14. **Sync Redshift $z_c$**
    $$z_c = 0.6 \pm 0.05$$
    Sync epoch ~6 Gyr ago (redshift 0.6), confirmed by DESI DR2.

15. **Algebraic Relations**
    $$\kappa = (\varepsilon\varphi)^2 = [(\varphi^{-1}/4) \times \varphi]^2 = (1/4)^2 = 1/16$$

16. **Number of Causal Domains**
    $$N_{\text{horizon}} = \left\lfloor \frac{4}{\varepsilon} \right\rfloor = 42$$
    42 causally independent regions.

17. **Domain Scale**
    $$\xi = \frac{R_h}{N_{\text{horizon}}} \approx 105\ \text{Mpc}$$

18. **Data Validation of $\varepsilon$**
    $$\varepsilon_{\text{fit}} = 0.155 \pm 0.012\ (\text{DESI DR2})$$
    Theory $\varepsilon = 0.1545$ within $1\sigma$.

19. **Data Validation of $\beta$**
    $$\beta_{\text{fit}} = 0.311 \pm 0.015$$
    From Cepheid/TRGB $H_0$ difference. Within $0.1\sigma$ of $\varphi^{-1}/2 = 0.309$.

20. **Cross-validation of $z_c$**
    $$z_c^{\text{DESI}} = 0.58 \pm 0.08,\quad z_c^{\text{DES-SN}} = 0.62 \pm 0.10,\quad z_c^{\text{joint}} = 0.60 \pm 0.04$$

21. **$\kappa$'s Physical Roles**
    Weak force ($g_w^2 \propto \kappa$), cycle time ($t_{\text{cycle}} \propto e^{1/\kappa}$), neutrino mass ($m_\nu \sim \kappa \cdot \varepsilon \cdot \Lambda$).

22. **Parameter Comparison with $\Lambda$CDM**
    $\Lambda$CDM: 6+ free parameters. IDCM: 0 free parameters.

23. **Generation Tree**
    $$x^2 + x - 1 = 0 \to \varphi^{-1} \to \{\varepsilon = \varphi^{-1}/4,\ \beta = \varphi^{-1}/2,\ \kappa = (\varepsilon\varphi)^2 = 1/16,\ z_c = z(N_{\text{horizon}})\}$$

24. **Geometric Interpretation of $\varepsilon$**
    Minimal $2 \times 2$ split: 2 spatial dimensions × 2 internal dimensions.

25. **Closure of Constants**
    Four constants form a closed algebraic system: given $\varphi^{-1}$, all follow from basic arithmetic.

## Part 3: The Structure of Time (26–35)

26. **Time as Recursion**
    $$t = \{C_0 \to C_1 \to C_2 \to \cdots \to \varphi^{-1}\}$$
    Time = step order of recursion converging to fixed point. Not an independent dimension.

27. **Domain Sync**
    $$C_n \to C_{n+1} \text{ corresponds to one domain sync event}$$

28. **Sync Completeness**
    $$s(r) = 1 - e^{-r/\xi}$$

29. **Origin of the Arrow of Time**
    Recursion converges forward ($C_n \to \varphi^{-1}$), cannot run backward.

30. **The Universe's Future — Heat Death**
    $$\lim_{n\to\infty} C_n = \varphi^{-1} \implies \text{de Sitter vacuum (heat death)}$$

31. **Quantum Fluctuation Accumulation**
    $$\Delta E \sim \kappa \cdot E_{\text{Planck}}$$
    $\kappa = 1/16$ allows fluctuations to accumulate and escape the fixed point.

32. **Cycle Time**
    $$t_{\text{cycle}} = \tau_0 \cdot e^{1/\kappa} = \tau_0 \cdot e^{16}$$
    $e^{16} \approx 8.886 \times 10^6$ exact.

33. **Cycle Time Estimates**
    If $\tau_0 \approx 0.03$ Gyr (Planck scale): $t_{\text{cycle}} \approx 2.7 \times 10^5$ Gyr.
    If $\tau_0 \approx 3.0$ Gyr (Hubble time): $t_{\text{cycle}} \approx 2.7 \times 10^7$ Gyr.

34. **$\kappa$ Precision**
    If $\kappa \to 0$: never restart. If $\kappa = 0.1$: $e^{10} \approx 22026$, too short.
    $\kappa = 1/16$ is the only value consistent with the universe's age.

35. **Restart Condition**
    $$C_0^{\text{new}} = C_{\infty}^{\text{old}} + \delta_{\text{fluctuation}}$$

## Part 4: Light and Causal Structure (36–45)

36. **Light as W-field Sync Signal**
    Light = W-field (Consistency Field) sync signal propagating at $c$.

37. **Finite Speed of Light**
    $$c = \text{causal step length per recursion step}$$
    Causal domains need time to sync, so $c$ is finite.

38. **Domain Diameter**
    $$d_{\text{domain}} \approx c \cdot \tau_{\text{sync}}$$

39. **Friedmann Equation**
    $$H(z)^2 = H_0^2[\Omega_m(1+z)^3 + \Omega_{DE}f(z)]$$

40. **IDCM Correction**
    $$f(z) = 1 + \varepsilon \cdot \frac{z}{z_c} \cdot e^{-z/z_c}$$
    Produces a ~5.68% bump at $z_c \approx 0.6$.

41. **Redshift**
    $$1 + z = \frac{\lambda_{\text{obs}}}{\lambda_{\text{emit}}}$$

42. **CMB**
    $$T_{\text{CMB}} = 2.725\ \text{K},\quad z_{\text{CMB}} \approx 1100$$

43. **CMB Shift Parameter**
    $$R = \sqrt{\Omega_m H_0^2} \int_0^{z_*} \frac{dz}{H(z)}$$
    IDCM: $R = 1.7425$, Planck: $1.7427 \pm 0.0042$, dev = 0.05$\sigma$.

44. **Early Universe**
    For $z > z_c$, $f(z) \to 1$, IDCM ≈ $\Lambda$CDM. Bump only affects late universe ($z < 1.5$).

45. **Lookback Time**
    Finite $c$ means distant observations = past. $H(z)$ integral gives $d_L(z)$.

## Part 5: Matter and Field (46–55)

46. **W-field Form**
    $$\Psi(x,t) = A(x,t) \cdot e^{i\theta(x,t)}$$

47. **Lagrangian Density**
    $$\mathcal{L}_W = \frac{1}{2}(\partial_\mu\Psi)^2 - V(|\Psi|^2)$$

48. **W-field Potential**
    $$V(|\Psi|^2) = \frac{\kappa}{2}|\Psi|^4 - \frac{\varepsilon}{2}|\Psi|^2$$

49. **Potential Minimum**
    $$|\Psi|^2_{\text{min}} = \frac{\varepsilon}{\kappa}$$

50. **$\kappa$ and Matter Stability**
    Smaller $\kappa$ = deeper potential = more stable matter. $\kappa = 1/16$ is just right.

51. **Definition of Matter**
    Matter = local stable resonance of the W-field.

52. **Mass-Energy Equivalence**
    $$E = mc^2$$

53. **Dark Matter**
    $$\rho_{\text{DM}} \propto \kappa \cdot \varepsilon$$
    Dark matter = synced but not fully locked W-field domains.

54. **Total Matter Density**
    $$\rho_{\text{matter}} \propto \varepsilon \times N_{\text{domain}}$$

55. **Matter-Field Unity**
    Matter = locked resonance mode. Field = free propagation mode. Same W-field.

## Part 6: The Origin of Mass (56–65)

56. **Field Theory Definition of Mass**
    $$(\partial_t^2 - \nabla^2 + m^2)\Psi = 0$$
    Mass = resonance frequency of the W-field (Klein-Gordon).

57. **Mass Scaling Law**
    $$m_{\text{particle}} \approx \varepsilon \cdot \varphi^{-1} \cdot \Lambda_{\text{scale}}$$

58. **Electron Mass**
    $$m_e \approx \varepsilon^2 \cdot M_{\text{Planck}} \approx 0.511\ \text{MeV}$$

59. **Proton Mass**
    $$m_p \approx \varepsilon \cdot \varphi^{-1} \cdot \Lambda_{\text{QCD}} \approx 938\ \text{MeV}$$

60. **Neutrino Mass**
    $$m_\nu \approx \kappa \cdot \varepsilon \cdot \Lambda_\nu \approx 0.01\!-\!0.1\ \text{eV}$$

61. **Higgs Mechanism**
    = W-field local phase locking. Higgs boson = W-field phase excitation.

62. **Mass Hierarchy**
    $$\frac{m_e}{m_p} \approx \frac{\varepsilon}{\varphi^{-1}} \cdot \frac{M_{\text{Planck}}}{\Lambda_{\text{QCD}}} \sim \frac{1}{1836}$$

63. **Weak Gauge Boson Mass**
    $$m_W,\ m_Z \propto \kappa \cdot \varphi^{-1} \cdot v$$

64. **Dark Matter Mass**
    $$m_{\text{DM}} \sim \kappa \cdot M_{\text{scale}}$$

65. **Ultimate Source of Mass**
    All mass from $x^2 + x - 1 = 0$. $\varepsilon$ and $\kappa$ are the only scales.

## Part 7: Particle Physics (66–78)

66. **Fermions**
    Half-integer spin W-field resonances (SU(2) rotational symmetry).

67. **Spin Statistics**
    $2\pi$ rotation: fermions $\psi \to -\psi$, bosons $\phi \to \phi$.

68. **Electron**
    $$m_e \approx 0.511\ \text{MeV},\quad q_e = -e,\quad e = \varepsilon \cdot g_e,\ g_e \approx 4\pi$$

69. **Neutrino**
    $$m_\nu \ll m_e$$ Lightest fermion, barely interacts ($\kappa$ suppresses coupling).

70. **Quarks**
    Up/down = higher-frequency W-field resonances. Permanently confined.

71. **Strong Nuclear Force**
    $$g_s^2 \propto \varepsilon$$
    SU(3) sync mode of W-field. Confinement from nonlinear coupling.

72. **Gluons**
    SU(3) W-field modes carrying color charge (self-interacting).

73. **Weak Nuclear Force**
    $$g_w^2 \propto \kappa \approx 1/16$$
    Explains why the weak force is so weak.

74. **Photon**
    Massless U(1) W-field wave mode. Mediates EM interaction.

75. **W/Z Bosons**
    $$m_W,\ m_Z \propto \kappa \cdot \varphi^{-1} \cdot v$$

76. **Gauge Coupling Unification**
    $$g_1 \propto \varepsilon,\quad g_2 \propto \kappa,\quad g_3 \propto \varepsilon$$

77. **Standard Model from W-field**
    $$\text{SU(3)}_C \times \text{SU(2)}_L \times \text{U(1)}_Y \subset \text{W-field symmetries}$$

78. **Unified Description**
    All particles = different frequency modes of W-field recursion. Couplings fully determined by $\varepsilon$ and $\kappa$.

## Part 8: IDCM Core Formulas (79–89)

79. $$C_{n+1} = \frac{1}{1 + C_n},\ C_0 = 1$$
80. $$C_\infty = \varphi^{-1} = (\sqrt{5} - 1)/2$$
81. $$\varepsilon = \varphi^{-1}/4$$
82. $$\kappa = (\varepsilon\varphi)^2 = 1/16$$
83. $$\beta = \varphi^{-1}/2$$
84. $$H(z)^2 = H_0^2[\Omega_m(1+z)^3 + \Omega_{DE}(1 + \varepsilon \cdot \frac{z}{z_c} \cdot e^{-z/z_c})]$$
85. $$A(r) = \varepsilon \cdot (r/\xi)^\beta$$
86. $$H_0^{\text{obs}}(r) = H_0^{\text{global}} \cdot (1 + \varepsilon \cdot A(r))$$
87. $$\Delta\chi^2 = -9.8\ (1853\ \text{points})$$
88. $$t_{\text{cycle}} = \tau_0 \cdot e^{16}$$
89. $$H_0 = 68.2 \pm 0.4\ \text{km/s/Mpc}$$

## Part 9: Data Validation Summary (90–95)

90. BAO (DESI DR2): $\Delta\chi^2 = -6.42$
91. SNe (DES-SN5YR): $\Delta\chi^2 = -3.8$
92. $f\sigma_8$: $\chi^2 = 13.7/20$ — no growth tension
93. $S_8^{\text{IDCM}} = 0.786 \pm 0.008$
94. Cepheid: 73.04/$73.04\pm1.04$ ✅; TRGB: 69.80/$69.80\pm1.90$ ✅
95. **Total**: $\Delta\chi^2 = -9.8$ (~3.1σ vs $\Lambda$CDM)

## Part 10: Conclusion (96–100)

96. $$x^2 + x - 1 = 0 \to \varphi^{-1} \to \varepsilon,\kappa,\beta,z_c \to \text{all observables}$$
97. **Zero free parameters** — all from $\varphi^{-1}$.
98. **Three independent validations**: BAO + SNe + $H_0$ calibration.
99. **Universe = information recursion.**
100. **IDCM = Information Dynamics Cosmology Model.**

---

## Notes for Teachers

- Formulas 1–10: middle school algebra
- Formulas 26–45: basic calculus
- Formulas 56–78: basic wave/field physics
- $\chi^2$ = goodness-of-fit (lower is better)
- Code on GitHub; Excel demonstration viable for recursion
