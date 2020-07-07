from distutils.core import setup

with open("README.md", "r",encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name="colabaudiopr_es",
    packages=['colabaudiopr_es'],
    version="1.0",
    description="Implementación para el análisis y modificacion de archvos .wav en Google Colaboratory",
    author="Alejandro Higuera",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email='ahiguerac@unal.edu.co',
    keywords=["Manipulation","Spanish","Audio","WAVFILE"],
    url="https://github.com/DarkNightSoldier/ColabAudioProcessing",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Education",
        "Topic :: Scientific/Engineering",
    ],
    install_requires=["scipy", "matplotlib","iPython","numpy"]
)
