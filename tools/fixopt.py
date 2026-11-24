"""Ubah teks opsi tertentu: python3 tools/fixopt.py fixes.txt  (baris: ID LETTER | teks baru)"""
import json,sys,re
b=json.load(open('data/bank.json'));by={q['id']:q for q in b['qs']}
n=0
for line in open(sys.argv[1],encoding='utf-8'):
    line=line.strip()
    if not line or line.startswith('//'): continue
    m=re.match(r'(\d+)\s+([A-E])\s*\|\s*(.+)$',line)
    if not m: raise SystemExit('format salah: '+line)
    q=by[int(m.group(1))]
    if q.get('tag') in ('asli','rekon','slide'): raise SystemExit(f'#{q["id"]} terkunci')
    q['o']['ABCDE'.index(m.group(2))][0]=m.group(3); n+=1
json.dump(b,open('data/bank.json','w'),ensure_ascii=False); print('diubah',n)
