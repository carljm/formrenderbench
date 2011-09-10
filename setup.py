import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "formrenderbench",
    version = "0.1",
    description = "Form rendering benchmarks",
    long_description = read('README.rst'),
    url = 'http://github.com/carljm/formrenderbench',
    license = 'BSD',
    author = 'Carl Meyer',
    author_email = 'carl@oddbird.net',
    packages = find_packages(),
    zip_safe=False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Topic :: System :: Benchmark'
    ],
    install_requires = ['djangobench'],
)
