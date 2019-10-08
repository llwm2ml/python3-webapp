# -*- coding: utf-8 -*-
import re
data = 'bit'
patt = 'bat|bit|but|hat|hit|hut'
str = re.match(patt, data)
if str is not None:
    print(str.group())
str = re.search(patt, data)
if str is not None:
    print(str.group())
data = 'zhang san'

str = re.split('\s', data)
for a in str:
    print(a);