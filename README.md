# Python Package Template
[![PyPI version](https://badge.fury.io/py/python-package-qtemplate.svg)](https://badge.fury.io/py/python-package-qtemplate)
![PyPI downloads](https://img.shields.io/pypi/dm/python-package-qtemplate)
![Python version](https://img.shields.io/badge/python-3.10+-brightgreen)
![Operating system](https://img.shields.io/badge/os-linux%20%7c%20macOS%20%7c%20windows-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

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
           * update PyPI badge url: 1st url & 2nd url
   * Disable
      1) Update README.md:
           * remove `pip install <package-slug>`
           * remove PyPI badge
4) Configure displayed project information
   * Enable releases
   * Disable deployments and packages
5) Configure settings
   * General >
     * Automatically delete head branches
     * Always suggest updating pull request branches
     * Disable allow merge commits
   * Actions > General > Workflow permissions
     * 	Allow GitHub Actions to create and approve pull requests
6) Enable pre-commit CI
   * Add project to [pre-commit ci app](https://github.com/settings/installations/48618708)

###### ============================================================
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
pip install git+https://github.com/quintenroets/python-package-template.git
```
