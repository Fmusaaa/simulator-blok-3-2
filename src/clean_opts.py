"""Hapus keterangan dalam kurung di teks opsi supaya tidak membocorkan jawaban.
Isi kurung dipindah ke kolom fakta/pembahasan opsi.
- Kurung berisi teks (tanpa angka/simbol hitung): selalu dihapus.
- Kurung berisi angka: dihapus hanya bila muncul di opsi kunci saja (asimetris),
  dibiarkan bila juga ada di opsi lain (bagian dari format/rumus opsi)."""
import re
P=re.compile(r'\s*\(([^()]*)\)')
NUM=re.compile(r'[\d<>≥≤×÷±%=+]')
def clean_q(q):
    has_num=[any(NUM.search(m.group(1)) for m in P.finditer(o[0])) for o in q['o']]
    key_only_num = has_num[q['a']] and sum(has_num)==1
    new=[]
    for i,o in enumerate(q['o']):
        t,f,r=o; moved=[]
        t=t.replace('(rujukan ','(').replace('(penurunan ','(').replace('(36 kkal × 45 kg)','(36 kkal/kg)')
        def rep(m):
            inner=m.group(1).strip()
            if inner in ('s',): moved.append(None); return inner   # TSH(s) -> TSHs
            if NUM.search(inner) and not (i==q['a'] and key_only_num): return m.group(0)
            moved.append(inner); return ''
        nt=P.sub(rep,t).strip()
        nt=re.sub(r'\s+([,;.])',r'\1',nt)
        mv=[x for x in moved if x]
        if mv: f='<b>Keterangan:</b> '+'; '.join(mv)+'. '+f
        new.append([nt,f,r])
    texts=[re.sub('<[^>]+>','',x[0]).strip().lower() for x in new]
    if len(set(texts))<len(texts) or any(not x for x in texts):
        return q,False        # jangan ubah bila jadi ganda/kosong
    q=dict(q); q['o']=new; return q,True
def clean_bank(b):
    out=[];n=0
    for q in b['qs']:
        nq,ch=clean_q(q); out.append(nq); n+=ch and nq['o']!=q['o']
    return dict(b,qs=out),n
