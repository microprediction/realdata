import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="realdata",
    version="0.1.0",
    description="Get real univariate time series data easily for testing",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/microprediction/realdata",
    author="microprediction",
    author_email="pcotton@intechinvestments.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["realdata"],
    test_suite='pytest',
    tests_require=['pytest'],
    include_package_data=True,
    install_requires=["timemachines>=0.15.0","pandas"],
    entry_points={
        "console_scripts": [
            "realdata=realdata.__main__:main",
        ]
    },
)
