# IDCM CY₃(36,98) — SageMath Toric Geometry Pipeline

**Date:** 2026-07-20  
**Status:** ✅ Complete (Phases 1-5)  
**Tool:** SageMath 9.1 + CYTools 1.4.12 export

---

## Pipeline Overview

```
CYTools fetch_polytopes(h11=36, h21=98)
  │
  ├── Polytope: 6V, 48P, Reflexive, Non-favorable
  │
  ├── FRST Triangulation: 144 simplices, 37 rays
  │
  ├── GLSM charge matrix: 32×37 (rank=32)
  │
  └── Export → JSON (cy36_98_sage_export.json)
         │
         ▼
SageMath pipeline:
  Phase 2: Fan(cones, rays) → 37 rays, 144 maximal cones
  Phase 3: CoxRing / (SR ideal + Lin ideal) → Chow ring
  Phase 4: CY restriction → h¹¹(CY)=36, extra=3 classes
  Phase 5: J* setup → GLSM charge-to-ray mapping
```

---

## Phase 2: Fan and Toric Variety

### Construction

From the CYTools triangulation, we built the resolved 4D fan:

| Parameter | Value |
|:----------|:------|
| Lattice points in polytope | 48 |
| Rays in fan | 37 (indices 0-36) |
| Maximal cones (4-simplices) | 144 |
| Lattice | $\mathbb{Z}^4$ (ToricLattice(4)) |

The 37 rays correspond to:
- 32 rays with GLSM charges (from the $32\times37$ GLSM matrix)
- 4 additional rays from the triangulation resolution
- 1 origin point (index 0, the interior of the reflexive polytope)

### Toric Variety

| Property | Value |
|:---------|:------|
| Dimension | 4 |
| Affine patches | 144 |
| Toric divisors | 37 |
| Fan type | Complete (from reflexive polytope) |

---

## Phase 3: Chow Ring

### Cox Ring

$$S = \mathbb{Q}[x_0, x_1, \ldots, x_{36}]$$

37 homogeneous coordinates corresponding to the 37 rays/fan divisors.

### Stanley-Reisner Ideal

475 unique generators (reduced from 484 CYTools generators after deduplication).
Examples:

$$x_1 x_2, \; x_1 x_4, \; x_1 x_5, \; \ldots$$

Each generator $x_i x_j = 0$ means the divisors $D_i$ and $D_j$ do not intersect
in the toric variety (their cones are not adjacent in the fan).

### Linear Relations Ideal

5 generators from the GLSM linear relations, encoding the charge constraints:

$$x_0 + 20x_2 + 64x_5 + \cdots + 2x_{36} = 0$$
$$-4x_2 + x_3 - 12x_5 - \cdots - x_{35} = 0$$
$$\vdots$$

### Chow Ring

$$A^*(X) = S / (I_{SR} + I_{lin})$$

| Quantity | Value |
|:---------|:------|
| Total ideal generators | 480 (475 SR + 5 linear) |
| Ambient divisor class rank | 33 |
| CY divisor class rank (h¹¹) | 36 |
| Extra classes | 3 (from CY cohomology) |

---

## Phase 4: CY Hypersurface Restriction

### Anti-canonical Class

$$-K_X = \sum_{i=0}^{36} D_i$$

The CY hypersurface is the zero set of a section of $-K_X$.

### Extra Divisor Classes

For this non-favorable CY, $h^{1,1}(CY) = 36$ exceeds the ambient Picard rank
of 33 by 3. These 3 extra divisor classes:

1. Exist only in the CY cohomology, not in the ambient toric variety
2. Correspond to interior lattice points on the 3-faces of the reflexive polytope
3. Complete the 36D Kähler moduli space needed for the $J^*$ fixed point

### Kähler Cone Structure

| Quantity | Value |
|:---------|:------|
| Ambient Kähler cone | 33D (from 37 rays - 4 dimensions) |
| CY Kähler moduli | 36D |
| CYTools Kähler cone | 185 hyperplanes in ℝ³² |

---

## Phase 5: GLSM Charge-to-Ray Mapping

### Key Mapping

| GLSM coord3 Charge | Fan Ray Index | IDCM FN Charge |
|:------------------:|:-------------:|:--------------:|
| 12 | 2 | — |
| **10** | **4** | **$k_u = 33\beta = 10.1976$** |
| 9 | 5, 18 | — |
| **8** | **6** | **$k_d = 26\beta - \varphi^{-4} = 7.8885$** |
| 7 | 19, 20 | — |
| **6** | **7, 8, 9, 21** | **$k_l = 19\beta = 5.8713$** |

### J* Fixed Point

The $J^*$ fixed point satisfies $\text{Vol}(CY) = \kappa^3 = 1/4096$.
At this point, the divisor volumes $\text{Vol}(D_i)$ give the FN exponents:

$$k_i = -\log_{\varphi}\left(\frac{\text{Vol}(D_i)}{\text{Vol}(CY)}\right)$$

The FN charges $k_u, k_d, k_l$ correspond to divisor volumes for
GLSM charges 10 (ray 4), 8 (ray 6), and 6 (rays 7, 8, 9, 21) respectively,
evaluated at the $J^*$ fixed point in the full 36D Kähler moduli space.

### Triple Intersection (Next Step)

To compute exact FN charges, we need the triple intersection numbers:

$$\kappa_{ijk} = \int_{CY} D_i \wedge D_j \wedge D_k = \int_X D_i \wedge D_j \wedge D_k \wedge (-K_X)$$

These are computed in the Chow ring $A^*(X)$ as the top-degree coefficient
of the product $D_i \cdot D_j \cdot D_k \cdot (-K_X)$. The 36D volume functional
is then:

$$\text{Vol}(t) = \frac{1}{6} \sum_{i,j,k} \kappa_{ijk} \cdot t^i t^j t^k$$

and $J^*$ is found by minimizing $|\text{Vol}(t) - \kappa^3|$ over the
Kähler cone.

---

## File Reference

| File | Description |
|:-----|:------------|
| `cy36_98_sage_export.json` | CYTools export (48 points, 144 simplices, GLSM, SR ideal) |
| `sagemath_phases234.json` | SageMath fan + Chow ring results |
| `sagemath_phase5.json` | J* setup + charge mapping |
| `idcm_sagemath_phases234.sage` | Phases 2-4 SageMath script |
| `idcm_sagemath_phase5.sage` | Phase 5 SageMath script |
