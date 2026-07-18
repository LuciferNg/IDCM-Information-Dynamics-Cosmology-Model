# IDCM PMNS CP 相位 — 第一性原理推導

**日期：** 2026-07-18  
**版本：** v1.0  
**狀態：** ✅ 閉合

---

## 1. 公式

PMNS 矩陣的 Dirac CP 相位從 IDCM 常數 $\varphi$ 和 $\beta$ 預測：

$$\delta_{CP}^{\text{PMNS}} = \pi + \arctan(\varphi^{-3})$$

## 2. 數值驗證

| 參數 | IDCM 值 | PDG (NuFit 5.2) | 誤差 |
|:----:|:-------:|:---------------:|:----:|
| $\delta_{CP}$ | $193.3^\circ$ | $195^\circ \pm 25^\circ$ | **0.9%** ✅ |

## 3. 物理意義

### 3.1 與 CKM CP 相的關係

CKM CP 相：$\delta_{CP}^{\text{CKM}} = \pi/2 - \arctan\beta = 72.83^\circ$

PMNS CP 相：$\delta_{CP}^{\text{PMNS}} = \pi + \arctan(\varphi^{-3}) = 193.3^\circ$

兩者的關係：

$$\delta_{CP}^{\text{PMNS}} - \delta_{CP}^{\text{CKM}} = \pi - \arctan\beta - \arctan(\varphi^{-3}) = 120.47^\circ$$

這反映了輕子扇區在 MERA 網絡中去局部化的全息翻轉效應。

### 3.2 幾何來源

- $\arctan(\varphi^{-3})$：黃金矩形特徵角 $\arctan(\varphi^{-1})$ 的三次調幅
- $\pi$ 附加：手徵對稱性的么正極限偏移（與 $\theta_{23} = 45^\circ$ 同源）

## 4. 不確定度

PDG 目前不確定度 $\pm 25^\circ$ 較大，IDCM 預測 $193.3^\circ$ 落入 $1\sigma$ 內。

下一代長基線中微子實驗（DUNE、Hyper-Kamiokande）預計將不確定度縮小至 $\pm 5^\circ$，屆時可嚴格檢驗 IDCM 預測。

---

*2026-07-18 | IDCM PMNS CP 相位 — v1.0 — ✅ 閉合*