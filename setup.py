import pathlib
import setuptools
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="liberation-direct",
    version="1.0.0",
    description="Parse Libération's live news page.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/massoncl/liberation-direct",
    author="Clément Masson",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=["beautifulsoup4", "markdownify"],
    packages=["liberation_direct"],
    include_package_data=True,
)
