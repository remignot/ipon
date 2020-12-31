# *basilic_ipy documentation*

***
## Table of Contents
* [General Info](#general-info)
* [Startup](#startup)
* [Aliases](#aliases)
* [Autoreload](#autoreload)

***
## General Info

See [```./README.md```](#./README.md). 

***
## Startup

To execute a piece of code at the start of **```basilic_ipy```**, 
you can create startup scripts in the root directory of your project. 
If one script, name it: ```./startup_basilic_ipy.py```. 
If some scripts, place them in the folder ```./startup_basilic_ipy.d/```, 
they will be launched after ```./startup_basilic_ipy.py``` (if existing), 
in alphabetical order. 

Remark: 
This is based on ```basilic.f_get_startup_code( '_basilic_ipy' )```. 
See the help of ```basilic.f_get_startup_code``` of the **```basilic```** library. 

***
## Aliases

**```basilic_ipy```** inherits all aliases and magic commands of ```ipython```. 
But others aliases are defined for ```basilic_ipy```:

* clc: CLear Command window. 

***
## Autoreload

**```basilic_ipy```** sets the ```autoreload``` option of ```ipython``` in 
order to automatically reload modified libraries. 

***
