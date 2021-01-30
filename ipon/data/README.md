# *ipon*
                             
***
## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Requirements](#requirements)
* [Installation](#installation)
* [Use](#use)
* [Author](#author)
* [License](#license)


***
## General Info

The ```ipon``` interpreter is nothing else than an ```ipython``` 
configuration, and with other things, working with ```python3``` only. 

If you still want to use it, it would be preferable to have a GNU/linux
distribution, because ```ipon``` has been done and tested with 
**linux only**. If you do not have linux, and even if you do not want to 
use ```ipon```, you better install a linux distribution. 



***
## Technologies
```ipon``` does not use any technology, only ```python3``` and ```ipython```. 

* [python3](https://www.python.org/): Tested version 3.8.5
* [ipython](https://ipython.org/): Tested version 7.19.0 


***
## Requirements

To see the details of the requirements, see 
[```./requirements.txt```](#./requirements.txt). 
Roughly, ```ipon``` only needs ```IPython```, of course, and the library 
[```basilic```](#https://github.com/remignot/basilic). 
It is a package of useless features, and so essential.


***
## Installation
In your shell, and with an internet connection, the installation instructions are:  
```
$ git clone https://github.com/remignot/ipon
$ pip install -r ipon/requirements.txt
$ pip install ipon/ 
``` 
According to your ```python``` distribution, you may use ```sudo``` or the option ```--user```.

**Remarks:**  

* The ```basilic``` libary will be also installed. 
* The script ```ipon``` will be copied somewhere in your path, which depends 
on your configuration and the used option. 
Also, your home will be polluted by some configuration files, 
usually in ```$HOME/.ipython/profile_ipon```. 

***
## Use

**In a shell:**  
To launch ```ipon```, only enter: ```$ ipon``` 
in your favorite shell. If ```ipon``` has been correctly installed, 
it should be in your path, cf. the variable ```$PATH```.

**In a python interpreter:**  
From a ```python``` interpreter, to launch the ```ipon```, enter: 
```
>>> import ipon
>>> ipon.start()
```

***
## Documentation
Let's see later.

***
## Author
Rémi Mignot

***
## License
MIT Expat License  
See [```./LICENSE.txt```](#./LICENSE.txt)

***
