# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'guanine'
copyright = '2025, eyes robson'
author = 'eyes robson'
release = '1.0.5'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_design"]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'shibuya'
html_static_path = ['_static']
root_doc = 'toctree'

html_sidebars = {
    "**": ["localtoc.html",
           "sidebars/repo-stats.html",
           "sidebars/edit-this-page.html"]
}

html_context = {
        "source_type": "github",
        "source_user": "ni-lab",
        "source_repo": "guanine"
}

html_extra_path = ['robots.txt']

html_theme_options = {
    "nav_links": [
        {
            "title": "Contact",
            "url": "https://eyes-robson.github.io",
        },
        {
            "title": "v1.0.5 Release",
            "url": "release-notes",
        },
        {
            "title": "Contributing",
            "url": "contributing",
        },
        {
            "title": "Citing GUANinE",
            "url": "license"
        },
    ],
     "globaltoc_expand_depth": 1,
     "toctree_collapse": False,
     "light_logo": "_static/guanine_logo.png",
     "dark_logo": "_static/guanine_logo_dark.png",
     "github_url": "https://github.com/ni-lab/guanine",
}

