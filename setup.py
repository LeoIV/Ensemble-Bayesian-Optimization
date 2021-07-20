from setuptools import setup, find_packages

setup(
    name="ebo",
    version="0.0.8",
    packages=find_packages(),
    install_requires=[
        "cython",
        "numpy",
        "scipy",
        "msrest",
        "pygame",
        "Box2D",
        "box2d-py",
        "requests",
        "azure-storage==0.32.0",
        "scikit-learn"],
)
