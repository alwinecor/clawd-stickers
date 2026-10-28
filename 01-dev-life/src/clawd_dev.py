"""
clawd-stickers · 01 Dev Life (克码人生) — inspired by clawd-moji by Qisi3344
https://github.com/Qisi3344/clawd-moji
Generates the animated Clawd stickers in ../gif/ and the WeChat versions in ../wechat/.

  pip install pillow
  python clawd_dev.py             # all
  python clawd_dev.py compact     # just one

No external font needed: command text uses the tiny pixel font defined below.

Clawd rules kept in every frame: 15x16 body grid, colour #D77757 (official clawd_body),
1x2 black square eyes, no mouth.
"""
import math, os, sys, random
from PIL import Image, ImageDraw
S=12; W,H=23,24; OX,OY=4,7
BODY='#D77757'; K='#1a1a1a'; WH='#FFFFFF'; BANG='#E5484D'
HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(HERE,'..','gif'); OUT_WX=os.path.join(HERE,'..','wechat')

# ---------- shared helpers, adapted from Qisi3344/clawd-moji 01-movie-night ----------
def rect(x0,y0,x1,y1): return [(x,y) for x in range(x0,x1+1) for y in range(y0,y1+1)]
def put(p,pts,c,dy=0):
    for x,y in pts: p[(x,y+dy)]=c
def clear(p,pts,dy=0):
    for x,y in pts: p.pop((x,y+dy),None)
UP=rect(0,7,1,8); MID=rect(0,8,1,9); DOWN=rect(0,9,1,10)
def mirror(pts): return [(14-x,y) for x,y in pts]
def base(arms_=True):
    p={}
    for x in range(2,13):
        for y in range(6,13): p[(x,y)]=BODY
    if arms_: put(p,DOWN+mirror(DOWN),BODY)
    for x in (3,5,9,11):
        for y in (13,14): p[(x,y)]=BODY
    for x in (4,10):
        for y in (8,9): p[(x,y)]=K
    return p
def arms(p,left=DOWN,right=DOWN):
    clear(p,rect(0,7,1,10)+rect(13,7,14,10))
    put(p,left,BODY); put(p,mirror(right),BODY); return p
TAU=2*math.pi; M=6
def clamp(x,a=0,b=1): return max(a,min(b,x))
def ease(t): t=clamp(t); return 0.5-0.5*math.cos(math.pi*t)
def lerp(a,b,t): return a+(b-a)*t
def kf(i,keys):
    if i<=keys[0][0]: return keys[0][1]
    for (a,va),(b,vb) in zip(keys,keys[1:]):
        if a<=i<=b: return va+(vb-va)*ease((i-a)/(b-a))
    return keys[-1][1]
def face(p,mode='n',dx=0,ey=0,blink=False):
    for x in range(2,13):
        for y in range(6,12):
            if p.get((x,y))==K: p[(x,y)]=BODY
    if mode=='n':
        for x in (4,10):
            for y in ((9,) if blink else (8,9)): p[(x+dx,y+ey)]=K
    elif mode=='hap':
        for ex in (4,10): put(p,[(ex-1+dx,9+ey),(ex+dx,8+ey),(ex+1+dx,9+ey)],K)
    else:  # '> <'
        put(p,[(3,7),(4,8),(3,9),(11,7),(10,8),(11,9)],K)
    return p
def canvas(pad=0): return Image.new('RGBA',((W+2*pad)*S,(H+2*pad)*S),(0,0,0,0))
def draw(img,p,pad=0):
    d=ImageDraw.Draw(img)
    for (x,y),c in p.items():
        X,Y=x+OX+pad,y+OY+pad
        if 0<=X<W+2*pad and 0<=Y<H+2*pad: d.rectangle([X*S,Y*S,(X+1)*S-1,(Y+1)*S-1],fill=c)
    return img
def xform(p,dx=0,dy=0,sx=1,sy=1,rot=0,piv=(7.5,15)):
    img=draw(canvas(M),p,M)
    Px,Py=(piv[0]+OX+M)*S,(piv[1]+OY+M)*S; Tx,Ty=dx*S,dy*S
    a=math.radians(rot); c,s=math.cos(a),math.sin(a)
    co=(c/sx,-s/sx,Px-(c*(Px+Tx)-s*(Py+Ty))/sx, s/sy,c/sy,Py-(s*(Px+Tx)+c*(Py+Ty))/sy)
    out=img.transform(img.size,Image.AFFINE,co,resample=Image.NEAREST)
    return out.crop((M*S,M*S,(M+W)*S,(M+H)*S))
def squash(v): return dict(sy=v,sx=1/math.sqrt(v))
def render(p,cs,ax,ay,rot=0,sx=1,sy=1):
    """Draw at any cell size cs; (ax,ay) in px is where the feet centre (7.5,15) lands."""
    img=canvas(); d=ImageDraw.Draw(img)
    for (x,y),c in p.items():
        X=math.floor(ax+(x-7.5)*cs+0.5); Y=math.floor(ay+(y-15)*cs+0.5)
        d.rectangle([X,Y,X+cs-1,Y+cs-1],fill=c)
    if rot or sx!=1 or sy!=1:
        a=math.radians(rot); c,s_=math.cos(a),math.sin(a)
        co=(c/sx,-s_/sx,ax-(c*ax-s_*ay)/sx, s_/sy,c/sy,ay-(s_*ax+c*ay)/sy)
        img=img.transform(img.size,Image.AFFINE,co,resample=Image.NEAREST)
    return img
def shadow(h=0,y=15,col='#D9D2CB'):
    w=9-4*clamp(h/3.5); x0=round(7.5-w/2); x1=round(7.5+w/2)-1
    return {(x,y):col for x in range(x0,x1+1)}
def comp(*layers):
    out=canvas()
    for L in layers:
        if L is None: continue
        if isinstance(L,dict): L=draw(canvas(),L)
        out.alpha_composite(L)
    return out
def bang(x,y): return {(x,y):BANG,(x,y+1):BANG,(x,y+2):BANG,(x,y+4):BANG}
def cx(x): return (x+OX)*S   # scene cell -> px
def cy(y): return (y+OY)*S

# ---------- tiny pixel font (3x5, row 5 = descender) ----------
GL={
 'a':["...","xx.","..x",".xx","xxx"], 'c':["...",".xx","x..","x..",".xx"],
 'e':["...",".x.","xxx","x..",".xx"], 'f':["..x",".x.","xxx",".x.",".x."],
 'g':["...",".xx","x.x",".xx","..x","xx."], 'i':["x",".","x","x","x"],
 'l':["x.","x.","x.","x.",".x"], 'm':[".....","xx.x.","x.x.x","x.x.x","x.x.x"],
 'n':["...","xx.","x.x","x.x","x.x"], 'o':["...",".x.","x.x","x.x",".x."],
 'p':["...","xx.","x.x","x.x","xx.","x.."], 'r':["...",".xx","x..","x..","x.."],
 't':[".x.","xxx",".x.",".x.","..x"], '-':["...","...","xxx","...","..."],
 '/':["..x","..x",".x.","x..","x.."], '>':["x..",".x.","..x",".x.","x.."],
 '<':["..x",".x.","x..",".x.","..x"], '=':["...","xxx","...","xxx","..."],
 '_':["...","...","...","...","xxx"], ' ':["..",".."],
 'b':["x..","xx.","x.x","x.x","xx."], 'd':["..x",".xx","x.x","x.x",".xx"],
 'h':["x..","xx.","x.x","x.x","x.x"], 'k':["x..","x.x","xx.","xx.","x.x"],
 's':["...",".xx","x..","..x","xx."], 'u':["...","x.x","x.x","x.x",".xx"],
 'w':[".....","x...x","x.x.x","x.x.x",".x.x."], 'y':["...","x.x","x.x",".xx","..x","xx."],
 'z':["...","xxx","..x",".x.","xxx"], ',':[".",".",".","x","x"],
 '(':[".x","x.","x.","x.",".x"], ')':["x.",".x",".x",".x","x."],
 ':':[".","x",".","x","."], '!':["x","x","x",".","x"],
 'E':["xxx","x..","xx.","x..","xxx"], 'L':["x..","x..","x..","x..","xxx"],
 'G':[".xx","x..","x.x","x.x",".xx"], 'T':["xxx",".x.",".x.",".x.",".x."],
 'M':["x...x","xx.xx","x.x.x","x...x","x...x"],
 '0':["xxx","x.x","x.x","x.x","xxx"], '1':[".x.","xx.",".x.",".x.","xxx"],
 '2':["xx.","..x",".x.","x..","xxx"], '3':["xx.","..x",".x.","..x","xx."],
 '4':["x.x","x.x","xxx","..x","..x"], '5':["xxx","x..","xx.","..x","xx."],
 '6':[".xx","x..","xx.","x.x",".x."], '7':["xxx","..x",".x.",".x.",".x."],
 '8':["xxx","x.x","xxx","x.x","xxx"], '9':["xxx","x.x","xxx","..x","xx."],
 '.':[".",".",".",".","x"], '?':["xx.","..x",".x.","...",".x."], "'":["x","x",".",".","."],
 'B':["xx.","x.x","xx.","x.x","xx."], 'A':[".x.","x.x","xxx","x.x","x.x"],
 'N':["x..x","xx.x","x.xx","x..x","x..x"], 'D':["xx.","x.x","x.x","x.x","xx."],
 'Y':["x.x","x.x",".x.",".x.",".x."], 'x':["...","x.x",".x.",".x.","x.x"],
}
def mix(c1,c2,t):
    a=[int(c1[k:k+2],16) for k in (1,3,5)]; b=[int(c2[k:k+2],16) for k in (1,3,5)]
    return '#'+''.join(f'{round(x+(y-x)*t):02X}' for x,y in zip(a,b))
def run_legs(p,f):
    """Alternate leg pairs for a running cycle; f is 0 or 1."""
    clear(p,rect(3,13,11,14))
    for x in ((3,9) if f else (5,11)): put(p,[(x,13)],BODY)
    for x in ((5,11) if f else (3,9)): put(p,[(x,13),(x,14)],BODY)
    return p
def term(img,x0,y0,x1,y1):
    box(img,x0,y0,x1,y1,'#3A3A48'); box(img,x0+4,y0+4,x1-4,y1-4,'#1E1E26')
def textc(img,s,mid,y,px,col): return text(img,s,round(mid-text_w(s)*px/2),y,px,col)
def spr(rows,x0,y0,pal):
    """Cell sprite from strings; chars not in pal are transparent."""
    return {(x0+k,y0+r):pal[ch] for r,row in enumerate(rows) for k,ch in enumerate(row) if ch in pal}
def confetti(i,start,n=16,seed=3):
    rng=random.Random(seed); fx={}; cols=['#F2C14E','#E5484D','#3B82F6','#2FB15A','#C77DFF']
    for k in range(n):
        x0=rng.uniform(-4,18); v=rng.uniform(0.5,0.9); ph=rng.uniform(0,6); c=cols[k%5]
        t=i-start-rng.uniform(0,8)
        if t<0: continue
        y=-7+t*v
        if y<16: fx[(round(x0+math.sin(t*0.5+ph)),round(y))]=c
    return fx
def text_w(s): return sum(len(GL[c][0])+1 for c in s)-1
def text(img,s,x,y,px,col):
    """Draw s with its top-left at (x,y) px, each font pixel px wide."""
    d=ImageDraw.Draw(img)
    for c in s:
        g=GL[c]
        for r,row in enumerate(g):
            for k,ch in enumerate(row):
                if ch=='x': d.rectangle([x+k*px,y+r*px,x+(k+1)*px-1,y+(r+1)*px-1],fill=col)
        x+=(len(g[0])+1)*px
    return x
def box(img,x0,y0,x1,y1,col):
    if round(x1)<=round(x0) or round(y1)<=round(y0): return
    ImageDraw.Draw(img).rectangle([round(x0),round(y0),round(x1)-1,round(y1)-1],fill=col)

# ---------- Thinking · 思考中 ----------
# Claude Code's spinner: · ✢ ✳ ✶ ✻ ✽ and back
_PL=lambda r:[(2,2+k) for k in range(-r,r+1)]+[(2+k,2) for k in range(-r,r+1)]
_X=lambda r:[(2+k,2+k) for k in range(-r,r+1)]+[(2+k,2-k) for k in range(-r,r+1)]
SPIN=[[(2,2)],_PL(1),_PL(2),_X(2)+[(2,2)],_PL(2)+_X(1),_PL(2)+_X(2)]
def thinking():
    fr=[]; N=60; ORG='#E8845F'; DOT='#C9A99A'
    seq=list(range(6))+list(range(4,0,-1))
    for i in range(N):
        sp={(x+5,y-6):ORG for x,y in SPIN[seq[(i//3)%len(seq)]]}
        k=(i//6)%4
        for j in range(3):
            if j<k: sp[(11+2*j,-2)]=DOT
        p=base(); look=(i//20)%3
        arms(p,DOWN,UP if 6<=i%30<26 else MID)
        face(p,'n',[1,-1,0][look] if look<2 else 0,-1,blink=(i%30 in (27,28)))
        rot=4*math.sin(TAU*i/30)
        ch=xform(p,0,-0.35*abs(math.sin(TAU*i/30)),rot=rot)
        fr.append((comp(shadow(),sp,ch),70))
    return fr

# ---------- /compact · 上下文压缩 ----------
def compact():
    fr=[]; N=64; PL='#4A4A56'; PL2='#6B6B7A'; TXT='#E6E1DA'; ROD='#8A8A98'
    for i in range(N):
        sy=kf(i,[(0,1),(18,1),(26,0.38),(40,0.38),(43,1.28),(46,0.88),(49,1.06),(52,1)])
        top=15-9*sy                       # body top under bottom-pivot squash
        hover=kf(i,[(0,-7),(6,-7),(18,6),(40,6),(44,-8)])
        pb=top if 18<=i<40 else min(hover,top)
        p=base()
        if i<18: face(p,'n',0,-1,blink=(i in (8,9)))
        elif i<42: face(p,'x'); arms(p,MID,MID)
        elif i<52: face(p,'hap'); arms(p,UP,UP)
        else: face(p,'n',0,0,blink=(i in (58,59)))
        sq=dict(sy=sy,sx=sy**-0.28) if sy!=1 else {}
        jig=0.35*math.sin(i*2.4) if 26<=i<40 else 0
        ch=xform(p,jig,0,**sq)
        img=canvas(); y1=cy(pb); y0=y1-4.5*S
        box(img,cx(7.5)-S/2,0,cx(7.5)+S/2,y0,ROD)
        box(img,cx(-2),y0,cx(17),y1,PL); box(img,cx(-2),y1-S/2,cx(17),y1,PL2)
        lbl='/compact'; px=4
        text(img,lbl,round(cx(7.5)-text_w(lbl)*px/2),round(y0+1.2*S),px,TXT)
        fx={}
        if 22<=i<40:
            for k,(x,y) in enumerate([(-2,13),(17,13),(-3,11),(18,11)]):
                ph=((i-22)/6+k/4)%1; fx[(x+(-1 if x<7 else 1)*round(ph*2),y-round(ph*2))]='#C9C4BC'
        if i>=52:
            q=[(6,-2),(7,-3),(8,-3),(9,-2),(9,-1),(8,0),(8,1),(8,3)]
            fx.update({(x,y+round(kf(i,[(52,1),(55,0)]))):'#3B82F6' for x,y in q})
        fr.append((comp(shadow(),ch,img,fx),60))
    fr[17]=(fr[17][0],200); fr[33]=(fr[33][0],300); fr[-1]=(fr[-1][0],700)
    return fr

# ---------- git clone · 克隆 ----------
def clone():
    fr=[]; N=64; T='#3A3A44'; G='#4CAF6A'
    for i in range(N):
        cs=round(kf(i,[(0,12),(12,12),(18,6),(46,6),(54,12)]))
        spread=kf(i,[(12,0),(22,90),(44,90),(54,0)])
        ay=264
        layers=[]
        img=canvas()
        cmd='git clone'; px=5; shown=cmd[:max(0,min(len(cmd),(i-2)//1))] if i<54 else ''
        if shown:
            x=round(cx(7.5)-text_w('> '+cmd)*px/2)
            x=text(img,'> ',x,cy(-6),px,G); text(img,shown,x,cy(-6),px,T)
        for k,sgn in enumerate((-1,1,0)):
            if sgn and spread<2: continue
            p=base()
            hop=0
            if 22<=i<44:
                ph=((i-22)/11-k*0.18)%1; hop=max(0,math.sin(math.pi*ph*1.4))*14 if ph<0.72 else 0
                face(p,'hap' if sgn else 'n',blink=(not sgn and i in (36,37)))
                if hop>4: arms(p,UP,UP)
            elif i<12:
                face(p,'x' if i>=5 else 'n',0,-1 if i<5 else 0); arms(p,MID,MID) if i>=5 else None
            else: face(p,'n',blink=(i in (58,59)))
            jx=(3*math.sin(i*2.5)) if 5<=i<12 else 0
            layers.append(render(p,cs,138+sgn*spread+jx,ay-hop))
        flash={}
        if 12<=i<15: flash={(x,y):'#FFF3B0' for x,y in [(7,3),(7,2),(2,5),(1,4),(13,5),(14,4)]}
        fr.append((comp(img,*layers,flash),60))
    fr[21]=(fr[21][0],200); fr[-1]=(fr[-1][0],500)
    return fr

# ---------- Merge Conflict · 合并冲突 ----------
def conflict():
    fr=[]; N=56; OURS='#2F9E5A'; THEIRS='#3B6FD8'; SEP='#9A9AA6'
    cs=8; ay=264; gap=60  # half body width at cs=8
    for i in range(N):
        off=kf(i,[(0,40),(8,0),(30,0),(34,34),(44,30),(52,40),(56,40)])
        lean=kf(i,[(6,0),(10,9),(30,9),(32,-6),(38,0)])
        jit=2*math.sin(i*2.7) if 10<=i<30 else 0
        L=base(); R=base()
        if 8<=i<32:
            face(L,'x'); face(R,'x'); arms(L,DOWN,MID); arms(R,MID,DOWN)
        else:
            face(L,'n',1,0,blink=(i in (46,47))); face(R,'n',-1,0,blink=(i in (48,49)))
        hop=kf(i,[(30,0),(33,10),(36,0)])
        li=render(L,cs,138-gap-off+jit,ay-hop,rot=lean)
        ri=render(R,cs,138+gap+off-jit,ay-hop,rot=-lean)
        img=canvas(); px=4
        y=cy(-6)
        for s,col,xx in (('<<<<<<<',OURS,cx(-3)),('>>>>>>>',THEIRS,cx(18)-text_w('>>>>>>>')*px)):
            text(img,s,round(xx),y,px,col)
        text(img,'=======',round(cx(7.5)-text_w('=======')*px/2),y+7*px,px,SEP)
        fx={}
        if 10<=i<30:
            for k,(x,y) in enumerate([(7,3),(6,2),(8,2),(7,5),(5,4),(9,4)]):
                if (i+k)%3==0: fx[(x,y+3)]='#FFC94A'
            if (i//2)%2: fx.update(bang(7,-1))
        fr.append((comp(img,li,ri,fx),60))
    fr[-1]=(fr[-1][0],300)
    return fr

# ---------- rm -rf · 删库 ----------
def rmrf():
    fr=[]; N=76; BG='#1E1E26'; ED='#3A3A48'; FG='#E6E1DA'; PR='#E8845F'; RED='#E5484D'
    cmd='rm -rf /'
    rng=random.Random(7); full=base()
    order=sorted([k for k,c in full.items() if c==BODY],key=lambda k:(-k[1]+rng.random()*2.2))
    eyes_px=[k for k,c in full.items() if c==K]
    for i in range(N):
        img=canvas(); px=4
        box(img,cx(-3),cy(-6),cx(18),cy(3),ED); box(img,cx(-3)+4,cy(-6)+4,cx(18)-4,cy(3)-4,BG)
        tx=cx(-3)+14; ty=cy(-6)+12
        typed=cmd[:clamp((i-4)//2,0,len(cmd))] if i<56 else ''
        x=text(img,'> ',tx,ty,px,PR); x=text(img,typed,x,ty,px,FG)
        if (i<24 or i>=56) and (i//4)%2==0: box(img,x+px,ty,x+4*px,ty+5*px,FG)
        if 26<=i<56:   # scrolling red delete log
            for r in range(3):
                w=[14,9,17,11,6,15][(i+r)%6]
                box(img,tx,ty+(8+r*5)*px,tx+w*px*2,ty+(8+r*5)*px+2*px,RED)
        p=base(); dy=0; fx={}
        if i<24:
            face(p,'n',1 if i<20 else 0,-1 if i<20 else 0)
            if 4<=i<20: arms(p,UP if i%2 else MID,MID if i%2 else UP)
        elif i<27:
            arms(p,UP,UP); dy=-kf(i,[(24,0),(25,1.5),(27,0)])
        elif i<56:
            face(p,'x')
            gone=int(len(order)*clamp((i-27)/20))
            for k in order[:gone]: p.pop(k,None)
            for k in order[max(0,gone-10):gone]:
                fx[(k[0],k[1]+1+(i%2))]='#B9B2AA'
            if 30<=i<44 and (i//2)%2: fx.update(bang(16,5))
            if i>=48:
                p={k:K for k in eyes_px}; face(p,'n',0,0,blink=(i in (51,52)))
                p={k:c for k,c in p.items() if c==K}
        else:
            p={}
            if i>=60:
                dy=kf(i,[(60,-14),(66,0)])
                p=base(); face(p,'n',blink=(i in (72,73)))
                if 66<=i<70: p=None
        if p is None:
            p=base(); ch=xform(p,0,0,**squash(kf(i,[(66,0.7),(68,1.15),(70,1)])))
        else: ch=xform(p,0,dy) if p else None
        sh=shadow(-dy) if (i<47 or i>=60) else None
        fr.append((comp(sh,ch,fx,img),60))   # terminal on top: Clawd drops back out of it
    fr[25]=(fr[25][0],250); fr[50]=(fr[50][0],400); fr[59]=(fr[59][0],400)
    return fr

# ---------- hello, world · 你好，世界 ----------
def hello():
    fr=[]; N=56; s='hello, world'
    for i in range(N):
        img=canvas(); px=5; y=cy(-5)
        n=clamp((i-2)//2,0,len(s))
        x=text(img,s[:n],round(cx(7.5)-text_w(s)*px/2),y,px,'#3A3A44')
        if n<len(s) or (i//4)%2==0: box(img,x+px,y,x+4*px,y+5*px,'#E8845F')
        p=base(); dy=0; rot=0
        if 4<=i<44:
            arms(p,DOWN,UP if (i//3)%2 else MID); face(p,'hap')
            dy=-0.6*abs(math.sin(TAU*i/12)); rot=3*math.sin(TAU*i/12)
        else: face(p,'n',blink=(i in (50,51)))
        fr.append((comp(shadow(),img,xform(p,0,dy,rot=rot)),70))
    fr[-1]=(fr[-1][0],500)
    return fr

# ---------- LGTM · 批准 ----------
def lgtm():
    fr=[]; N=60; RED='#D23C3C'
    STAMP=["...hhh...","...hhh...","....n....","....n....",".rrrrrrr.",".RRRRRRR."]
    pal={'h':'#6B4A3A','n':'#8A6A55','r':'#D64545','R':'#A83232'}
    def imprint(px,ang):
        img=canvas(); s='LGTM'; w=text_w(s)*px; h=5*px; bw=max(4,px//2); my=cy(-2.5)
        X0,Y0,X1,Y1=138-w/2-2*px,my-h/2-1.5*px,138+w/2+2*px,my+h/2+1.5*px
        box(img,X0,Y0,X1,Y1,RED); box(img,X0+bw,Y0+bw,X1-bw,Y1-bw,(0,0,0,0))
        text(img,s,round(138-w/2),round(my-h/2),px,RED)
        rng=random.Random(5); d=ImageDraw.Draw(img)
        for _ in range(70):   # worn-ink texture
            x=rng.uniform(X0,X1); y=rng.uniform(Y0,Y1); d.rectangle([x,y,x+px//2,y+px//2],fill=(0,0,0,0))
        return img.rotate(ang,resample=Image.NEAREST,center=(138,my))
    for i in range(N):
        p=base(); st=None; dy=0; sq={}; imp=None; shake=0
        if i<15:
            arms(p,UP,UP); face(p,'n',0,-1)
            st=spr(STAMP,3,round(kf(i,[(0,0),(10,-2),(13,-3),(15,6)])),pal)
            if i>=13: sq=squash(0.9)
        else:
            face(p,'hap')
            if i<19: sq=squash(kf(i,[(15,0.85),(19,1)]))
            elif i<48: dy=-0.5*abs(math.sin(TAU*(i-19)/16))
            imp=imprint([14,12,10][min(i-15,2)],8)
            if i<20: shake=0.25 if i%2 else -0.25
        fr.append((comp(shadow(),xform(p,shake,dy,**sq),st,imp),60))
    fr[12]=(fr[12][0],200); fr[-1]=(fr[-1][0],600)
    return fr

# ---------- Tests Passed · 测试通过 ----------
def passed():
    fr=[]; N=56; G='#2FB15A'; G2='#1F7A3E'
    path=[(4,-3),(5,-2),(6,-1),(7,-2),(8,-3),(9,-4),(10,-5),(11,-6)]
    for i in range(N):
        n=clamp(i-3,0,len(path)); ck={}
        for x,y in path[:n]: ck[(x,y+1)]=G2
        for x,y in path[:n]: ck[(x,y)]=G
        p=base(); dy=0; sq={}
        if i<12:
            arms(p,MID,MID); face(p,'n',0,-1); dx=0.2*math.sin(i*2.6)
        else:
            t=((i-12)%12)/12; dx=0; dy=-3.2*math.sin(math.pi*t)
            face(p,'hap')
            if dy<-0.8: arms(p,UP,UP)
            if t<0.1: sq=squash(0.86)
        fr.append((comp(shadow(-dy),ck,xform(p,dx,dy,**sq),confetti(i,12)),60))
    fr[11]=(fr[11][0],200)
    return fr

# ---------- Error · 报错 ----------
def error():
    fr=[]; N=60
    for i in range(N):
        img=canvas()
        if i>=6 and (i>=28 or (i//2)%2==0): textc(img,'Error',138,cy(-6),7,'#E5484D')
        p=base(); dx=0; dy=0; rot=0; fx={}
        if i<6: face(p,'n',blink=(i in (2,3)))
        elif i<28:
            arms(p,UP,UP); face(p,'x'); dx=0.3*math.sin(i*2.7)
            fx.update(bang(-2,4) if (i//3)%2 else bang(16,4))
        elif i<52:
            face(p,'x'); rot=kf(i,[(28,0),(34,180)]); dy=-kf(i,[(28,0),(31,3),(34,0)])
            if i>=34:   # legs-up wiggle
                clear(p,rect(3,13,11,14))
                for k,x in enumerate((3,5,9,11)): put(p,[(x,13)]+([(x,14)] if (i//2+k)%2 else []),BODY)
                for k in range(3):
                    a=TAU*(i/12+k/3); fx[(round(7+4*math.cos(a)),round(3+1.2*math.sin(a)))]='#F2C14E'
        else:
            face(p,'n',blink=(i in (57,58))); rot=kf(i,[(52,180),(56,360)]); dy=-kf(i,[(52,0),(54,3),(56,0)])
        fr.append((comp(shadow(-dy),img,xform(p,dx,dy,rot=rot,piv=(7.5,10)),fx),60))
    fr[-1]=(fr[-1][0],400)
    return fr

# ---------- Coffee Break · 咖啡续命 ----------
def coffee():
    fr=[]; N=64
    MUG=["wwww.","wrrwh","wwwwh","wwww."]; pal={'w':'#4F7BD9','r':'#FFFFFF','h':'#3A5FB0'}
    for i in range(N):
        p=base(); dx=0; dy=0; rot=0; fx={}
        mx=round(kf(i,[(18,14),(24,9),(34,9),(40,14)])); my=round(kf(i,[(18,8),(24,5),(34,5),(40,8)]))
        if i<18:
            face(p,'n',blink=True); rot=4*math.sin(TAU*i/24); arms(p,DOWN,MID)
        elif i<40:
            face(p,'n',blink=True); arms(p,DOWN,UP)
        else:
            face(p,'n'); put(p,[(4,7),(10,7)],K); arms(p,UP,MID)
            dx=0.25*math.sin(i*3.1); dy=-kf(i,[(40,0),(42,2),(44,0)])
            if i<50: fx.update(bang(-2,3))
            for k,(x,y) in enumerate([(-2,9),(16,5),(0,1)]):
                if (i+k)%4<2: fx.update({(x,y):'#F2C14E',(x+1,y-1):'#F2C14E'})
        p.update(spr(MUG,mx,my,pal))
        if not 22<=i<36:
            for k in range(3):
                t=((i+k*5)%15)/15; fx[(mx+1+k%2+round(0.6*math.sin(t*6)),my-1-round(t*4))]='#D8D2CA'
        fr.append((comp(shadow(),xform(p,dx,dy,rot=rot),fx),70))
    fr[30]=(fr[30][0],300)
    return fr

# ---------- Friday Deploy · 周五上线 ----------
def deploy():
    fr=[]; N=64
    for i in range(N):
        img=canvas(); x=round(cx(7.5)-text_w('friday deploy')*4/2)
        x=text(img,'friday ',x,cy(-6),4,'#E5484D'); text(img,'deploy',x,cy(-6),4,'#3A3A44')
        p=base(); arms(p,MID,MID); face(p,'n',blink=True)
        put(p,[(x,y) for x in (5,7,9) for y in range(3,10)],'#8B5A2B')
        put(p,[(5,2),(7,2),(9,2)],'#FF6A3D' if (i//3)%2 else '#FFB03D')
        sy=1
        for b in (8,26,44):
            if b<=i<b+14: sy=kf(i,[(b,1),(b+5,0.86),(b+9,0.86),(b+14,1)])
        tip=15-13*sy; fx={}
        for k in range(6):
            t=((i+k*4)%24)/24
            fx[(5+2*(k%3)+round(1.2*math.sin(t*7+k)),round(tip-1-t*8))]='#CFC8C0' if t<0.6 else '#E6E1DA'
        fr.append((comp(shadow(),img,xform(p,0,0,sy=sy),fx),70))
    return fr

# ---------- Works on My Machine · 在我电脑上能跑 ----------
def works():
    fr=[]; N=60
    LAP=["ttttttttttttt","mmmmmmwmmmmmm","bbbbbbbbbbbbb"]; pal={'t':'#B8BDC5','m':'#9AA0A8','w':'#FFFFFF','b':'#6E747C'}
    for i in range(N):
        img=canvas()
        textc(img,'works on',138,cy(-6),4,'#3A3A44'); textc(img,'my machine',138,cy(-6)+28,4,'#2FB15A')
        p=base(); dy=0; rot=0; fx={}
        shrug=(2<=i<12) or (18<=i<28)
        if shrug: arms(p,UP,UP); face(p,'hap'); dy=-0.6
        elif i<34: arms(p,MID,MID); face(p,'n',1 if i<16 else -1)
        else:
            arms(p,MID,MID); face(p,'hap'); rot=5*math.sin(TAU*(i-34)/13)
            for k in range(2):
                t=((i-34+k*7)%14)/14
                if t<0.85: fx.update(spr(["x.x","xxx",".x."],12-12*k+k,round(4-t*8),{'x':'#F59A9A'}))
        p.update(spr(LAP,1,10,pal))
        fr.append((comp(shadow(),img,xform(p,0,dy,rot=rot),fx),70))
    return fr

# ---------- Bug Hunt · 抓虫 ----------
def bug():
    fr=[]; N=56
    BA=[".gg.","gGgk","l.l."]; BB=[".gg.","gGgk",".l.l"]; pal={'g':'#4C9A4F','G':'#2E6B30','k':'#222222','l':'#222222'}
    for i in range(N):
        if i<20: bx=lerp(-5,6,i/20)
        elif i<32: bx=6
        elif i<46: bx=lerp(6,20,(i-32)/14)
        else: bx=None
        bg=spr(BA if (i//2)%2 else BB,round(bx),13,pal) if bx is not None and not 21<=i<32 else None
        p=base(); dy=0; sq={}; fx={}; dx=0
        if i<14: face(p,'n',-1 if bx<4 else 0,1)
        elif i<17: face(p,'n',0,1); sq=squash(0.85)
        elif i<21: face(p,'x'); arms(p,UP,UP); dy=-kf(i,[(17,0),(19,3),(21,0)])
        elif i<32:
            face(p,'hap'); arms(p,UP,UP) if i>=24 else None
            if i<24: sq=squash(kf(i,[(21,0.78),(24,1)]))
        elif i<36: face(p,'n',1,1)
        elif i<46:
            face(p,'x'); dx=0.25*math.sin(i*2.8)
            if (i//2)%2: fx.update(bang(16,3))
        else: face(p,'n',blink=(i in (52,53)))
        fr.append((comp(shadow(-dy),bg,xform(p,dx,dy,**sq),fx),60))
    fr[-1]=(fr[-1][0],400)
    return fr

# ---------- Slacking Off · 摸鱼 ----------
def fish():
    fr=[]; N=56
    F=["..bbbbb..t",".bbbbbbbtt","bkbBbbbbtt",".wwwwwww.t"]
    F2=["..bbbbb...",".bbbbbbbtt","bkbBbbbbtt",".wwwwwwwtt"]
    pal={'b':'#7FA7C9','B':'#5E86A8','k':'#222222','t':'#5E86A8','w':'#C9DCEB'}
    for i in range(N):
        p=base(); arms(p,MID,[]); face(p,'hap',blink=False)
        hx=round(4+6*(0.5-0.5*math.cos(TAU*i/14)))
        fsh=F if (i//3)%2 else F2
        if i%20 in (10,11): fsh=[r.replace('k','b') for r in fsh]
        p.update(spr(fsh,2,10,pal)); put(p,rect(hx,10,hx+1,11),'#C9694B'); fx={}
        for k in range(2):
            t=((i+k*14)%28)/28
            if t<0.8: fx.update(spr([".x.x.","xxxxx",".xxx.","..x.."] if t<0.4 else ["x.x","xxx",".x."],12-12*k,round(3-t*9),{'x':'#F59A9A'}))
        fr.append((comp(shadow(),xform(p,0,-0.3*abs(math.sin(TAU*i/28))),fx),70))
    return fr

# ---------- Clock Out · 下班 ----------
def offwork():
    fr=[]; N=60
    for i in range(N):
        img=canvas(); box(img,cx(1),cy(-6),cx(14),cy(0),'#24242C')
        t='18:00' if 14<=i<44 else '17:59'
        textc(img,t,cx(7.5),cy(-6)+18,7,'#4ADE80' if t=='18:00' else '#FF7A59')
        if 14<=i<18: fx_border=True; box(img,cx(1),cy(0),cx(14),cy(0)+4,'#F2C14E')
        p=base(); dx=0; dy=0; rot=0; sq={}; fx={}; ch=True
        if i<14: arms(p,MID,MID); face(p,'n',0,-1); dy=-0.4*((i//3)%2)
        elif i<18: face(p,'hap'); sq=squash(0.8)
        elif i<28:
            face(p,'hap'); arms(p,MID,MID); dx=26*((i-18)/10)**2; rot=-12
            for y in (8,10,12):
                for k in range(4): fx[(round(dx)-2-k-(y%4),y)]='#CFC8C0'
            if i<22: fx.update({(1,14):'#D9D2CB',(0,13):'#D9D2CB',(-1,14):'#D9D2CB'})
        elif i<44: ch=False
        else:
            dx=kf(i,[(44,-24),(56,0)]); face(p,'n',blink=True); dy=-0.4*((i//2)%2)
        if 28<=i<34: fx.update({(1,14):'#E6E1DA',(-1,13):'#E6E1DA'})
        fr.append((comp(img,shadow() if ch and i<18 or i>=54 else None,xform(p,dx,dy,rot=rot,**sq) if ch else None,fx),60))
    fr[13]=(fr[13][0],300); fr[40]=(fr[40][0],500)
    return fr

# ---------- Overtime · 加班 ----------
def overtime():
    fr=[]; N=64
    MOON=[".yyy","yy..","yy..",".yyy"]
    for i in range(N):
        sky=spr(MOON,-3,-6,{'y':'#F2D57E'})
        for k,(x,y) in enumerate([(3,-5),(15,-1),(10,-6),(-2,1)]):
            if (i//4+k)%3: sky[(x,y)]='#F2D57E'
        img=canvas(); tw=text_w('02:00')*4; text(img,'02:00',cx(18)-tw-6,cy(-6),4,'#E5484D')
        desk={}
        put(desk,rect(-4,11,18,11),'#A5825F'); put(desk,rect(-4,12,18,12),'#8B6B4E')
        put(desk,rect(-2,13,-2,15)+rect(16,13,16,15),'#6B5139')
        put(desk,rect(12,6,17,9),'#C7CCD3'); put(desk,rect(11,10,18,10),'#9AA0A8'); desk[(14,7)]='#FFFFFF'
        p=base(); c=i%32; dy=0; rot=0; fx={}
        if c<16:
            face(p,'n',blink=True); dy=kf(c,[(0,0),(14,1.5)]); rot=kf(c,[(0,0),(14,-6)])
            if c>=6:
                t=(c-6)/10; text(img,'z',cx(-1),round(cy(4)-t*30),[3,4,5][min(2,int(t*3))],'#8C9BD8')
        elif c<22:
            face(p,'n'); put(p,[(4,7),(10,7)],K); dy=-kf(c,[(16,0),(17,1),(19,0)])
            fx.update(bang(7,-1) if c<20 else {})
        else: face(p,'n',blink=(c>=28))
        fr.append((comp(sky,img,xform(p,0,dy,rot=rot),desk,fx),80))
    return fr

# ---------- Good Night · 晚安 ----------
def sleep():
    fr=[]; N=60
    CAP=["...........ww",".........bbww",".......bbbb..","....bbbbbb...","..bbbbbbbb...","wwwwwwwwwww.."]
    for i in range(N):
        p=base(); face(p,'n'); clear(p,[(4,8),(4,9),(10,8),(10,9)]); put(p,[(4,8),(4,9),(10,8),(10,9)],BODY)
        put(p,[(3,9),(4,9),(10,9),(11,9)],K)
        p.update(spr(CAP,2,0,{'b':'#4C6EF5','w':'#C9D3F2'}))
        sy=1-0.035*(1+math.sin(TAU*i/30))
        img=canvas()
        for k in range(3):
            t=((i+k*20)%60)/60
            text(img,'z',round(cx(-3)+t*24),round(cy(5)-t*110),[3,4,5,6][min(3,int(t*4))],'#7C8FD9')
        fr.append((comp(shadow(),xform(p,0,0,sy=sy),img),90))
    return fr

# ---------- 404 Not Found · 找不到 ----------
def notfound():
    fr=[]; N=60; Q=[(6,-2),(7,-3),(8,-3),(9,-2),(9,-1),(8,0),(8,1),(8,3)]
    for i in range(N):
        bx={}; put(bx,rect(-1,9,15,16),'#C8925A'); put(bx,rect(-1,9,15,9),'#B98249')
        put(bx,rect(-1,10,-1,15)+rect(15,10,15,15)+rect(-1,16,15,16),'#A6743F')
        lab=canvas(); textc(lab,'404',cx(7.5),cy(10)+12,8,'#6B4423')
        dy=kf(i,[(0,6),(8,6),(14,-1),(30,-1),(33,6)])
        p=base()
        if i<22: face(p,'n',-1 if i>=14 else 0)
        elif i<28: face(p,'n',1)
        elif i<30: face(p,'n')
        else: face(p,'x')
        fx={}
        if 34<=i<52: fx={(x,y+5+round(kf(i,[(34,1),(37,0)]))):'#3B82F6' for x,y in Q}
        fr.append((comp(xform(p,0,dy),bx,lab,fx),60))
    fr[29]=(fr[29][0],250); fr[-1]=(fr[-1][0],300)
    return fr

# ---------- while(true) · 死循环 ----------
def loop():
    fr=[]; N=48; C=(7,5); R=10
    for i in range(N):
        wh={}
        for x in range(-4,19):
            for y in range(-7,17):
                if abs(math.hypot(x-C[0],y-C[1])-R)<0.55: wh[(x,y)]='#8D93A0'
        ang=-i*0.18
        for k in range(4):
            a=ang+k*TAU/4
            for r in range(2,R):
                wh.setdefault((round(C[0]+r*math.cos(a)),round(C[1]+r*math.sin(a))),'#C9CDD6')
        for k in range(16):
            a=ang+k*TAU/16; wh[(round(C[0]+(R-1)*math.cos(a)),round(C[1]+(R-1)*math.sin(a)))]='#B5BAC4'
        put(wh,rect(6,4,7,5),'#8D93A0')
        img=canvas(); textc(img,'while(true)',138,4,4,'#3A3A44')
        p=base(); f=(i//2)%2
        clear(p,rect(3,13,11,14))
        for x in (3,9) if f else (5,11): put(p,[(x,13)],BODY)
        for x in (5,11) if f else (3,9): put(p,[(x,13),(x,14)],BODY)
        arms(p,MID if f else DOWN,DOWN if f else MID); fx={}
        if i<24: face(p,'n',1)
        else:
            face(p,'x')
            for k in range(2):
                t=((i+k*4)%8)/8; fx[(round(1-t*4),round(5-k*2+t*2))]='#7FB2E5'
        fr.append((comp(wh,xform(p,0,-0.4*f,rot=-6),fx,img),60))
    return fr

# ---------- Force Push · 强推 ----------
def forcepush():
    fr=[]; N=64
    for i in range(N):
        img=canvas(); x=round(cx(7.5)-text_w('git push --force')*4/2)
        x=text(img,'git push ',x,cy(-6),4,'#3A3A44'); text(img,'--force',x,cy(-6),4,'#E5484D')
        if i<22: bx=11+0.6*clamp(i/22)
        elif i<30: bx=11.6+20*((i-22)/8)**2
        elif i<44: bx=40
        else: bx=kf(i,[(44,30),(52,11)])
        p=base(); fx={}; rot=0
        if i<22:
            dx=-4+0.6*clamp(i/22)+0.2*math.sin(i*2.9); rot=-6; arms(p,DOWN,MID); face(p,'x')
        elif i<30: dx=kf(i,[(22,-3.4),(30,0)]); rot=kf(i,[(22,-6),(27,-18),(30,0)]); face(p,'x'); arms(p,DOWN,MID)
        elif i<44: dx=0; arms(p,UP,UP); face(p,'hap')
        else:
            dx=min(0,bx-15); face(p,'x' if bx<16 else 'n',1)
            if 48<=i<58 and (i//2)%2: fx.update(bang(-3,3))
        blk={}
        b=round(bx)
        if b<19:
            put(blk,rect(b,3,b+7,14),'#7A7F8C'); put(blk,rect(b,3,b+7,3)+rect(b,14,b+7,14)+rect(b,3,b,14)+rect(b+7,3,b+7,14),'#5B606C')
            if 22<=i<30 or 44<=i<52:
                for y in (5,8,11): put(fx,[(b-2-k,y) for k in range(3)],'#CFC8C0')
        lab=canvas()
        if b<19: textc(lab,'main',cx(b+4),cy(7),4,'#FFFFFF')
        fr.append((comp(img,shadow(),blk,lab,xform(p,dx,0,rot=rot),fx),60))
    fr[-1]=(fr[-1][0],400)
    return fr

# ---------- Yes, Proceed · 疯狂同意 ----------
def proceed():
    fr=[]; N=64; ORG='#E8845F'; FG='#E6E1DA'
    presses=[8,18,26,32,37,41,44,47,50,53,56]
    for i in range(N):
        done=[t for t in presses if t<=i]; n=len(done); since=i-done[-1] if done else 99
        img=canvas()
        for off in (12,6):   # the queue of dialogs waiting behind
            x0,y0=cx(-3)+off,cy(-5)-off
            box(img,x0,y0,cx(16)+off,cy(2)-off,'#9C5A43'); box(img,x0+4,y0+4,cx(16)+off-4,cy(2)-off-4,'#1E1E26')
        if since>=1:
            x0,y0=cx(-3),cy(-5)
            box(img,x0,y0,cx(16),cy(2),ORG); box(img,x0+4,y0+4,cx(16)-4,cy(2)-4,'#1E1E26')
            text(img,'proceed?',x0+14,y0+14,4,FG)
            box(img,x0+10,y0+44,x0+92,y0+72,'#3A3A48'); text(img,'> yes',x0+16,y0+48,4,ORG)
        p=base(); dy=0; sq={}
        face(p,'x' if n>=5 else 'n',0,-1 if n<5 else 0)
        if since<1: arms(p,DOWN,MID); dy=0.5; sq=squash(0.92)
        else: arms(p,DOWN,UP)
        dx=0.25*math.sin(i*2.9) if n>=6 else 0
        fr.append((comp(shadow(),img,xform(p,dx,dy,**sq)),60))
    return fr

# ---------- Esc · 急停 ----------
def esc():
    fr=[]; N=56
    for i in range(N):
        ky=round(kf(i,[(8,-22),(12,0),(44,0),(50,-24)]))
        key={}
        put(key,rect(12,8+ky,18,12+ky),'#E9E6E1'); put(key,rect(12,13+ky,18,14+ky),'#BDB8B0')
        put(key,rect(12,8+ky,18,8+ky)+rect(12,8+ky,12,14+ky)+rect(18,8+ky,18,14+ky),'#8E8A84')
        lab=canvas(); textc(lab,'esc',cx(15.5),cy(9+ky)+6,5,'#3A3A44')
        p=base(); rot=0; fx={}
        dx=kf(i,[(0,-14),(14,-3)]) if i<14 else -3
        if i<14:
            run_legs(p,(i//2)%2); face(p,'n',1 if i<11 else 0); arms(p,MID if (i//2)%2 else DOWN,DOWN if (i//2)%2 else MID)
            for y in (8,10,12): put(fx,[(round(dx)-2-k,y) for k in range(3)],'#CFC8C0')
        elif i<26:
            face(p,'x'); rot=kf(i,[(14,0),(16,10),(22,10),(26,0)])
            if i<20:
                for k in range(3): fx[(round(dx)+1-k-(i-14),14-k%2)]='#D9D2CB'
            if 16<=i<24 and (i//2)%2: fx.update(bang(7,0))
        else: face(p,'n',1,0,blink=(i in (34,35)))
        fr.append((comp(shadow(),xform(p,dx,0,rot=rot),key,lab,fx),60))
    fr[13]=(fr[13][0],120); fr[-1]=(fr[-1][0],300)
    return fr

# ---------- Usage Limit · 额度用完 ----------
def limit():
    """A battery drains while Clawd types; at empty it reads 'limit reached' and Clawd melts flat."""
    fr=[]; N=72; RED='#E5484D'; YEL='#F2C14E'; G='#2FB15A'; OL='#3A3A44'
    for i in range(N):
        f=kf(i,[(0,1),(28,0),(56,0),(62,1)]) if i<62 else 1
        img=canvas(); bx0,bx1,by0,by1=cx(2),cx(12),cy(-6),cy(-2)
        empty=f<0.02
        if not (empty and 32<=i<56 and (i//3)%2):   # empty battery blinks
            box(img,bx0,by0,bx1,by1,OL); box(img,bx0+5,by0+5,bx1-5,by1-5,(0,0,0,0))
            box(img,bx1,by0+14,bx1+8,by1-14,OL)
            col=G if f>0.5 else YEL if f>0.2 else RED
            if f>0: box(img,bx0+9,by0+9,bx0+9+(bx1-bx0-18)*f,by1-9,col)
        if 30<=i<58: textc(img,'limit reached',138,cy(-1)-2,5,RED)
        p=base(); dx=0; dy=0; sq={}; fx={}
        if i<28:
            slow=1+2*(i>=18)          # typing slows as the battery runs low
            face(p,'n',0,1 if i<18 else 0,blink=(i>=20))
            tap=(i//slow)%2; arms(p,UP if tap else MID,MID if tap else UP)
            if i>=20: sq=dict(sy=kf(i,[(20,1),(28,0.92)]),sx=1)
        elif i<56:
            face(p,'n',blink=True); arms(p,DOWN,DOWN)
            sy=kf(i,[(28,0.92),(34,0.5)]); sq=dict(sy=sy,sx=sy**-0.4)
            if 36<=i<54 and (i//6)%2==0:
                fx[(15,8)]='#7FB2E5'; fx[(15,9)]='#7FB2E5'
        else:
            face(p,'hap'); arms(p,UP,UP)
            sy=kf(i,[(56,0.5),(60,1.2),(63,0.9),(66,1)]); sq=dict(sy=sy,sx=sy**-0.4)
            dy=-kf(i,[(58,0),(61,2),(64,0)])
        fr.append((comp(shadow(-dy),img,xform(p,dx,dy,**sq),fx),70))
    fr[31]=(fr[31][0],300); fr[-1]=(fr[-1][0],300)
    return fr

# ---------- Plan Mode · 计划模式 ----------
def plan():
    fr=[]; N=60; TEAL='#2E9C8F'
    HAT=["....yyyyyyy....","...yyyyyyyyy...",".ddddddddddddd."]
    LINES=[(x,13) for x in range(4,11)]+[(4,12),(10,12)]+[(4,11),(5,11),(6,11),(7,11),(8,11),(9,11),(10,11)]+[(7,12)]
    for i in range(N):
        img=canvas(); tw=text_w('plan mode')*4; x0=round(138-(tw+20)/2); y0=cy(-6)
        box(img,x0,y0+2,x0+5,y0+18,TEAL); box(img,x0+9,y0+2,x0+14,y0+18,TEAL)
        text(img,'plan mode',x0+20,y0,4,TEAL)
        p=base(); arms(p,MID,MID); dy=0
        if i<10: face(p,'n')
        elif i<40: face(p,'n',-1 if (i//8)%2 else 1,0,blink=(i in (30,31))); dy=0.4 if (i//6)%2 else 0
        else: face(p,'hap')
        if 42<=i<50: dy=-kf(i,[(42,0),(45,2),(48,0)])
        p.update(spr(HAT,0,3,{'y':'#F2C14E','d':'#D9A532'}))
        w=kf(i,[(2,1),(10,11)])
        put(p,[(x,y) for x in range(round(7-w/2),round(7+w/2)+1) for y in range(10,15)],'#3B6FD8')
        put(p,[(x,y) for x in range(round(7-w/2),round(7+w/2)+1) for y in (10,14)],'#2E5AB8')
        if i>=10: put(p,LINES[:clamp((i-10)//2+1,0,len(LINES))],'#DCE8FF')
        fr.append((comp(shadow(-dy),img,xform(p,0,dy)),70))
    fr[-1]=(fr[-1][0],400)
    return fr

# ---------- /clear · 清空上下文 ----------
def clear_ctx():
    fr=[]; N=60; FG='#E6E1DA'; ORG='#E8845F'; rng=random.Random(11)
    bars=[rng.randint(6,26) for _ in range(40)]
    for i in range(N):
        img=canvas(); X0,Y0,X1,Y1=cx(-3),cy(-6),cx(18),cy(4); term(img,X0,Y0,X1,Y1)
        tx=X0+14; px=4
        if i<18:
            for r in range(5):
                box(img,tx,Y0+14+r*16,tx+bars[r+i//3]*px*2,Y0+14+r*16+8,'#8A8A98')
            typed='/clear'[:clamp((i-4)//2,0,6)]; py=Y1-30
            x=text(img,'> ',tx,py,px,ORG); x=text(img,typed,x,py,px,FG)
            if (i//4)%2==0: box(img,x+px,py,x+4*px,py+5*px,FG)
        elif i<24:
            for r in range(5-(i-18)):
                box(img,tx,Y0+14+(r+(i-18))*16,tx+bars[r]*px*2,Y0+14+(r+(i-18))*16+8,'#8A8A98')
        else:
            x=text(img,'> ',tx,Y0+14,px,ORG)
            if (i//4)%2==0: box(img,x+px,Y0+14,x+4*px,Y0+14+5*px,FG)
        p=base(); rot=0; fx={}
        if i<18:
            face(p,'x'); rot=3*math.sin(i*1.3)
            if 4<=i<16: arms(p,UP if i%2 else MID,MID if i%2 else UP)
        else:
            face(p,'hap' if i<48 else 'n',blink=(i in (54,55)))
            if i<40:
                for k,(x,y) in enumerate([(-2,7),(16,6),(0,4),(15,10)]):
                    if (i+k)%4<2: fx.update({(x,y):'#F2C14E',(x+1,y):'#F2C14E',(x,y-1):'#F2C14E'})
        fr.append((comp(shadow(),img,xform(p,0,0,rot=rot),fx),60))
    fr[17]=(fr[17][0],200); fr[-1]=(fr[-1][0],400)
    return fr

# ---------- ultrathink · 深度思考 ----------
def ultrathink():
    fr=[]; N=60; RAIN=['#E5484D','#F2994A','#F2C14E','#2FB15A','#3B82F6','#8B5CF6']
    BULB=[".yyy.","yyyyy","yyyyy",".yyy.",".ggg.","..g.."]
    w='ultrathink'; px=5
    for i in range(N):
        img=canvas(); x=round(138-text_w(w)*px/2)
        for k,c in enumerate(w[:clamp(i-1,0,len(w))]):
            x=text(img,c,x,cy(-6)-4,px,RAIN[(k+i//2)%6])+px
        p=base(); dx=0; fx={}
        heat=kf(i,[(12,0),(40,1),(44,1),(48,0)])
        if i<12: face(p,'n',0,-1)
        elif i<44:
            face(p,'x'); dx=0.25*math.sin(i*3)
            for k in range(4):
                t=((i+k*3)%12)/12; fx[(3+k*3+round(math.sin(t*6+k)),round(5-t*6))]='#CFC8C0' if t<0.6 else '#E6E1DA'
        else:
            face(p,'hap'); fx.update(spr(BULB,5,-2,{'y':'#FFE066','g':'#9AA0AA'}))
            if (i//3)%2: fx.update({(3,-2):'#FFE066',(11,-2):'#FFE066',(3,2):'#FFE066',(11,2):'#FFE066',(7,-4):'#FFE066'})
        hot=mix(BODY,'#E0402A',heat)
        p={k:(hot if c==BODY else c) for k,c in p.items()}
        fr.append((comp(shadow(),img,xform(p,dx,0),fx),60))
    fr[44]=(fr[44][0],200); fr[-1]=(fr[-1][0],400)
    return fr

# ---------- Subagents · 子代理 ----------
def subagents():
    fr=[]; N=64; G='#2FB15A'; CK=[(0,1),(1,2),(2,1),(3,0)]
    paths=[[(6,138),(20,-40),(34,-40),(48,138)],[(8,138),(22,316),(36,316),(50,138)],[(10,138),(26,-40),(38,-40),(52,138)]]
    for i in range(N):
        tiny=[]; img=canvas(); d=ImageDraw.Draw(img)
        for k,pth in enumerate(paths):
            if not pth[0][0]<=i<pth[-1][0]: continue
            tx=kf(i,pth); back=i>=pth[2][0]
            q=run_legs(base(),(i//2)%2); face(q,'hap' if back else 'n',(-1 if tx<138 else 1) if not back else 0)
            tiny.append(render(q,4,tx,264))
            if back:
                for cx_,cy_ in CK: d.rectangle([tx-8+cx_*4,264-60+cy_*4,tx-8+cx_*4+3,264-60+cy_*4+7],fill=G)
        p=base(); dy=0; fx={}
        if i<12: arms(p,UP if (i//4)%2 else MID,MID if (i//4)%2 else UP); face(p,'n',-1 if (i//4)%2 else 1)
        elif i<48: face(p,'n',-1 if (i//10)%2 else 1,blink=(i in (30,31)))
        else:
            face(p,'hap')
            if i<58: dy=-2*abs(math.sin(math.pi*(i-48)/5)); arms(p,UP,UP)
        if i>=50:
            for k in range(3):
                if i>=48+2*k: fx.update({(x+1+5*k,y+1):G for x,y in CK})
        fr.append((comp(shadow(-dy),*tiny,xform(p,0,dy),img,fx),60))
    fr[-1]=(fr[-1][0],400)
    return fr

# ---------- Todo List · 待办清单 ----------
def todo():
    fr=[]; N=64; FG='#E6E1DA'; ORG='#E8845F'; G='#2FB15A'
    T=[12,24,36,48]; L=[22,16,25,13]
    for i in range(N):
        img=canvas(); X0,Y0,X1,Y1=cx(-3),cy(-6),cx(18),cy(4); term(img,X0,Y0,X1,Y1)
        cur=next((r for r,t in enumerate(T) if i<t),None)
        for r in range(4):
            y=Y0+14+r*28; bx=X0+14
            if i>=T[r]:
                box(img,bx,y,bx+16,y+16,G)
                for cx_,cy_ in [(0,2),(1,3),(2,2),(3,1),(4,0)]: box(img,bx+2+cx_*2.4,y+4+cy_*2.4,bx+5+cx_*2.4,y+7+cy_*2.4,'#FFFFFF')
                box(img,bx+26,y+4,bx+26+L[r]*6,y+12,'#5B5B66'); box(img,bx+24,y+7,bx+28+L[r]*6,y+9,'#9A9AA6')
            else:
                col=ORG if r==cur else '#B5B5C0'
                box(img,bx,y,bx+16,y+16,col); box(img,bx+3,y+3,bx+13,y+13,'#1E1E26')
                box(img,bx+26,y+4,bx+26+L[r]*6,y+12,col)
        p=base(); dy=0; tick=any(t-3<=i<t for t in T)
        if i<T[-1]:
            face(p,'n',0,-1); arms(p,DOWN,UP if tick else MID)
        else:
            face(p,'hap'); t2=((i-T[-1])%8)/8; dy=-2.5*math.sin(math.pi*t2); arms(p,UP,UP)
        fr.append((comp(shadow(-dy),img,xform(p,0,dy),confetti(i,T[-1]) if i>=T[-1] else None),60))
    return fr

# ---------- You're Absolutely Right! · 您说得对 ----------
def right():
    fr=[]; N=56; ORG='#E8845F'; DK='#3A3A44'
    lines=[("You're",DK),('absolutely',ORG),('right!',DK)]
    for i in range(N):
        img=canvas()
        for k,(s,c) in enumerate(lines):
            if i>=3+k*6: textc(img,s,138,4+k*30,4,c)
        p=base(); dy=0; sq={}; fx={}
        if i<3: face(p,'n')
        else:
            face(p,'hap'); t=((i-3)%8)/8; dy=0.8*max(0,math.sin(TAU*t))
            if dy>0.4: sq=squash(0.94)
            arms(p,UP if ((i-3)//8)%2 else MID,UP if ((i-3)//8)%2 else MID)
        if i>=15:
            for k,(x,y) in enumerate([(-3,9),(17,7),(-2,4),(16,12)]):
                if (i+k*2)%6<3: fx.update({(x,y):'#F2C14E',(x+1,y):'#F2C14E',(x,y+1):'#F2C14E',(x-1,y):'#F2C14E',(x,y-1):'#F2C14E'})
        fr.append((comp(shadow(),img,xform(p,0,dy,**sq),fx),60))
    return fr

# ---------- /exit · 拜拜 ----------
def bye():
    fr=[]; N=60; FG='#E6E1DA'; ORG='#E8845F'
    for i in range(N):
        img=canvas(); X0,Y0,X1,Y1=cx(-3),cy(-6),cx(18),cy(1); term(img,X0,Y0,X1,Y1)
        tx,ty,px=X0+14,Y0+14,4
        x=text(img,'> ',tx,ty,px,ORG); x=text(img,'/exit'[:clamp((i-2)//2,0,5)],x,ty,px,FG)
        if i<14 and (i//4)%2==0: box(img,x+px,ty,x+4*px,ty+5*px,FG)
        if i>=42:
            x=text(img,'bye!',tx,ty+36,px,FG)
            if (i//4)%2==0: box(img,x+px,ty+36,x+4*px,ty+36+5*px,FG)
        p=base(); ch=None
        if i<14:
            face(p,'n',0,-1)
            if 2<=i<12: arms(p,UP if i%2 else MID,MID if i%2 else UP)
            ch=xform(p)
        elif i<30:
            face(p,'hap'); arms(p,DOWN,UP if (i//3)%2 else MID); ch=xform(p,0,0,rot=3*math.sin(TAU*i/12))
        elif i<42:
            face(p,'hap'); arms(p,UP,UP)
            cs=round(kf(i,[(30,12),(41,1)])); ch=render(p,cs,138,kf(i,[(30,264),(41,108)]))
        fr.append((comp(shadow() if i<30 else None,ch,img),60))
    fr[13]=(fr[13][0],200); fr[-1]=(fr[-1][0],600)
    return fr

# ---------- Banned · 封号 ----------
def banned():
    fr=[]; N=64; RED='#E5484D'; GRAY='#9C9A97'
    def gavel(ang):
        img=canvas(); g={}
        put(g,rect(3,0,9,5),'#6B4A3A'); put(g,rect(3,1,9,1)+rect(3,4,9,4),'#C9A27A')
        put(g,rect(10,2,19,3),'#8B6B4E')
        draw(img,g)
        return img.rotate(ang,resample=Image.NEAREST,center=(cx(19),cy(2.5)))
    for i in range(N):
        ang=kf(i,[(0,-70),(10,-70),(16,0),(22,0),(30,-80)])
        p=base(); dy=0; sq={}; fx={}; shake=0
        if i<16:
            face(p,'hap'); arms(p,UP if (i//2)%2 else MID,MID if (i//2)%2 else UP)
        else:
            face(p,'x') if i<34 else face(p,'n',blink=True)
            sy=kf(i,[(16,0.62),(20,0.62),(30,0.9)]); sq=dict(sy=sy,sx=sy**-0.3)
            if i<20: shake=0.3 if i%2 else -0.3
            if 16<=i<24:
                for k,(x,y) in enumerate([(1,4),(13,4),(0,7),(14,7)]):
                    if (i+k)%2: fx[(x,y)]='#F2C14E'
            g=kf(i,[(16,0),(24,1)])
            p={k:(mix(BODY,GRAY,g) if c==BODY else c) for k,c in p.items()}
            if 40<=i<56 and (i//8)%2==0: fx[(11,10)]='#7FB2E5'; fx[(11,11)]='#7FB2E5'
        txt=None
        if i>=16 and not (i>=40 and (i//4)%2):
            txt=canvas(); px=[9,7,6][min(i-16,2)]; w=text_w('BANNED')*px; y0=cy(-6)
            box(txt,138-w/2-px*2,y0,138+w/2+px*2,y0+9*px,RED)
            box(txt,138-w/2-px,y0+px,138+w/2+px,y0+8*px,'#FFFFFF')
            text(txt,'BANNED',round(138-w/2),y0+2*px,px,RED)
            txt=txt.rotate(-6,resample=Image.NEAREST,center=(138,y0+4.5*px))
        bars={}
        if i>=30:
            drop=round(kf(i,[(30,-14),(34,0)]))
            for x in range(-2,18,3): put(bars,[(x,y+drop) for y in range(3,16)],'#4A4A56')
            put(bars,[(x,3+drop) for x in range(-2,17)],'#4A4A56')
        fr.append((comp(shadow(),xform(p,shake,dy,**sq),fx,bars,gavel(ang) if i<30 else None,txt),60))
    fr[16]=(fr[16][0],200); fr[-1]=(fr[-1][0],600)
    return fr

def to_gif(frames,path):
    gf=[]
    for im,_ in frames:
        a=im.split()[3]; pal=im.convert('RGB').convert('P',palette=Image.ADAPTIVE,colors=255)
        pal.paste(255,a.point(lambda v:255 if v<128 else 0)); gf.append(pal)
    gf[0].save(path,save_all=True,append_images=gf[1:],duration=[d for _,d in frames],loop=0,transparency=255,disposal=2)
    return os.path.getsize(path)
def wechat(frames):
    """240x240, <=100KB: pad to square, downscale, drop frames until it fits."""
    sq=[]
    for im,d in frames:
        c=Image.new('RGBA',(H*S,H*S),(0,0,0,0)); c.paste(im,((H*S-W*S)//2,0))
        sq.append((c.resize((240,240),Image.NEAREST),d))
    return sq
def save(nm,fr):
    os.makedirs(OUT,exist_ok=True); os.makedirs(OUT_WX,exist_ok=True)
    n=to_gif(fr,os.path.join(OUT,nm+'.gif'))
    wx=wechat(fr); step=1
    while True:
        sub=[(wx[k][0],sum(d for _,d in wx[k:k+step])) for k in range(0,len(wx),step)]
        m=to_gif(sub,os.path.join(OUT_WX,nm+'.gif'))
        if m<=100_000 or step>=3: break
        step+=1
    print(f'{nm}: {len(fr)} frames, {n//1024}KB | wechat {len(sub)} frames, {m//1024}KB')

ALL=['thinking','compact','clone','conflict','rmrf','hello','lgtm','passed','error','coffee',
     'deploy','works','bug','fish','offwork','overtime','sleep','notfound','loop','forcepush',
     'proceed','esc','limit','plan','clear_ctx','ultrathink','subagents','todo','right','bye','banned']
FILE={'clear_ctx':'clear'}   # clear() is already a drawing helper
if __name__=='__main__':
    for nm in (sys.argv[1:] or ALL):
        nm={v:k for k,v in FILE.items()}.get(nm,nm)
        save(FILE.get(nm,nm),globals()[nm]())
