(* IDCM Dark Matter Mass from Stabilized Kahler Class *)
(* Date: 2026-07-18 *)

Print["========================================================"];
Print["IDCM — DARK MATTER MASS FROM STABILIZED GEOMETRY"];
Print["========================================================"];

(* IDCM Constants *)
phi = N[(1 + Sqrt[5])/2, 16];
eps = phi^(-1)/4;
kap = 1/16;

(* Stabilized Kahler class volume *)
Vcy = 2.458132*10^(-4);
kap3 = kap^3;
Print["V_CY = ", Vcy];
Print["kappa^3 = ", kap3];
Print["Ratio = ", Vcy/kap3];

(* Planck mass *)
Mp = 1.220910*10^19;
Print[""];
Print["M_Planck = ", Mp, " GeV"];

(* Warped circle *)
kR = 1/(2*Pi);
Print["kR = 1/(2*Pi) = ", kR];

(* =============== KK Tower =============== *)
Print[""];
Print["=== KK Mode Masses (S1_w x CY3) ==="];
V16 = Vcy^(1/6);
Print["V_CY^(1/6) = ", V16];

For[n=0, n<=5, n++,
  mGeV = n * Exp[-1] * Mp * V16;
  mMeV = mGeV * 1000;
  Print["n=", n, "   ", CForm[N[mGeV,6]], " GeV   ", CForm[N[mMeV,6]], " MeV"]
];

(* =============== W-field DM Tower =============== *)
Print[""];
Print["=== W-field DM Tower ==="];
V13 = Vcy^(1/3);
Print["V_CY^(1/3) = ", V13];

For[n=0, n<=10, n++,
  mGeV = Mp * Exp[-n] * V13;
  mMeV = mGeV * 1000;
  mkeV = mMeV * 1000;
  Print["n=", n, "   ", CForm[N[mGeV,6]], " GeV   ", CForm[N[mMeV,6]], " MeV   ", CForm[N[mkeV,6]], " keV"]
];

(* =============== kappa-threshold prediction =============== *)
Print[""];
Print["=== Kappa-threshold DM prediction ==="];
nstar = Log[16.0];
Print["n* = ln(16) = ", nstar];

MDM = Mp * Exp[-nstar] * phi^(-nstar);
Print["M_DM = M_P * exp(-n*) * phi^(-n*)"];
Print["M_DM = ", CForm[N[MDM,8]], " GeV"];
Print["      = ", N[MDM*1000,8], " MeV"];
Print["      = ", N[MDM*1000*1000,8], " keV"];
Print[""];

(* Check: what is the ratio to 13.8 MeV? *)
MEV13 = 0.0138;
Print["Ratio to 13.8 MeV target: ", N[MDM/MEV13, 6]];
Print[""];

(* Also check pure warped KK *)
Print["=== First KK mode mass (warped) ==="];
MKK1 = Exp[-1] * Mp * V16;
Print["M_KK1 = M_P * e^(-1) * V_CY^(1/6)"];
Print["M_KK1 = ", CForm[N[MKK1,8]], " GeV"];
Print["       = ", N[MKK1*1000,8], " MeV"];
Print["       = ", N[MKK1*1000*1000,8], " keV"];

(* Combined: warp + kappa threshold *)
Print[""];
Print["=== Combined (warp + kappa) ==="];
Mcomb = Mp * Exp[-1] * phi^(-nstar);
Print["M_comb = M_P * e^(-1) * phi^(-n*)"];
Print["M_comb = ", CForm[N[Mcomb,8]], " GeV"];
Print["        = ", N[Mcomb*1000,6], " MeV"];
Print["        = ", N[Mcomb*1000*1000,6], " keV"];

(* The IDCM unified formula *)
Print[""];
Print["========================================================"];
Print["IDCM DM Mass Formula: M_DM = M_P * λ^n* * κ^3"];
Print["  where λ = φ^(-1), n* = ln(16), κ = 1/16"];
lam = phi^(-1);
MDM2 = Mp * (lam^nstar) * (kap^3);
Print["  λ^n* = ", N[lam^nstar,8]];
Print["  κ^3 = ", N[kap^3,8]];
Print["  M_DM = ", CForm[N[MDM2,8]], " GeV"];
Print["        = ", N[MDM2*1000,8], " MeV"];
Print["========================================================"];
