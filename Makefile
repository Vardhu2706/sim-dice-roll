# Makefile for sim-dice-roll

.PHONY: install lint test format coverage clean all

# Install dependencies (editable mode + requirements)
install:
	pip install -e .
	pip install -r requirements.txt

# Lint the code using flake8
lint:
	flake8 sim_dice_roll tests

# Run all tests with pytest
test:
	pytest tests

# Auto-format code with black
format:
	black sim_dice_roll tests

# Run tests with coverage report
coverage:
	pytest --cov=sim_dice_roll tests/

# Clean up cache files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -r {} +

# Run all (install, lint, test)
all: install lint test
