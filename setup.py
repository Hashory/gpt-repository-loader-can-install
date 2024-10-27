from setuptools import setup, find_packages

setup(
    name="gpt-repository-loader",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here
    ],
    entry_points={
        "console_scripts": [
            "gpt-repository-loader=gpt_repository_loader.gpt_repository_loader:main",
        ],
    },
    author="mpoon, Hahory",
    author_email="89839285+Hashory@users.noreply.github.com",
    description="A command-line tool that converts the contents of a Git repository into a text format.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Hashory/gpt-repository-loader-can-install.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
