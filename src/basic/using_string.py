# -*- coding: utf-8 -*-
'''
@author: xxzhwx
'''

def using_string():
    
    s = 'hello, python!'
    
    print(s.capitalize()) # 首字母大写
    print(s.upper())
    print(s.lower())
    print(s.swapcase())
    
    print(s.lstrip())
    print(s.rstrip())
    print(s.strip())
    
    print(s.count('o')) # 子串出现次数
    print(s.find('o')) # 检测子串首次出现的开始索引值或-1
    print(s.rfind('o'))
    print(s.replace('python', 'world'))
    
    print(s.startswith('hello'))
    print(s.endswith('on!'))
    
    print(s.isalpha())
    print(s.isdigit())
    print(s.isspace())
    
    print(s.split(','))
    print(s.splitlines(False))
    
    print('python' in s)
    
    print('\n'.join(['A', 'b', 'c']))
    
    print(s[0:s.find('python')])
    print(s[s.rfind('python'):].replace('python', ''))
    
# Usage
using_string()