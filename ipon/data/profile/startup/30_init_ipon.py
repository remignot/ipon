# ------------------------------------------------------------------------------
"""
  Call startup scripts for ipon. 

  Author: Rémi Mignot, 2021.
"""


# Only script...
if __name__ == "__main__":
  
  # Import librairies
  import ipon as __ipon_tmp
  import inspect as __inspect_tmp
  import basilic as __bc_tmp
  import os as __os_tmp
    
  # Get the directory which contains the startup scripts (inside the ipon module)
  __startup_dir_tmp = __os_tmp.path.dirname( __inspect_tmp.getfile( __ipon_tmp ) ) + '/data' 
  
  # Get and execute the code: 
  exec( __bc_tmp.f_get_startup_code( directory_k=__startup_dir_tmp )  ) 
  
  # Clean up the variables
  del __ipon_tmp, __bc_tmp, __os_tmp, __inspect_tmp, __startup_dir_tmp
  
#.endif __main__
