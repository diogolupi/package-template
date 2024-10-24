# setup.py
from setuptools import setup, find_packages

setup(
    name='image_processing_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
    author='Riam Martinelli',
    author_email='riammartinelli@hotmail.com',
    description='A simple image processing package with basic filters and transformations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/richboyyy/package-template',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
