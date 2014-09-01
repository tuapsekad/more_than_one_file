# -*- coding: cp1251 -*-
import os

for top, dirs, files in os.walk(u'h:\dir'):
    name = filter(lambda x: x.endswith(''), files)
    if name:
        print os.path.join(top + name[0])
