import json,os,random,sys,urllib.request
VAL=[0,100,320,330,500,900,0]
PH=[0,0,1,1,2,4,0]
MATE=100000
INF=10000000
NL=25000
PP=[0,0,0,0,50,50,50,50,10,10,20,30,5,5,10,25,0,0,0,20,5,-5,-10,0,5,10,10,-20,0,0,0,0]
NP=[-50,-40,-30,-30,-40,-20,0,0,-30,0,10,15,-30,5,15,20,-30,0,15,20,-30,5,10,15,-40,-20,0,5,-50,-40,-30,-30]
BP=[-20,-10,-10,-10,-10,0,0,0,-10,0,5,10,-10,5,5,10,-10,0,10,10,-10,10,10,10,-10,5,0,0,-20,-10,-10,-10]
RP=[0,0,0,0,5,10,10,10,-5,0,0,0,-5,0,0,0,-5,0,0,0,-5,0,0,0,-5,0,0,0,0,0,0,5]
QP=[-20,-10,-10,-5,-10,0,0,0,-10,0,5,5,-5,0,5,5,0,0,5,5,-10,5,5,5,-10,0,5,0,-20,-10,-10,-5]
KM=[-30,-40,-40,-50,-30,-40,-40,-50,-30,-40,-40,-50,-30,-40,-40,-50,-20,-30,-30,-40,-10,-20,-20,-20,20,20,0,0,20,30,10,0]
KE=[-50,-40,-30,-20,-30,-20,-10,0,-30,-10,20,30,-30,-10,30,40,-30,-10,30,40,-30,-10,20,30,-30,-30,0,0,-50,-30,-30,-30]
GM=[None,PP,NP,BP,RP,QP,KM]
GE=[None,PP,NP,BP,RP,QP,KE]
ND=(33,31,18,14,-33,-31,-18,-14)
KD=(1,-1,16,-16,15,17,-15,-17)
BD=(17,15,-15,-17)
RD=(1,-1,16,-16)
R=random.Random(20261116)
ZB=[[R.getrandbits(64) for _ in range(64)] for _ in range(12)]
ZS=R.getrandbits(64)
ZC=[R.getrandbits(64) for _ in range(16)]
ZE=[R.getrandbits(64) for _ in range(8)]
PL={"P":1,"N":2,"B":3,"R":4,"Q":5,"K":6,"p":-1,"n":-2,"b":-3,"r":-4,"q":-5,"k":-6}
OL={2:"n",3:"b",4:"r",5:"q"}
def q6(s):
 return (s&7)|((s>>4)<<3)
def mv(f,t,pr=0):
 return f|(t<<7)|(pr<<14)
def uo(m):
 f,t,pr=m&127,(m>>7)&127,(m>>14)&7
 s="abcdefgh"[f&7]+str((f>>4)+1)+"abcdefgh"[t&7]+str((t>>4)+1)
 return s+(OL[pr] if pr else "")
def mu(u):
 f=(int(u[1])-1)*16+(ord(u[0])-97)
 t=(int(u[3])-1)*16+(ord(u[2])-97)
 return mv(f,t,{"n":2,"b":3,"r":4,"q":5}[u[4]] if len(u)==5 else 0)
class P:
 __slots__=("b","t","c","e","h","kw","kb","z","s")
 def __init__(s):
  s.b=[0]*128;s.t=1;s.c=0;s.e=-1;s.h=0;s.kw=4;s.kb=116;s.z=0;s.s=[]
def pf(fen):
 a=fen.split();p=P();b=p.b
 for r,row in enumerate(a[0].split("/")):
  rk=7-r;f=0
  for ch in row:
   if ch.isdigit(): f+=int(ch)
   else:
    sq=rk*16+f;b[sq]=PL[ch];f+=1
 p.t=1 if a[1]=="w" else -1
 c=0
 if "K" in a[2]: c|=1
 if "Q" in a[2]: c|=2
 if "k" in a[2]: c|=4
 if "q" in a[2]: c|=8
 p.c=c;p.e=-1
 if a[3]!="-": p.e=(int(a[3][1])-1)*16+(ord(a[3][0])-97)
 p.h=int(a[4]) if len(a)>4 else 0
 z=0
 for s in range(128):
  if s&0x88: continue
  pc=b[s]
  if pc:
   if pc==6: p.kw=s
   elif pc==-6: p.kb=s
   z^=ZB[(0 if pc>0 else 6)+abs(pc)-1][q6(s)]
 if p.t<0: z^=ZS
 z^=ZC[c]
 if p.e>=0: z^=ZE[p.e&7]
 p.z=z
 return p
def atk(b,s,w):
 pw=1 if w else -1
 for d in ((-15,-17) if w else (15,17)):
  t=s+d
  if not (t&0x88) and b[t]==pw: return True
 for d in ND:
  t=s+d
  if not (t&0x88) and b[t]==(2 if w else -2): return True
 for d in KD:
  t=s+d
  if not (t&0x88) and b[t]==(6 if w else -6): return True
 for d in BD:
  t=s+d
  while not (t&0x88):
   q=b[t]
   if q:
    if (q>0)==w and abs(q) in (3,5): return True
    break
   t+=d
 for d in RD:
  t=s+d
  while not (t&0x88):
   q=b[t]
   if q:
    if (q>0)==w and abs(q) in (4,5): return True
    break
   t+=d
 return False
def gen(p,cp):
 b,t=p.b,p.t;ms=[]
 for s in range(128):
  if s&0x88: continue
  pc=b[s]
  if pc==0 or (pc>0)!=(t>0): continue
  a=abs(pc)
  if a==1:
   d=16 if t>0 else -16;rk=7 if t>0 else 0
   if not cp:
    to=s+d
    if not (to&0x88) and b[to]==0:
     if (to>>4)==rk:
      for pr in (5,4,3,2): ms.append(mv(s,to,pr))
     else:
      ms.append(mv(s,to))
      if (s>>4)==(1 if t>0 else 6):
       to2=s+2*d
       if b[to2]==0: ms.append(mv(s,to2))
   for dd in (d-1,d+1):
    to=s+dd
    if to&0x88: continue
    q=b[to]
    if q and (q>0)!=(t>0):
     if (to>>4)==rk:
      for pr in (5,4,3,2): ms.append(mv(s,to,pr))
     else: ms.append(mv(s,to))
    elif to==p.e and q==0: ms.append(mv(s,to))
  elif a==2:
   for d in ND:
    to=s+d
    if to&0x88: continue
    q=b[to]
    if q==0:
     if not cp: ms.append(mv(s,to))
    elif (q>0)!=(t>0): ms.append(mv(s,to))
  elif a==6:
   for d in KD:
    to=s+d
    if to&0x88: continue
    q=b[to]
    if q==0:
     if not cp: ms.append(mv(s,to))
    elif (q>0)!=(t>0): ms.append(mv(s,to))
   if not cp:
    if t>0 and s==4:
     if p.c&1 and b[5]==0 and b[6]==0 and b[7]==4 and not atk(b,4,False) and not atk(b,5,False) and not atk(b,6,False): ms.append(mv(4,6))
     if p.c&2 and b[3]==0 and b[2]==0 and b[1]==0 and b[0]==4 and not atk(b,4,False) and not atk(b,3,False) and not atk(b,2,False): ms.append(mv(4,2))
    elif t<0 and s==116:
     if p.c&4 and b[117]==0 and b[118]==0 and b[119]==-4 and not atk(b,116,True) and not atk(b,117,True) and not atk(b,118,True): ms.append(mv(116,118))
     if p.c&8 and b[115]==0 and b[114]==0 and b[113]==0 and b[112]==-4 and not atk(b,116,True) and not atk(b,115,True) and not atk(b,114,True): ms.append(mv(116,114))
  else:
   for d in (BD if a==3 else RD if a==4 else BD+RD):
    to=s+d
    while not (to&0x88):
     q=b[to]
     if q==0:
      if not cp: ms.append(mv(s,to))
     else:
      if (q>0)!=(t>0): ms.append(mv(s,to))
      break
     to+=d
 return ms
def mk(p,m):
 f,t,pr=m&127,(m>>7)&127,(m>>14)&7
 b=p.b;pc=b[f];cap=b[t];ep=-1
 if abs(pc)==1 and t==p.e and cap==0:
  ep=t-(16 if p.t>0 else -16);cap=b[ep];b[ep]=0
 rf=rt=-1
 if abs(pc)==6 and abs(t-f)==2:
  if t>f: rf,rt=f+3,f+1
  else: rf,rt=f-4,f-1
  b[rt]=b[rf];b[rf]=0
 z=p.z
 z^=ZB[(0 if pc>0 else 6)+abs(pc)-1][q6(f)]
 if cap: z^=ZB[(0 if cap>0 else 6)+abs(cap)-1][q6(ep if ep>=0 else t)]
 npc=(pr if p.t>0 else -pr) if pr else pc
 z^=ZB[(0 if npc>0 else 6)+abs(npc)-1][q6(t)]
 if rf>=0:
  z^=ZB[(0 if p.t>0 else 6)+3][q6(rf)];z^=ZB[(0 if p.t>0 else 6)+3][q6(rt)]
 z^=ZC[p.c];nc=p.c
 if f==4: nc&=~3
 elif f==116: nc&=~12
 elif f==7 or t==7: nc&=~1
 elif f==0 or t==0: nc&=~2
 elif f==119 or t==119: nc&=~4
 elif f==112 or t==112: nc&=~8
 z^=ZC[nc]
 if p.e>=0: z^=ZE[p.e&7]
 ne=-1
 if abs(pc)==1 and abs(t-f)==32:
  ne=f+(16 if p.t>0 else -16);z^=ZE[ne&7]
 z^=ZS
 p.s.append((m,cap,ep,p.c,p.e,p.h,rf,rt,p.z))
 b[t]=npc;b[f]=0
 if abs(pc)==6:
  if p.t>0: p.kw=t
  else: p.kb=t
 p.c=nc;p.e=ne;p.h=0 if (abs(pc)==1 or cap) else p.h+1;p.t=-p.t;p.z=z
def um(p):
 m,cap,ep,oc,oe,oh,rf,rt,oz=p.s.pop()
 f,t,pr=m&127,(m>>7)&127,(m>>14)&7
 b=p.b;p.t=-p.t;pc=b[t]
 if pr: pc=1 if p.t>0 else -1
 b[f]=pc;b[t]=0
 if cap: b[ep if ep>=0 else t]=cap
 if rf>=0: b[rf]=b[rt];b[rt]=0
 if abs(pc)==6:
  if p.t>0: p.kw=f
  else: p.kb=f
 p.c=oc;p.e=oe;p.h=oh;p.z=oz
def ev(p):
 b=p.b;mg=eg=ph=0;wb=bb=0
 for s in range(128):
  if s&0x88: continue
  pc=b[s]
  if not pc: continue
  a=abs(pc);r=s>>4;f=s&7
  if f>3: f=7-f
  i=((7-r) if pc>0 else r)*4+f;v=VAL[a];g=1 if pc>0 else -1
  mg+=g*(v+GM[a][i]);eg+=g*(v+GE[a][i]);ph+=PH[a]
  if a==3:
   if pc>0: wb+=1
   else: bb+=1
 if wb>=2: mg+=30;eg+=30
 if bb>=2: mg-=30;eg-=30
 if ph>24: ph=24
 return ((mg*ph+eg*(24-ph))//24)*p.t
TT={}
KL=[[0,0] for _ in range(128)]
HI=[[0]*128 for _ in range(12)]
NN=0
HS=set()
PA=set()
class Ab(Exception): pass
def oc(p,m,tm,pl):
 if m==tm: return 1<<30
 f,t=m&127,(m>>7)&127;pc=p.b[f];cap=p.b[t]
 if cap==0 and abs(pc)==1 and (f&7)!=(t&7) and t==p.e: cap=1 if p.t>0 else -1
 if cap: return (1<<28)+10*VAL[abs(cap)]-VAL[abs(pc)]//10
 if m==KL[pl][0]: return 1<<24
 if m==KL[pl][1]: return 1<<23
 return HI[(0 if pc>0 else 6)+abs(pc)-1][t]
def sr(p,d,al,be,pl):
 global NN
 NN+=1
 if NN>NL: raise Ab
 if p.h>=100: return 0
 if d<=0: return qs(p,al,be,pl)
 e=TT.get(p.z);tm=0
 if e and e[0]>=d:
  tm=e[3]
  if e[1]==0: return e[2]
  if e[1]==1: al=max(al,e[2])
  else: be=min(be,e[2])
  if al>=be: return e[2]
 a0=al
 sc=sorted(((oc(p,m,tm,pl),m) for m in gen(p,False)),reverse=True)
 best=-INF;bm=0;lg=0
 for _,m in sc:
  mk(p,m)
  k=p.kw if p.t<0 else p.kb
  if atk(p.b,k,p.t>0):
   um(p);continue
  lg+=1
  try:
   if p.z in HS or p.z in PA: v=0
   else:
    PA.add(p.z)
    try: v=-sr(p,d-1,-be,-al,pl+1)
    finally: PA.discard(p.z)
  finally: um(p)
  if v>best: best=v;bm=m
  if v>al: al=v
  if al>=be:
   f,t=m&127,(m>>7)&127;pc=p.b[f]
   if p.b[t]==0 and not (abs(pc)==1 and (f&7)!=(t&7)):
    if m!=KL[pl][0]: KL[pl][1]=KL[pl][0];KL[pl][0]=m
    HI[(0 if pc>0 else 6)+abs(pc)-1][t]+=d*d
   break
 if lg==0:
  k=p.kw if p.t>0 else p.kb
  return -MATE+pl if atk(p.b,k,p.t<0) else 0
 fl=0 if best>a0 and best<be else (1 if best>=be else 2)
 if len(TT)>400000: TT.clear()
 TT[p.z]=(d,fl,best,bm)
 return best
def qs(p,al,be,pl):
 global NN
 NN+=1
 if NN>NL: raise Ab
 if p.h>=100: return 0
 if pl>96: return ev(p)
 k=p.kw if p.t>0 else p.kb;ic=atk(p.b,k,p.t<0)
 if not ic:
  st=ev(p)
  if st>=be: return be
  if st>al: al=st
 sc=sorted(((oc(p,m,0,pl),m) for m in gen(p,not ic)),reverse=True)
 lg=0
 for _,m in sc:
  mk(p,m)
  k2=p.kw if p.t<0 else p.kb
  if atk(p.b,k2,p.t>0):
   um(p);continue
  lg+=1
  try:
   if p.z in HS or p.z in PA: v=0
   else:
    PA.add(p.z)
    try: v=-qs(p,-be,-al,pl+1)
    finally: PA.discard(p.z)
  finally: um(p)
  if v>al: al=v
  if al>=be: break
 if ic and lg==0: return -MATE+pl
 return al
def ch(p,lu):
 global NN
 ms=[mu(u) for u in lu];best=ms[0];NN=0;PA.add(p.z)
 try:
  for d in range(1,64):
   sc=sorted(((oc(p,m,0,0),m) for m in ms),reverse=True)
   bs=-INF;bm=ms[0];al=-INF
   for _,m in sc:
    mk(p,m)
    try:
     if p.z in HS or p.z in PA: v=0
     else:
      PA.add(p.z)
      try: v=-sr(p,d-1,-INF,-al,1)
      finally: PA.discard(p.z)
    finally: um(p)
    if v>bs: bs=v;bm=m
    if v>al: al=v
    if al>=INF: break
   best=bm
   if abs(bs)>MATE-1000: break
 except Ab: pass
 finally: PA.discard(p.z)
 return best
def gh(sf,us):
 p=pf(sf);h=set()
 for u in us:
  h.add(p.z);mk(p,mu(u))
 return h
def post(path,body):
 u=os.environ.get("MAKEFUN_ENV_URL")
 if not u: sys.exit("MAKEFUN_ENV_URL is not set")
 req=urllib.request.Request(u+path,data=json.dumps(body).encode(),headers={"content-type":"application/json"})
 try:
  with urllib.request.urlopen(req) as r: return json.load(r)
 except Exception as e: sys.exit(f"{path}: {e}")
def main():
 global HS
 while True:
  g=post("/game",{})
  if g["status"]=="done": break
  while g["status"]=="your_move":
   p=pf(g["fen"])
   HS=gh(g.get("start_fen",""),g.get("moves",[])) if g.get("start_fen") else set()
   m=ch(p,g["legal_moves"]);u=uo(m)
   if u not in g["legal_moves"]: u=g["legal_moves"][0]
   g=post("/move",{"game":g["game"],"move":u})
  print(f"game {g['game']}: {g['outcome']} by {g['reason']}",file=sys.stderr)
 print(f"done: {g.get('wins')} won, {g.get('draws')} drawn, {g.get('losses')} lost",file=sys.stderr)
if os.environ.get("MAKEFUN_ENV_URL"): main()
