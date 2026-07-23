import math
phi = (1 + 5**0.5) / 2
phi_inv = phi - 1
M, Nh, h11, ngen = 33, 42, 36, 3

print("M/5 DERIVATION CANDIDATES:")
print(f"{'Source':>25} → {'Value':>8}  Match?")
print("-" * 48)
for name, val in {
    "MERA: 2³ - ngen": 2**3 - ngen,
    "(M-3)/6": (M-3)/6,
    "h11-31": h11-31,
    "Nh/8.4": Nh/8.4,
    "(Nh-2)/8": (Nh-2)/8,
}.items():
    m = "✅" if abs(val-5)<0.01 else ("🟡" if abs(val-5)<0.5 else "❌")
    print(f"{name:>25} → {val:>8.4f}  {m}")

print(f"\nMERA: 2³ - ngen = {2**3} - {ngen} = {2**3-ngen}")
print(f"→ M/(2³-ngen) = {M}/{2**3-ngen} = {M/(2**3-ngen):.4f}")
print(f"→ V_cb = φ^(-{M/(2**3-ngen):.2f}) = {phi**(-M/(2**3-ngen)):.6f}")
print(f"PDG V_cb = 0.042")
