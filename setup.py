"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = []

setup_requirements = []
develop_requirements = ["ipython", "unittest", "ipdb", "black", "pre-commit", "watchdog", "sphinx", "coverage",
                        "sphinx-rtd-theme"]
test_requirements = []

setup(
    author="Jeffrey Ma",
    author_email="mjw814@163.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    description="Jingwei AI Kit for AI exploration and development.",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords="JAIKit",
    name="JAIKit",
    packages=find_packages(include=["JAIKit*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/DoliteMatheo/JAIKit.git",
    version="0.0.0",
    zip_safe=False,
)