"""
IDCM 5.0 — Comprehensive Spectrum Validation
==============================================
1.  Lagrangian inversion: V(phi) from w(z)
2.  Weak lensing S8 constraint
3.  Growth rate f_sig8(z) full curve + residuals
4.  Galaxy cluster abundance approximation
5.  Strong lensing time-delay H0 consistency
6.  Full chi2 summary table

Pure numpy/scipy. No LLM involved in numerical computation.
"""

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d
import json, os

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EPS = (np.sqrt(5) - 1) / 8
ZC = 0.6
C_SPEED = 299792.458

# IDCM posterior parameters
Om, h, ombh2, sig8 = 0.3045, 0.6821, 0.02237, 0.780
ODE = 1 - Om
H0 = h * 100

print("=" * 68)
print("IDCM 5.0 — Comprehensive Validation")
print("=" * 68)

# ═══ Model Core ═══
def f_de(z):
    x = z / ZC
    return 1.0 + EPS * x * np.exp(-x)

def E2(z):
    return Om*(1+z)**3 + ODE*f_de(z)

def H(z):
    return H0 * np.sqrt(E2(z))

def w_DE(z):
    """Dark energy equation of state"""
    x = z / ZC
    fp = EPS/ZC * np.exp(-x) * (1 - x)
    return -1.0 + (1+z)/3.0 * fp / f_de(z)

def DM(z):
    """Comoving distance in Mpc"""
    return quad(lambda zp: C_SPEED/np.sqrt(E2(zp)), 0, z, limit=500)[0] / h

# ═══════════════════════════════
# 1. LAGRANGIAN INVERSION: V(phi)
# ═══════════════════════════════
print(f"\n{'─'*68}")
print("1. Lagrangian Inversion (V(phi) from w(z))")
print(f"{'─'*68}")

# For scalar field DE: w = (phi_dot^2/2 - V)/(phi_dot^2/2 + V)
# rho_phi = phi_dot^2/2 + V
# Continuity eq: rho_dot_phi + 3H(1+w)rho_phi = 0
# -> phi_dot^2 = (1+w)rho_phi
# -> V = (1-w)rho_phi/2

rho_DE0 = ODE
print(f"  rho_DE(z=0) = {rho_DE0:.4f} x rho_crit")
print(f"  Omega_DE = {ODE:.4f}")

def dphi_dz(z):
    """dphi/dz = +/- sqrt((1+w)rho_DE) / ((1+z)H)"""
    w = w_DE(z)
    rho = rho_DE0 * f_de(z)
    if 1+w < 0:
        return 0
    return np.sqrt(abs(1+w) * rho) / ((1+z) * np.sqrt(E2(z)))

def V_z(z):
    """Potential V(phi) from w(z) and rho(z)"""
    w = w_DE(z)
    rho = rho_DE0 * f_de(z)
    if 1+w < 0:
        return (1 - w) * rho / 2
    return (1 - w) * rho / 2
