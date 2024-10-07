from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pytreeview",
    version="0.1.0",
    author="mhhio",
    author_email="mhhajivandy@gmail.com",
    description="A tool to generate a tree-like structure of files inside specific directory in Markdown format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mhhio/treeview",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "pytreeview=pytreeview.main:main",
        ],
    },
)