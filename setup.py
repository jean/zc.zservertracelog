from setuptools import setup, find_packages

entry_points = """
[console_scripts]
tracereport = zc.zservertracelog.tracereport:main
"""

name = 'zc.zservertracelog'
setup(
    name = name,
    version = '0.1',
    author = 'Jim Fulton',
    author_email = 'jim@zope.com',
    description = 'Zope 3 tracelog implementation for zserver',
    license = 'ZPL 2.1',
    keywords = 'zope3',
    
    packages = find_packages('src'),
    namespace_packages = ['zc'],
    package_dir = {'': 'src'},
    install_requires = 'setuptools',
    zip_safe = False,
    entry_points=entry_points,
    )
