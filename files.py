# -*- coding: cp1251 -*-
import os

for top, dirs, files in os.walk(u'h:\dir'):
    name = filter(lambda x: x.endswith('.xml'), files)
    if name[1:]:
        print os.path.join(top + u' - Больше одного файла XML')
