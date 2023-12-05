from setuptools import setup, find_packages

version = "0.0.1"
author = "JJSepulveda"

setup(
    name="ofacturama",
    version=version,
    author=author,
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    license="MIT License",
    keywords="facturama",
)
