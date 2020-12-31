# ------------------------------------------------------------------------------
"""
  basilic_ipy profile check
  
  Check the profile files when launching basilic_ipy. 
  
  If needed, the profile is updated, and if a customization is seen, 
  it is asked to the user what he prefers to... 
  
  Author: Rémi Mignot, 2020.
"""


import IPython
import os, sys, json, shutil


# ------------------------------------------------------------------------------
# Making of statistics of the files included in "start_path", return a dictionary
def __f_make_listing_folder( start_path ):  
  stat_info_d = dict() 
  for path, notused, files_v in os.walk( start_path ): 
    for fich in files_v: 
      file_path = path + '/' + fich 
      stat_info = os.stat( file_path )       
      stat_dict = \
        { k: getattr(stat_info, k) \
          for k in dir(stat_info) if k.startswith('st_')} 
      del stat_dict[ 'st_atime' ] 
      del stat_dict[ 'st_atime_ns' ] 
      file_sub_path = file_path[ len(start_path)+1: ]
      stat_info_d[ file_sub_path ] = stat_dict 
  return stat_info_d
#.enddef '__f_make_listing_folder'


# ------------------------------------------------------------------------------  
# Making of statistics information of some files included in "start_path"
#   these files are given by: start_path + '/' + file_sub_path_v[iii]
def __f_make_listing_files( start_path, file_sub_path_v ):  
  stat_info_d = dict()   
  for file_sub_path in file_sub_path_v: 
    file_path = start_path + '/' + file_sub_path 
    if os.path.isfile( file_path ):
      stat_info = os.stat( file_path )
      stat_dict = \
        { k: getattr(stat_info, k) \
          for k in dir(stat_info) if k.startswith('st_')}  
      del stat_dict[ 'st_atime' ] 
      del stat_dict[ 'st_atime_ns' ] 
      stat_info_d[ file_sub_path ] = stat_dict    
  return stat_info_d
#.enddef '__f_make_listing_files'


# ------------------------------------------------------------------------------
# Get the file path of the 3 stored statistic information dictionaries. 
def __f_get_dictionary_file( home_profile_path ):
  return  home_profile_path + '/stat_info_ref.json', \
          home_profile_path + '/stat_info_home.json', \
          home_profile_path + '/stat_info_start.json'
#.enddef '__f_get_dictionary_file'


# ------------------------------------------------------------------------------
# Make and store the 3 stat info dict
def __f_make_dictionary_files( home_profile_path, ref_profile_path, custom_b=False ):
  stat_info_ref_profile_path, \
  stat_info_home_profile_path, \
  stat_info_start_profile_path = __f_get_dictionary_file( home_profile_path )
  
  # of reference files
  stat_info_ref_profile_d = __f_make_listing_folder( ref_profile_path )
  with open( stat_info_ref_profile_path, 'w') as fp:        
    json.dump( stat_info_ref_profile_d, fp, indent=1 )  
  
  # If the profile has been customized, the other dictionaries are not remade
  if custom_b == True:
    return
    
  # of reference files from the home profile
  stat_info_home_profile_d = \
    __f_make_listing_files( home_profile_path, stat_info_ref_profile_d.keys() )
  with open( stat_info_home_profile_path, 'w') as fp:  
    json.dump( stat_info_home_profile_d, fp, indent=1 )  
    
  # and of all files from home/startup (excepted the README)
  stat_info_start_profile_d = \
    __f_make_listing_folder( home_profile_path + '/startup'  )
  if 'README' in stat_info_start_profile_d.keys():
    del stat_info_start_profile_d['README']
  with open( stat_info_start_profile_path, 'w') as fp:  
    json.dump( stat_info_start_profile_d, fp, indent=1 )  
#.enddef '__f_make_dictionary_files'


# ------------------------------------------------------------------------------
# Preparation of the update: deletion and copy of files... 
def __f_preupdate_the_profile( home_profile_path, ref_profile_path ):
  
  # Make a backup of the history file... 
  history_file_path   = home_profile_path + '/history.sqlite'
  backup_history_path = home_profile_path + '_history.sqlite' 
  if os.path.isfile( history_file_path): 
    backup_history_path = home_profile_path + '_history.sqlite' 
    shutil.move( history_file_path, backup_history_path )
    
  # delete all the home configuration
  shutil.rmtree( home_profile_path ) 
  
  # Copy all the reference configuration files
  shutil.copytree( ref_profile_path, home_profile_path, dirs_exist_ok=True );   
  
  # Restore the history file
  if os.path.isfile( backup_history_path): 
    shutil.move( backup_history_path, history_file_path )
#.enddef '__f_preupdate_the_profile'


# ------------------------------------------------------------------------------
# Main code:
def __f_run():
  
  # Directory of the reference profile files
  this_file_path, notused = os.path.split( __file__ )   
  ref_profile_path = this_file_path + "/data/profile"  
  
  # Directory of the ipython home profile 
  home_profile_path = IPython.paths.get_ipython_dir() + '/profile_basilic_ipy' 
  
  
  # -----
  # 1) Check if the profile exists
  if not os.path.isdir( home_profile_path ): 
    
    # If not, MAKE THE PROFILE, and copy the reference files    
    print( 'Creation of the basilic_ipy profile.' )
    
    IPython.start_ipython( [ 'profile',  'create',  'basilic_ipy' ] );  
    shutil.copytree( ref_profile_path, home_profile_path, dirs_exist_ok=True );
    
    # and create the stat info dictionnaries... 
    __f_make_dictionary_files( home_profile_path, ref_profile_path )
    print(' ')
    return
  #.endif '1)'
  
  
  # -----
  # 2) Check if the reference profile files have changed since last time...
  
  # File path where to store the statistic information dictionnaries  
  stat_info_ref_profile_path, \
  stat_info_home_profile_path, \
  stat_info_start_profile_path = __f_get_dictionary_file( home_profile_path )
  
  # Load the previously stored stat info dict of reference files
  with open( stat_info_ref_profile_path ) as fp:  
    stat_info_prev_ref_profile_d = json.load( fp ) 
  
  # Making of the info dict of the current reference files
  stat_info_ref_profile_d = __f_make_listing_folder( ref_profile_path )
      
  # If idem, that's fine... in 99.9% of the time, it's fine.
  if stat_info_prev_ref_profile_d == stat_info_ref_profile_d:
    return
  
  
  # So the reference profile files has changed...
  # an update is needed... 
  
  
  # -----
  # 3) Check if the home profile has been customized since the last update ! 
  
  # Check the initial files: 
  with open( stat_info_home_profile_path ) as fp:  
    stat_info_prev_home_profile_d = json.load( fp )     
  stat_info_home_profile_d = \
    __f_make_listing_files( home_profile_path, stat_info_prev_home_profile_d.keys() )
  modified_ref_home_b = ( stat_info_home_profile_d != stat_info_prev_home_profile_d )
    
  # Check the startup content (without README)
  with open( stat_info_start_profile_path ) as fp:  
    stat_info_prev_start_profile_d = json.load( fp )    
  stat_info_start_profile_d = \
    __f_make_listing_folder( home_profile_path + '/startup'  )
  if 'README' in stat_info_start_profile_d.keys():
    del stat_info_start_profile_d['README']    
  modified_startup_b = ( stat_info_start_profile_d != stat_info_prev_start_profile_d )
  
  # If no customization, the home profile is only updated...
  if not ( modified_startup_b or modified_ref_home_b ):
    print( 'Update of the basilic_ipy profile.\n' )
    __f_preupdate_the_profile( home_profile_path, ref_profile_path );     
    __f_make_dictionary_files( home_profile_path, ref_profile_path );
    return
  #.endif
  
  
  # -----
  # 4) If change, the profile has been updated, we need to ask: 
  sentence_k = ( 
    '""" basilic_ipy update: """ \n' 
    '  the module basilic_ipy needs to be updated, \n'
    '  but it seems you have customized your basilic_ipy profile. \n'
    '    see: %s \n' 
    '  -> do you wish to: \n' 
    '       1) ask again to me later (keep it unchanged for now) ? \n'
    '       2) delete and replace your profile ? \n'
    '       3) keep it as it is now without any update ? \n'
    '       4) backup your current profile and install the new one ? \n '
    ) % home_profile_path; 
  print( sentence_k )
  
  while True:
    try:
      answer = int(input("  answer (1, 2, 3 or 4): "))
      assert( 0 < answer <= 4 )
    except:
      print( "  ¡ sorry, please only integer: 1, 2, 3 or 4 ! ")
      continue
    else:
      break
  #.endwhile


  # """ ask again to me later (keep it unchanged for now) """
  if answer == 1: 
    # Nothing to do, only exit... 
    print( ' ' )
    return
    
    
  # """ delete and replace your profile """
  elif answer == 2: 
    print( ( 'Deletion of the current basilic_ipy profile, '
             'and copy of the new profile files.' ) )
    __f_preupdate_the_profile( home_profile_path, ref_profile_path ); 
    custom_b = False;
        
    
  # """ keep it as it is now without any update """
  elif answer == 3: 
    # Nothing to do, only refresh the dictionary files, cf. below, 
    custom_b = True;
    pass; 
    
    
  # """ backup your current profile and install the new one """
  elif answer == 4: 
    print( 'Backup of the current basilic_ipy profile, and new profile created.' )
    custom_b = False;
    
    # Rename the current configuration directory: 
    from datetime import datetime
    date_now = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dirtmp_path = home_profile_path + date_now
    shutil.move( home_profile_path, backup_dirtmp_path )
    
    # Copy all the reference configuration files
    shutil.copytree( ref_profile_path, home_profile_path, dirs_exist_ok=True );   
    
    # move the backup
    backup_dir_path = home_profile_path + '/backup_' + date_now
    shutil.move( backup_dirtmp_path, backup_dir_path )
    print( '-> the backup is in ' + backup_dir_path )
    
    # restore the history
    backup_history_path = backup_dir_path + '/history.sqlite'
    if os.path.isfile( backup_history_path ):
      shutil.copy( backup_history_path, home_profile_path  + '/history.sqlite' )
    
    
  #.endif
  
  # Remake the profile, to complete the files... 
  IPython.start_ipython( [ 'profile',  'create',  'basilic_ipy' ] );  
  
  # and create the new information dictionnaries... 
  __f_make_dictionary_files( home_profile_path, ref_profile_path, custom_b )   
  print( ' ' )
    
#.endif '__f_run'
