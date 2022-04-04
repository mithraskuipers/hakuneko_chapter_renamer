# Tool to rename the folders downloaded using HakuNeko manga downloader.
# Purpose? Give all downloaded manga chapters a naming scheme that can be
# alphabetically sorted correctly.

import os
import re
import shutil

cwd = os.getcwd()


# Rename
nlen = []
basedir = cwd
for fn in os.listdir(basedir):
    if os.path.isdir(os.path.join(basedir, fn)):
        if ".git" in fn: 
            continue
        # remove substring van fn
        fn_short = fn.replace("Ch. ","")
        #fn_new = fn_new[1:]
        fn_short_split = fn_short.split(" ")
        len = len(fn_short_split[0])
        if (len < 4):
            fn_short_split[0] = fn_short_split[0].zfill(4)
        fn_new = " ".join(fn_short_split)
        os.rename(fn,fn_new)


# Zip
for fn in os.listdir(basedir):
    if os.path.isdir(os.path.join(basedir, fn)):
        fn_new = fn.split(" ")
        if (len(fn_new[0]) == 1): # Exclude .git
            continue
        shutil.make_archive(fn, 'zip', fn)


        #nlen.append(re.sub("[^0-9]", "ygygyggyugy", fn[0]))
        #new.append(fn[0].zfill(4))    
        
        
'''
  continue # Not a directory
if ',' in fn:
  continue # Already in the correct form
if ' ' not in fn:
  continue # Invalid format
firstname,_,surname = fn.rpartition(' ')
os.rename(os.path.join(basedir, fn),os.path.join(basedir, surname + ', ' + firstname))
'''