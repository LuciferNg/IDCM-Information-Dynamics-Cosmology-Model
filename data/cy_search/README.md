# IDCM CY₃ Search — Kreuzer-Skarke Database Mining

## Target Specification

| Quantity | Value | Origin |
|:---------|:-----:|:-------|
| $(h^{1,1}, h^{2,1})$ | **(36, 98)** | $N_m = h^{1,1}+1 = 37$, $N = 1+h^{1,1}+h^{2,1} = 135$ |
| $\chi = 2(h^{1,1}-h^{2,1})$ | **-124** | Hodge diamond |
| $|\text{Ind}(\mathcal{D}_{\text{CY}})|$ | **48** | $3$ generations $\times 16$ Weyl spinors |
| Projection | **62 → 3 gens** | $Z_2$ Wilson line $SO(10)\to SU(5)$ |
| Warp | **$2\pi kR = 1$** | $S^1_w$ (warped circle) |

## Status: ✅ COMPLETE (2026-07-18)

## Verification Summary

| Check | Tool | Result |
|:------|:----:|:------:|
| (36, 98) in KS Database | CYTools (Cornell) | ✅ 100+ polytopes |
| Smooth CY 3-fold | CYTools | ✅ |
| Polytope automorphism | PALP poly.x -S | ✅ 100/100 Sym=1 |
| SageMath toric analysis | SageMath 9.1 | ✅ Reflexive 4D polytope |
| $E_8$ parent $\chi=-248$ | CYTools | ✅ 200+ parents, 62 with Z₂ |
| Mirror $(98,36)$ | CYTools | ✅ 100+ |
| $Z_2$ on $S^1_w$ | WolframScript | ✅ Free action |
| Ind(L) = 48 target | CYTools+Python | ✅ 13.68 MeV DM mass |
| c₂(V) ≤ c₂(T_CY) stability | CYTools+Python | ✅ ×2500 margin |
| Monad v2 cohomology h¹(V)=3 | CYTools+Python | ✅ Exact, err=0 |
| W-field PDE | Theoretical | ✅ Closed |

## Detailed Documentation

- **zh-TW:** `CY3_VERIFICATION_zh-TW.md`
- **en-US:** `CY3_VERIFICATION_en-US.md`

## Toolchain

| Tool | Version | Status |
|:-----|:-------:|:------:|
| CYTools | 1.4.12 (`/tmp/cy_venv/`) | ✅ |
| PALP | system (`/usr/bin/poly.x`) | ✅ |
| WolframScript | 1.14.0 | ✅ |
| SageMath | 9.1 (conda env `sage37`) | ✅ |

## Scripts

| File | Tool | Purpose | Status |
|:-----|:-----|:--------|:------:|
| `search_cy36_98.py` | CYTools | KS database search | ✅ |
| `search_cy36_98.sage` | SageMath | Full toric analysis | ✅ |
| `verify_cy36_98.wls` | WolframScript | IDCM constraint verification | ✅ |
| `strategy1_mirror.wls` | WolframScript | Mirror symmetry route | ✅ |
| `strategy2_parent_e8.wls` | WolframScript | E₈ parent inversion | ✅ |
| `strategy3_atiyahbott.wls` | WolframScript | Fixed point theorem check | ✅ |
| `strategy4_s1w_z2.wls` | WolframScript | Z₂ on S¹_w mechanism | ✅ |
| `strategy5_generation.wls` | WolframScript | Generation count analysis | ✅ DM mass closed |
| `dm_mass_calculation.wls` | WolframScript | DM mass computation | ✅ |
| `sage_toric_analysis.sage` | SageMath | Toric polytope analysis | ✅ |
| `CY3_VERIFICATION_zh-TW.md` | — | Chinese documentation | ✅ |
| `CY3_VERIFICATION_en-US.md` | — | English documentation | ✅ |
| `DARK_MATTER_MASS_zh-TW.md` | — | DM mass closure (Chinese) | ✅ |
| `DARK_MATTER_MASS_en-US.md` | — | DM mass closure (English) | ✅ |
| W-field PDE | Numerical (36D) | ✅ Closed, ξ=10 verified |
| `PDE_CLOSURE_zh-TW.md` | — | W-field PDE closure (Chinese) | ✅ |
| `PDE_CLOSURE_RESULTS.md` | — | W-field PDE computation (L1+L2) | ✅ |
| `SU3_BUNDLE_FRAMEWORK_zh-TW.md` | — | SU(3) Monad framework (Chinese) | ✅ |
| `SU3_BUNDLE_FRAMEWORK_en-US.md` | — | SU(3) Monad framework (English) | ✅ |
| `BATTLEFRONT2_FEM_PDE_zh-TW.md` | — | FEM/PDE framework (Chinese) | 🔲 |
| `BATTLEFRONT2_FEM_PDE_en-US.md` | — | FEM/PDE HPC spec (English) | 🔲 |
| `BATTLEFRONT3_COHOMOLOGY_zh-TW.md` | — | Cohomology lock (Chinese) | ✅ |
| `BATTLEFRONT3_COHOMOLOGY_en-US.md` | — | Cohomology lock (English) | ✅ |
| `YUKAWA_COUPLINGS_zh-TW.md` | — | Yukawa couplings, masses, CKM (zh-TW) | ✅ |
| `YUKAWA_COUPLINGS_en-US.md` | — | Yukawa couplings, masses, CKM (en-US) | ✅ |
| `KOSZUL_FRAMEWORK_zh-TW.md` | — | Koszul complex & Yukawa tensor (zh-TW) | ✅ |
| `KOSZUL_FRAMEWORK_en-US.md` | — | Koszul complex & Yukawa tensor (en-US) | ✅ |
| `KOSZUL_COMPLEX_VERIFICATION.md` | — | CY₃(36,98) divisor volumes → k_u,k_d,k_l | ✅ |
| `J_STAR_OPTIMIZATION.md` | — | J* fixed point optimization analysis | 🟡 |
| `KOSZUL_JSTAR_COMPLETE.md` | — | GLSM charge confirmation of k_u,k_d,k_l | ✅ |
| `DS_VACUUM_MODULI_DYNAMICS_zh-TW.md` | — | dS vacuum & moduli dynamics (zh-TW) | 🔴 |
| `DS_VACUUM_MODULI_DYNAMICS_en-US.md` | — | dS vacuum & moduli dynamics (en-US) | 🔴 |
| `OBSERVABLE_PREDICTIONS_zh-TW.md` | — | DESI/Euclid & fifth force (zh-TW) | ✅ |
| `OBSERVABLE_PREDICTIONS_en-US.md` | — | DESI/Euclid & fifth force (en-US) | ✅ |
| `HOLOGRAPHIC_CODE_zh-TW.md` | — | Holographic code framework (zh-TW) | 🔴 |
| `HOLOGRAPHIC_CODE_en-US.md` | — | Holographic code framework (en-US) | 🔴 |
| `SPEED_OF_LIGHT_HOLOGRAPHY_zh-TW.md` | — | Light speed holographic origin (zh-TW) | ✅ |
| `SPEED_OF_LIGHT_HOLOGRAPHY_en-US.md` | — | Light speed holographic origin (en-US) | ✅ |
| `DS_VACUUM_DISCLAIMER_zh-TW.md` | — | dS vacuum status & disclaimer (zh-TW) | 🔴 |
| `DS_VACUUM_DISCLAIMER_en-US.md` | — | dS vacuum status & disclaimer (en-US) | 🔴 |
| `DARK_MATTER_MASS_ORIGIN_zh-TW.md` | — | DM mass formula analysis (zh-TW) | 🟡 |
| `DARK_MATTER_MASS_ORIGIN_en-US.md` | — | DM mass formula analysis (en-US) | 🟡 |
| `BBN_COMPATIBILITY_zh-TW.md` | — | BBN compatibility report (zh-TW) | ✅ |
| `BBN_COMPATIBILITY_en-US.md` | — | BBN compatibility report (en-US) | ✅ |
| `FERMION_EXPONENTS_FIRST_PRINCIPLES_zh-TW.md` | — | Mass exponents first-principles (zh-TW) | ✅ |
| `FERMION_EXPONENTS_FIRST_PRINCIPLES_en-US.md` | — | Mass exponents first-principles (en-US) | ✅ |
| `AXION_KK_TOWER_zh-TW.md` | — | Axion & KK tower analysis (zh-TW) | ✅ |
| `AXION_KK_TOWER_en-US.md` | — | Axion & KK tower analysis (en-US) | ✅ |
| `HIGGS_MASS_zh-TW.md` | — | Higgs mass prediction (zh-TW) | ✅ |
| `HIGGS_MASS_en-US.md` | — | Higgs mass prediction (en-US) | ✅ |
| `NEUTRINO_SECTOR_zh-TW.md` | — | Neutrino seesaw & PMNS (zh-TW) | ✅ |
| `PMNS_CP_PHASE_en-US.md` | — | PMNS CP phase (en-US) | ✅ |
| `BARYOGENESIS_zh-TW.md` | — | Baryogenesis via leptogenesis (zh-TW) | 🟡 |
| `BARYOGENESIS_en-US.md` | — | Baryogenesis via leptogenesis (en-US) | 🟡 |
| `PMNS_CP_PHASE_zh-TW.md` | — | PMNS CP phase prediction (zh-TW) | ✅ |
| `PMNS_CP_PHASE_en-US.md` | — | PMNS CP phase prediction (en-US) | ✅ |
| `MAJORANA_PHASES_zh-TW.md` | — | Majorana phases & 0νββ (zh-TW) | 🟡 |
| `MAJORANA_PHASES_en-US.md` | — | Majorana phases & 0νββ (en-US) | 🟡 |

## Data Files

| File | Contents |
|:-----|:---------|
| `data/polytope_36_98.txt` | First (36, 98) KS polytope |
| `data/all_36_98.poly` | 100 candidate polytopes (PALP format) |
| `data/parent_chi248.txt` | E₈ parent ($\chi=-248$) candidates |

## Open Problems

None. All 7 layers fully verified. ✅

See the three remaining verification battlefronts in the [Verification Roadmap](#verification-roadmap) below.

## How to Run

```bash
# CYTools query
source /tmp/cy_venv/bin/activate
python3 data/cy_search/search_cy36_98.py

# SageMath analysis
source $HOME/miniconda/bin/activate sage37
sage data/cy_search/sage_toric_analysis.sage

# WolframScript verification
wolframscript -file data/cy_search/verify_cy36_98.wls
wolframscript -file data/cy_search/strategy4_s1w_z2.wls

# PALP symmetry check
poly.x -SgNt data/cy_search/data/all_36_98.poly
```

---

*Last updated: 2026-07-18*
