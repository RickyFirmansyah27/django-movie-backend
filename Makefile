# Python Default Variable
PY=py
PIP=pip

PYTHON=py

# Paths
VENV_DIR=venv


install:
	$(PY) -m venv $(VENV_DIR)
	$(VENV_DIR)/Scripts/$(PIP) install -r requirements.txt

dev:
	$(VENV_DIR)/Scripts/python manage.py runserver 8000

clean:
	@echo "Clearing Python __pycache__ directories..."
	@find . -type d -name '__pycache__' -exec rm -rf {} +

# Help message
help:
	@echo "Makefile targets:"
	@echo "  install   - Set up a local virtual environment and install dependencies from requirements.txt"
	@echo "  dev       - Run Server"
	@echo "  clean     - Remove all __pycache__ directories in the project"
	@echo "  help      - Show this help message"
