"""Bangun ulang index.html: python3 src/build_bank.py && python3 build.py"""
import json
b=json.load(open('data/bank.json'))
s=json.dumps(b,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
open('index.html','w').write(open('src/template.html').read().replace('__BANK__',s))
print('index.html:',len(b['qs']),'soal')
