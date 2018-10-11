from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'readme.md')) as f:
  readme = f.read()

setup(
    name="username_validator",
    version="0.0.1",
    url="https://github.com/ogrodnek/username_validator",
    description="Username validation",
    author="Larry Ogrodnek",
    author_email="larry@ogrodnek.com",
    license="BSD",
    long_description = readme,
    long_description_content_type="text/markdown",
    classifiers=[
      "Programming Language :: Python :: 2.7",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.7",
      "License :: OSI Approved :: BSD License"
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
      "confusable_homoglyphs"
    ]
)
