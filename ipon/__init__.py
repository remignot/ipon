# ------------------------------------------------------------------------------
"""
  ipython based basilic interpeter

  Call basilic interpeter based on ipython, from a python console. 
  
  >>> import ipon
  >>> ipon.start()

  Author: Rémi Mignot, 2020.
"""


# ------------------------------------------------------------------------------
# Check modules...
try:   
  import IPython, pygments, basilic
  
except ModuleNotFoundError:       
  requirement_file = os.path.dirname(__file__) + '/data/requirements.txt' 
  raise ModuleNotFoundError( 
    "\n\n\033[1m\033[91m"
    "Missing required modules, install all using: \n" 
    "$ pip install -r %s \033[0m\n" %  requirement_file )  

else:
  del IPython, pygments, basilic
#.endtry 


# ------------------------------------------------------------------------------
def start(  ): 
  """ Start ipon interpreter. """
  
  # Imports
  import sys, IPython
  
  # Check: not from IPython... 
  _f_check_not_from_IPtyhon()
  
  # Check the version: only python3 ! 
  __f_check_python_version()
      
  # Check if it is a linux kernel
  __f_check_linux()
  
  # Check (and update) the profil 
  __f_check_profile()
    
  # Get the option for the history file 
  history_option_k = __f_get_history_file()
  
    
  # -----------------------------------------------------------------
  # Launch ipython with : ipon
  
  # Arguments: profile, etc..., + arguments of the fonction
  args_ipy = [  history_option_k, \
                '--no-banner', \
                '--profile=ipon' ] \
              + sys.argv[ 1: ]
  
  
  # Call ipython with arguments...  
  sys.exit( IPython.start_ipython( args_ipy ) )  
  # ------------------------------------------------------------  
#.enddef 'start'


# ------------------------------------------------------------------------------
def __f_check_python_version():  
  """ Check the python version """
  import sys
  if sys.version_info.major != 3: 
    raise Exception( "\"ipon\" only works with python3 ! " ) 
  #.endif
#.enddef '__check_python_version'


# ------------------------------------------------------------------------------
def __f_check_linux():
  """ Check if working on linux """
  
  import sys
  if sys.platform != 'linux':
    warning_messages_v = \
    ( 'WARNING: ipon has been developped and tested with GNU/Linux only.', 
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
  #.endif
#.enddef '__check_linux'


# ------------------------------------------------------------------------------
def __f_check_profile():
  """ Check profile """   
  import ipon.__check_profile
  ipon.__check_profile.__f_run();  
#.enddef '__check_profile'


# ------------------------------------------------------------------------------
def _f_check_not_from_IPtyhon():
  """ Check, the interpreter cannot be launched from IPython """  
  import IPython
  if IPython.get_ipython().__class__.__name__ == 'TerminalInteractiveShell':
    raise Exception(  '"ipon" cannot be launched from ipython, ' + \
                      'but it can be launched from python, or cpython. ' ) 
#.enddef _f_check_not_from_IPtyhon


# ------------------------------------------------------------------------------
def __f_get_history_file():
  """ Get the history file to use... """  
  import ipon.history, os
  ipon_hist_file_name =  os.path.abspath( os.getcwd() ) + '/' \
                        + ipon.history.__f_get_std_file_name()  
  if os.path.isfile( ipon_hist_file_name  ):    
    history_option_k = '--HistoryManager.hist_file=%s' % ipon_hist_file_name 
  else:
    history_option_k = ''
  
  return history_option_k
#.enddef __f_get_history_file
