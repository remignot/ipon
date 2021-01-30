# ------------------------------------------------------------------------------
"""
  Launch startup script(s):  
    ./startup_basilic.py
    ./startup_basilic.d/*

  Author: Rémi Mignot, 2020-2021.
"""


# Only script...
if __name__ == "__main__":
  
  
  # Get the startup script(s) code (if any) in the current folder : 
  import basilic as __bc
  __startup_string, __n_scripts \
    = __bc.f_get_startup_code( '_basilic', True ) 
  
  
  # If scripts found
  if len( __startup_string ) > 0: 
    
    # print 
    print( '""" ipon found startup %i script(s) to execute """' 
            % __n_scripts ) 
    
    # Execute the code of the startup script(s) in the current environment
    exec( __startup_string ) 
    
  #.endif 
  
  
  # Cleaning variables of the environment
  del __bc, __startup_string, __n_scripts
  
#.endif __main__
