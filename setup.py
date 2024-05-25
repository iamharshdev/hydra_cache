import os
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="hydra_cache",
    version="0.1.0",
    author="Harsh Vardhan Goswami",
    author_email="me@iamharsh.dev",
    description="A mixin that unleash the Kraken of DJANGO Caching Power",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iamharshdev/hydra_cache",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "Django>=4.2.10",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Django",
    ],
    python_requires=">=3.6",
)
