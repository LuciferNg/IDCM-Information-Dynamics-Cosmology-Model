"""
IDCM — Publication-quality visualisations
==========================================
Generates:
  idcm_fz_bump.png          — f(z) bump curve vs LCDM
  idcm_h0_sync_phase.png    — H0 sync phase (Cepheid/TRGB)
  idcm_recursion_conv.png   — Recursion convergence to phi^{-1}
  idcm_chi2_comparison.png  — Chi-squared bar chart
"""

import numpy as np
from math import sqrt, exp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Common constants
phi_inv = (sqrt(5) - 1) / 2
EPS = phi_inv / 4
ZC = 0.6
BETA = phi_inv / 2
XI = 105.0
H0_GLOBAL = 68.2
C = 299792.458

rc = {'axes.unicode_minus': False}
plt.rcParams.update(rc)

# ─────────────────────────────────────────────
# 1. f(z) BUMP CURVE
# ─────────────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

z = np.logspace(-2, 1.2, 500)
x = z / ZC
f_idcm = 1.0 + EPS * x * np.exp(-x)
f_lcdm = np.ones_like(z)

# Left: f(z) absolute
ax1.semilogx(z, f_idcm, '#1a5276', lw=2.5, label='IDCM')
ax1.semilogx(z, f_lcdm, '#888888', lw=1.5, ls='--', label=r'$\Lambda$CDM')
ax1.axvline(ZC, color='#c0392b', lw=1, ls=':', alpha=0.7,
            label=r'$z_c = %.1f$' % ZC)
ax1.axhline(1.0, color='#888', lw=0.5)
ax1.fill_between(z, 1.0, f_idcm, alpha=0.12, color='#1a5276',
                  label=r'+5.68% bump')
ax1.set_xlabel('Redshift z', fontsize=13)
ax1.set_ylabel(r'$f(z) = \tilde{\Omega}_\Lambda(z) / \Omega_\Lambda$', fontsize=13)
ax1.set_title('Dark Energy Density Modulation', fontsize=14, fontweight='bold')
ax1.legend(fontsize=11)
ax1.set_xlim(0.01, 15)
ax1.set_ylim(0.98, 1.08)
ax1.grid(True, alpha=0.2)

# Right: relative deviation
ax2.semilogx(z, (f_idcm - 1.0) * 100, '#1a5276', lw=2.5)
ax2.axvline(ZC, color='#c0392b', lw=1, ls=':', alpha=0.7)
ax2.axhline(0, color='#888', lw=0.5)
ax2.fill_between(z, 0, (f_idcm - 1.0) * 100, alpha=0.12, color='#1a5276')
ax2.set_xlabel('Redshift z', fontsize=13)
ax2.set_ylabel('Deviation from LCDM [%]', fontsize=13)
ax2.set_title('Relative Deviation from LCDM', fontsize=14, fontweight='bold')
peak_amp = EPS * exp(-1) * 100
ax2.text(0.02, 0.95,
         'Peak at z = %.1f\nAmplitude = %.2f%%' % (ZC, peak_amp),
         transform=ax2.transAxes, fontsize=11, va='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
ax2.set_xlim(0.01, 15)
ax2.set_ylim(-0.5, 6.5)
ax2.grid(True, alpha=0.2)

plt.tight_layout()
fig.savefig('/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/idcm_fz_bump.png',
            dpi=200, bbox_inches='tight')
plt.close()
print("OK idcm_fz_bump.png")

# ─────────────────────────────────────────────
# 2. H0 SYNC PHASE
# ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 6))

r_arr = np.logspace(np.log10(0.01), np.log10(200), 500)
A_sync = EPS * (r_arr / XI) ** BETA
H0_arr = H0_GLOBAL * (1 + A_sync)

r_data = np.array([0.05, 1.77])
h0_data = np.array([69.80, 73.05])
h0_err = np.array([1.90, 1.04])
labels = ['TRGB (Freedman)', 'Cepheid (SH0ES)']

ax.semilogx(r_arr, H0_arr, '#1a5276', lw=2.5,
            label=r'H0 sync: H0(r) = H0_g * (1 + e*(r/xi)^b)')
ax.axhline(H0_GLOBAL, color='#888', lw=1, ls='--', alpha=0.8,
           label=r'H0_global = %.1f km/s/Mpc' % H0_GLOBAL)
for i in range(2):
    ax.errorbar(r_data[i], h0_data[i], yerr=h0_err[i], fmt='o',
                color='#c0392b', ms=8, capsize=4, capthick=1.5,
                label='%s: H0 = %.1f +/- %.2f' % (labels[i], h0_data[i], h0_err[i]))

ratio_pred = (1.77 / 0.05) ** BETA
ax.annotate('Cepheid/TRGB ratio\npredicted: %.2f' % ratio_pred,
            xy=(0.3, 72), fontsize=11, ha='center',
            bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

ax.set_xlabel('Distance r [Mpc]', fontsize=13)
ax.set_ylabel(r'H0(r) [km/s/Mpc]', fontsize=13)
ax.set_title(r'H0 Sync Phase: Position-Dependent Calibration', fontsize=14, fontweight='bold')
ax.legend(fontsize=10, loc='lower right')
ax.set_xlim(0.01, 200)
ax.set_ylim(66, 76)
ax.grid(True, alpha=0.2)

plt.tight_layout()
fig.savefig('/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/idcm_h0_sync_phase.png',
            dpi=200, bbox_inches='tight')
plt.close()
print("OK idcm_h0_sync_phase.png")

# ─────────────────────────────────────────────
# 3. RECURSION CONVERGENCE
# ─────────────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

C_list = [1.0]
for _ in range(12):
    C_list.append(1 / (1 + C_list[-1]))
C_arr = np.array(C_list)
n_vals = np.arange(len(C_arr))

ax1.plot(n_vals, C_arr, 'o-', color='#1a5276', lw=2, ms=6,
         label=r'C_{n+1} = 1/(1 + C_n)')
ax1.axhline(phi_inv, color='#c0392b', lw=1.5, ls='--', alpha=0.8,
            label=r'phi^-1 = %.5f' % phi_inv)
ax1.fill_between(n_vals, phi_inv * 0.995, phi_inv * 1.005,
                 alpha=0.08, color='#c0392b', label=r'+/-0.5% band')
ax1.set_xlabel('Iteration n', fontsize=13)
ax1.set_ylabel('C_n', fontsize=13)
ax1.set_title(r'Recursion: C_{n+1} = 1/(1 + C_n)', fontsize=14, fontweight='bold')
ax1.legend(fontsize=11)
ax1.set_xlim(-0.5, 12.5)
ax1.set_ylim(0.5, 1.05)
ax1.grid(True, alpha=0.2)

err = np.abs(C_arr - phi_inv)
ax2.semilogy(n_vals, err, 'o-', color='#1a5276', lw=2, ms=6)
ax2.axhline(1e-3, color='#888', lw=1, ls=':', alpha=0.7, label=r'$10^{-3}$ (8-step)')
ax2.axhline(1e-12, color='#888', lw=1, ls=':', alpha=0.7, label=r'$10^{-12}$ (float limit)')

lam = phi_inv ** 2
n_fit = np.arange(1, 9)
ax2.plot(n_fit, err[1] * lam ** (n_fit - 1), '--', color='#c0392b', lw=1.5, alpha=0.7,
         label=r'Lyapunov: lambda^(n-1)')

ax2.set_xlabel('Iteration n', fontsize=13)
ax2.set_ylabel(r'|C_n - phi^-1|', fontsize=13)
ax2.set_title(r'Convergence: lambda = phi^-2 = %.4f < 1' % lam,
              fontsize=14, fontweight='bold')
ax2.legend(fontsize=10)
ax2.set_xlim(-0.5, 12.5)
ax2.set_ylim(1e-16, 2)
ax2.grid(True, alpha=0.2)

plt.tight_layout()
fig.savefig('/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/idcm_recursion_conv.png',
            dpi=200, bbox_inches='tight')
plt.close()
print("OK idcm_recursion_conv.png")

# ─────────────────────────────────────────────
# 4. CHI-SQUARED COMPARISON (DES-SN5YR MCMC)
# ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 5.5))

datasets = ['DESI DR2\nBAO', 'Planck\nCMB', 'DES-SN5YR\n(1820 SNe)', 'H(z)\ncompilation']
chi2_idcm = [15.8, 1.1, 1638.9, 25.5]
chi2_lcdm = [20.6, 6.1, 1641.3, 23.2]
x = np.arange(len(datasets))
w = 0.30

bars1 = ax.bar(x - w/2, chi2_idcm, w, color='#1a5276', alpha=0.85,
               label='IDCM', edgecolor='white', linewidth=0.5)
bars2 = ax.bar(x + w/2, chi2_lcdm, w, color='#888888', alpha=0.6,
               label=r'LCDM', edgecolor='white', linewidth=0.5)

y_max_total = max(max(chi2_idcm), max(chi2_lcdm))
for i in range(len(datasets)):
    delta = chi2_lcdm[i] - chi2_idcm[i]
    sign = '+' if delta > 0 else ''
    y_max = max(chi2_idcm[i], chi2_lcdm[i])
    ax.annotate(r'D = %s%.1f' % (sign, delta),
                xy=(i, y_max + y_max_total * 0.02),
                ha='center', fontsize=11, fontweight='bold',
                color='#1a5276' if delta > 0 else '#c0392b')

ax.set_ylabel(r'chi^2', fontsize=14)
ax.set_title('IDCM vs LCDM: Likelihood Contributions', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(datasets, fontsize=12)
ax.legend(fontsize=12)
ax.grid(True, alpha=0.2, axis='y')

chi2_total_idcm = sum(chi2_idcm)
chi2_total_lcdm = sum(chi2_lcdm)
delta_total = chi2_total_lcdm - chi2_total_idcm
fig.text(0.15, 0.01,
         'Total chi2: IDCM = %.1f  |  LCDM = %.1f  |  Dchi2 = %.1f  |  1869 dof  |  ~3.2sigma' %
         (chi2_total_idcm, chi2_total_lcdm, delta_total),
         fontsize=12, ha='left', fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.subplots_adjust(bottom=0.15)
fig.savefig('/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data/idcm_chi2_comparison.png',
            dpi=200, bbox_inches='tight')
plt.close()
print("OK idcm_chi2_comparison.png")

print("\nAll 4 figures generated.")
