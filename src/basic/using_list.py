# -*- coding: utf-8 -*-
'''
@author: xxzhwx
'''

def using_list():
    
    mylist = []
    
    mylist.append(0)
    mylist.extend([1, 2, 3])
    mylist += [4, 5]
    
    mylist.remove(0) # 删除首次出现的指定的值
    
    mylist = mylist * 2 # 重复
    
    print(len(mylist))
    
    print(0 in mylist) # 成员关系操作
    
    print([m * 2 for m in mylist]) # 列表解析
    
    print(mylist[:])
    print(mylist[:65536]) # 超过长度不会出错
    print(mylist[::2]) # 步长
    print(mylist[::-1])
    
    print(mylist.reverse())
    
    for i, v in enumerate(mylist):
        print('mylist[{}] is {}'.format(i, v))
        
    # 逆序遍历
    for v in range(len(mylist)-1, -1, -1):
        print(v)
        
    print(zip(mylist, ['a', 'b', 'c']))
    
    # 清空列表
    #mylist = []
    del mylist[:]
    print(mylist)

# Usage
using_list()