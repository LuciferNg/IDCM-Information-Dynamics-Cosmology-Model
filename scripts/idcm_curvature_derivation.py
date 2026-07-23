#!/usr/bin/env python3
"""IDCM 曲率半徑下限推導 — 數值驗證"""
import numpy as np
from math import sqrt

# === IDCM constants ===
phi = (1 + sqrt(5))/2
phi_inv = phi - 1
kappa = 1/16
epsilon = phi_inv/4
beta = phi_inv/2
C_star = phi_inv

# === Observational constants ===
H0 = 67.4  # km/s/Mpc (Planck 2018)
c = 299792.458  # km/s
cH0_Mpc = c / H0  # Mpc
cH0_Gpc = cH0_Mpc / 1000  # Gpc

print("=" * 65)
print("IDCM 曲率半徑下限推導 — 數值驗證")
print("=" * 65)

print(f"\nIDCM 基本常數:")
print(f"  φ  = {phi:.15f}")
print(f"  φ⁻¹ = {phi_inv:.15f}")
print(f"  κ  = {kappa}")
print(f"  ε  = {epsilon:.15f}")
print(f"  κ×ε = {kappa*epsilon:.15e}")
print(f"  H₀ = {H0} km/s/Mpc")
print(f"  c/H₀ = {cH0_Gpc:.4f} Gpc")

# ============================================================
print("\n" + "=" * 65)
print("【推導 A】κ×ε 乘積 — IDCM 第一原理")
print("=" * 65)

Omega_A = (kappa * epsilon) ** 2
R_A_Gpc = cH0_Gpc / sqrt(Omega_A)
R_A_ly = R_A_Gpc * 3.26156e9

print(f"\n  |Ω_k| = (κ×ε)² = ({kappa} × {epsilon:.4f})²")
print(f"       = {Omega_A:.6e}")
print(f"       = (φ⁻¹)²/4096 = {phi_inv**2:.6f}/4096")

print(f"\n  R_curv > c/(H₀ × κε)")
print(f"         = {cH0_Gpc:.4f} / √({Omega_A:.6e})")
print(f"         = {cH0_Gpc:.4f} / {sqrt(Omega_A):.6f}")
print(f"         = {R_A_Gpc:.2f} Gpc")
print(f"         = {R_A_ly:.4e} light-years")
print(f"         ≈ {R_A_ly/1e12:.4f} 萬億光年")
print(f"  = (64/φ⁻¹) × c/H₀ = {64/phi_inv:.4f} × {cH0_Gpc:.4f} Gpc")

# ============================================================
print("\n" + "=" * 65)
print("【推導 B】CFAS 版本")
print("=" * 65)

Omega_B = 1e-4
R_B_Gpc = cH0_Gpc / sqrt(Omega_B)
R_B_ly = R_B_Gpc * 3.26156e9

print(f"\n  |Ω_k| < {Omega_B:.0e} (CFAS, from κ=1/16 precision)")
print(f"  R_curv > {R_B_Gpc:.2f} Gpc = {R_B_ly:.4e} ly")
print(f"         ≈ {R_B_ly/1e12:.4f} 萬億光年")
print(f"  = 100 × c/H₀ (exact scaling)")

# ============================================================
print("\n" + "=" * 65)
print("【推導 C】從 Sync Dip ε 精度")
print("=" * 65)

N_h = 44
d_H_zc = 5.0  # Gpc, horizon at z_c ≈ 0.6
eps_err = 0.01
eps_pred = epsilon

delta = eps_err / eps_pred
R_C_Gpc = d_H_zc / sqrt(2 * delta)
R_C_ly = R_C_Gpc * 3.26156e9

print(f"\n  ε = {eps_pred:.4f} (predicted), observed ±{eps_err}")
print(f"  (d_H/R_curv)² < 2×δε/ε = {2*delta:.4f}")
print(f"  R_curv > d_H(z_c)/√(2δε/ε) = {R_C_Gpc:.2f} Gpc")
print(f"  → 不是主要曲率探針 (bound 太弱)")

# DESI future
eps_err_f = 0.005
R_fut = d_H_zc / sqrt(2 * eps_err_f / eps_pred)
print(f"  DESI DR2 (±0.005): R_curv > {R_fut:.1f} Gpc (仍弱)")

# ============================================================
print("\n" + "=" * 65)
print("【推導 D】Planck 2018 交叉檢驗")
print("=" * 65)

Ok_mean = 0.001
Ok_err = 0.002
Ok_95 = Ok_mean + 2 * Ok_err
R_D_Gpc = cH0_Gpc / sqrt(Ok_95)
R_D_ly = R_D_Gpc * 3.26156e9

print(f"\n  Planck 2018: Ω_k = {Ok_mean} ± {Ok_err}")
print(f"  95% CL: |Ω_k| < {Ok_95}")
print(f"  R_curv > {R_D_Gpc:.2f} Gpc = {R_D_ly:.4e} ly")
print(f"  IDCM vs Planck: {(Omega_A-Ok_mean)/Ok_err:.2f}σ 差別")
print(f"  → IDCM 預測 ({Omega_A:.1e}) < Planck 誤差")

# ============================================================
print("\n" + "=" * 65)
print("【推導 E】κ×ε×√N_horizon — 域結構完整 bound")
print("=" * 65)

Omega_E = (kappa * epsilon / sqrt(N_h)) ** 2
R_E_Gpc = cH0_Gpc / sqrt(Omega_E)
R_E_ly = R_E_Gpc * 3.26156e9

print(f"\n  |Ω_k| = (κ×ε/√N_h)² = ({kappa}×{epsilon:.4f}/√{N_h})²")
print(f"       = {Omega_E:.6e}")
print(f"\n  R_curv > {R_E_Gpc:.2f} Gpc = {R_E_ly:.4e} ly")
print(f"         ≈ {R_E_ly/1e12:.4f} 萬億光年")

# ============================================================
print("\n" + "=" * 65)
print("最終比較表")
print("=" * 65)

print(f"\n{'推導':<35} {'|Ω_k| bound':<18} {'R_curv(min)':<22} {'(萬億光年)':<15}")
print("-" * 85)
rows = [
    ("A: κ×ε (第一原理)", f"{Omega_A:.4e}", f"{R_A_Gpc:.2f} Gpc", f"{R_A_ly/1e12:.4f}"),
    ("B: CFAS (|Ω_k|<10⁻⁴)", f"{Omega_B:.0e}", f"{R_B_Gpc:.2f} Gpc", f"{R_B_ly/1e12:.4f}"),
    ("C: Sync dip ε (當前)", "N/A (弱)", f"{R_C_Gpc:.2f} Gpc", f"{R_C_ly/1e12:.4f}"),
    ("D: Planck 95% CL", f"{Ok_95:.4f}", f"{R_D_Gpc:.2f} Gpc", f"{R_D_ly/1e12:.4f}"),
    ("E: κ×ε×√N_h (完整)", f"{Omega_E:.4e}", f"{R_E_Gpc:.2f} Gpc", f"{R_E_ly/1e12:.4f}"),
]
for r in rows:
    print(f"{r[0]:<35} {r[1]:<18} {r[2]:<22} {r[3]:<15}")

print(f"\nIDCM 推薦 bound：|Ω_k| < {Omega_A:.4e}（推導A，第一原理）")
print(f"對應 R_curv > {R_A_Gpc:.1f} Gpc ≈ {R_A_ly/1e12:.4f} 萬億光年")

# === Extra: full derivation chain for display ===
print("\n" + "=" * 65)
print("完整推導鍵")
print("=" * 65)
print(f"""
κ = 1/16  (4-body sync threshold, from 2⁴ = 16)
ε = φ⁻¹/4  (sync dip depth, from recursion fixed point)

→ |Ω_k| = (κ·ε)²
        = (1/16 × φ⁻¹/4)²
        = (φ⁻¹/64)²
        = (φ⁻¹)² / 4096
        = 0.381966... / 4096
        = {Omega_A:.6e}

→ R_curv > c / (H₀ · κ·ε)
         = (64/φ⁻¹) × (c/H₀)
         = 64φ × (c/H₀)      [since φ⁻¹ = φ-1, 1/φ⁻¹ = φ]
         = 103.556 × (c/H₀)  [64φ = {64*phi:.4f}]

Final (H₀ = 67.4 km/s/Mpc):
  R_curv > {R_A_Gpc:.2f} Gpc ≈ {R_A_ly/1e12:.4f} × 10¹² ly
""")
