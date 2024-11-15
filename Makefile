#PYTHONEXE=trainscanner_gui.py pass1_gui.py stitch_gui.py shakereduction.py rect.py helix.py hans_style.py film.py add_instruction.py
#PYTHONLIB=canvas.py imagebar.py pass1.py imageselector2.py qrangeslider.py trainscanner.py stitch.py
PIP=pip3
PYTHON=python3

all: #macapp install #macapp-personally
	echo There is no 'all' to be built for now.

##############################
#  PyPI
##############################
prepare: # might require root privilege.
	$(PIP) install twine

test-deploy: build
	twine upload -r pypitest dist/*
test-install:
	$(PIP) install --index-url https://test.pypi.org/simple/ trainscanner



install:
	$(PYTHON) ./setup.py install
uninstall:
	-$(PIP) uninstall -y trainscanner
build: README.md $(wildcard trainscanner/*.py)
	$(PYTHON) ./setup.py sdist # bdist_wheel


deploy: build
	twine upload dist/*
check:
	$(PYTHON) ./setup.py check
clean:
	-rm $(ALL) *~ */*~
	-rm -rf build dist *.egg-info
	-find . -name __pycache__ | xargs rm -rf

# old stuff
test1: test1.png
test1.png: test1.tsconf
	$(PYTHON) ./stitch_gui.py @$<
test1.tsconf:
	$(PYTHON) ./pass1_gui.py examples/sample.mov --log test1
distclean:
	-rm -rf dist build *.egg-info __pycache__ *.pyc
	make -C examples distclean
