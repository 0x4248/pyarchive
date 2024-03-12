# pyarchive
# Quickly create and manage archives for large amount of data
# GitHub: https://www.github.com/lewisevans2007/pyarchive
# Licence: GNU General Public License v3.0
# By: Lewis Evans
        print(Fore.GREEN+"[+] "+Style.RESET_ALL+message)

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyarchive',
    url='',
    author='Lewis',
    packages=['pyarchive'],
    install_requires=[''],
    version="0.1",
    license='',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='Quickly create and manage archives for large amount of data'
)
