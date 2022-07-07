from codecs import open
from os import path
from setuptools import find_packages, setup

name = "perspective_workspace_react_tornado"
pjoin = path.join
here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read().replace("\r\n", "\n")

requires = [
    "tornado",
]

requires_test = [
    "pytest>=4.3.0",
    "pytest-cov>=2.6.1",
]

requires_dev = (
    requires
    + requires_test
    + [
        "black>=20.8b1",
        "bump2version>=1.0.0",
        "check-manifest",
        "flake8>=3.7.8",
        "flake8-black>=0.2.1",
    ]
)

setup(
    name=name,
    version="0.1.0",
    description="Perspective workspace powered by tornado",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/timkpaine/perspective_workspace_react_tornado",
    author="Tim Paine",
    author_email="t.paine154@gmail.com",
    license="Apache 2.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: Jupyter",
        "Framework :: Jupyter :: JupyterLab",
    ],
    platforms="Linux, Mac OS X, Windows",
    include_package_data=True,
    zip_safe=False,
    packages=find_packages(),
    install_requires=requires,
    test_suite="perspective_workspace_react_tornado.tests",
    tests_require=requires_test,
    extras_require={
        "dev": requires_dev,
        "develop": requires_dev,
    },
    python_requires=">=3.7",
)
