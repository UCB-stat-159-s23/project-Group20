.ONESHELL:
SHELL = /bin/bash

## env: creates and configures the environment
.PHONY : env 
env :
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml -p ~/envs/housing
	conda activate housing
	conda install ipykernel
	python -m ipykernel install --user --name housing --display-name "IPython - housing"

## all: runs the notebook
.PHONY : all
all :
	jupyter execute code_notebook.ipynb

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