# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'guanine'
copyright = '2025, eyes robson'
author = 'eyes robson'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

html_logo = "_static/guanine_logo.png"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'shibuya'
html_static_path = ['_static']

html_sidebars = {
    "**": [
        "globaltoc.html",
    ]
}

html_theme_options = {
    "nav_links": [
        {
            "title": "Contact",
            "url": "eyes-robson.github.io",
        },
    ],
     "toctree_collapse": True
}

