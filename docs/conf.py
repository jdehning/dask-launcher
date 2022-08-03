"""Sphinx configuration."""
project = "Dask Launcher"
author = "Jonas Dehning"
copyright = "2022, Jonas Dehning"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
