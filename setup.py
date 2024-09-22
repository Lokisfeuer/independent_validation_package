import os.path

from setuptools import find_packages, setup


def read(rel_path: str) -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    # intentionally *not* adding an encoding option to open
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            # __version__ = "0.9"
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="independent_validation",
    version=get_version("independent_validation/version.py"),
    description="This package implements an alternative to cross validation called independent validation.",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    url="https://github.com/Lokisfeuer/independent_validation_package",
    author="Lokisfeuer",
    author_email="jonas.v.oertzen@web.de",
    install_requires=[
        "numpy",
        "scikit-learn",
        "scipy",
        "matplotlib",
    ],
    extras_require={
        "dev": [
            "check-manifest",
            "twine",
            "black",
        ],
    },
)

# TODO: Edit this file:
'''
# https://gist.github.com/pouyaardehkhani/dc483e8bbfec2dc25b4725a1411c7b39
Let's dive into it:
    For changing the package name edit this name="Name_of_the_package".
    Edit this version=get_version("folder_that_contaions/version.py") to version=get_version("name_of_package/version.py").
    Write your name in here author="name", and your email here author_email="email of the author",.
    For url you can use the github repo url here url="url of the repository(mostly we use github repo url)",.
    classifiers are like tags.
    Add description of your package here description="Discription of the package",.
    In install_requires = [ write every package that your code needs in order to run properly.
'''