from setuptools import setup
from setuptools import find_packages

setup(
    name='a_la_romana_services',
    version='0.1.0',
    author='Guido Barbaglia',
    author_email='guido.barbaglia@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    description='REST services for the "A-la Romana" project.',
    install_requires=[
        'watchdog', 'flask', 'flask-cors'
    ],
    url='http://pypi.python.org/pypi/a_la_romana_services/'
)