# ------------------------------------------------------------------------------
"""
  ipython based basilic interpeter

  Call basilic prompt based on ipython, from a python console. 
  
  >>> import basilic_ipy
  >>> basilic_ipy.start()

  Author: Rémi Mignot, 2020.
"""


# --------------------------------------------------------------------------
# Import and check modules...
import sys
try:   
  import IPython
  import pygments
  import setuptools
  import basilic
except ModuleNotFoundError:     
  import os
  requirement_file = os.path.dirname(__file__) + '/data/requirements.txt' 
  raise ModuleNotFoundError( 
    "\n\n\033[1m\033[91m"
    "Missing required modules, install all using: \n" 
    "$ pip install -r %s \033[0m\n" %  requirement_file )  
#.endtry 


# --------------------------------------------------------------------------
def start(  ): 
  """ Start basilic_ipy interpreter. """
  
  # Check the version: only python3 ! 
  __f_check_python_version()
      
  # Check if it is a linux kernel
  __f_check_linux()
  
  # Check (and update) the profil 
  __f_check_profile()
  
  
  # -----------------------------------------------------------------
  # Launch ipython with : basilic_ipy
  
  # Arguments: profile, etc..., + arguments of the fonction
  args_ipy = [  \
                '--no-confirm-exit', \
                '--no-banner', \
                '--InteractiveShellApp.extensions=autoreload', \
                '--profile=basilic_ipy' ] \
              + sys.argv[ 1: ]
  
  # Call ipython with arguments...  
  sys.exit( IPython.start_ipython( args_ipy ) )  
  # ------------------------------------------------------------
  
#.enddef 'start'


# --------------------------------------------------------------------------
def __f_check_python_version():  
  if sys.version_info.major != 3: 
    raise Exception("\"basilic_ipy\" only works with python3 ! ") 
#.enddef '__check_python_version'


# --------------------------------------------------------------------------
def __f_check_linux():
  if sys.platform != 'linux':
    warning_messages_v = \
    ( 'WARNING: basilic_ipy has been developped and tested with GNU/Linux only.', 
      'WARNING: tux is beautiful !!!', 
      'WARNING: tux is the champion, my friends, tada, tada...', 
      'WARNING: the apple is rotten, linux is wonderful.', 
      'WARNING: try the command: "C:\ format C:", then install linux', 
      'PERKELE! you\'re not on linux, change your OS ASAP !' )
    
    import random
    n_mess    = len(warning_messages_v)    
    imessage  = random.randint(2, n_mess*10 ) 
    imessage  = imessage if imessage <= n_mess else 1
    print( '\033[91m' + warning_messages_v[ imessage - 1 ] + '\033[0m'  )
#.enddef '__check_linux'


# --------------------------------------------------------------------------
def __f_check_profile():
  import basilic_ipy.__check_profile
  basilic_ipy.__check_profile.__f_run();  
#.enddef '__check_profile'
