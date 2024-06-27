'''
Private classes are typically not exportable from a file and can only be used within the file in which they are declared
In python, there is no real such thing as public and private but there are standard ways in which we denote public and 
private classes in python.  Private classes in python are prefixed with the '_' key.
'''

class _Private:
    def __init__(self, name):
        self.name = name

class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)

    def _display(self):
        print("hello")

    def display(self):
        print('hi')