from setuptools import setup, find_packages

# You can have one or more plugins.  Just list them all here.
# For each one, add a setup function in plugins/__init__.py
#
entry_points = """
[ginga.rv.plugins]
mosaicauto=plugins:setup_mosaicauto
backgroundsub=plugins:setup_backgroundsub
"""

setup(
    name='ginga_plugin_exp',
    version="0.1.dev",
    description="Experimental plugins for the Ginga reference viewer",
    author="Pey Lian Lim",
    license="BSD",
    # change this to your URL
    url="http://github.com/pllim/ginga_plugin_exp",
    install_requires=["ginga>=2.6.1"],
    packages=find_packages(),
    include_package_data=True,
    package_data={},
    entry_points=entry_points
)
