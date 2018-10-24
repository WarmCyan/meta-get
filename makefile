# display all the possible make commands
help:
	@echo "possible make commands:"
	@echo "    make lint         runs the various python linters"
	@echo "    make tests        runs the testing suite"
	@echo "    make docs         generate the documentation pages (html)"
	@echo "    make opendocs     opens the documentation pages in a browser (utilizes xdg-open)"
	@echo "    make clean        deletes any .pyc files"

lint:
	pylint meta/*

tests:
	pytest meta/tests

docs:
	@cd docs; make html

opendocs: docs
	@cd docs/build/html; xdg-open index.html

clean:
	-rm meta/*.pyc
	-rm meta/tests/*.pyc

.PHONY: help, tests, docs, opendocs, lint, clean
