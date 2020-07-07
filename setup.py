from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="colabaudiopr_Es",
    packages=find_packages(),
    version="1.0",
    description="Implementación en Google Colab para el analisis y modificacion de archivos .wav",
    author="Alejandro Higuera",
    license="MIT",
    url="https://github.com/DarkNightSoldier/colabaudiopr_es",
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
