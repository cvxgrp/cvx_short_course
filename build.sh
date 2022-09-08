#!/bin/bash
pip install jupyter-book jupyter-cache
jupyter-book clean book
jupyter-book build book
