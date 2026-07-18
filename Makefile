.PHONY: all validate validate-all clean setup

# IDCM Validation Makefile
SHELL := /bin/bash
VENV := .venv
PYTHON := $(VENV)/bin/python3

all: validate

$(VENV):
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install -r requirements.txt

setup: $(VENV)

validate: setup
	@echo "=== IDCM Validation Suite ==="
	$(PYTHON) data/cy_search/validation/v1_masses.py
	$(PYTHON) data/cy_search/validation/v1_ckm.py
	$(PYTHON) data/cy_search/validation/v1_dm.py

validate-all: setup
	@echo "=== Full IDCM Validation Suite ==="
	cd data/cy_search/validation && source $(VENV)/bin/activate && bash run_all.sh

clean:
	rm -rf $(VENV)
	find . -name '__pycache__' -type d -exec rm -rf {} + 2>/dev/null || true
	find . -name '*.pyc' -delete
