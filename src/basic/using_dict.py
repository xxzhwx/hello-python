# -*- coding: utf-8 -*-
'''
@author: xxzhwx
'''

def using_dict():
    
    # mydict = {}
    # mydict = {'name': 'earth', 'port': 80}
    # mydict = {}.fromkeys(('x', 'y'), -1)
    mydict = dict((['name', 'earth'], ['port', 80]))
    
    print(mydict)
    print(mydict['name'])
    
    print('name' in mydict)
    
    mydict['keepalive'] = True
    print(mydict.pop('keepalive')) # 删除并返回值
    
    print(mydict.keys())
    print(mydict.values())
    print(mydict.items())
    print(mydict.update({'how': 'tcp'}))
    
    for key in mydict:
        print('key={}, value={}'.format(key, mydict[key]))
        
    print(mydict.clear())

# Usage
using_dict()