# Python Package Template

## Usage
1) Choose repository name
2) Instantiate new repository from the template repository
3) Enable or disable PyPI publishing
   * Enable
      1) Choose public package name
      2) Configure trusted publisher on [PyPI](https://pypi.org/manage/account/publishing/)
      3) Update public package name
         * pyproject.toml: update `name = ..`
         * README.md:
           * update `pip install ..`
           * remove `pip install git+https://github.com..`
   * Disable
      1) README.md: remove `pip install python-package-qtemplate`
5) Configure displayed project information
   * Enable releases
   * Disable deployments and packages
=============================================================
Run
```shell
python_package_template
```
## Installation
```shell
pip install python-package-qtemplate
```
or
```shell
pip install git+https://github.com/quintenroets/python-package-template
```

Make sure you are using python3.10+
