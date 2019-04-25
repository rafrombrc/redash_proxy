import os
from setuptools import setup

_here = os.path.dirname(__file__)

setup(
    name="redash_proxy",
    packages=["redash_proxy"],
    version="0.0.1",
    entry_points={"console_scripts": ["redash_proxy=redash_proxy.server:main"]},
    description="A small server that proxies queries to a remote redash API server",
    long_description=open(os.path.join(_here, "README.rst")).read(),
    author="Rob Miller",
    author_email="rmiller@mozilla.com",
    # url="https://github.com/rafrombrc/redash_proxy",
    keywords=["redash", "proxy"],
    classifiers=[],
    install_requires=["redash_client", "flask == 1.0.2", "flask-cors"],
)
