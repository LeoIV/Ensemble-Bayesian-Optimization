from setuptools import setup, find_packages

setup(
    name="ebo",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["numpy",
                      "scipy",
                      "msrest",
                      "requests",
                      "azure-storage==0.32.0",
                      "scikit-learn"],
)
