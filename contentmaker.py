# coding=gbk
import codecs
import re

with open('t.txt','r') as f:
    words = f.read()

if words[:3] == codecs.BOM_UTF8:
    words = words[3:]
words=words.decode('utf-8')

print u'共有',len(words),u'字'

pat = u'第*[一二三四五六七八九十零百千0]+[章节卷]'
pattern = re.compile(pat)
match = pattern.findall(words)

#print [t.encode("utf-8") for t in match]
print  u'共有',len(match),u'章'

for ind in range(len(match)):
    print match[ind],
print
