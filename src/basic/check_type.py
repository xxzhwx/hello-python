# -*- coding: utf-8 -*-
'''
@author: xxzhwx
'''
from types import IntType

def is_int_type(num):
    
    # 对象身份比较
    if type(num) is IntType:
        return True
    
    return False

def is_int_typeX(num):
    
    if isinstance(num, int):
        return True
    
#     if type(num) is int:
#         return True
    
    return False

# Usage
print(is_int_type(1))
print(is_int_type(1.0))
print(is_int_type(''))

print(is_int_typeX(1))
print(is_int_typeX(1.0))
print(is_int_typeX(''))