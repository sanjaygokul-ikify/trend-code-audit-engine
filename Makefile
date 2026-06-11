SIMULATED = 1

build:
	@echo "Building audit engine with optimizations"
	rust build --release

validate:
	python tests/smoke.py
	run --simulated audit

dev:
	MODE=dev ./bin/server

verify:
	python3 -m pytest tests/