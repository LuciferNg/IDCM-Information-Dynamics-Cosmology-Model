# IDCM CY₃(36,98) — SageMath Toric Geometry Pipeline（中文版）

**日期：** 2026-07-20  
**狀態：** ✅ 完成（Phases 1-5）  
**工具：** SageMath 9.1 + CYTools 1.4.12 export

---

## Pipeline 概覽

```
CYTools fetch_polytopes(h11=36, h21=98)
  │
  ├── Polytope: 6V, 48P, Reflexive, Non-favorable
  │
  ├── FRST 三角化: 144 個 4-simplices, 37 條 rays
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

## Phase 2: Fan 與 Toric Variety

### 建構

從 CYTools 三角化建構 resolved 4D fan：

| 參數 | 值 |
|:----|:----|
| Polytope 晶格點 | 48 |
| Fan 的 rays | 37（indices 0-36） |
| Maximal cones（4-simplices） | 144 |
| Lattice | $\mathbb{Z}^4$（ToricLattice(4)） |

37 條 rays 對應於：
- 32 條有 GLSM charges 的 rays（來自 $32\times37$ GLSM matrix）
- 4 條三角化新增的 rays
- 1 個原點（index 0，reflexive polytope 的內點）

### Toric Variety

| 屬性 | 值 |
|:----|:----|
| 維度 | 4 |
| Affine patches | 144 |
| Toric divisors | 37 |
| Fan type | Complete（from reflexive polytope） |

---

## Phase 3: Chow Ring

### Cox Ring

$$S = \mathbb{Q}[x_0, x_1, \ldots, x_{36}]$$

37 個 homogeneous coordinates，對應 37 條 fan rays。

### Stanley-Reisner Ideal

475 個唯一 generator（CYTools 的 484 個去重後）。
例子：

$$x_1 x_2, \; x_1 x_4, \; x_1 x_5, \; \ldots$$

每個 generator $x_i x_j = 0$ 代表 divisor $D_i$ 和 $D_j$ 不相交。

### Linear Relations Ideal

5 個 generator，來自 GLSM linear relations：

$$x_0 + 20x_2 + 64x_5 + \cdots + 2x_{36} = 0$$
$$-4x_2 + x_3 - 12x_5 - \cdots - x_{35} = 0$$
$$\vdots$$

### Chow Ring

$$A^*(X) = S / (I_{SR} + I_{lin})$$

| 量 | 值 |
|:---|:----|
| 總 ideal generators | 480（475 SR + 5 linear） |
| Ambient divisor class rank | 33 |
| CY divisor class rank（h¹¹） | 36 |
| Extra classes | 3（來自 CY cohomology） |

---

## Phase 4: CY Hypersurface Restriction

### Anti-canonical Class

$$-K_X = \sum_{i=0}^{36} D_i$$

CY hypersurface 是 $-K_X$ 的 section 的零點集。

### Extra Divisor Classes

對於 non-favorable CY，$h^{1,1}(CY) = 36$ 大於 ambient Picard rank 33 的 3 個 extra divisor classes：

1. 只存在於 CY cohomology，不在 ambient toric variety
2. 對應於 reflexive polytope 的 3-face 上的 interior lattice points
3. 補足 $J^*$ fixed point 所需的完整 36D Kähler moduli space

### Kähler Cone Structure

| 量 | 值 |
|:---|:----|
| Ambient Kähler cone | 33D（37 rays - 4 dimensions） |
| CY Kähler moduli | 36D |
| CYTools Kähler cone | 185 hyperplanes in ℝ³² |

---

## Phase 5: GLSM Charge-to-Ray Mapping

### 關鍵映射

| GLSM coord3 Charge | Fan Ray Index | IDCM FN Charge |
|:------------------:|:-------------:|:--------------:|
| 12 | 2 | — |
| **10** | **4** | **$k_u = 33\beta = 10.1976$** |
| 9 | 5, 18 | — |
| **8** | **6** | **$k_d = 26\beta - \varphi^{-4} = 7.8885$** |
| 7 | 19, 20 | — |
| **6** | **7, 8, 9, 21** | **$k_l = 19\beta = 5.8713$** |

### J* Fixed Point

$J^*$ fixed point 滿足 $\text{Vol}(CY) = \kappa^3 = 1/4096$。
在此點，divisor volumes $\text{Vol}(D_i)$ 給出 FN exponents：

$$k_i = -\log_{\varphi}\left(\frac{\text{Vol}(D_i)}{\text{Vol}(CY)}\right)$$

FN charges $k_u, k_d, k_l$ 對應於 GLSM charges 10（ray 4）、8（ray 6）、
6（rays 7, 8, 9, 21）在 $J^*$ fixed point 的 divisor volumes。

### Triple Intersection（下一步）

要計算精確 FN charges，需要 triple intersection numbers：

$$\kappa_{ijk} = \int_{CY} D_i \wedge D_j \wedge D_k = \int_X D_i \wedge D_j \wedge D_k \wedge (-K_X)$$

在 Chow ring $A^*(X)$ 中計算為 $D_i \cdot D_j \cdot D_k \cdot (-K_X)$ 的 top-degree coefficient。
36D volume functional 為：

$$\text{Vol}(t) = \frac{1}{6} \sum_{i,j,k} \kappa_{ijk} \cdot t^i t^j t^k$$

$J^*$ 通過最小化 $|\text{Vol}(t) - \kappa^3|$ 在 Kähler cone 上找到。

---

## 文件參考

| 文件 | 說明 |
|:----|:-----|
| `cy36_98_sage_export.json` | CYTools export（48 points, 144 simplices, GLSM, SR ideal） |
| `sagemath_phases234.json` | SageMath fan + Chow ring 結果 |
| `sagemath_phase5.json` | J* setup + charge mapping |
| `idcm_sagemath_phases234.sage` | Phases 2-4 SageMath script |
| `idcm_sagemath_phase5.sage` | Phase 5 SageMath script |
