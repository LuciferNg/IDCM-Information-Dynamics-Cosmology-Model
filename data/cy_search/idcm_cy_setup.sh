#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════
# IDCM CY₃ Search — Full Setup & Execution Pipeline
# ═══════════════════════════════════════════════════════════════════
# Run on Ubuntu 22.04+ with sudo access.
# Estimated time: ~30 min (KS DB download) + ~20 min (nef.x scan)
# ═══════════════════════════════════════════════════════════════════

set -euo pipefail
VERSION="2026-07-18"
START_TIME=$(date +%s)
LOG_FILE="$HOME/idcm_cy_setup_$(date +%Y%m%d_%H%M%S).log"

# ──────────────────────────────────────────────
# Logging
# ──────────────────────────────────────────────
log() { echo "[$(date +%H:%M:%S)] $*" | tee -a "$LOG_FILE"; }
ok()  { echo "  ✔ $*" | tee -a "$LOG_FILE"; }
fail(){ echo "  ✘ $*" | tee -a "$LOG_FILE"; exit 1; }

echo ""
echo "═══════════════════════════════════════════"
echo "  IDCM CY₃ Search — Setup & Execution"
echo "  Version: $VERSION"
echo "═══════════════════════════════════════════"
echo ""

# ──────────────────────────────────────────────
# Step 1: System Update & Base Tools
# ──────────────────────────────────────────────
echo "─── Step 1/6: System Update ───"
sudo apt-get update -qq || true
sudo apt-get install -y -qq wget curl screen 2>&1 | tail -1
ok "System packages updated"

# ──────────────────────────────────────────────
# Step 2: Install PALP (nef.x, poly.x)
# ──────────────────────────────────────────────
echo "─── Step 2/6: Installing PALP (nef.x + poly.x) ───"
if command -v nef.x &>/dev/null; then
    ok "PALP already installed ($(nef.x -v 2>&1 | head -1))"
else
    sudo apt-get install -y -qq palp 2>&1 | tail -1
    if command -v nef.x &>/dev/null; then
        ok "PALP installed"
    else
        log "  PALP not in apt. Building from source..."
        cd /tmp
        curl -sL "https://webhome.physik.rwth-aachen.de/~hesselmann/palp/palp_v6.1.tar.gz" -o palp.tar.gz
        tar xzf palp.tar.gz
        cd palp-*
        ./configure --prefix=/usr/local
        make -j$(nproc)
        sudo make install
        cd /tmp
        ok "PALP built from source"
    fi
fi

# Verify PALP
nef.x -h > /dev/null 2>&1 && ok "nef.x ready" || fail "nef.x failed"
poly.x -h > /dev/null 2>&1 && ok "poly.x ready" || fail "poly.x failed"

# ──────────────────────────────────────────────
# Step 3: Install SageMath (via conda or flatpak)
# ──────────────────────────────────────────────
echo "─── Step 3/6: Installing SageMath ───"
if command -v sage &>/dev/null; then
    ok "SageMath already installed ($(sage -v 2>&1 | head -1))"
else
    log "  SageMath not in apt. Trying conda..."
    if command -v conda &>/dev/null; then
        log "  Installing via conda-forge..."
        conda install -y -c conda-forge sage 2>&1 | tail -1
        if command -v sage &>/dev/null; then
            ok "SageMath installed via conda"
        else
            log "  WARNING: conda install failed. Try flatpak:"
            log "    flatpak install flathub org.sagemath.SageMath"
        fi
    elif command -v flatpak &>/dev/null; then
        log "  Installing via flatpak..."
        flatpak install -y flathub org.sagemath.SageMath 2>&1 | tail -1
        if flatpak list 2>/dev/null | grep -qi sage; then
            ok "SageMath installed via flatpak"
        else
            log "  WARNING: flatpak install failed"
        fi
    else
        log "  Neither conda nor flatpak available."
        log "  Install SageMath manually: https://www.sagemath.org/download.html"
        log "  Continuing with WolframScript + PALP only."
    fi
fi

# ──────────────────────────────────────────────
# Step 4: Setup Project Directory
# ──────────────────────────────────────────────
echo "─── Step 4/6: Project Setup ───"
PROJECT_DIR="$HOME/idcm_cy_search"
mkdir -p "$PROJECT_DIR/data"

# Path to the IDCM IDCM-Information-Dynamics-Cosmology-Model
IDCM_DIR="$HOME/IDCM/IDCM-Information-Dynamics-Cosmology-Model"

if [ -d "$IDCM_DIR" ]; then
    cp -r "$IDCM_DIR/data/cy_search/"* "$PROJECT_DIR/"
    ok "Scripts copied from IDCM repo ($PROJECT_DIR)"
else
    log "  IDCM repo not found at $IDCM_DIR"
    log "  Will create standalone project"
    # Write minimal scripts here or notify user
fi

cd "$PROJECT_DIR"

# ──────────────────────────────────────────────
# Step 5: Download KS Database
# ──────────────────────────────────────────────
echo "─── Step 5/6: Downloading KS Database ───"
KS_FILE="$PROJECT_DIR/data/KS_database.txt"

if [ -f "$KS_FILE" ] && [ $(stat -f%z "$KS_FILE" 2>/dev/null || stat -c%s "$KS_FILE" 2>/dev/null) -gt 1000000000 ]; then
    ok "KS database already present ($(ls -lh "$KS_FILE" | awk '{print $5}'))"
else
    log "  Downloading KS database (~7 GB)..."
    log "  This will take time. Using background download."
    
    # Try multiple mirrors for KS database
    MIRRORS=(
        "https://www.thphys.uni-heidelberg.de/~kreuzer/CY/"
        "https://th.physik.uni-heidelberg.de/~kreuzer/CY/"
        "https://www-thphys.physics.ox.ac.uk/projects/CalabiYau/"
    )
    
    downloaded=false
    for mirror in "${MIRRORS[@]}"; do
        log "  Trying: $mirror"
        # Test connectivity
        if curl -sI --max-time 15 "$mirror" 2>/dev/null | head -1 | grep -q "200\|301\|302"; then
            log "  Mirror reachable: $mirror"
            # Pattern for KS database files (the exact filename varies)
            for fname in "h11h21.txt" "KS_database.txt" "weight_matrix_d4_r4.tar.gz"; do
                url="${mirror}${fname}"
                log "  Trying: $url"
                wget -c -q --timeout=60 --show-progress -O "$PROJECT_DIR/data/$fname" "$url" 2>&1 | tail -1
                if [ -f "$PROJECT_DIR/data/$fname" ] && [ $(stat -c%s "$PROJECT_DIR/data/$fname" 2>/dev/null || echo 0) -gt 1000 ]; then
                    downloaded=true
                    log "  Downloaded: $fname ($(du -h "$PROJECT_DIR/data/$fname" | awk '{print $1}'))"
                    break 2
                fi
            done
        else
            log "  Mirror unreachable: $mirror"
        fi
    done
    
    if [ "$downloaded" = false ]; then
        log "  WARNING: KS database not available from any mirror."
        log "  You need to download it manually from:"
        log "    https://www.thphys.uni-heidelberg.de/~kreuzer/CY/"
        log "  And place it in: $PROJECT_DIR/data/"
        log "  File names: h11h21.txt (Hodge list, ~30 MB) OR"
        log "              weight_matrix_d4_r4.tar.gz (full DB, ~7 GB)"
        log "  With just the Hodge list (h11h21.txt), we can still:"
        log "    - Check if (36,98) exists ✅"
        log "    - Check if chi=-248 parents exist ✅"
        log "    - Search for (98,36) mirror ✅"
    else
        ok "Database downloaded"
    fi
fi

# ──────────────────────────────────────────────
# Step 6: Run Pipeline
# ──────────────────────────────────────────────
echo "─── Step 6/6: Running Search Pipeline ───"

if [ -f "$PROJECT_DIR/data/h11h21.txt" ]; then
    log "  Hodge list available. Running targeted search..."
    
    # Quick check: does (36,98) exist in the Hodge list?
    grep "^36 98\|^36,98" "$PROJECT_DIR/data/h11h21.txt" > "$PROJECT_DIR/data/h36_98_found.txt" 2>/dev/null
    count36_98=$(wc -l < "$PROJECT_DIR/data/h36_98_found.txt" 2>/dev/null || echo 0)
    log "  (36,98) candidates: $count36_98"
    
    # Quick check: chi = -248 parents
    awk '{h11=\$1; h21=\$2; chi=2*(h11-h21); if(chi==-248) print}' "$PROJECT_DIR/data/h11h21.txt" \
        > "$PROJECT_DIR/data/parents_chi248.txt" 2>/dev/null
    count_parents=$(wc -l < "$PROJECT_DIR/data/parents_chi248.txt" 2>/dev/null || echo 0)
    log "  chi=-248 parent candidates: $count_parents"
    
    # Check: (98,36) mirror
    grep "^98 36\|^98,36" "$PROJECT_DIR/data/h11h21.txt" > "$PROJECT_DIR/data/mirror_98_36.txt" 2>/dev/null
    count_mirror=$(wc -l < "$PROJECT_DIR/data/mirror_98_36.txt" 2>/dev/null || echo 0)
    log "  (98,36) mirror candidates: $count_mirror"
    
elif [ -f "$KS_FILE" ] && [ $(stat -c%s "$KS_FILE" 2>/dev/null || echo 0) -gt 1000000000 ]; then
    log "  Starting nef.x scan for χ = -248 parents..."
    log "  This will take ~20 minutes on a modern CPU."
    
    # Strategy 2: Search for χ = -248 parent manifolds
    screen -dmS idcm_cy bash -c "
        cd '$PROJECT_DIR'
        echo '[IDCM] Starting nef.x scan...' | tee -a scan.log
        
        # Phase 1: Scan for χ = -248 (parent)
        nef.x -N -H -f < '$KS_FILE' 2>/dev/null \
            | awk -F'[,: ]' '\$2+0>0 && \$3+0>0 {chi=2*(\$2-\$3); if(chi==-248) print}' \
            > data/parents_chi248.txt 2>/dev/null
        
        count=\$(wc -l < data/parents_chi248.txt 2>/dev/null || echo 0)
        echo \"[IDCM] Found \$count parent candidates with χ=-248\" | tee -a scan.log
        
        # Phase 2: Check Z2 symmetry
        if [ \"\$count\" -gt 0 ]; then
            echo '[IDCM] Checking Z2 symmetry...' | tee -a scan.log
            poly.x -G < data/parents_chi248.txt 2>/dev/null > data/z2_check.txt 2>/dev/null
            z2_count=\$(grep -ci 'z2\|Z2\|order.2' data/z2_check.txt 2>/dev/null || echo 0)
            echo \"[IDCM] Found \$z2_count candidates with Z2 symmetry\" | tee -a scan.log
        else
            echo '[IDCM] No χ=-248 parents found.' | tee -a scan.log
            echo '[IDCM] Falling back to direct (36,98) search...' | tee -a scan.log
            nef.x -N -H -f < '$KS_FILE' 2>/dev/null \
                | grep 'H:36,98' \
                > data/direct_36_98.txt 2>/dev/null
            direct_count=\$(wc -l < data/direct_36_98.txt 2>/dev/null || echo 0)
            echo \"[IDCM] Found \$direct_count direct (36,98) candidates\" | tee -a scan.log
        fi
        
        echo '[IDCM] Scan complete. Results in data/ directory.' | tee -a scan.log
        echo '[IDCM] Running WolframScript verification...' | tee -a scan.log
        
        # Phase 3: Verify with WolframScript
        if command -v wolframscript &>/dev/null; then
            wolframscript -file strategy2_parent_e8.wls >> scan.log 2>&1
            wolframscript -file verify_cy36_98.wls >> scan.log 2>&1
        fi
        
        echo '[IDCM] Pipeline complete!' | tee -a scan.log
    "
    
    log "  Pipeline launched in screen session 'idcm_cy'."
    log "  Check progress: screen -r idcm_cy"
    log "  View log: tail -f $PROJECT_DIR/scan.log"
else
    log "  KS database not available. Skipping scan."
    log "  To run manually after database download:"
    log "    screen -dmS idcm_cy bash run_pipeline.sh"
fi

# ──────────────────────────────────────────────
# Summary
# ──────────────────────────────────────────────
DURATION=$(( $(date +%s) - START_TIME ))
echo ""
echo "═══════════════════════════════════════════"
echo "  IDCM CY₃ Setup Complete"
echo "  Duration: ${DURATION}s"
echo "═══════════════════════════════════════════"
echo ""
echo "  Project:  $PROJECT_DIR"
echo "  Log:      $LOG_FILE"
echo ""
echo "  Commands:"
echo "    View pipeline progress:  screen -r idcm_cy"
echo "    Detach from screen:     Ctrl+A, D"
echo "    Check candidates:       cat $PROJECT_DIR/data/parents_chi248.txt"
echo "    Rerun verification:     wolframscript -file $PROJECT_DIR/strategy2_parent_e8.wls"
echo "    Deep analysis:          sage $PROJECT_DIR/search_cy36_98.sage"
echo ""
echo "  Hit Ctrl+A then D to detach from screen."
echo "═══════════════════════════════════════════"