#!/usr/bin/env python3

# ------------------------------------------------------------------------------
"""
  Setup file of basilic_ipy. 

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
  name        = 'basilic_ipy', 
  version     = '0.1.0', 
  author      = 'Rémi Mignot', 
  # author_email = 'no@email.com', 
  packages    = [ 'basilic_ipy' ], 
  scripts     = [ 'basilic_ipy/bin/basilic_ipy' ], 
  url         = 'https://github.com/remignot/basilic_ipy', 
  license     = 'LICENSE.txt', 
  keywords    = [ 'ipython', 'shell', 'basilic' ], 
  description = 'A good prompt for python, based on ipython.', 
  long_description = open( 'README.md' ).read(), 
  
  include_package_data = True,
  package_data \
    = { 'basilic_ipy': [ 'data/*', 'data/*/*', 'data/*/*/*' ] },
  
  python_requires   = '>=3',
  install_requires  = requirements, 
)
