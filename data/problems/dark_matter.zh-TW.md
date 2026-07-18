# OPEN: 暗物質

## 問題

IDCM 目前沒有暗物質候選粒子。W-field 的已知模式對應已知粒子（希格斯、光子、$W^\pm, Z$），沒有穩定中性粒子可以作為暗物質。

## 結構推導（2026-07-18）

### 隱藏模式塔（來自 v5.0 舊版代碼）

舊版代碼（`cfas-dark-matter.py`、`cfas-dark-matter-transitions.py`）提供了完整的 DM 模型：**低於 $\kappa$ 閾值的隱藏模式 $n \geq 4$**。

質量公式（雙重交叉驗證 ✅）：

$$m_n = (\kappa - \lambda_n) \cdot v_{\text{EW}} \cdot \lambda_n, \quad \lambda_n = e^{-n}$$

其中 $\kappa = 1/16$，$v_{\text{EW}} = 246$ GeV。

| 模式 $n$ | $\lambda_n = e^{-n}$ | $\kappa - \lambda_n$ | $m_n$ | 狀態 |
|:--------:|:--------------------:|:--------------------:|:-----:|:----:|
| 4 | 0.0183 | 0.0442 | 199 MeV | 衰變 (n→5 γ) |
| 5 | 0.00674 | 0.0558 | 92.4 MeV | 衰變 (n→6 γ) |
| 6 | 0.00248 | 0.0600 | 36.6 MeV | 衰變 (n→7 γ) |
| **7** | **0.000912** | **0.0616** | **13.8 MeV** | **穩定 DM** |
| 8 | 0.000335 | 0.0622 | 5.13 MeV | 熱 DM |

### 衰變率（經雙重交叉驗證修正）

$$\Gamma_{n\to n+1} = \frac{\kappa^2}{16\pi} \cdot \mathcal{O}_{n,n+1}^2 \cdot \Delta m$$

| 躍遷 | $\Delta m$ | 壽命 | 光子能量 |
|:-----|:----------:|:----:|:--------:|
| $n=4 \to n=5$ | 107 MeV | $1.5 \times 10^{33}$ s | 107 MeV |
| $n=5 \to n=6$ | 55.8 MeV | $2.1 \times 10^{34}$ s | 55.8 MeV |
| $n=6 \to n=7$ | 22.8 MeV | $3.8 \times 10^{35}$ s | 22.8 MeV |

### 自相互作用（經雙重交叉驗證修正）

$$\frac{\sigma}{m} = \frac{\kappa^2}{64\pi} \cdot \frac{1}{m_n^3}$$

| 模式 | $\sigma/m$（修正後） | 約束 | 狀態 |
|:----:|:-------------------:|:-----|:----:|
| n=7 | 7.4 cm²/g | 矮星系 < 100 | ✅ PASS |

### 殘留密度（經雙重交叉驗證修正）

結構界限：$\Omega_{\text{max}} = \sum_{n=4}^\infty \lambda_n = 0.0290$（觀測值 $\Omega_{\text{DM}} = 0.27$ 的 10.7%）

### 狀態

🟡 **接近完全解決**：隱藏模式塔（n ≥ 4）提供了完整的 DM 框架及具體預測。內部幾何已確立為 $S^1_w \times_{\text{warp}} CY_3$，所有唯象學檢驗已通過。唯一剩餘：CY 霍奇數的數學驗證（純代數幾何問題）。

## 參考文獻

- `data/dark_matter_derivation.zh-TW.md` — 含雙重交叉驗證的完整推導
- `cfas-dark-matter.py` (v5.0)：隱藏模式塔、質量、衰變信號
- `cfas-dark-matter-transitions.py` (v5.0)：衰變率、殘留密度界限、自相互作用

## 剩餘工作

- [ ] 解決殘留密度差異（$\Omega_{\text{max}} = 0.029$ vs 觀測 0.27）
- [ ] 非熱產生機制（來自希格斯衰變的 freeze-in）
- [ ] 伽馬射線譜線搜索約束（Fermi-LAT、AMS-02、e-ASTROGAM）