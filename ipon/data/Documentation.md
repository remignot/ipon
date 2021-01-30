# *ipon documentation*

***
## Table of Contents
* [General Info](#general-info)
* [Startup](#startup)
* [Aliases](#aliases)
* [Shortcuts](#shortcuts)
* [Autoreload](#autoreload)
* [Auto Import](#auto-import)
* [History](#history)

***
## General Info

See [```./README.md```](#./README.md). 

***
## Startup

To execute a piece of code at the start of **```ipon```**, 
you can create startup scripts in the root directory of your project. 
If one script, name it: ```./startup_ipon.py```. 
If some scripts, place them in the folder ```./startup_ipon.d/```, 
they will be launched after ```./startup_ipon.py``` (if existing), 
in alphabetical order. 

Remark: 
This is based on ```basilic.f_get_startup_code( '_ipon' )```. 
See the help of ```basilic.f_get_startup_code``` of the **```basilic```** library. 

***
## Aliases

**```ipon```** inherits all aliases and magic commands of ```ipython```. 
But others aliases are defined for ```ipon```:

* ```clc```: CLear Command window. 

***
## Shortcuts

**```ipon```** inherits all shortcuts of ```ipython```. 
But some shortcuts have been redifined:

* ```ctrl+c```: cancel the current command line without clearing it. A message 
  ```KeyboardInterrupt``` is printed, and the prompt come back on a 
  new line. That's the standard behaviour of ```cpython```. 

* ```ctrl+y```: store the current command line in the history list. 

* ```ctrl+shift+delete```: clear the current command line, as the default 
  behaviour of the ```ipython ctrl+c``` shortcut. 

***
## Autoreload

**```ipon```** sets the ```autoreload``` option of ```ipython``` in 
order to automatically reload modified libraries. 

***
## Auto Import

At startup, **```ipon```** automatically import modules for an fast use. 
The imported modules are: 
```sys```, ```os```, ```ipon```, and 
```basilic``` imported as ```bc```. 

***
## History

**```ipon```** makes possible to store the command histories separately 
for each project. 
To create a new history in the current directory (main directory of your project)
enter: 
```
>>> import ipon.history
>>> ipon.history.create()
```

A file ```./.history_ipon.sqlite``` is created to store the new input 
commands. At the launch of ```ipon```, if a history file is present 
in the current directory, it is loaded. Otherwize, the used history file 
is this of the profile. 

Other history management:
```
>>> ipon.history.save()
>>> ipon.history.clear()
```

The function ```save()``` saves the current command history into the 
currently used history file, and ```clear()``` clears the content of the 
currently used history file. 

***
