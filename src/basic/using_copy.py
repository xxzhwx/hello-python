# -*- coding: utf-8 -*-
'''
@author: xxzhwx
'''
import copy

def using_copy():
    
    mylist = [1, 2, 3, 4, [5]]
    mylist2 = copy.copy(mylist)
    mylist3 = copy.deepcopy(mylist) # 深拷贝，注意原子类型没有被拷贝一说
    
    print('{0}, {1}, {2}'
          .format(id(mylist[0]), id(mylist2[0]), id(mylist3[0])))
    
    print('{0}, {1}, {2}'
          .format(id(mylist[-1]), id(mylist2[-1]), id(mylist3[-1])))

# Usage
using_copy()