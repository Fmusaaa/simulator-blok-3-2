import json,re,sys
b=json.load(open('data/bank.json'));st=lambda s:re.sub('<[^>]+>','',s)
for q in b['qs']:
  if q['ppt']!=sys.argv[1] or q.get('tag') in ('asli','rekon','slide'):continue
  ls=[len(st(o[0])) for o in q['o']];a=q['a'];oth=sorted(l for i,l in enumerate(ls) if i!=a)
  if ls[a]==max(ls) and ls.count(max(ls))==1: print(q['id'],'key',ls[a],'next',oth[-1],'diff',ls[a]-oth[-1])
