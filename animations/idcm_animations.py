"""
IDCM — Animated GIFs
=====================
Generates 4 publication-quality GIFs:
  1. idcm_recursion.gif       — Recursion convergence to phi^{-1}
  2. idcm_h0_sync_phase.gif   — H0 sync phase scan
  3. idcm_fz_bump.gif         — f(z) bump scan over redshift
  4. idcm_cosmic_cycle.gif    — Cosmic heat-death-restart cycle
"""

import numpy as np
from math import sqrt, exp, log10, pi
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

OUT = '/home/wsl/IDCM/IDCM-Information-Dynamics-Cosmology-Model/data'

# Shared constants
phi = (1 + sqrt(5)) / 2
phi_inv = (sqrt(5) - 1) / 2
EPS = phi_inv / 4
ZC = 0.6
BETA = phi_inv / 2
XI = 105.0
H0_GLOBAL = 68.2
KAP = 1.0 / 16.0
C_LIGHT = 299792.458

# ════════════════════════════════════════════
# ANIMATION 1: Recursion Convergence
# ════════════════════════════════════════════
print("Generating idcm_recursion.gif ...")
C_list = [1.0]
for _ in range(12):
    C_list.append(1 / (1 + C_list[-1]))
C_arr = np.array(C_list)
n_vals = np.arange(len(C_arr))
err_arr = np.abs(C_arr - phi_inv)

fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

def init_rec():
    for ax in [ax1, ax2]:
        ax.clear()
    ax1.set_xlabel('Iteration n', fontsize=12)
    ax1.set_ylabel('C_n', fontsize=12)
    ax1.set_title(r'Recursion: $C_{n+1}=1/(1+C_n)$', fontsize=13, fontweight='bold')
    ax1.set_xlim(-0.5, 12.5)
    ax1.set_ylim(0.48, 1.05)
    ax1.grid(True, alpha=0.2)
    ax1.axhline(phi_inv, color='#c0392b', lw=1.5, ls='--', alpha=0.8,
                label=r'$\varphi^{-1} \approx 0.61803$')
    ax1.legend(fontsize=10, loc='upper right')
    
    ax2.set_xlabel('Iteration n', fontsize=12)
    ax2.set_ylabel(r'$|C_n - \varphi^{-1}|$', fontsize=12)
    ax2.set_title('Convergence (log scale)', fontsize=13, fontweight='bold')
    ax2.set_xlim(-0.5, 12.5)
    ax2.set_ylim(1e-16, 2)
    ax2.grid(True, alpha=0.2)
    ax2.axhline(1e-3, color='#888', lw=1, ls=':', alpha=0.6, label=r'$10^{-3}$')
    ax2.axhline(1e-12, color='#888', lw=1, ls=':', alpha=0.6, label=r'$10^{-12}$')
    # Lyapunov reference line
    lam = phi_inv ** 2
    n_fit = np.arange(1, 9)
    ax2.plot(n_fit, err_arr[1] * lam ** (n_fit - 1), '--', color='#c0392b',
             lw=1.2, alpha=0.5, label=r'$\lambda^{n-1}$')
    ax2.legend(fontsize=9, loc='lower left')
    return []

def animate_rec(frame):
    for ax in [ax1, ax2]:
        ax.clear()
    # Re-init
    ax1.set_xlim(-0.5, 12.5); ax1.set_ylim(0.48, 1.05)
    ax1.grid(True, alpha=0.2); ax1.set_xlabel('Iteration n', fontsize=12)
    ax1.set_ylabel('$C_n$', fontsize=12)
    ax1.set_title(r'Recursion: $C_{n+1}=1/(1+C_n)$', fontsize=13, fontweight='bold')
    ax1.axhline(phi_inv, color='#c0392b', lw=1.5, ls='--', alpha=0.8,
                label=r'$\varphi^{-1} \approx 0.61803$')
    
    ax2.set_xlim(-0.5, 12.5); ax2.set_ylim(1e-16, 2)
    ax2.grid(True, alpha=0.2); ax2.set_xlabel('Iteration n', fontsize=12)
    ax2.set_ylabel(r'$|C_n - \varphi^{-1}|$', fontsize=12)
    ax2.set_title('Convergence (log)', fontsize=13, fontweight='bold')
    ax2.axhline(1e-3, color='#888', lw=1, ls=':', alpha=0.6)
    ax2.axhline(1e-12, color='#888', lw=1, ls=':', alpha=0.6)
    lam = phi_inv ** 2
    n_fit = np.arange(1, 9)
    ax2.plot(n_fit, err_arr[1] * lam ** (n_fit - 1), '--', color='#c0392b',
             lw=1.2, alpha=0.4, label=r'Lyapunov $\lambda^{n-1}$')
    ax2.legend(fontsize=9, loc='lower left')
    
    n_show = min(frame + 1, 13)
    c = C_arr[:n_show]
    n = n_vals[:n_show]
    
    # Color: past → present gradient
    colors = plt.cm.Blues(np.linspace(0.3, 0.85, len(n)))
    
    ax1.plot(n, c, 'o-', color='#1a5276', lw=1.5, ms=5, zorder=2)
    for i in range(len(n)):
        ax1.plot(n[i], c[i], 'o', color=colors[i], ms=7, zorder=3)
    
    # Error plot
    e = err_arr[:n_show]
    ax2.semilogy(n, e, 'o-', color='#1a5276', lw=1.5, ms=5)
    for i in range(len(n)):
        ax2.semilogy(n[i], e[i], 'o', color=colors[i], ms=7, zorder=3)
    
    # Iteration counter
    ax1.text(0.98, 0.05, 'n = %d' % frame, transform=ax1.transAxes,
             fontsize=14, fontweight='bold', ha='right',
             bbox=dict(facecolor='white', alpha=0.7))
    
    if frame == 8:
        ax1.axhline(phi_inv, color='#c0392b', lw=2, ls='--', alpha=0.8,
                    label=r'$\varphi^{-1} \approx 0.61803$')
        ax1.text(0.98, 0.12, '8-step convergence!', transform=ax1.transAxes,
                 fontsize=11, ha='right', color='#c0392b', fontweight='bold')
    
    ax1.legend(fontsize=10, loc='upper right')
    return []

anim1 = FuncAnimation(fig1, animate_rec, frames=13, init_func=init_rec, blit=False, repeat=True)
anim1.save(OUT + '/idcm_recursion.gif', writer=PillowWriter(fps=2))
plt.close(fig1)
print("  OK (13 frames)")

# ════════════════════════════════════════════
# ANIMATION 2: H0 Sync Phase
# ════════════════════════════════════════════
print("Generating idcm_h0_sync_phase.gif ...")
r_arr = np.logspace(log10(0.01), log10(200), 500)
A_sync = EPS * (r_arr / XI) ** BETA
H0_arr = H0_GLOBAL * (1 + A_sync)

r_data = np.array([0.05, 1.77])
h0_data = np.array([69.80, 73.05])
h0_err = np.array([1.90, 1.04])
data_labels = ['TRGB\n(Freedman)', 'Cepheid\n(SH0ES)']

fig2, ax_h0 = plt.subplots(figsize=(10, 6))

n_frames_h0 = 100

def init_h0():
    ax_h0.clear()

def animate_h0(frame):
    ax_h0.clear()
    ax_h0.loglog(r_arr, H0_arr, '#1a5276', lw=2.5, zorder=2,
                 label=r'IDCM: $H_0(r) = H_0^{\rm global} \cdot (1+\varepsilon\cdot(r/\xi)^\beta)$')
    ax_h0.axhline(H0_GLOBAL, color='#888', lw=1, ls='--', alpha=0.7,
                  label=r'$H_0^{\rm global} = %.1f$ km/s/Mpc' % H0_GLOBAL)
    
    for i in range(2):
        ax_h0.errorbar(r_data[i], h0_data[i], yerr=h0_err[i], fmt='o',
                       color='#c0392b', ms=7, capsize=3, capthick=1.5, zorder=3)
        ax_h0.annotate(data_labels[i], xy=(r_data[i] * 1.5, h0_data[i] + 0.3),
                       fontsize=10, color='#c0392b')
    
    # Scan marker
    frac = frame / n_frames_h0
    r_scan = 0.01 * (200 / 0.01) ** frac
    H0_scan = H0_GLOBAL * (1 + EPS * (r_scan / XI) ** BETA)
    
    ax_h0.plot(r_scan, H0_scan, 'v', color='#ff8c00', ms=10, zorder=5)
    ax_h0.axvline(r_scan, color='#ff8c00', lw=1, ls=':', alpha=0.5)
    
    # Info box
    info = 'r = %.2f Mpc\nH0(r) = %.2f km/s/Mpc' % (r_scan, H0_scan)
    ax_h0.text(0.05, 0.05, info, transform=ax_h0.transAxes, fontsize=12,
               fontweight='bold', va='bottom',
               bbox=dict(facecolor='wheat', alpha=0.8, boxstyle='round'))
    
    ax_h0.set_xlabel('Distance r [Mpc]', fontsize=13)
    ax_h0.set_ylabel(r'$H_0(r)$ [km/s/Mpc]', fontsize=13)
    ax_h0.set_title(r'$H_0$ Sync Phase: Position-Dependent Calibration', fontsize=14, fontweight='bold')
    ax_h0.set_xlim(0.01, 200); ax_h0.set_ylim(66, 76)
    ax_h0.grid(True, alpha=0.2)
    ax_h0.legend(fontsize=9, loc='lower right')

anim2 = FuncAnimation(fig2, animate_h0, frames=n_frames_h0, init_func=init_h0, blit=False, repeat=True)
anim2.save(OUT + '/idcm_h0_sync_phase.gif', writer=PillowWriter(fps=10))
plt.close(fig2)
print("  OK (%d frames)" % n_frames_h0)

# ════════════════════════════════════════════
# ANIMATION 3: f(z) Bump Scan
# ════════════════════════════════════════════
print("Generating idcm_fz_bump.gif ...")
z_full = np.logspace(-2, 1.2, 500)
x_full = z_full / ZC
f_full = 1.0 + EPS * x_full * np.exp(-x_full)

fig3, (ax_b1, ax_b2) = plt.subplots(1, 2, figsize=(12, 5))
n_frames_b = 100

def animate_bump(frame):
    frac = frame / n_frames_b
    z_max = 0.01 * (15 / 0.01) ** frac
    
    for ax in [ax_b1, ax_b2]:
        ax.clear()
    
    mask = z_full <= z_max
    z_cur = z_full[mask]
    f_cur = f_full[mask]
    
    ax_b1.semilogx(z_cur, f_cur, '#1a5276', lw=2.5)
    ax_b1.semilogx(z_full, np.ones_like(z_full), '#888888', lw=1.5, ls='--',
                   alpha=0.5, label=r'$\Lambda$CDM')
    if len(z_cur) > 2:
        ax_b1.fill_between(z_cur, 1.0, f_cur, alpha=0.12, color='#1a5276')
    ax_b1.axhline(1.0, color='#888', lw=0.5)
    ax_b1.set_xlabel('Redshift z', fontsize=12)
    ax_b1.set_ylabel(r'$f(z)$', fontsize=12)
    ax_b1.set_title('Dark Energy Modulation', fontsize=13, fontweight='bold')
    ax_b1.set_xlim(0.01, 15); ax_b1.set_ylim(0.98, 1.08)
    ax_b1.grid(True, alpha=0.2)
    ax_b1.legend(fontsize=10)
    ax_b1.text(0.98, 0.05, 'z_max = %.2f' % z_max, transform=ax_b1.transAxes,
               fontsize=12, fontweight='bold', ha='right',
               bbox=dict(facecolor='white', alpha=0.7))
    
    dev = (f_cur - 1.0) * 100 if len(f_cur) > 2 else np.array([0])
    ax_b2.semilogx(z_cur, dev, '#1a5276', lw=2.5)
    ax_b2.axhline(0, color='#888', lw=0.5)
    if len(z_cur) > 2:
        ax_b2.fill_between(z_cur, 0, dev, alpha=0.12, color='#1a5276')
    ax_b2.set_xlabel('Redshift z', fontsize=12)
    ax_b2.set_ylabel('Deviation [%]', fontsize=12)
    ax_b2.set_title('Relative Deviation from LCDM', fontsize=13, fontweight='bold')
    ax_b2.set_xlim(0.01, 15); ax_b2.set_ylim(-0.5, 6.5)
    ax_b2.grid(True, alpha=0.2)
    
    if z_max > ZC * 0.5:
        ax_b2.axvline(ZC, color='#c0392b', lw=1, ls=':', alpha=0.5,
                      label=r'$z_c = 0.6$')
        ax_b2.legend(fontsize=10)

anim3 = FuncAnimation(fig3, animate_bump, frames=n_frames_b, blit=False, repeat=True)
anim3.save(OUT + '/idcm_fz_bump.gif', writer=PillowWriter(fps=10))
plt.close(fig3)
print("  OK (%d frames)" % n_frames_b)

# ════════════════════════════════════════════
# ANIMATION 4: Cosmic Cycle
# ════════════════════════════════════════════
print("Generating idcm_cosmic_cycle.gif ...")
tau0 = 13.8  # current age in Gyr
t_cycle = tau0 * exp(16)  # ~8.9e6 Gyr

phases = [
    ('Big Bang', 0, '#1a5276'),
    ('Structure\nFormation', 0.1 * t_cycle, '#2e86c1'),
    ('Present', tau0, '#27ae60'),
    ('Heat Death\n(DE decays ~5%)', 0.2 * t_cycle, '#c0392b'),
    ('Fluctuation\nGrowth', 0.5 * t_cycle, '#d35400'),
    ('Restart\nTrigger', 0.95 * t_cycle, '#f39c12'),
    ('New Cycle\nRebirth', t_cycle, '#8e44ad'),
]

fig4, ax_c = plt.subplots(figsize=(12, 3.5))
n_frames_c = 100

def animate_cycle(frame):
    frac = frame / n_frames_c
    t_cur = frac * t_cycle * 1.1
    
    ax_c.clear()
    ax_c.set_xlim(0, t_cycle * 1.15)
    ax_c.set_ylim(0, 1)
    ax_c.set_xlabel('Time [Gyr]', fontsize=12)
    ax_c.set_title('IDCM Cosmic Cycle', fontsize=14, fontweight='bold')
    ax_c.set_yticks([])
    ax_c.grid(True, alpha=0.2, axis='x')
    
    # Draw timeline
    ax_c.plot([0, t_cycle * 1.1], [0.5, 0.5], 'k-', lw=2, zorder=1)
    
    # Draw phases
    for name, t, color in phases:
        x = t
        ax_c.plot(x, 0.5, 'o', color=color, ms=8, zorder=3)
        ax_c.annotate(name, xy=(x, 0.5), xytext=(x, -0.15 if t < 0.5 * t_cycle else 1.1),
                     ha='center', fontsize=9, color=color, fontweight='bold',
                     arrowprops=dict(arrowstyle='->', color=color, lw=0.8))
    
    # Current position marker
    if t_cur <= t_cycle:
        ax_c.plot(t_cur, 0.5, 'v', color='#ff8c00', ms=12, zorder=5)
    
    # Time labels
    ax_c.text(0, -0.45, 't=0', fontsize=9, ha='center', color='#1a5276')
    ax_c.text(tau0, -0.45, 'Today\n%.1f Gyr' % tau0, fontsize=9, ha='center', color='#27ae60')
    ax_c.text(t_cycle, -0.45, 't_cycle\n%.1e Gyr' % t_cycle, fontsize=9, ha='center', color='#8e44ad')
    
    # Info box
    if t_cur <= tau0:
        info = 'Phase: Expansion / $f(z)$ active\nTime: %.1f Gyr (z=%.2f)' % (t_cur, 1 / (t_cur / tau0 + 0.01) - 1)
    elif t_cur <= 0.2 * t_cycle:
        info = 'Phase: Asymptotic Heat Death\nOmega_L ~ 0.9515, expansion continues'
    elif t_cur <= 0.8 * t_cycle:
        info = 'Phase: W-field zero-point fluctuations\nDelta C ~ sqrt(kappa) = 0.25'
    else:
        info = 'Phase: Restart imminent!\nN-domain cumulative fluctuation ~ 1'
    
    ax_c.text(0.98, 0.85, info, transform=ax_c.transAxes, fontsize=11,
              ha='right', va='top',
              bbox=dict(facecolor='lightyellow', alpha=0.85, boxstyle='round'))

anim4 = FuncAnimation(fig4, animate_cycle, frames=n_frames_c, blit=False, repeat=True)
anim4.save(OUT + '/idcm_cosmic_cycle.gif', writer=PillowWriter(fps=10))
plt.close(fig4)
print("  OK (%d frames)" % n_frames_c)

print("\nAll 4 GIFs generated in " + OUT)
