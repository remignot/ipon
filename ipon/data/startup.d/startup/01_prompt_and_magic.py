# ------------------------------------------------------------------------------
"""
  Initialisation of the ipon prompt, and ipython magic command. 

  Author: Rémi Mignot, 2020.
"""


# Only script...
if __name__ == "__main__":
  
  
  # ----------------------------------------------------------------------------
  def __main_init_ipon():
    """ Main function to initialise ipon """
    
    
    # --------------------------------------------------
    # Locally import modules
    import sys
    import IPython
    from IPython.terminal.prompts import Prompts
    from IPython.terminal.prompts import Token
    
    
    # --------------------------------------------------
    # Print the python version: 
    ver = sys.version_info
    print( '""" ipon with python%s.%s.%s """' \
          %  ( ver.major, ver.minor, ver.micro ) )
    
    
    # --------------------------------------------------
    class MyPrompt( Prompts ):
      """ Class for the prompt of ipon. """
      
      # See:
      # - https://stackoverflow.com/questions/38275585/adding-color-to-new-style-ipython-v5-prompt
      # - https://ipython.readthedocs.io/en/stable/config/details.html#custom-prompts
      
      # Prompt in
      def in_prompt_tokens( self, cli=None ):
        return [ ( Token.Prompt, '>)> ' ) ]
      
      # Prompt out (to print the result)
      def out_prompt_tokens( self ):
        return [ ( Token.OutPrompt, '    ' ) ]
      
      # Prompt for the continuation of the commend on a new line... 
      def continuation_prompt_tokens( self, cli=None, width=None ):
        return [ ( Token.PromptNum, '... ' ) ]      
    #.endclass __MyPrompt
    
    
    # --------------------------------------------------
    # ipython settings : 
    
    # See: https://ipython.readthedocs.io/en/stable/interactive/magics.html 
    
    # Get a handle to IPython
    ipy_tmp = IPython.get_ipython( )
    
    # Basilic prompt
    ipy_tmp.prompts = MyPrompt( ipy_tmp )
      
    # IPython magic commands:  
    
    # To reload the modified packages
    ipy_tmp.magic( '%load_ext autoreload' )
    ipy_tmp.magic( '%autoreload 2' )
    
    # Set Aliases for an easier interactive use of iPython
    ipy_tmp.magic( '%alias clc clear' )
    
  #.enddef __main_init_ipon
  
  
  
  # ----------------------------------------------------------------------------
  # Main code: 
  
  # ----------------------------------------------
  # Import packages and libraries 
  #   -> they remain in the environment...
  import ipon 
  import basilic as bc 
  import os,sys 
  
  # ----------------------------------------------
  # Call the main function:
  __main_init_ipon()
  del __main_init_ipon
  
#.endif __main__
