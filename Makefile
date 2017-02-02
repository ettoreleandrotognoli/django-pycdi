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


