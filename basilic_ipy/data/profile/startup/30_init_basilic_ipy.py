# ------------------------------------------------------------------------------
"""
  Basilic prompt based on ipython. 

  Author: Rémi Mignot, 2020.
"""

# ------------------------------------------------------------------------------
"""
  Remark: 
  - cf. https://stackoverflow.com/questions/38275585/adding-color-to-new-style-ipython-v5-prompt
"""


from IPython.terminal.prompts import Prompts, Token


# ------------------------------------------------------------------------------
class __MyPrompt( Prompts ):
  """ Class for the prompt of basilic. """
    
  # --- Prompt in
  def in_prompt_tokens( self, cli=None ):
    return [ ( Token.Prompt, '>)> ' ) ]

  # --- Prompt out (to print the result)
  def out_prompt_tokens( self ):
    return [ ( Token.OutPrompt, '    ' ) ]
  
  # --- Prompt for the continuation of the commend on a new line... 
  def continuation_prompt_tokens( self, cli=None, width=None ):
    return [ ( Token.PromptNum, '... ' ) ]
      
#.endclass __MyPrompt


# ------------------------------------------------------------------------------
if __name__ == "__main__":
  """ Run commands, for a new prompt, aliases, etc... """
  
  # ----------------------------------------------
  # Import packages and libraries
  import basilic as bc
  from basilic import *
  import os,sys
  
  
  # ----------------------------------------------
  # First prints: 
  
  # Print the python version: 
  ver = sys.version_info
  print( '""" basilic_ipy with python%s.%s.%s """' \
         %  ( ver.major, ver.minor, ver.micro ) )
      
  # Print the loaded packages...
  print('>)> init basilic_ipy')
  print('>)> from basilic import *')
  print('>)> import basilic as bc')
  print('>)> import os,sys')
  
  
  # ----------------------------------------------
  # ipython settings : 
  
  # Get a handle to IPython
  __ipy_tmp = get_ipython( )
  
  # Basilic prompt
  __ipy_tmp.prompts = __MyPrompt( __ipy_tmp )
    
  # IPython magic commands:  
  
  # To reload the modified packages
  __ipy_tmp.magic( '%autoreload 2' )
  
  # Set Aliases for an easier interactive use of iPython
  __ipy_tmp.magic( 'alias clc clear' )
  
  
  # ----------------------------------------------
  # Run startup script(s) (if any) in the current folder :
  __startup_string, __n_scripts = bc.f_get_startup_code( '_basilic_ipy', True )
  if len( __startup_string ) > 0:
    print( '""" basilic_ipy found startup %i script(s) to execute """' 
            % __n_scripts )
    exec( __startup_string )    
  #.endif
  
  
  # ----------------------------------------------
  # Cleaning :
  
  # del variables and some imported packages    
  del __startup_string
  del __ipy_tmp
  del Prompts
  # del Token 
  
#.endif main for run
