#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['pep440']

package_data = \
{'': ['*']}

extras_require = \
{'lint': ['check-manifest', 'mypy'],
 'test': ['pytest-console-scripts', 'pytest-cov', 'pytest']}

entry_points = \
{'console_scripts': ['pep440 = pep440.__main__:main']}

setup(name='pep440',
      version='%%PORTVERSION%%',
      description='A simple package with utils to check whether versions number match PEP 440.',
      author=None,
      author_email='Matthias Bussonnier <bussonniermatthias@gmail.com>',
      url=None,
      packages=packages,
      package_data=package_data,
      extras_require=extras_require,
      entry_points=entry_points,
      python_requires='>=3.7',
     )
