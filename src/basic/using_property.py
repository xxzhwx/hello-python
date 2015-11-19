# -*- coding: utf-8 -*-
'''
@author: xxzhwx
'''

class X(object):
    def __init__(self, x):
        self.x = x
        
@property
def x():
    def fget(self):
        return ~self.__x
    
    def fset(self, x):
        assert isinstance(x, int), \
            '"x" must be an integer!'
        self.__x = ~x
        
    return locals()


# Usage
inst = X(10)
print(inst.x)

inst.x += 10
print(inst.x)