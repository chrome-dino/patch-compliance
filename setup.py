from setuptools import setup, find_packages

setup(
    name = "patch_compliance",
    py_modules=['patch_compliance'],
    packages=find_packages(where='src'),
    package_dir={'':'src'},
)