from pathlib import Path

from setuptools import setup, find_packages

version = "0.2.0"

# Read the contents of README file
source_root = Path(".")
with (source_root / "README.md").open(encoding="utf-8") as f:
    long_description = f.read()

# Read the requirements
with (source_root / "requirements.txt").open(encoding="utf8") as f:
    requirements = f.readlines()

with (source_root / "src" / "cqu_jxgl" / "version.py").open(
        "w", encoding="utf-8"
) as f:
    f.writelines(
        [
            '"""This file is auto-generated by setup.py, please do not alter."""\n',
            f'__version__ = "{version}"\n',
            "",
        ]
    )

setup(
    name="cqu-jxgl",
    version=version,
    description="第三方重庆大学教务处登录模块",
    author='maxoyed',
    author_email='maxoyed@gmail.com',
    maintainer="CQU-AI",
    maintainer_email="peter@mail.loopy.tech",
    url="https://github.com/CQU-AI/cqu-jxgl",
    license="GPL License",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"": ["config_default.yaml"]},
    platforms=["all"],
    install_requires=requirements,
    python_requires=">=3.6",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
