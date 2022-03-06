get_ipython().run_line_magic("load_ext", " autoreload")
get_ipython().run_line_magic("autoreload", " 2")


import simple_package1
simple_package1.function()
simple_package1.__file__


import simple_package2
simple_package2.function()
simple_package2.__file__


simple_package1.function()
simple_package2.function()


# May not work on windows
get_ipython().getoutput("pip list |grep simple")


# You need to install the content of `simple-package-3`

from importlib import metadata

# for python bellow 3.8 
# get_ipython().getoutput("pip install importlib_metadata")
# import importlib_metadata as metadata 

metadata.metadata('simple-package-3')["Author"]











get_ipython().getoutput("pip install -e ./package4")


import simple_package4
simple_package4.function()





get_ipython().getoutput("pip install ./package6_moo")


get_ipython().getoutput("moo ")
