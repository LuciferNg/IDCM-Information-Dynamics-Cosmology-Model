#!/bin/bash
# IDCM Validation Suite — Run All
echo "=============================================="
echo "IDCM VALIDATION SUITE"
echo "=============================================="

# Need CYTools venv
source /tmp/cy_venv/bin/activate 2>/dev/null || true

echo ""
echo "--- TIER 1: PDG EXPERIMENT ---"
python3 v1_masses.py
echo ""
python3 v1_ckm.py
echo ""
python3 v1_dm.py

echo ""
echo "--- TIER 2: KS/CYTools ---"
# Skip CYTools if not available
if python3 -c "from cytools import fetch_polytopes" 2>/dev/null; then
    python3 v2_cy_existence.py
else
    echo "CYTools not available in current venv"
fi

echo ""
echo "--- TIER 3: COMPUTATION ---"
python3 v3_jstar.py

echo ""
echo "--- TIER 4: FRAMEWORK ---"
python3 v4_mera.py
echo ""
python3 v4_kuramoto.py

echo ""
echo "=============================================="
echo "VALIDATION COMPLETE"
echo "=============================================="
