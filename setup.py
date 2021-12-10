from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = "ANN-implementation" 
USER_NAME = "YogeshRajgure"

setup(
    name= "src",
    version="1.0.2",
    author=USER_NAME,
    author_email="yogeshrajgure.vraj@gmail.com",
    description="Its an implementation of ANN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YogeshRajgure/ANN-implementation",
    packages=["src"],
    python_requires=">=3.7",

    install_requirements=[
        "numpy",
        "matplotlib",
        "pandas",
        "seaborn",
        "PyYAML",
        "tensorflow"
    ]
)

