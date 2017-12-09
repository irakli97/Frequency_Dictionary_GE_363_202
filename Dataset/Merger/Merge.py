# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 12:35:14 2017

@author: ikobe
"""
import re
import operator


allWords = open(r'allwords-unique-sorted.txt','r', encoding="utf8");
filteredWords = open(r'Filtered.txt','r', encoding="utf8");
f = open('workfile.txt', 'w', encoding="utf8")



dict1 = {}
key = ""
val = 0;


allWords.readline()
filteredWords.readline()


for i in allWords:
    m = re.search(r'[ა-ჰ]+', i)
    key = m.group(0)
    m = re.search(r'\d+', i)
    val = int(m.group(0))
    dict1.update({key:val})



index = 0;
strs = ["" for x in range(550000)]

for i in filteredWords:
    if dict1.get(i[:len(i)-1]):
        f.write((i[:len(i)-1] + " " + str(dict1[i[:len(i)-1]])) + '\n')
        
        
f.close()
f = open('workfile.txt', 'r', encoding="utf8")
dict1 = {}
for i in f:
    m = re.search(r'[ა-ჰ]+', i)
    key = m.group(0)
    m = re.search(r'\d+', i)
    val = int(m.group(0))
    dict1.update({key:val})
    
sorted_x = sorted(dict1.items(), key=operator.itemgetter(1), reverse=True)
f.close()



f = open('sorted_filtered.txt', 'w', encoding="utf8")

for i in range(len(sorted_x)):
    f.write(sorted_x[i][0] + " " + str(sorted_x[i][1]) + "\n");

  



allWords.close()
filteredWords.close()
f.close()

