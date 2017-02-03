python_version_full := $(wordlist 2,4,$(subst ., ,$(shell python --version 2>&1)))
python_version_major := $(word 1,${python_version_full})
python_version_minor := $(word 2,${python_version_full})
python_version_patch := $(word 3,${python_version_full})

coverage: clean
	PYTHONPATH=$(CURDIR) coverage run  -a demo${python_version_major}/manage.py test demo${python_version_major}/
	coverage html --include="django_pycdi/*,demo2/*,demo3/*"

coverage-all: clean
	PYTHONPATH=$(CURDIR) coverage run -a demo2/manage.py test demo2/
	PYTHONPATH=$(CURDIR) coverage3 run -a demo3/manage.py test demo3/
	PYTHONPATH=$(CURDIR) coverage3 html --include="django_pycdi/*,demo2/*,demo3/*"
	python -mwebbrowser htmlcov/index.html &

public:
	python setup.py register -r pypi
	python setup.py sdist upload -r pypi

public-test:
	python setup.py register -r pypitest
	python setup.py sdist upload -r pypitest

clean:
	rm -f $(shell find . -name "*.pyc")
	rm -rf htmlcov/ coverage.xml .coverage
	rm -rf dist/ build/
	rm -rf *.egg-info


