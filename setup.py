from setuptools import setup, find_packages

setup(
    name="math-utils",
    version="0.1.0",
    author="Your Name",
    author_email="your@email.com",
    description="A library of useful math functions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)