from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

__version__ = "0.1.0"

setup(
    name="ridge",
    version=__version__,
    author="Eshin Jolly",
    author_email="eshin.jolly.gr@dartmouth.edu",
    install_requires=requirements,
    license="LICENSE.txt",
    description="A very fast ridge regression implementation for machine-learning.",
    keywords=[
        "modeling",
        "regression",
        "analysis",
        "cross-validation",
        "regularization",
    ],
    packages=["ridge"],
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
    ],
)
