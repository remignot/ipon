#!/usr/bin/env python3

# ------------------------------------------------------------------------------
"""
  Setup file of ipon. 

  Author: Rémi Mignot, 2020.
"""

from setuptools import setup 

# Load requirements: 
with open('requirements.txt') as f:
  requirements = f.read().splitlines()
  
  
# Problem with 'install_requires' and distant git repositories... 
# use $ pip install -r requirements.txt
for req in requirements:
  if req.find( '://' ) != -1: requirements.remove( req ); 
  
  
# ------------------------------------------------------------------------------
# Setup configuration
setup(
  name        = 'ipon', 
  version     = '0.1.1', 
  author      = 'Rémi Mignot', 
  # author_email = 'no@email.com', 
  packages    = [ 'ipon' ], 
  scripts     = [ 'ipon/bin/ipon' ], 
  url         = 'https://github.com/remignot/ipon', 
  license     = 'LICENSE.txt', 
  keywords    = [ 'ipython', 'shell', 'basilic' ], 
  description = 'A good prompt for python, based on ipython.', 
  long_description = open( 'README.md' ).read(), 
  
  include_package_data = True,
  package_data \
    = { 'ipon': [ 'data/*', 'data/*/*', 'data/*/*/*' ] },
  
  python_requires   = '>=3',
  install_requires  = requirements, 
)
