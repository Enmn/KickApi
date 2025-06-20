from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='KickApi',
    description='A Python package for interacting with the Kick API to retrieve channel and video data.',
    version='0.3.5',
    packages=find_packages(),
    install_requires=[
        'cloudscraper',
        'ua-generator'
    ],
    license="MIT",
    keywords=[
        'kick', 
        'api', 
        'kickapi',
        'live streaming',
        'kick.com',
        'video api',
        'streaming platform',
        'python kick sdk',
        'kick bot',
        'kick integration'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown', 
    author='Enmn',
    url='https://github.com/Enmn/KickApi',
)