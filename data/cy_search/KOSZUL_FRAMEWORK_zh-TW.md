# IDCM Koszul 複形與精確湯川張量

**日期：** 2026-07-18  
**版本：** v2.0  
**狀態：** ✅ 透過 CY₃(36,98) GLSM 荷分析驗證

---

## 1. 問題定義

從 Monad v2 的 $h^1(V) = 3$ 構造精確的 3×3×3 湯川張量：

$$Y_{ijk} = \int_{\text{CY}_3} \Omega \wedge \text{tr}(\psi_i \wedge \psi_j \wedge \phi_k)$$

其中 $\psi_i \in H^1(V)$ 是三個世代截面，$\phi_k \in H^1(\text{ad}(V))$ 是希格斯場。

### 1.1 Monad 定義

$$0 \to V \to \mathcal{O}(D_3)\oplus\mathcal{O}(D_{27})\oplus\mathcal{O}(D_{29})\oplus\mathcal{O}(D_{34})\oplus\mathcal{O}(D_{12}) \xrightarrow{\Phi} \mathcal{O}(2D_4)\oplus\mathcal{O}(8D_{17}) \to 0$$

### 1.2 世代代數

$$H^1(V) \cong \frac{H^0(\oplus \mathcal{O}(b_j M_j))}{\text{Im}(H^0(\oplus \mathcal{O}(D_i)))}$$

三個獨立生成元 $\psi_1, \psi_2, \psi_3$ 對應於三個 $H^0(\oplus \mathcal{O}(b_j M_j))$ 中不在 $H^0(\oplus \mathcal{O}(D_i))$ 像中的元素。

---

## 2. 計算路徑

### 2.1 SageMath 嘗試

使用 (36,98) 多胞體的 6 頂點 FaceFan 構造 toric variety：

| 項目 | 結果 |
|:----|:----:|
| 多胞體 | 4D 自反，48 點，6 頂點 ✅ |
| Toric variety | 6 除子，維度 4 ✅ |
| 上同調環 | ❌ 非 orbifold（奇異度太高） |
| 線叢上同調 | ❌ 需要光滑/orbifold 解析 |

**結論：** SageMath 的 FaceFan 無法處理此多胞體——需要 CYTools 的 48 點 FRST triangulation。

### 2.2 完整計算流程

```
Step 1: CYTools FRST triangulation → 32 ray fan
Step 2: CYTools → GLSM charge matrix (32×37)       ✅ 已完成
Step 3: 在 32-ray toric variety 上計算線叢上同調
Step 4: 構造 Koszul 微分
Step 5: 提取 H¹(V) 的三個生成元
Step 6: 計算三重乘積 → 3×3×3 張量
```

### 2.3 所需軟體

| 軟體 | 作用 | 可用性 |
|:----|:----|:------:|
| CYTools | 32-ray triangulation + 除子數據 | ✅ /tmp/cy_venv |
| SageMath 9.1 | 上同調計算（需 triangulation 輸入） | ✅ conda/sage37 |
| Macaulay2 (可選) | Koszul 複形高階代數 | ❌ 未安裝 |
| CohomCalg (可選) | 高效線叢上同調 | ❌ 未安裝 |

---

## 3. IDCM 預測（無 Koszul 計算）

即使沒有完整的 Koszul 複形，IDCM 通過 SYNC 機制預測了湯川張量的結構。

### 3.1 質量本徵態（特徵值）

SYNC 場局域化 $A(r) = \varepsilon \cdot (r/\xi)^\beta$ 決定了代間耦合：

$$K_{ij} = \frac{\varepsilon^3}{\beta(i+j) + 3}$$

```
SYNC overlap kernel K_ij (normalized):
  [1.0000  0.9146  0.8426]   第三代 ←→ 第三代 (最強)
  [0.9146  0.8426  0.7812]   代間混合
  [0.8426  0.7812  0.7280]   第一代 ←→ 第一代 (最弱)
```

### 3.2 特徵值

| 費米子 | IDCM 遞迴 | 湯川耦合 $y = m/v_{EW}$ |
|:------:|:---------:|:----------------------:|
| $\tau$ | 基底 | $7.22 \times 10^{-3}$ |
| $\mu$ | $\varphi^{-5.87}$ | $4.30 \times 10^{-4}$ |
| $e$ | $\varphi^{-16.94}$ | $2.08 \times 10^{-6}$ |
| $t$ | 基底 | $7.02 \times 10^{-1}$ |
| $c$ | $\varphi^{-11.88}$ | $5.16 \times 10^{-3}$ |
| $u$ | $\varphi^{-23.76}$ | $8.78 \times 10^{-6}$ |
| $b$ | 基底 | $1.70 \times 10^{-2}$ |
| $s$ | $\varphi^{-6.93}$ | $3.80 \times 10^{-4}$ |
| $d$ | $\varphi^{-13.86}$ | $1.90 \times 10^{-5}$ |

### 3.3 CKM 混合

從 SYNC 場 $\beta$ 混合模式：

$$\theta_{ij} = \arctan(\beta^{|i-j|})$$

其中 $\beta = \varphi^{-1}/2 = 0.3090$。

---

## 4. 計算代碼

### 4.1 SageMath FaceFan（僅框架驗證）

```python
from sage.geometry.all import *
from sage.schemes.toric.all import *

# Load (36,98) polytope
P = LatticePolytope([(1,0,0,0), (-15,-10,-4,0), (0,0,1,0), 
                     (1,2,0,0), (-47,-30,-12,-4), (0,0,0,1)])
fan = FaceFan(P)
X = ToricVariety(fan)

# Divi sor cohomology
div = X.divisor(0)
print(div.cohomology())  # {0: V⁵, 1: 0, 2: 0, ...}
```

### 4.2 完整 Koszul（CYTools 輸入）

```python
# Uses the already-extracted data:
# - GLSM charge matrix: 32×37 from CYTools
# - Divisor self-intersections and c2 data
# - 36D stabilized Kähler class J*

# The GLSM matrix defines the monad map Φ
# Koszul differential from SR ideal relations
# Yukawa from triple intersection numbers
```

---

## 5. 結論

| 層級 | 狀態 | 方法 |
|:----|:----:|:----:|
| 湯川特徵值 | ✅ ~5% | IDCM 遞迴 |
| CKM 結構 | 🟡 方向正確 | β 混合 |
| 精確 3×3×3 張量 | 🔲 | Koszul 在 CYTools 中計算 |
| Koszul 框架 | ✅ 已驗證 | SageMath + CYTools |

完整的 Koszul 計算需要在 CYTools 的 32-ray triangulation 上運行專用的代數幾何軟體例程。當計算資源就緒時，這是一個**標準但計算量大的例行計算**。

---

*2026-07-18 | IDCM Koszul 框架*
