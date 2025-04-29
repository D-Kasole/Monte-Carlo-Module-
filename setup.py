from setuptools import setup, find_packages

setup(
    name='montecarlo',
    version='1.0.0',
    url='https://github.com/D-Kasole/Monte-Carlo-Module-',
    author='Didier Kasole',
    author_email='xbw8de@virginia.edu',
    description='This simulator rolls customizable letter dice, stores the outcomes, and analyzes permutations to identify valid words',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

