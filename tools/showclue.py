import json,re,sys,subprocess
ppt=sys.argv[1]
out=subprocess.run([sys.executable,'tools/bank_tool.py','validate','--ppt',ppt],capture_output=True,text=True).stdout
ids=[int(x) for x in re.findall(r'\d+',re.search(r'menonjol_id": \[(.*?)\]',out,re.S).group(1))]
b=json.load(open('data/bank.json'));st=lambda s:re.sub('<[^>]+>','',s)
for q in b['qs']:
  if q['id'] in ids:
    print(q['id'],'key','ABCDE'[q['a']]); [print('  ','ABCDE'[i],len(st(o[0])),st(o[0])) for i,o in enumerate(q['o'])]
