'''
Author: XPectuer
LastEditor: XPectuer
'''

import sys
import os

filename = sys.argv[1]
path = os.path.abspath(filename)
with open(path, 'r') as f:
    str = f.read()

str.replace("")