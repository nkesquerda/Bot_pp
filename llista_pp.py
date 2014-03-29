# -*- encoding: utf-8 -*-

import json, urllib, sys
from StringIO import StringIO

sol = 'http://ca.wikiquote.org/w/api.php?action=query&list=embeddedin&format=json&eititle=Plantilla%3ARef-llibre&eilimit=500'
req = urllib.urlopen(sol)
data = req.read().decode('utf-8')

j = json.load(StringIO(data))

a = 0
txt = open('llista.txt', 'w')

while a != 500:
    b = j['query']['embeddedin'][a]['title'].encode('utf-8')
    print b
    txt.write(b + '\n')
    a = a + 1
