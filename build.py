"""Bangun ulang kedua simulator:
   python3 src/build_bank.py && python3 build.py
   -> index.html                 (Simulator Blok 3.2, bank PPT)
   -> recall-uam-2024/index.html (Simulator Recall UAM 3.2 tahun 2024, terpisah)"""
import json,os,re,sys
sys.path.insert(0,'src')
from clean_opts import clean_bank
T=open('src/template.html').read()
def render(bank,out,title,logo,h1,intro,examtitle,key,showall=False,tpl=None,custom=False,clean=True):
    # bank v2 (index.html) sudah lolos validator anti-clue (tools/bank_tool.py) -> tidak dibersihkan lagi
    if clean: bank,n=clean_bank(bank); print(out,'opsi dibersihkan di',n,'soal')
    s=json.dumps(bank,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
    h=tpl or T
    for a,b in [('__TITLE__',title),('__LOGO__',logo),('__H1__',h1),('__INTRO__',intro),('__EXAMTITLE__',examtitle),('__KEY__',key),('__SHOWALL__','true' if showall else 'false'),('__CUSTOM__','true' if custom else 'false'),('__BANK__',s)]:
        h=h.replace(a,b)
    os.makedirs(os.path.dirname(out) or '.',exist_ok=True)
    open(out,'w').write(h); print(out,len(bank['qs']),'soal')

# 1) Simulator utama = platform v2 (src/app/*)
def app_template():
    A='src/app/'
    sh=open(A+'shell.html').read()
    css=open(A+'base.css').read()+'\n'+open(A+'app.css').read()
    js=open(A+'app.js').read().replace('__OLDKEY__','sim-blok32-v1')
    return sh.replace('/*__CSS__*/',css).replace('/*__JS__*/',js)
b=json.load(open('data/bank.json'))
render(b,'index.html','Simulator Blok 3.2 · Medical Exam & Learning','Simulator <span>Blok 3.2</span>','Bank soal Blok 3.2',
       '','Simulasi ujian Blok 3.2','sim-blok32-v2',tpl=app_template(),clean=False)

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

# ---- simulator per angkatan (Articulatio vs Calcaneus), terpisah ----
import html as _html, subprocess
subprocess.run([sys.executable,'src/angkatan/make_template.py'],check=True)
subprocess.run([sys.executable,'src/angkatan/build_angkatan.py'],check=True)
A=json.load(open('data/angkatan.json'))
E=lambda t:_html.escape(t,quote=False)
for q in A['qs']:
    q['s']=E(q['s']); q['p']=E(q['p']); q['n']=E(q['n']); q['o']=[[E(o[0]),E(o[1]),E(o[2])] for o in q['o']]
render(A,'angkatan/index.html','Bank Soal Angkatan 3.2','Soal <span>Angkatan · 3.2</span>','Bank soal angkatan Blok 3.2',
 'soal UAM & UAS 3.2 dari dua angkatan: Articulatio dan Calcaneus. Pilih angkatan atau set soal, lalu kerjakan dengan kunci angkatan atau kunci terverifikasi.',
 'Simulasi Ujian 3.2 (soal angkatan)','sim-angkatan32-v1',showall=True,tpl=open('src/angkatan/template_angkatan.html').read())
