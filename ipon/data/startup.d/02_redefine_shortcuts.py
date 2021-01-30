# ------------------------------------------------------------------------------
"""
  ipon reset behaviour of some ipython shortcuts. 
  
  Author: Rémi Mignot, 2021.
"""

# ------------------------------------------------------------------------------
"""
  Remark
  - Web pages to see: 
    https://stackoverflow.com/questions/45599850/leave-incomplete-line-on-screen-when-hitting-ctrl-c-in-ipython-5-0
    https://ipython.readthedocs.io/en/latest/config/details.html#keyboard-shortcuts   
"""


# Only script...
if __name__ == "__main__":
  
  
  # ----------------------------------------------------------------------------
  def __f_main_redefine_shortcut():
    """ Main function to redefine shortcuts """
    
    import IPython
    
    
    # ------------------------------------------------------------------
    # Sub-function definitions, locally to the main function: 
    
    # ----------------------------------------------------------
    def f_get_values():
      """ Sub-function: get registry, redraw_args and doprint """
      
      ipy_tmp = IPython.get_ipython()
      try:
        # IPython 5-6; render_as_done doesn't exist, but manual print works
        registry    = ipy_tmp.pt_cli.application.key_bindings_registry
        redraw_args = {}
        doprint     = True
        
      except AttributeError:
        # IPython 7+; render_as_done necessary, and removes need for print
        registry    = ipy_tmp.pt_app.key_bindings
        redraw_args = {'render_as_done': True}
        doprint     = False
      #.endtry
        
      return registry, redraw_args, doprint
    #.enddef


    # ----------------------------------------------------------
    def f_on_ctrl_c( event ):
      """ Redifine Ctrl+c shortcut to behave as the cpython Ctrl+c shortcut """    
        
      # Get redraw_args and doprint: 
      _, redraw_args, doprint = f_get_values()    
      
      # Actions:
      line_length = len(event.cli.current_buffer.text)      
      if line_length > 0:
        event.cli.current_buffer.text += ' ^C'
      line_length = len(event.cli.current_buffer.text)      
      event.cli.current_buffer.cursor_position = line_length
      event.cli._redraw(**redraw_args)  
      if doprint: print()
      event.cli.reset() 
      event.cli.current_buffer.reset()       
    #.enddef __f_on_ctrl_c
    
    
    # ----------------------------------------------------------
    def f_on_ctrl_y( event ):  
      """ Add Crtl+y shortcut to add the current line into the history """  
      if event.cli.current_buffer.text.strip():
        event.cli.current_buffer.append_to_history()    
      ooo = event.cli.current_buffer
    #.enddef __f_on_ctrl_y
    
    
    # ----------------------------------------------------------
    def f_on_ctrl_shift_delete( event ):  
      """ Add Crtl+Shift+delete shortcut as the initial ipython Crtl+c """  
      event.cli.current_buffer.cursor_position = 0
      event.cli.current_buffer.text = '' 
    #.enddef __f_on_ctrl_shift_delete
    
    
    # ------------------------------------------------------------------
    # Actions of the main function: 
    
    # Importation (internal to the main function)
    from prompt_toolkit.enums   import DEFAULT_BUFFER
    from prompt_toolkit.keys    import Keys
    from prompt_toolkit.filters import HasFocus, ViInsertMode, EmacsInsertMode
      
    # Get registry, and set the actions for shortcuts
    try:    
      registry, _, _ = f_get_values()    
      
    except AttributeError:
      pass  # Old IPython doesn't need special handler
      
    else:
      
      # ControlY
      registry.add_binding(Keys.ControlY,
          filter=(HasFocus(DEFAULT_BUFFER) & (ViInsertMode() | EmacsInsertMode()))
          )(f_on_ctrl_y)
      
      # ControlC
      registry.add_binding(Keys.ControlC,
          filter=(HasFocus(DEFAULT_BUFFER) & (ViInsertMode() | EmacsInsertMode()))
          )(f_on_ctrl_c)
      
      # ControlShiftDelete
      registry.add_binding(Keys.ControlShiftDelete,
          filter=(HasFocus(DEFAULT_BUFFER) & (ViInsertMode() | EmacsInsertMode()))
          )(f_on_ctrl_shift_delete)
      
    #.endtry
  #.enddef __f_main_redefine_shortcut
  
  
  
  # ----------------------------------------------------------------------------
  # Call the main function:
  __f_main_redefine_shortcut()  
  del __f_main_redefine_shortcut

#.endif __main__
