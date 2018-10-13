# display all the possible make commands
help:
	@echo "possible make commands:"
	@echo "    make tests        runs the testing suite"
	@echo "    make docs         generate the documentation pages (html)"

tests:
	@cd meta; pytest

docs:
	@cd docs; make html

.PHONY: help, tests, docs
