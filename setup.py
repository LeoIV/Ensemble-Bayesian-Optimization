from setuptools import setup, find_packages

setup(
    name="ebo",
    version="0.0.5",
    packages=find_packages(),
    install_requires=[
        "cython",
        "numpy",
        "scipy",
        "msrest",
        "scikit-sparse",
        "pygame",
        "Box2D",
        "requests",
        "azure-storage==0.32.0",
        "scikit-learn"],
)
