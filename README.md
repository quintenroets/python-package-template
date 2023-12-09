# Python Package Template
Python package published on PyPI

## Usage
1) Choose repository name
2) Instantiate new repository from the template repository
3) Optional: configure PyPI publishing
   * Configure
     1) Chose public package name
     2) Configure trusted publisher on [PyPI](https://pypi.org/manage/account/publishing/)
     3) Update public package name in
        * pyproject.toml: name = ..
        * README.md: pip install ..
4) Configure displayed project information
   * Enable releases
   * Disable deployments and packages
5) Run
     ```shell
     python_package_template
     ```
## Installation

Make sure you are using python3.10+

```shell
pip install python-package-template
```
