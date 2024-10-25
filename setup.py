from pathlib import Path
from setuptools import setup, find_packages

setup(
    name="md2tgmd",
    version="0.3.6",
    description="md2tgmd is a Markdown to Telegram-specific-markdown converter.",
    long_description=Path("README.md").open(encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=["md2tgmd"],
)