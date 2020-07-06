from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="colabaudiopr_Es",
    packages=find_packages(),
    version="1.1.0",
    description="Analisis y modificacion .wav",
    author="Alejandro Higuera",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/timsainb/noisereduce",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
    ],
    install_requires=["scipy", "matplotlib","iPython","numpy"]
    }
)
