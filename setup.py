import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="omniglot",
    version="0.2.0",
    author="Dennis Merkus",
    description="Language processing and annotation for language learning in multiple languages",
    long_description=long_description,
    url="https://github.com/DennisMerkus/omniglot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.8",
)
