testpy: ## Clean and Make unit tests
	python -m pytest -v perspective_workspace_react_tornado/tests --cov=perspective_workspace_react_tornado --junitxml=python_junit.xml --cov-report=xml --cov-branch

testjs: ## Clean and Make js tests
	cd js; yarn test

test: tests
tests: testpy testjs ## run the tests

lintpy:  ## Black/flake8 python
	python -m black --check perspective_workspace_react_tornado setup.py
	python -m flake8 perspective_workspace_react_tornado setup.py

lintjs:  ## ESlint javascript
	cd js; yarn lint

lint: lintpy lintjs  ## run linter

fixpy:  ## Black python
	python -m black perspective_workspace_react_tornado/ setup.py

fixjs:  ## ESlint Autofix JS
	cd js; yarn fix

fix: fixpy fixjs  ## run black/tslint fix

check: checks
checks:  ## run lint and other checks
	check-manifest -v

build:  ## build python/javascript
	python -m build .

develop:  ## install to site-packages in editable mode
	python -m pip install --upgrade build pip setuptools twine wheel
	cd js; yarn
	python -m pip install -e .[develop]

watchjs:  ## watch for javacsript changes and rebuild
	cd js; yarn watch

watchpy:   ## watch for python changes and restart
	python -m perspective_workspace_react_tornado --watch

watch:  ## watch for changes and rebuild
	make -j2 watchjs watchpy

install:  ## install to site-packages
	python -m pip install .

dist: clean build  ## create dists
	python -m twine check dist/*

publishpy:  ## dist to pypi
	python -m twine upload dist/* --skip-existing

publish: dist publishpy  ## dist to pypy

clean: ## clean the repository
	find . -name "__pycache__" | xargs  rm -rf
	find . -name "*.pyc" | xargs rm -rf
	find . -name ".ipynb_checkpoints" | xargs  rm -rf
	rm -rf .coverage coverage *.xml build dist *.egg-info lib node_modules .pytest_cache *.egg-info
	rm -rf perspective_workspace_react_tornado/static
	cd js && yarn clean
	git clean -fd

# Thanks to Francoise at marmelab.com for this
.DEFAULT_GOAL := help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

print-%:
	@echo '$*=$($*)'

.PHONY: testjs testpy tests test lintpy lintjs lint fixpy fixjs fix checks check build develop watch install dist publishpy publish clean
