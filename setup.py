import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = "ANN-implementation" 
USER_NAME = "YogeshRajgure"

setuptools.setup(
    name= f"{PROJECT_NAME}-{USER_NAME}",
    version="1.0.1",
    author=USER_NAME,
    author_email="yogeshrajgure.vraj@gmail.com",
    description="Its an implementation of ANN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YogeshRajgure/ANN-implementation",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",

    install_requirements=[
        "numpy",
        "matplotlib",
        "pandas",
        "seaborn",
        #"tensorflow"
    ]
)