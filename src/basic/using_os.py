# -*- coding: utf-8 -*-
'''
@author: xxzhwx
'''
import os

def using_os():
    # 换行符
    print('os.linesep: ' + os.linesep),
    # 路径分隔符
    print('os.sep: ' + os.sep)
    print('os.path.sep: ' + os.path.sep)
    # 可选的路径分隔符，如果当前系统没有，则为None
    print('os.altsep: ' + os.altsep)
    print('os.path.altsep: ' + os.path.altsep)
    # 后缀分隔符
    print('os.extsep: ' + os.extsep)
    print('os.path.extsep: ' + os.path.extsep)

if __name__ == '__main__':
    using_os()