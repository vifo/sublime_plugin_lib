all: docs

docs: docs-html

docs-html:
	cd sublime_plugin_lib/docs && make html

clean:
	cd sublime_plugin_lib/docs && make clean
	find . -name '__pycache__' -and -type d -print0 | xargs -0 --no-run-if-empty rm -rf
	find . -name '*.pyc' -and -type f -print0 | xargs -0 --no-run-if-empty rm -rf
	find . -name '*.py' -and -type f | xargs --no-run-if-empty chmod 644

.PHONY: clean docs
