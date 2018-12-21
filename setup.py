import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'ez_sten',
    version = '0.0.0',
    author = 'Dane Morgan',
    author_email = 'danemorgan91@gmail.com',
    description = 'a quick and easy way to store text in files',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/deadlift1226/ez-sten',
    install_requires = [''], #3rd party pip packages
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

