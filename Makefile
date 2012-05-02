# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         = 
DOCDIR        = doc
BUILDDIR      = $(DOCDIR)/_build
APPNAME	      = apptemplate

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) ./doc
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help clean htmldoc apidoc doc sdist uploaddoc

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  htmldoc       to make HTML doc files"
	@echo "  apidoc        to make module doc files"
	@echo "  doc           to make HTML and module doc files"
	@echo "  uploaddoc     to upload doc files to server"
	@echo "  sdist         to make and upload a sdist file"

clean:
	-rm -rf $(DOCDIR)/_build
	-rm -rf $(DOCDIR)/apidoc

htmldoc: 
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

apidoc:
	sphinx-apidoc -o doc/apidoc/ $(APPNAME) -f
	@echo
	@echo "Apidoc built."
	
doc: apidoc htmldoc
	@echo
	@echo "Doc built"
		
uploaddoc: 
	@echo
	@echo "Docs uploaded"	
	
sdist: doc uploaddoc
	python setup.py sdist upload -r local
	@echo
	@echo "sdist built and uploaded"

