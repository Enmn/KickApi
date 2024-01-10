from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='KickApi',
    description='A Python package for interacting with the Kick API to retrieve channel and video data.',
    version='0.3.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    license="MIT",
    keywords=['kick', 'api', 'kickapi'],
    long_description=long_description,
    long_description_content_type='text/markdown', 
    author='Enmn',
    url='https://github.com/Enmn/KickApi',
)