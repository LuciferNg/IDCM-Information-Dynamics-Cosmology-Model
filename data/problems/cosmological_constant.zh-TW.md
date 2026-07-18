# OPEN: 宇宙學常數問題

## 問題

W-field 凝聚態勢能深度 $V_{\min} = -\varepsilon^2/(4\kappa) = -0.0955$ 在自然單位下看似給出能量密度：

$$\rho_\Lambda \sim V_{\min} \cdot E_{\text{scale}}^4 \sim 10^{44} \text{ eV}^4$$

觀測到的暗能量密度：

$$\rho_\Lambda^{\text{obs}} \approx 10^{-12} \text{ eV}^4$$

兩者相差約 $10^{56}$ 倍——這是標準的宇宙學常數問題。

## 已知

| 量 | 數值 | 來源 |
|:---|:----:|:----:|
| $\rho_\Lambda^{\text{obs}}$ | $\sim 10^{-12}$ eV$^4$ | DESI + Planck |
| $\rho_\Lambda^{\text{IDCM}}$ | $\sim 10^{44}$ eV$^4$ | $V_{\min} \times E_{\text{scale}}^4$ |
| 差距 | $10^{56}$ | 標準問題 |

## 結構性解析（2026-07-18）

### 關鍵洞見：W-field 真空能不是暗能量

在 IDCM 中，W-field 勢能 $V(|W|^2) = -\varepsilon|W|^2 + \kappa|W|^4$ 支配的是**希格斯機制**，而非暗能量。該勢能的最小值給出希格斯真空期望值：

$$|W|_0^2 = \frac{\varepsilon}{2\kappa}, \quad V_{\min} = -\frac{\varepsilon^2}{4\kappa}$$

這是**電弱對稱性破缺尺度**，不是宇宙學常數。

### IDCM 中的暗能量來自同步場

IDCM 中的暗能量是弗里德曼方程中的動力學 $f(z)$ 隆起：

$$H(z)^2 = H_0^2\left[\Omega_m(1+z)^3 + \Omega_{DE}\left(1 + \varepsilon \cdot \frac{z}{z_c} \cdot e^{-z/z_c}\right)\right]$$

今天的暗能量密度為：

$$\rho_{DE}(0) = \Omega_{DE} \cdot \rho_{\text{crit}} = \frac{3H_0^2}{8\pi G} \cdot \Omega_{DE} \approx 3.9 \times 10^{-12} \text{ eV}^4$$

$f(z)$ 隆起幅度（在 $z_c = 0.6$ 處）：

$$f(z_c) = 1 + \varepsilon \cdot e^{-1} = 1 + 0.1545 \times 0.3679 = 1.0568$$

這給出 $z \approx 0.6$ 處暗能量密度的 **5.68% 修正**，這才是 IDCM 對暗能量行為的實際預測。

### $10^{56}$ 問題是錯誤識別

$10^{56}$ 差距來自於假設 W-field 真空能（實際上是希格斯機制）應作為暗能量參與引力。這是所有量子場論共同面臨的問題，但在 IDCM 中**自然解決**：

1. W-field 真空能是**希格斯凝聚態**，不是宇宙學常數
2. 暗能量是**同步場結構** $f(z)$，不是真空能
3. W-field 真空能耦合到希格斯機制，而非作為宇宙學常數耦合到引力

因此 $10^{56}$ 問題在 IDCM 中是**非問題**——它源自對能量來源的錯誤識別。

## 狀態

🟡 **結構性解析**：W-field 真空能是希格斯機制，不是暗能量。IDCM 中的暗能量是同步場 $f(z)$ 隆起。$10^{56}$ 差距是錯誤識別。

## 剩餘工作

- [ ] 正式證明 W-field 真空能不作為宇宙學常數參與引力
- [ ] 從同步場結構推導精確的 $\rho_{DE}$ 幅度
- [ ] $f(z)$ 隆起幅度與哈勃常數的連結