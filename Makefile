install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	black *.py	
#test:
#	python -m pytest -vv --cov testadd.py
lint:
	pylint --disable=R,C main.py