from setuptools import setup

setup(
package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.json", "*.toml"],
    }
)
