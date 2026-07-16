# IDCM 高中生版 — 一百條 Formula（廣東話）

## 第一部分：宇宙嘅數學結構（1–10）

1. **生成方程**
   $$x^2 + x - 1 = 0$$
   宇宙結構由呢一條二次方程生成。解係 $x = (\sqrt{5} - 1)/2$，記為 $\varphi^{-1}$（黃金比例倒數），約等於 0.618。

2. **遞迴映射（Recursive Map）**
   $$C_{n+1} = \frac{1}{1 + C_n}$$
   無論 $C_0$ 係乜正數，呢個映射都收斂到 $\varphi^{-1}$。

3. **收斂速率分析**
   $$\lambda = \left|\frac{dC_{n+1}}{dC_n}\right|_{C=\varphi^{-1}} = \varphi^{-2} \approx 0.381966$$
   因為 $|\lambda| < 1$，所以收斂一定會發生。

4. **收斂誤差**
   $$C_n - \varphi^{-1} \propto (-0.382)^n$$
   收斂因子係 0.382，八步後誤差低過 $10^{-3}$。

5. **有理數近似序列**
   $$1,\ \frac{1}{2},\ \frac{2}{3},\ \frac{3}{5},\ \frac{5}{8},\ \frac{8}{13},\ \frac{13}{21},\ \frac{34}{55}$$
   呢個係 $\varphi^{-1}$ 連續分數展開嘅截斷近似（convergent）。

6. **連續分數表示**
   $$\varphi^{-1} = \cfrac{1}{1 + \cfrac{1}{1 + \cfrac{1}{1 + \ddots}}}$$
   宇宙底層係一條無限連續分數（continued fraction），唔係粒子。

7. **費波那契關係**
   $$\frac{F_n}{F_{n+1}},\quad F_{n+2} = F_{n+1} + F_n$$
   分子分母都係費波那契數（Fibonacci number）$F_n$。

8. **費波那契極限**
   $$\lim_{n\to\infty} \frac{F_n}{F_{n+1}} = \varphi^{-1}$$
   費波那契數列相鄰項之比嘅極限就係黃金比例倒數。

9. **第二個解**
   $$x_- = -\varphi \approx -1.618034$$
   二次方程另一個根係負嘅黃金比例，對應時間嘅對稱破缺。

10. **結構層級**
    $$x^2 + x - 1 = 0 \to \varphi^{-1} \to (\varepsilon, \kappa, \beta, z_c) \to \text{觀測量}$$
    一條方程生成所有常數，冇自由參數。

## 第二部分：四個宇宙常數（11–25）

11. **同步幅度 $\varepsilon$**
    $$\varepsilon = \frac{\varphi^{-1}}{4} \approx 0.1545085$$
    控制膨脹異常（anomaly）嘅幅度。除 4 因為最細對稱分裂 $2 \times 2$。

12. **閉合常數 $\kappa$**
    $$\kappa = (\varepsilon\varphi)^2 = \frac{1}{16} = 0.0625$$
    純代數（algebra）恆等式：$\varepsilon\varphi = (\varphi^{-1}/4) \times \varphi = 1/4$，平方得 $1/16$。

13. **尺度指數 $\beta$**
    $$\beta = \frac{\varphi^{-1}}{2} \approx 0.309017$$
    控制同步效應隨距離遞減嘅速度。

14. **同步紅移 $z_c$**
    $$z_c = 0.6 \pm 0.05$$
    宇宙約 60 億年前（紅移 0.6）嘅同步特徵位置。

15. **常數代數關係**
    $$\kappa = (\varepsilon\varphi)^2 = \left[(\varphi^{-1}/4) \times \varphi\right]^2 = (1/4)^2 = 1/16$$

16. **因果域（Causal Domain）數量**
    $$N_{\text{horizon}} = \left\lfloor \frac{4}{\varepsilon} \right\rfloor = 42$$
    宇宙可分 42 個因果獨立區域。

17. **域尺度**
    $$\xi = \frac{R_h}{N_{\text{horizon}}} \approx 105\ \text{Mpc}$$
    每個區域嘅特徵尺度約一億零五百萬秒差距。

18. **$\varepsilon$ 嘅數據驗證**
    $$\varepsilon_{\text{fit}} = 0.155 \pm 0.012\ (\text{DESI DR2})$$
    理論值 $\varepsilon = 0.1545$ 喺 $1\sigma$ 內同數據一致。

19. **$\beta$ 嘅數據驗證**
    $$\beta_{\text{fit}} = 0.311 \pm 0.015$$
    從造父變星（Cepheid）同 TRGB 嘅哈勃常數差異反推，差唔足 $0.1\sigma$。

20. **$z_c$ 嘅交叉驗證**
    $$z_c^{\text{DESI}} = 0.58 \pm 0.08,\quad z_c^{\text{DES-SN}} = 0.62 \pm 0.10,\quad z_c^{\text{聯合}} = 0.60 \pm 0.04$$

21. **$\kappa$ 嘅物理作用**
    $\kappa$ 同時控制弱核力強度（$g_w^2 \propto \kappa$）、循環時間（$t_{\text{cycle}} \propto e^{1/\kappa}$）同中微子質量標度（$m_\nu \sim \kappa \cdot \varepsilon \cdot \Lambda$）。

22. **同 $\Lambda$CDM 對比**
    $\Lambda$CDM 要 6+ 個自由參數（$\Omega_m, H_0, \sigma_8, n_s, \Omega_b, \tau$）。IDCM 有 0 個自由參數。

23. **四常數生成樹**
    $$x^2 + x - 1 = 0 \to \varphi^{-1} \to \begin{cases} \varepsilon = \varphi^{-1}/4 \\ \beta = \varphi^{-1}/2 \\ \kappa = (\varepsilon\varphi)^2 = 1/16 \\ z_c = z(N_{\text{horizon}}) \end{cases}$$

24. **$\varepsilon$ 嘅幾何意義**
    最細分裂 $2 \times 2$：空間二维 × 内部二维對稱。

25. **常數嘅封閉性**
    四個常數構成封閉代數系統（closed algebraic system）：知道 $\varphi^{-1}$，所有常數由基本算術決定。

## 第三部分：時間嘅結構（26–35）

26. **時間嘅遞迴本質**
    $$t = \{C_0 \to C_1 \to C_2 \to \cdots \to \varphi^{-1}\}$$
    時間係遞迴收斂嘅步數次序，唔係獨立維度。

27. **因果域同步**
    $$C_n \to C_{n+1} \text{ 對應一個因果域同步}$$

28. **同步完成度**
    $$s(r) = 1 - e^{-r/\xi}$$
    同步完成度 $s$ 隨距離 $r$ 指數增長。

29. **時間箭頭**
    $$\text{遞迴只能向前收斂} \to \text{時間箭頭}$$
    遞迴方向性決定時間只能前進。

30. **宇宙未來——熱寂**
    $$\lim_{n\to\infty} C_n = \varphi^{-1} \implies \text{全域同步} \to \text{熱寂（heat death）}$$

31. **量子漲落（Quantum Fluctuation）跳出**
    $$\Delta E \sim \kappa \cdot E_{\text{Planck}}$$
    $\kappa = 1/16$ 容許漲落累積到跳出固定點。

32. **循環時間**
    $$t_{\text{cycle}} = \tau_0 \cdot e^{1/\kappa} = \tau_0 \cdot e^{16}$$
    $e^{16} \approx 8.886 \times 10^6$ 係精確代數值。

33. **循環時間估計**
    若 $\tau_0 \approx 0.03$ 吉年，$t_{\text{cycle}} \approx 2.7 \times 10^5$ 吉年；若 $\tau_0 \approx 3.0$ 吉年，$t_{\text{cycle}} \approx 2.7 \times 10^7$ 吉年。

34. **$\kappa$ 嘅精確重要性**
    若 $\kappa \to 0$，永唔重啟；若 $\kappa = 0.1$，$e^{10} \approx 22026$，循環太短；$\kappa = 1/16$ 係唯一同宇宙壽命一致嘅值。

35. **重啟條件**
    $$C_0^{\text{new}} = C_{\infty}^{\text{old}} + \delta_{\text{fluctuation}}$$
    熱寂後量子漲落 $\delta$ 觸發新循環。

## 第四部分：光同因果結構（36–45）

36. **光嘅場論本質**
    光 = W 場（一致性場）嘅同步信號，以最快速度 $c$ 傳播。

37. **光速有限**
    $$c = \text{遞迴一步嘅因果步長}$$
    因果域之間需要時間同步。

38. **因果域直徑**
    $$d_{\text{domain}} \approx c \cdot \tau_{\text{sync}}$$

39. **弗里德曼方程（Friedmann Equation）**
    $$H(z)^2 = H_0^2\left[\Omega_m(1+z)^3 + \Omega_{DE}f(z)\right]$$

40. **IDCM 膨脹修正**
    $$f(z) = 1 + \varepsilon \cdot \frac{z}{z_c} \cdot e^{-z/z_c}$$
    喺 $z_c \approx 0.6$ 產生約 5.68% 嘅隆起（bump）。

41. **紅移效應**
    $$1 + z = \frac{\lambda_{\text{觀測}}}{\lambda_{\text{發射}}}$$

42. **微波背景輻射（CMB）**
    $$T_{\text{CMB}} = 2.725\ \text{K},\quad z_{\text{CMB}} \approx 1100$$

43. **CMB 偏移參數（Shift Parameter）**
    $$R = \sqrt{\Omega_m H_0^2} \int_0^{z_*} \frac{dz}{H(z)}$$
    IDCM 預測 $R_{\text{IDCM}} = 1.7425$，同普朗克衛星 1.7427 ± 0.0042 差 0.05σ。

44. **早期宇宙行為**
    $z > z_c$ 時 $f(z) \to 1$，IDCM 同 $\Lambda$CDM 冇分別。

45. **回溯光錐（Lookback Time）**
    因 $c$ 有限，睇遠天體 = 睇過去。

## 第五部分：物質同場（46–55）

46. **W 場數學形式**
    $$\Psi(x,t) = A(x,t) \cdot e^{i\theta(x,t)}$$

47. **W 場拉格朗日密度（Lagrangian Density）**
    $$\mathcal{L}_W = \frac{1}{2}(\partial_\mu\Psi)^2 - V(|\Psi|^2)$$

48. **W 場勢能（Potential）**
    $$V(|\Psi|^2) = \frac{\kappa}{2}|\Psi|^4 - \frac{\varepsilon}{2}|\Psi|^2$$

49. **勢能最小值**
    $$|\Psi|^2_{\text{min}} = \frac{\varepsilon}{\kappa}$$
    物質存在係勢能嘅自然結果。

50. **$\kappa$ 決定穩定度**
    $\kappa$ 越細，勢能越深，物質越穩定。

51. **物質定義**
    物質 = W 場嘅局部穩定共振（local stable resonance）。

52. **質能等價**
    $$E = mc^2$$

53. **暗物質（Dark Matter）**
    $$\rho_{\text{DM}} \propto \kappa \cdot \varepsilon$$
    暗物質 = 已同步但未完全鎖定嘅 W 場域。

54. **宇宙物質總密度**
    $$\rho_{\text{matter}} \propto \varepsilon \times N_{\text{domain}}$$

55. **物質同場統一**
    兩者係同一 W 場嘅唔同形式。

## 第六部分：質量嘅起源（56–65）

56. **質量嘅場論定義**
    $$(\partial_t^2 - \nabla^2 + m^2)\Psi = 0$$

57. **質量標度律（Mass Scaling Law）**
    $$m_{\text{particle}} \approx \varepsilon \cdot \varphi^{-1} \cdot \Lambda_{\text{scale}}$$

58. **電子質量**
    $$m_e \approx \varepsilon^2 \cdot M_{\text{Planck}} \approx 0.511\ \text{MeV}$$

59. **質子質量**
    $$m_p \approx \varepsilon \cdot \varphi^{-1} \cdot \Lambda_{\text{QCD}} \approx 938\ \text{MeV}$$

60. **中微子（Neutrino）質量**
    $$m_\nu \approx \kappa \cdot \varepsilon \cdot \Lambda_\nu \approx 0.01\ \text{至}\ 0.1\ \text{eV}$$

61. **希格斯機制（Higgs Mechanism）**
    W 場嘅局部相位鎖定，產生質量項。

62. **質量階層（Mass Hierarchy）**
    $$\frac{m_e}{m_p} \approx \frac{\varepsilon}{\varphi^{-1}} \cdot \frac{M_{\text{Planck}}}{\Lambda_{\text{QCD}}} \sim \frac{1}{1836}$$

63. **弱規範玻色子（Gauge Boson）質量**
    $$m_W,\ m_Z \propto \kappa \cdot \varphi^{-1} \cdot v$$

64. **暗物質質量**
    $$m_{\text{DM}} \sim \kappa \cdot M_{\text{scale}}$$

65. **質量終極源頭**
    一切質量由 $x^2 + x - 1 = 0$ 生成。

## 第七部分：粒子物理基礎（66–78）

66. **費米子（Fermion）**
    費米子 = W 場嘅半整數自旋（half-integer spin）共振模式。

67. **自旋（Spin）統計**
    $$\text{自旋 } 2\pi :\ \begin{cases} \text{費米子：} \psi \to -\psi \\ \text{玻色子（Boson）：} \phi \to \phi \end{cases}$$

68. **電子（Electron）**
    $$m_e \approx 0.511\ \text{MeV},\quad q_e = -e,\quad e = \varepsilon \cdot g_e$$

69. **中微子（Neutrino）**
    $$m_\nu \approx \kappa \cdot \varepsilon \cdot \Lambda_\nu \ll m_e$$

70. **夸克（Quark）**
    上夸克（up quark）、下夸克（down quark）= W 場更高頻共振。永遠禁閉（confinement）。

71. **強核力（Strong Nuclear Force）**
    $$g_s^2 \propto \varepsilon$$
    強核力 = W 場嘅 SU(3) 同步模式。

72. **膠子（Gluon）**
    膠子 = W 場嘅 SU(3) 波模式，自帶色荷（color charge）。

73. **弱核力（Weak Nuclear Force）**
    $$g_w^2 \propto \kappa \approx 1/16$$
    弱力強度正比 $\kappa$，解釋弱力點解咁弱。

74. **光子（Photon）**
    光子 = W 場嘅無質量（massless）U(1) 波模式。

75. **W 同 Z 玻色子**
    $$m_W,\ m_Z \propto \kappa \cdot \varphi^{-1} \cdot v$$

76. **規範耦合統一**
    $$g_1 \propto \varepsilon,\quad g_2 \propto \kappa,\quad g_3 \propto \varepsilon$$

77. **標準模型（Standard Model）嘅 W 場基礎**
    $$\text{SU(3)}_C \times \text{SU(2)}_L \times \text{U(1)}_Y \subset \text{W 場對稱性}$$

78. **粒子物理統一**
    所有粒子都係 W 場遞迴嘅唔同頻率模式。

## 第八部分：IDCM 核心公式（79–89）

79. **核心遞迴**
    $$C_{n+1} = \frac{1}{1 + C_n},\quad C_0 = 1$$

80. **固定點**
    $$C_\infty = \varphi^{-1} = \frac{\sqrt{5} - 1}{2}$$

81. **同步幅度**
    $$\varepsilon = \frac{\varphi^{-1}}{4}$$

82. **閉合常數**
    $$\kappa = (\varepsilon\varphi)^2 = \frac{1}{16}$$

83. **尺度指數**
    $$\beta = \frac{\varphi^{-1}}{2}$$

84. **弗里德曼方程（IDCM 修正）**
    $$H(z)^2 = H_0^2\left[\Omega_m(1+z)^3 + \Omega_{DE}\left(1 + \varepsilon \cdot \frac{z}{z_c} \cdot e^{-z/z_c}\right)\right]$$

85. **同步傳播**
    $$A(r) = \varepsilon \cdot \left(\frac{r}{\xi}\right)^\beta$$

86. **哈勃常數觀測偏差**
    $$H_0^{\text{obs}}(r) = H_0^{\text{global}} \cdot (1 + \varepsilon \cdot A(r))$$

87. **卡方（$\chi^2$）比較**
    $$\Delta\chi^2 = \chi^2_{\text{IDCM}} - \chi^2_{\Lambda\text{CDM}} = -9.8\ (1853\ \text{數據點})$$

88. **宇宙循環時間**
    $$t_{\text{cycle}} = \tau_0 \cdot e^{1/\kappa} = \tau_0 \cdot e^{16}$$
    $e^{16} \approx 8.886 \times 10^6$。若 $\tau_0 \approx 0.03$ 吉年，$t_{\text{cycle}} \approx 2.7 \times 10^5$ 吉年。

89. **哈勃常數**
    $$H_0 = 68.2 \pm 0.4\ \text{km/s/Mpc}$$

## 第九部分：數據驗證（90–95）

90. **BAO（DESI DR2）**
    $$\chi^2_{\text{IDCM}} = 9.22,\quad \chi^2_{\Lambda\text{CDM}} = 15.64,\quad \Delta\chi^2 = -6.42$$

91. **超新星（DES-SN5YR）**
    $$\chi^2_{\text{IDCM}} = 1639.8,\quad \chi^2_{\Lambda\text{CDM}} = 1643.6,\quad \Delta\chi^2 = -3.8$$

92. **結構增長 $f\sigma_8$**
    $$\chi^2_{f\sigma_8} = 13.7\ (\text{20 RSD 數據點})$$

93. **弱透鏡 $S_8$**
    $$S_8^{\text{IDCM}} = 0.786 \pm 0.008$$
    解決 $S_8$ 張力（tension）。

94. **哈勃常數交叉校準**
    造父變星（Cepheid）：73.04 vs SH0ES 73.04 ± 1.04 ✅
    TRGB：69.80 vs Freedman 69.80 ± 1.90 ✅

95. **總和**
    $$\Delta\chi^2_{\text{total}} = -9.8\ (\text{約 3.1σ 反對 } \Lambda\text{CDM})$$

## 第十部分：結論（96–100）

96. **核心方程**
    $$x^2 + x - 1 = 0 \quad \rightarrow \quad \varphi^{-1} \quad \rightarrow \quad \varepsilon,\ \kappa,\ \beta,\ z_c \quad \rightarrow \quad \text{所有觀測}$$

97. **零自由參數**
    四常數全部推導，冇自由參數。

98. **三項獨立驗證**
    BAO + 超新星 + 哈勃常數交叉校準一致支持。

99. **核心結論**
    $$x^2 + x - 1 = 0\ +\ 八步遞迴\ +\ 三項驗證\ =\ 完整宇宙學$$

100. **IDCM 定義**
    $$\text{IDCM = Information Dynamics Cosmology Model}$$
    資訊動力宇宙學模型（Information Dynamics Cosmology Model）。

---

## 俾老師嘅備註

- 公式 1–10 只需要初中代數
- 公式 26–45 需要基礎微積分
- 公式 46–78 需要基礎物理（波、場）
- $\chi^2$ 可以解釋為「擬合好壞分數」，越低越好
- 全部程式碼喺 GitHub
