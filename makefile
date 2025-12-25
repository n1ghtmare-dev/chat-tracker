APP=chat_tracker.main
PYTHON=poetry run python

.PHONY: run install lint test check

install:
	poetry install

run:
	$(PYTHON) -m $(APP)

lint: 
	poetry run ruff check .

test:
	poetry run pytest

check: 
	make lint
	make test