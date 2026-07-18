"""
mcmc_idcm.py — MCMC joint fit of IDCM with DESI DR2 BAO + CMB + DES-SN5YR
==========================================================================
Uses emcee with fast D_C interpolation.

Fixed constants (from recursion, not fitted):
    ε = φ⁻¹/4 ≈ 0.1545084972   (sync amplitude)
    z_c = 0.6                  (sync redshift)
    β = φ⁻¹/2 ≈ 0.309017       (scale exponent)

Free parameters: H₀, Ω_m  (2 params, n_dim=2)

SNe dataset: DES-SN5YR (1820 SNe, full 1820×1820 covariance matrix)
             with analytic M marginalisation.
"""

import numpy as np
import emcee
import corner
import time, os
from math import sqrt

# ============================================================
# IDCM derived constants
# ============================================================
phi_inv = (sqrt(5) - 1) / 2          # φ⁻¹ ≈ 0.618033988749895
EPS = phi_inv / 4                     # ε = φ⁻¹/4 ≈ 0.1545084972
ZC = 0.6                              # z_c — sync redshift
BETA = phi_inv / 2                    # β = φ⁻¹/2 ≈ 0.3090169944

# Physical constants
C = 299792.458
Z_REC = 1089.92
R_S_BAO = 147.09
R_S_CMB = 144.43
PR = 1.7502; PRE = 0.0046
PLA = 301.808; PLAE = 0.090
PRLAC = 0.47
LAM = 0.001  # secular efficiency (fixed, undetectable at z<2)

# ============================================================
# BAO data (DESI DR2, 12 pts: D_M, D_H, D_V at 6 redshift bins)
# ============================================================
BAO_MEAN = np.array([
    7.92512927, 13.62003080, 20.98334647,
    16.84645313, 20.07872919,
    21.70841761, 17.87612922,
    27.78720817, 13.82372285,
    26.07217182, 39.70838281, 8.52256583,
])
BAO_COV = np.array([
    [2.2723e-02, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 6.3466e-02, -6.8534e-02, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -6.8534e-02, 3.7297e-01, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1.0198e-01, -7.9940e-02, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, -7.9940e-02, 3.5445e-01, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 7.9568e-02, -3.8011e-02, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -3.8011e-02, 1.1994e-01, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4.7657e-01, -1.2941e-01, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, -1.2941e-01, 1.7827e-01, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 4.4713e-01, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8.8975e-01, -7.6948e-02],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -7.6948e-02, 2.9186e-02],
])
BAO_Z = np.array([0.295, 0.510, 0.510, 0.706, 0.706, 0.930, 0.930,
                  1.317, 1.317, 1.491, 2.330, 2.330])
BAO_T = ['DV', 'DM', 'DH', 'DM', 'DH', 'DM', 'DH', 'DM', 'DH', 'DV', 'DM', 'DH']
BAO_ICOV = np.linalg.inv(BAO_COV)

# ============================================================
# H(z) data
# ============================================================
HZ = np.array([
    [0.07, 69, 19.5], [0.09, 69, 12], [0.12, 68.6, 26.2], [0.17, 83, 8],
    [0.179, 75, 4], [0.199, 75, 5], [0.20, 72.9, 29.6], [0.27, 77, 14],
    [0.28, 88.8, 36.6], [0.352, 83, 14], [0.38, 81.5, 1.9], [0.4, 82.8, 1.2],
    [0.4004, 77, 10.2], [0.4247, 87.1, 11.2], [0.44, 82.6, 7.8],
    [0.4448, 92.8, 12.9], [0.47, 89, 49.6], [0.4783, 80.9, 9],
    [0.48, 97, 62], [0.51, 90.4, 1.9], [0.56, 93.34, 2.3], [0.57, 92.4, 4.5],
    [0.593, 104, 13], [0.6, 87.9, 6.1], [0.61, 97.3, 2.1], [0.68, 92, 8],
    [0.73, 97.3, 7], [0.78, 97.6, 4], [0.781, 105, 12], [0.875, 125, 17],
    [0.88, 90, 40], [0.9, 117, 23], [1.037, 154, 20], [1.3, 168, 17],
    [1.363, 160, 33.6], [1.43, 177, 18], [1.53, 140, 14],
    [1.75, 202, 40], [1.965, 186.5, 50.4],
])

# ============================================================
# DES-SN5YR data loading
# ============================================================
DATA_DIR = os.path.dirname(os.path.abspath(__file__))

print("Loading DES-SN5YR data...")

# Load HD.csv — space-separated, CID="SN: NAME" as first two tokens
with open(os.path.join(DATA_DIR, 'DES_SN5YR_DES-Dovekie_HD.csv')) as f:
    lines = [l.strip() for l in f if not l.startswith('#')]

sne_zs, sne_zhel, sne_mu = [], [], []
for l in lines[1:]:  # skip VARNAMES row
    parts = l.split()
    # CID = 'SN: NAME' (2 tokens), then: IDSURVEY, zHD, zHEL, MU, MUERR, ...
    sne_zs.append(float(parts[3]))
    sne_zhel.append(float(parts[4]))
    sne_mu.append(float(parts[5]))

sne_zs = np.array(sne_zs)
sne_zhel = np.array(sne_zhel)
sne_mu = np.array(sne_mu)
N_SNE = len(sne_zs)
print(f"  {N_SNE} SNe loaded, z range: [{sne_zs.min():.4f}, {sne_zs.max():.4f}]")

# Load inverse covariance matrix from npz (upper triangular format)
d = np.load(os.path.join(DATA_DIR, 'DES_SN5YR_STAT+SYS.npz'))
nsn = d['nsn'][0]
assert nsn == N_SNE, f"nsn mismatch: {nsn} vs {N_SNE}"
ICOV = np.zeros((N_SNE, N_SNE))
ICOV[np.triu_indices(N_SNE)] = d['cov']
i_lower = np.tril_indices(N_SNE, -1)
ICOV[i_lower] = ICOV.T[i_lower]
print(f"  Covariance matrix: {N_SNE}×{N_SNE}, cond = {np.linalg.cond(ICOV):.1e}")


# ============================================================
# Fast cosmology: precomputed D_C interpolation
# ============================================================

def build_cosmology(H0, Om):
    """
    Compute IDCM cosmology with fixed ε = φ⁻¹/4, z_c = 0.6.
    IDCM f(z) = 1 + ε·(z/z_c)·exp(-z/z_c)  (bump).
    """
    Ol = 1.0 - Om
    h = H0 / 100.0
    Or = 4.15e-5 / h**2

    N = 500
    z_low = np.linspace(0, 0.01, 50)
    z_high = np.logspace(np.log10(0.011), np.log10(Z_REC * 1.5), N)
    z_grid = np.unique(np.concatenate([z_low, z_high]))

    x = z_grid / ZC
    f_trans = 1.0 + EPS * x * np.exp(-x)

    E2 = Om * (1 + z_grid)**3 + Or * (1 + z_grid)**4 + Ol * f_trans
    E = np.sqrt(np.maximum(E2, 1e-30))

    inv_E = 1.0 / E
    DC = np.zeros_like(z_grid)
    # Cumulative trapezoidal: include [0, z_grid[0]] interval
    DC[0] = 0.5 * (1.0 + inv_E[0]) * z_grid[0]  # E(0) = 1
    for i in range(1, len(z_grid)):
        dz = z_grid[i] - z_grid[i-1]
        DC[i] = DC[i-1] + 0.5 * (inv_E[i] + inv_E[i-1]) * dz
    DC *= C / H0

    from scipy.interpolate import interp1d
    DC_interp = interp1d(z_grid, DC, kind='cubic', bounds_error=False, fill_value=0.0)

    def E_at_z(z):
        z = np.asarray(z, float)
        x = z / ZC
        ft = 1.0 + EPS * x * np.exp(-x)
        e2 = Om * (1 + z)**3 + Or * (1 + z)**4 + Ol * ft
        return np.sqrt(np.maximum(e2, 1e-30))

    return {
        'H0': H0, 'Om': Om, 'Ol': Ol, 'Or': Or,
        'E': E_at_z,
        'DC': lambda z: float(DC_interp(z)),
        'DC_arr': lambda z: DC_interp(np.asarray(z, float)),
    }


# ============================================================
# SNe likelihood: analytic M marginalisation
# Formula from https://arxiv.org/abs/astro-ph/0104009v1 Eq. A9-12
# ============================================================

def sne_log_likelihood(mu_model, mu_obs, inv_cov):
    """
    Modified likelihood that analytically marginalises over
    the SN absolute magnitude M (degenerate with H₀).
    """
    delta = mu_model - mu_obs
    chi2 = delta @ inv_cov @ delta
    B = np.sum(inv_cov @ delta)
    C = np.sum(inv_cov)
    chi2_marg = chi2 - (B**2 / C) + np.log(C / (2 * np.pi))
    return -0.5 * chi2_marg


# ============================================================
# Log-likelihood: BAO + CMB + DES-SN5YR + H(z)
# ============================================================

def ln_like(params):
    """Log-likelihood: -0.5 × total χ² (H(z) + BAO + CMB + DES-SN5YR)."""
    H0, Om = params

    if not (55 < H0 < 80): return -np.inf
    if not (0.15 < Om < 0.45): return -np.inf

    cosmo = build_cosmology(H0, Om)

    # — H(z) χ² —
    hz_pred = cosmo['H0'] * cosmo['E'](HZ[:, 0])
    chi2_h = np.sum(((hz_pred - HZ[:, 1]) / HZ[:, 2])**2)

    # — DESI BAO χ² (12 points, full covariance) —
    pred = np.zeros(12)
    for i in range(12):
        z = BAO_Z[i]
        t = BAO_T[i]
        if t == 'DM':
            pred[i] = cosmo['DC'](z) / R_S_BAO
        elif t == 'DH':
            pred[i] = C / (cosmo['H0'] * cosmo['E'](z)) / R_S_BAO
        elif t == 'DV':
            dm = cosmo['DC'](z)
            pred[i] = (C * z * dm**2 / (cosmo['H0'] * cosmo['E'](z)))**(1/3) / R_S_BAO
    chi2_b = (pred - BAO_MEAN) @ BAO_ICOV @ (pred - BAO_MEAN)

    # — CMB χ² (shift parameter R + acoustic scale l_A) —
    DC_rec = cosmo['DC'](Z_REC)
    I_rec = DC_rec * cosmo['H0'] / C
    R_val = sqrt(Om) * I_rec
    la_val = np.pi * DC_rec / R_S_CMB

    var_r = PRE**2; var_la = PLAE**2; cov_rl = PRLAC * PRE * PLAE
    det = var_r * var_la - cov_rl**2
    i_r = var_la / det; i_la = var_r / det; i_rl = -cov_rl / det
    dr = R_val - PR; dla = la_val - PLA
    chi2_c = i_r * dr**2 + 2 * i_rl * dr * dla + i_la * dla**2

    # — DES-SN5YR χ² (1820 SNe, full 1820×1820 cov, M marginalised) —
    # D_A = D_C/(1+z), D_L = (1+z_CMB)(1+z_HEL) × D_A = (1+z_HEL) × D_C
    DC_arr = cosmo['DC_arr'](sne_zs)
    mu_model = 5.0 * np.log10((1.0 + sne_zhel) * DC_arr) + 25.0
    like_sne = sne_log_likelihood(mu_model, sne_mu, ICOV)

    logL = -0.5 * (chi2_h + chi2_b + chi2_c) + like_sne
    return logL


# ============================================================
# MCMC
# ============================================================

print("=" * 72)
print("  MCMC JOINT FIT — IDCM (H₀, Ω_m)")
print(f"  Fixed: ε = φ⁻¹/4 = {EPS:.10f}")
print(f"         z_c = {ZC}, β = {BETA:.6f}")
print("  Datasets: DESI DR2 BAO (12 pts, full cov)")
print("            Planck CMB (R + l_A)")
print("            DES-SN5YR (1820 SNe, 1820×1820 cov)")
print("            H(z) compilation (39 pts)")
print("=" * 72)

n_dim = 2
n_walkers = 16
n_burn = 500
n_steps = 3000
n_thin = 3

p0_best = np.array([69.0, 0.300])
p0_scale = np.array([2.0, 0.02])

rng = np.random.default_rng(42)
p0 = p0_best + p0_scale * rng.normal(size=(n_walkers, n_dim))

for i in range(n_walkers):
    while True:
        h, o = p0[i]
        if 55 < h < 80 and 0.15 < o < 0.45:
            break
        p0[i] = p0_best + p0_scale * rng.normal(size=n_dim)

print(f"\nWalkers: {n_walkers}, burn: {n_burn}, steps: {n_steps}")
print(f"Initial: H₀={p0_best[0]:.1f}, Ω_m={p0_best[1]:.3f}")
print(f"\nStarting MCMC (this will take several minutes)...")
t_start = time.time()

sampler = emcee.EnsembleSampler(n_walkers, n_dim, ln_like,
                                moves=emcee.moves.DEMove())
sampler.run_mcmc(p0, n_burn + n_steps, progress=True)

elapsed = time.time() - t_start
print(f"\nMCMC done: {elapsed:.0f}s ({elapsed/60:.1f} min)")

chain = sampler.get_chain(discard=n_burn, thin=n_thin, flat=True)
log_prob = sampler.get_log_prob(discard=n_burn, thin=n_thin, flat=True)

chi2_arr = -2.0 * log_prob
i_best = np.argmin(chi2_arr)
map_params = chain[i_best]
map_chi2 = chi2_arr[i_best]

print(f"\nMinimum χ² = {map_chi2:.1f}")
print(f"MAP:")
print(f"  H₀    = {map_params[0]:.1f} ± {np.std(chain[:, 0]):.1f}")
print(f"  Ω_m   = {map_params[1]:.4f} ± {np.std(chain[:, 1]):.4f}")

perc = [16, 50, 84]
for i, name in enumerate(['H₀', 'Ω_m']):
    q = np.percentile(chain[:, i], perc)
    print(f"  {name} = {q[1]:.4f} +{q[2]-q[1]:.4f} -{q[1]-q[0]:.4f}")

# Corner plot
print("\nGenerating corner plot...")
fig = corner.corner(chain, labels=['$H_0$', '$\\Omega_m$'],
                    truths=map_params, quantiles=[0.16, 0.5, 0.84],
                    show_titles=True, title_fmt='.4f',
                    plot_datapoints=True, fill_contours=True,
                    levels=(0.68, 0.95), color='#222222',
                    smooth=True, smooth1d=True)
fig.savefig(os.path.join(DATA_DIR, "mcmc_corner_idcm_des5yr.png"), dpi=200)
print("Saved: mcmc_corner_idcm_des5yr.png")

# Save chain
np.savez(os.path.join(DATA_DIR, "mcmc_chain_idcm_des5yr.npz"),
         chain=chain, log_prob=log_prob,
         map_params=map_params, names=['H0', 'Om'],
         chi2_min=map_chi2)
print("Saved: mcmc_chain_idcm_des5yr.npz")

# Summary
print(f"\n{'=' * 72}")
print(f"  RESULTS — IDCM with DES-SN5YR")
print(f"{'=' * 72}")
print(f"""
  Dataset combination:
    • DESI DR2 BAO    (12 pts, full cov)
    • Planck CMB      (R + l_A)
    • DES-SN5YR       ({N_SNE} SNe, 1820×1820 cov, M marg.)
    • H(z)            (39 pts)

  Parameter     MAP (±1σ)
  ────────  ─────────────────
  H₀        {map_params[0]:.2f} ± {np.std(chain[:, 0]):.2f}
  Ω_m       {map_params[1]:.4f} ± {np.std(chain[:, 1]):.4f}

  Fixed: ε = {EPS:.6f}, z_c = {ZC}, β = {BETA:.6f}
  χ²_min = {map_chi2:.1f} (2 free params, {N_SNE + 12 + 2 + 39 - 2} effective dof)
""")
