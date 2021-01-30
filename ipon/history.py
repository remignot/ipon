# ------------------------------------------------------------------------------
"""
  hystory manegement

  Simple management of the history of the ipon interpreter. 
  
  Author: Rémi Mignot, 2021.
"""


# ------------------------------------------------------------------------------
def __f_get_std_file_name( ):
  """ Sub-function: get the standard file name """  
  return '.history_ipon.sqlite'
#.enddef __f_get_std_file_name


# ------------------------------------------------------------------------------
def __f_reset_history( new_hist_file ):
  """ Sub-function: reset/create the input history file """
  
  from IPython.core.history import HistoryManager
  import IPython, os, time, shutil
  
  # get ipython
  ip = IPython.get_ipython()    
  
  # If we want to create a new history file at the same location, we need to 
  #   disconnect the current_hist_file beforehand
  current_hist_file = os.path.abspath( ip.history_manager.hist_file )
  if current_hist_file == new_hist_file:
    ip.history_manager = HistoryManager( shell=ip, hist_file='' )
  
  # Removal of an existing file, if any
  if os.path.isfile( new_hist_file ):
    os.remove( new_hist_file )
  
  # Creation of the new HistoryManager with the new history file: 
  ip.history_manager = HistoryManager( shell=ip, hist_file=new_hist_file )
  
#.enddef __f_reset_history

  
# ------------------------------------------------------------------------------
def create():
  """ 
    Create a new empty history file in the current directory. 
    
    The history file is so './.history_ipon.sqlite'. 
    This file will be used the next time you will start ipon from this
    directory. 
  """  
  import os
  file_name = __f_get_std_file_name()
  new_hist_file = os.path.abspath( '.' ) + '/' + file_name  
  __f_reset_history( new_hist_file )   
#.enddef create


# ------------------------------------------------------------------------------  
def clear():
  """
    Clear the currently used history file. 
  """  
  import Python, os
  ip = IPython.get_ipython()
  current_hist_file = os.path.abspath( ip.history_manager.hist_file )
  __f_reset_history( current_hist_file )  
#.enddef reset

  
# ------------------------------------------------------------------------------  
def save():
  """ 
    Save the current command history to the currently used history file. 
    
    The currently used history file is 
    - either the profile history file by default: 
      -> $HOME/.ipython/profile_ipon/history.sqlite
    - or the automatically loaded history file when having started ipon, 
    - or the previously created history file using the function 'create'. 
  """  
  import IPython  
  ip = IPython.get_ipython()  
  ip.history_manager.writeout_cache()
#.enddef save
