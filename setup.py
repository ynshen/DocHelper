"""Setup for doc_helper
See: https://github.com/ynshen/DocHelper
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dochelper',
    version='1.0',
    description='Compose docstrings with repeated arguments',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/pypa/sampleproject',
    author='Yuning Shen',
    author_email='ynshen23@gmail.com',
    license='BSD3',
    keywords='documentation docstring utility',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.5',
    install_requires=['pandas'],
    project_urls={
        'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
        'Source': 'https://github.ciw/pypa/sampleproject/',
    },
)
