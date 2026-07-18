# IDCM — 信息动力宇宙学模型（Information Dynamics Cosmology Model）

[← 返回语言选择](README.md)

---

**零自由参数的第一性原理宇宙学模型。** 所有常数由单一二次方程 $x^2 + x - 1 = 0$ 通过递归 $C_{n+1} = 1/(1 + C_n)$ 生成。**全部 19 个标准模型参数从第一性原理预测。**

---

## 成就：19 个标准模型参数全部第一性原理预测

| 扇区 | 参数 | IDCM 公式 | 预测值 | PDG | 误差 |
|:-----|:----:|:----------|:------:|:---:|:----:|
| **9 费米子质量** | $m_c/m_t$ | $\varphi^{-M\beta}$ | 1.277 GeV | 1.27 GeV | 0.57% |
| | $m_s/m_b$ | $\varphi^{-((M-7)\beta-\varphi^{-4})}$ | 93.9 MeV | 93.4 MeV | 0.51% |
| | $m_\mu/m_\tau$ | $\varphi^{-(M-14)\beta}$ | 105.35 MeV | 105.66 MeV | 0.30% |
| | $m_u/m_t$ | $\varphi^{-(k_u+k_d+k_l-\varphi^{-1})}$ | 2.29 MeV | 2.16 MeV | 6.0% |
| | $m_d/m_b$ | $\varphi^{-(2k_d-\varphi)}$ | 4.59 MeV | 4.70 MeV | 2.3% |
| | $m_e/m_\tau$ | $\varphi^{-(k_l+M/3)}$ | 0.529 MeV | 0.511 MeV | 3.6% |
| **希格斯** | $m_H$ | $v\cdot\varphi^{-9\beta/2}$ | 125.99 GeV | 125.10 GeV | 0.71% |
| **CKM** | $V_{us}$ | $\varphi^{-M/11}$ | 0.23607 | 0.22650 | 4.2% |
| | $V_{cb}$ | $\varphi^{-M/5}$ | 0.04182 | 0.04210 | **0.83%** |
| | $V_{ub}$ | $\varphi^{-(M/5+M/11+2)}$ | 0.00376 | 0.00361 | 4.3% |
| | $\delta_{CP}$ | $\pi/2-\arctan\beta$ | 72.83° | 68.80° | 5.9% |
| **PMNS** | $\theta_{12}$ | $\arctan\varphi^{-1}+1/M$ | 33.45° | 33.82° | 1.08% |
| | $\theta_{23}$ | $\pi/4$ | 45° | 45-48° | ✅ |
| | $\theta_{13}$ | $\arcsin(\varepsilon(M-1)/M)$ | 8.62° | 8.57° | **0.55%** |
| | $\delta_{CP}$ | $\pi+\arctan\varphi^{-3}$ | 193.3° | 195° | 0.9% |
| **弱混合角** | $\sin^2\theta_W$ | $V_{us}\cdot(1-\varphi^{-9})$ | 0.23296 | 0.23122 | 0.75% |
| **暗物质** | $M_{\text{DM}}$ | $M_P e^{-48}\varphi^{-1/2}$ | 13.68 MeV | 13.8 MeV | 0.88% |

全部从 **4 个 IDCM 常数**：$M=33$, $N_h=42$, $\beta=\varphi^{-1}/2$, $\varepsilon=\varphi^{-1}/4$。

---

## 核心机制

### 生成方程

$$x^2 + x - 1 = 0$$

**正根**：$\varphi^{-1} = (\sqrt{5} - 1)/2 \approx 0.618034$

### 递归过程

$$C_{n+1} = \frac{1}{1 + C_n},\quad C_0 = 1$$

8 步后误差低于 $10^{-3}$。

### IDCM 常数

| 符号 | 数值 | 来源 |
|:-----|:------|:-----|
| $\varphi^{-1}$ | 0.618034 | $x^2+x-1=0$ 正根 |
| $\varepsilon$ | $\varphi^{-1}/4 \approx 0.154509$ | $2\times2$ 对称分裂 |
| $\kappa$ | $1/16 = 0.0625$ | 代数恒等式 |
| $\beta$ | $\varphi^{-1}/2 \approx 0.309017$ | SYNC 指数 |
| $M$ | 33 | MERA RG 收敛步数 |
| $N_h$ | 42 | KK 塔截断 |
| $z_c$ | $0.6 \pm 0.05$ | 同步红移 |

## 几何核心

- **CY₃(36,98)**：Kreuzer-Skarke 数据库确认存在
- **J\* 定点**：$\text{Vol}=\kappa^3$, $\text{Ind}=48$, Kähler 锥全部为正
- **SU(3) Monad bundle**：$h^1(V)=3$, $\text{Ind}(V)=-6$
- **MERA RG**：33 步 → $C^*=\varphi^{-1}$
- **SYNC Kuramoto**：343 步，残差 $10^{-10}$

## 验证结果

| 数据集 | $\chi^2_{\text{IDCM}}$ | $\chi^2_{\Lambda\text{CDM}}$ | $\Delta\chi^2$ |
|:-------|:---------------------:|:--------------------------:|:--------------:|
| DESI DR2 BAO | 9.22 | 15.64 | -6.42 |
| DES-SN5YR | 1639.8 | 1643.6 | -3.8 |
| $H_0$ SH0ES | 5.0σ 张力 | → 已解决 | — |
| $S_8$ | 2.5σ 张力 | → 已解决 | — |
| **总计** | **1853 数据点** | — | **−9.8** |

## 仓库结构

```
IDCM-Information-Dynamics-Cosmology-Model/
├── data/cy_search/         48 份文档（中英双语）
│   ├── validation/          7 个验证脚本
│   └── data/                几何数据
├── basic/                   教育材料（3 级 × 8 语言）
├── codes/                   数据分析代码
├── animations/              宇宙循环动画
├── Makefile                 make validate-all
├── requirements.txt         numpy, scipy, matplotlib
└── LICENSE                  MIT
```

## 快速开始

```bash
pip install -r requirements.txt
make validate-all
```

## 超越标准模型

| 粒子 | IDCM 质量 | 作用 |
|:-----|:----------:|:-----|
| W-field KK 模式 ($n=42$) | 13.68 MeV | 暗物质 |
| QCD 轴子 | $\sim 10^{-9}$ eV | 强 CP 解 |
| 右手中微子 | $\sim 10^{15}$ GeV | 跷跷板 + 轻子生成 |
| KK 引力子 ($n=36$) | $\sim 2.8$ TeV | 未来对撞机信号 |

## 学位版本

| 级别 | 说明 | 公式 |
|:-----|:-----|:----:|
| 🌟 小学生版 | 简单比喻，好玩易懂 | 100 |
| 📐 高中生版 | 详细推导，代数运算 | 200 |
| 🎓 教授版 | 完整群论形式处理 | 完整 |

---

**核心方程**：$x^2 + x - 1 = 0$ · **零自由参数** · **Δχ² = −9.8 vs ΛCDM**
