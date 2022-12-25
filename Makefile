
all: compile deploy

deploy:
	rsync -ruvt html/* uberspace:html

compile:
	python compile.py
