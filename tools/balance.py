"""Seimbangkan posisi kunci (A–E) soal non-locked per PPT.
python3 tools/balance.py <ppt> [<ppt>...]
Kunci dipindah ke posisi yang paling jarang dipakai; urutan distraktor dipertahankan."""
import json,sys,collections
LOCK={'asli','rekon','slide'}
b=json.load(open('data/bank.json'))
for p in sys.argv[1:]:
    qs=[q for q in b['qs'] if q['ppt']==p and q.get('tag') not in LOCK and len(q['o'])==5]
    cnt=collections.Counter(); moved=0
    for q in sorted(qs,key=lambda q:q['id']):
        cur=q['a']; tgt=min(range(5),key=lambda i:(cnt[i],(i-q['id'])%5))
        if tgt!=cur:
            key=q['o'][cur]; rest=[o for i,o in enumerate(q['o']) if i!=cur]
            q['o']=rest[:tgt]+[key]+rest[tgt:]; q['a']=tgt; moved+=1
        cnt[tgt]+=1
    print(p,'dipindah',moved,dict(sorted(cnt.items())))
json.dump(b,open("data/bank.json","w"),ensure_ascii=False)
