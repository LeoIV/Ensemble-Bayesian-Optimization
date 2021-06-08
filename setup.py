from setuptools import setup, find_packages

setup(
    name="ebo",
    version="0.0.6",
    packages=find_packages(),
    install_requires=[
        "cython",
        "numpy",
        "scipy",
        "msrest",
        "pygame",
        "Box2D",
        "requests",
        "azure-storage==0.32.0",
        "scikit-learn"],
)
