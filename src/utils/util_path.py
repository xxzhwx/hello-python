# -*- coding: utf-8 -*-
'''
目录和文件操作
@author: xxzhwx
'''
import os.path
import shutil
import filecmp

def get_parent(path, count):
    parent = path
    for _ in range(count):
        parent = os.path.dirname(parent)
    return parent

def make_dir(path):
    if os.path.isdir(path):
        return
    
    try:
        os.makedirs(path)
    except Exception as e:
        print(u'making dir {}: {}'.format(path, e))

def remove(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
    except Exception as e:
        print(u'removing {}: {}'.format(path, e))
        
def copy(src, dst):
    if os.path.isfile(src):
        try:
            parent = os.path.dirname(dst)
            make_dir(parent)
            shutil.copy2(src, dst)
        except Exception as e:
            print(u'copying {} to {}: {}'.format(src, dst, e))
            
    if not os.path.isdir(src):
        return
    
    for p in os.listdir(src):
        sp = os.path.join(src, p)
        dp = os.path.join(dst, p)
        copy(sp, dp)
        
def get_paths_under(path):
    '''
    Get all dirs and files under the given path recursively.
    '''
    paths = []
    for path, dirs, files in os.walk(path):
        paths.extend([os.path.join(path, d) for d in dirs])
        paths.extend([os.path.join(path, f) for f in files])
    return paths

def get_files_under(path, suffix=None):
    '''
    Get all files under the given path recursively, with the given suffix, ignore all dirs.
    '''
    files = []
    for path, _, fs in os.walk(path):
        for f in fs:
            if suffix != None and not f.endswith(suffix):
                continue
            files.append(os.path.join(path, f))
    return files

def cmp_files(filemap1, filemap2):
    '''
    Compare filemap1 with filemap2
    @return: true if the two given map have exactly the same files, otherwise return false
    '''
    if set(filemap1.keys()) != set(filemap2.keys()):
        return False
    
    for k, v in filemap1.iteritems():
        if not filecmp.cmp(v, filemap2[k], False):
            return False
        
    return True