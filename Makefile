.ONESHELL:
SHELL = /bin/bash

## env: creates and configures the environment
.PHONY : env 
env :
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml 
	conda activate housing
	conda install ipykernel
	python -m ipykernel install --user --name ligo --display-name "IPython - ligo"

## html: build the JupyterBook normally
.PHONY : html 
html: 
	jupyter-book build . 

## clean: clean up the figures folder
.PHONY : clean
clean: 
	rm -rf figures/*

.PHONY : help
help : Makefile
	@sed -n '/^##/p' $<