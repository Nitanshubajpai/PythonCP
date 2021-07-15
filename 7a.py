

# Python code to illustrate the Modules
class Bmw:
    # First we create a constructor for this class
    # and add members to it, here models
    def __init__(self):
        self.models = ['i8', 'x1', 'x5', 'x6']
   
    # A normal print function
    def outModels(self):
        print('These are the available models for BMW')
        for model in self.models:
            print('\t%s ' % model)



( Then we create another file with the name Audi.py and add the similar type of code to it with different members.)
# Python code to illustrate the Module
class Audi:
    # First we create a constructor for this class
    # and add members to it, here models
    def __init__(self):
        self.models = ['q7', 'a6', 'a8', 'a3']
  
    # A normal print function
    def outModels(self):
        print('These are the available models for Audi')
        for model in self.models:
            print('\t%s ' % model)

(Then we create another file with the name Nissan.py and add the similar type of code to it with different members)

# Python code to illustrate the Module
class Nissan:
    # First we create a constructor for this class
    # and add members to it, here models
    def __init__(self):
        self.models = ['altima', '370z', 'cube', 'rogue']
  
    # A normal print function
    def outModels(self):
        print('These are the available models for Nissan')
        for model in self.models:
            print('\t%s ' % model)

(Finally we create the __init__.py file. This file will be placed inside Cars directory and can be left blank or we can put this initialisation code into it.)


from Bmw import Bmw
from Audi import Audi
from Nissan import Nissan
(Now, let’s use the package that we created. To do this make a sample.py file in the same directory where Cars package is located and add the following code to it:)
# Import classes from your brand new package
from Cars import Bmw
from Cars import Audi
from Cars import Nissan
   
# Create an object of Bmw class & call its method
ModBMW = Bmw()
ModBMW.outModels()
   
# Create an object of Audi class & call its method
ModAudi = Audi()
ModAudi.outModels()
  
# Create an object of Nissan class & call its method
ModNissan = Nissan()
ModNissan.outModels()
