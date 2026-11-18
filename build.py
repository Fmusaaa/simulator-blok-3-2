"""Bangun ulang kedua simulator:
   python3 src/build_bank.py && python3 build.py
   -> index.html                 (Simulator Blok 3.2, bank PPT)
   -> recall-uam-2024/index.html (Simulator Recall UAM 3.2 tahun 2024, terpisah)"""
import json,os,re
T=open('src/template.html').read()
def render(bank,out,title,logo,h1,intro,examtitle,key,showall=False):
    s=json.dumps(bank,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
    h=T
    for a,b in [('__TITLE__',title),('__LOGO__',logo),('__H1__',h1),('__INTRO__',intro),('__EXAMTITLE__',examtitle),('__KEY__',key),('__SHOWALL__','true' if showall else 'false'),('__BANK__',s)]:
        h=h.replace(a,b)
    os.makedirs(os.path.dirname(out) or '.',exist_ok=True)
    open(out,'w').write(h); print(out,len(bank['qs']),'soal')

# 1) Simulator utama
b=json.load(open('data/bank.json'))
render(b,'index.html','Simulator Blok 3.2','Simulator <span>Blok 3.2</span>','Bank soal Blok 3.2',
       'soal dari 20 judul PPT dosen + recall UAM 3.2.','Simulasi ujian Blok 3.2','sim-blok32-v1')

# 2) Simulator recall UAM 3.2 tahun 2024 (terpisah)
U=[]
exec(open('src/recall_uam_2024.py').read())
order=[p['id'] for p in b['ppts']]
used=[p for p in b['ppts'] if any(x['c']==p['id'] for x in U)]
qs=[]
for i,x in enumerate(sorted(U,key=lambda x:order.index(x['c'])),1):
    qs.append(dict(id=i,ppt=x['c'],topik='Recall no. '+x['no'],s=x['s'],o=x['o'],a=0,p=x['p'],k=x['k'],t=x['t'],n=x['n'],tag=x['tag'],src='uam2024',ord=int(re.match(r'\d+',x['no']).group())))
for p in used:
    if p['id']=='lain': p=dict(p); 
lain=[dict(p,title='Di luar 20 PPT (radiologi, K3, onkologi, hemostasis)',dosen='Kunci dari literatur standar') if p['id']=='lain' else p for p in used]
json.dump(dict(ppts=lain,qs=qs),open('data/recall_uam_2024.json','w'),ensure_ascii=False)
na=sum(q['tag']=='asli' for q in qs)
render(dict(ppts=lain,qs=qs),'recall-uam-2024/index.html','Recall UAM 3.2 2024','Recall <span>UAM 3.2 · 2024</span>','Recall UAM 3.2 tahun 2024',
       'soal recall UAM 3.2 tahun 2024 ('+str(na)+' asli, '+str(len(qs)-na)+' direkonstruksi), dikelompokkan per PPT. Kunci dicek ke slide dosen; 8 kunci recall dikoreksi.',
       'Simulasi recall UAM 3.2 2024','sim-recall-uam32-2024-v1',showall=True)
