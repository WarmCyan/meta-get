# display all the possible make commands
help:
	@echo "possible make commands:"
	@echo "    make tests        runs the testing suite"
	@echo "    make docs         generate the documentation pages (html)"
	@echo "    make opendocs     opens the documentation pages in a browser (utilizes xdg-open)"

tests:
	@cd meta; pytest

docs:
	@cd docs; make html

opendocs: docs
	@cd docs/build/html; xdg-open index.html

.PHONY: help, tests, docs, opendocs
