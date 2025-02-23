# project_creator/setup.py
from setuptools import setup, find_packages

setup(
    name="codify",
    version="0.1.0",
    description="A tool to create project structures for deep learning projects.",
    author="Remosy",
    author_email="remosyxu@gmail.com",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "codify = codify.generate:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)