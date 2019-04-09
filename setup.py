#
# (C) BLACKTRIANGLES 2019
# http://www.blacktriangles.com
#

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plotsh-com.blacktriangles",
    version="0.1.0",
    author="Howard N Smith",
    author_email="hsmith@blacktriangles.com",
    description="Simple ANSI terminal plotting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/blacktriangles/tools/plotsh",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "click"
    ]
)
