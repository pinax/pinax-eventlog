from setuptools import find_packages, setup

VERSION = "6.0.0"
LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/pinax-eventlog.svg
    :target: https://pypi.python.org/pypi/pinax-eventlog/

==============
Pinax EventLog
==============

.. image:: https://img.shields.io/pypi/v/pinax-eventlog.svg
    :target: https://pypi.python.org/pypi/pinax-eventlog/

\

.. image:: https://img.shields.io/github/actions/workflow/status/pinax/pinax-eventlog/test.yml?branch=master
    :target: https://github.com/pinax/pinax-eventlog/actions
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-eventlog.svg
    :target: https://codecov.io/gh/pinax/pinax-eventlog
.. image:: https://img.shields.io/github/contributors/pinax/pinax-eventlog.svg
    :target: https://github.com/pinax/pinax-eventlog/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-eventlog.svg
    :target: https://github.com/pinax/pinax-eventlog/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-eventlog.svg
    :target: https://github.com/pinax/pinax-eventlog/pulls?q=is%3Apr+is%3Aclosed

\

.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT/

\

`pinax-eventlog` provides an easy and clean interface for logging diagnostic
as well as business intelligence data about activity that occurs in your site.

Supported Django and Python Versions
------------------------------------

+-----------------+-----+------+------+------+------+
| Django / Python | 3.9 | 3.10 | 3.11 | 3.12 | 3.13 |
+=================+=====+======+======+======+======+
|  4.2            |  *  |  *   |  *   |  *   |  *   |
|  5.1            |     |  *   |  *   |  *   |  *   |
|  5.2            |     |  *   |  *   |  *   |  *   |
+-----------------+-----+------+------+------+------+
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="an event logger for Django projects",
    name="pinax-eventlog",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    version=VERSION,
    url="http://github.com/pinax/pinax-eventlog/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "eventlog": []
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.1",
        "Framework :: Django :: 5.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "django>=4.2",
    ],
    python_requires=">=3.9",
    tests_require=[
    ],
    extras_require={},
    test_suite="runtests.runtests",
    zip_safe=False
)
