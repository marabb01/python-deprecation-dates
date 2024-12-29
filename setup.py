from setuptools import setup, find_packages

def load_requirements(filename="requirements.txt"):
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


setup(
    name="python-deprecation-dates",
    version="0.2.5",
    description="A library to fetch Python version deprecation dates from endoflife.date.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Martin Abberley",
    author_email="mart.abberley@gmail.com",
    url="https://github.com/marabb01/python-deprecation-dates",
    packages=find_packages(),
    install_requires=[load_requirements()],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
