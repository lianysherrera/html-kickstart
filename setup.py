from setuptools import setup

setup(
    name="html-kickstart",
    version="1.0.0",
    py_modules=["html_generator"],
    entry_points={
        "console_scripts": [
            "html-kickstart=html_generator:main",
        ],
    }
)