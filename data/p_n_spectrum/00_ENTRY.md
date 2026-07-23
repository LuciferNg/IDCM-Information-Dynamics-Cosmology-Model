# P_n Spectrum — 入口

**日期：** 2026-07-21
**框架：** IDCM v5.0（統一 P_n formula）
**位置：** `data/p_n_spectrum/`

## Purpose

系統性計算 P_n 公式的完整光譜（n=0 到 n=6），檢驗每個 n 的物理對應，標註閉合/開放狀態。

## P_n Formula

$$
P_n = \tau([H,P_\kappa]@W^\dagger W) \times \left(\frac{\kappa^2}{16\pi^2}\right)^n \times \frac{\sin^2\theta(\lambda)}{\lambda} \times M_{Pl}^2
$$

| 符號 | 值 | 含義 |
|:----|:---|:-----|
| $\kappa$ | $1/16$ | 4-body tensor contraction |
| $\kappa^2/(16\pi^2)$ | $2.473662 \times 10^{-5}$ | 每 loop factor |
| $M_{Pl}$ | $1.220890 \times 10^{19}$ GeV | Planck mass |

## 已知閉合點

| n | 物理 | 狀態 | 依據 |
|:-:|:-----|:----:|:-----|
| 0 | Consciousness (C formula) | ✅ | `C = |τ([H,P_κ]@WW†)|` |
| 6 | Neutrino mass (~0.05 eV) | ✅ | 6-loop, replaced seesaw |

## 未知 n=1–5 光譜

這組文件計算每個 n 的 energy scale 並評估其物理意義。

---

**下一份：** `01_P0_consciousness.md`
