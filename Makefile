# taken from https://www.codementor.io/@adammertz/quick-tip-how-i-use-pip-tools-to-wrangle-dependencies-1fzreskhok
# This is usually my first target so as soon as a developer clones
# a project and creates a virtualenv they can just run `make` to get things going.
install:
	@pip install \
	-r requirements.txt \
	-r requirements-dev.txt

compile:
	@rm -f requirements*.txt
	@pip-compile --strip-extras requirements.in
	@pip-compile --strip-extras requirements-dev.in

sync:
	@pip-sync requirements*.txt
