from setuptools import find_packages, setup

setup(
    name="financial_pipeline",
    packages=find_packages(exclude=["financial_pipeline_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-webserver"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
