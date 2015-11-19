# -*- coding: utf-8 -*-
'''
@author: xxzhwx
'''

def using_set():
    
    myset = set('abcde') # 可变集合
    # myset = frozenset('abcde') # 不可变集合
    
    print(myset)
    print('a' in myset)
    print('a' not in myset)
    
    myset.add('fgh')
    print(myset)
    
    myset.update('opqr')
    print(myset)
    
    myset.remove('r')
    print(myset)
    
    myset -= set('opqr')
    print(myset)
    
    print(myset.issubset(set('abc')))
    print(myset.issuperset(set('abc')))
    
    print(myset | set('opqr'))
    print(myset & set('abc'))
    print(myset - set('abc'))
    print(myset ^ set('abcopqr'))

# Usage
using_set()