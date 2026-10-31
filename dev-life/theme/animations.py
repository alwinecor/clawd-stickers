# SPDX-License-Identifier: MIT
# License: ../../LICENSE
"""Animations that exist only in the clawd-on-desk theme, drawn with the helpers in ../src/clawd_dev.py."""
import math
from clawd_dev import *

# ---------- Tests Passed · 测试通过, extended ----------
def passed_long():
    """Tests Passed, hopping for as long as LGTM and ending on a full hop, with a second wave of confetti."""
    fr=[]; N=72; G='#2FB15A'; G2='#1F7A3E'
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
        conf=confetti(i,12)
        conf.update(confetti(i,48,seed=5))   # the first wave has landed by now
        fr.append((comp(shadow(-dy),ck,xform(p,dx,dy,**sq),conf),60))
    fr[11]=(fr[11][0],200)
    return fr

# ---------- detached HEAD · 头掉了, extended ----------
def detached_long():
    """detached HEAD, hopping with relief soon after the head is back instead of freezing."""
    fr=[]; N=90
    for i in range(N):
        img=canvas(); textc(img,'detached HEAD',138,cy(-6),4,'#3A3A44')
        bx=kf(i,[(12,0),(20,5),(28,-5),(36,0)])
        p=base(); fx={}; dy=0
        if i<8: face(p,'n')
        elif i<12: face(p,'x')
        elif i<44: face(p,'n',1 if bx>0.5 else -1 if bx<-0.5 else 0)
        else: face(p,'hap')
        apart=12<=i<44
        if 12<=i<36: run_legs(p,(i//2)%2)
        if 8<=i<46:
            hy=-kf(i,[(8,0),(12,2.5),(40,2.5),(44,0)])+(0.3*math.sin(i*0.6) if apart else 0)
            head={k:c for k,c in p.items() if k[1]<=9 and 2<=k[0]<=12}
            body={k:c for k,c in p.items() if k not in head}
            layers=[xform(body,bx,0),xform(head,0,hy)]
            if 8<=i<12: fx={(1,4):'#F2C14E',(13,4):'#F2C14E',(7,1):'#F2C14E'}
        else:
            sq=squash(kf(i,[(46,0.85),(49,1)])) if 46<=i<49 else {}
            if i>=50:
                t=((i-50)%10)/10; dy=-2.5*math.sin(math.pi*t)
                if dy<-0.8: arms(p,UP,UP)
                if t<0.1: sq=squash(0.86)
            layers=[xform(p,0,dy,**sq)]
        fr.append((comp(shadow(-dy),img,*layers,fx),60))
    return fr

# ---------- Banned · 封号, extended ----------
def banned_long():
    """Banned, with the sign flashing and the tears falling for the whole double-click duration."""
    fr=[]; N=88; RED='#E5484D'; GRAY='#9C9A97'
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
            if 40<=i<80 and (i//8)%2==0: fx[(11,10)]='#7FB2E5'; fx[(11,11)]='#7FB2E5'
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
    fr[16]=(fr[16][0],200)
    return fr

# ---------- Dizzy · 转晕 ----------
ROLL=[(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]   # eye offsets going round clockwise
def dizzy():
    """Usage Limit spun round by the mouse: no keyboard, the eyes roll round and Clawd sways as the battery drains."""
    fr=[]; N=72; RED='#E5484D'; YEL='#F2C14E'; G='#2FB15A'; OL='#3A3A44'
    # i counts 70 ms steps; the spin runs at half steps so its eyes and sway move smoothly
    ts=[k/2 for k in range(56)]+list(range(28,N))
    for i in ts:
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
            ph=i if i<18 else 18+(i-18)/1.5   # spin winds down with the battery
            face(p,'n',*ROLL[int(ph)%8]); arms(p,MID,MID)
            rot=6*math.sin(TAU*ph/6)
            sq=dict(sy=kf(i,[(20,1),(28,0.92)]),sx=1,rot=rot)
        elif i<56:
            face(p,'n',blink=True); arms(p,DOWN,DOWN)
            sy=kf(i,[(28,0.92),(34,0.5)]); sq=dict(sy=sy,sx=sy**-0.4)
            if 36<=i<54 and (i//6)%2==0:
                fx[(15,8)]='#7FB2E5'; fx[(15,9)]='#7FB2E5'
        else:
            face(p,'hap'); arms(p,UP,UP)
            sy=kf(i,[(56,0.5),(60,1.2),(63,0.9),(66,1)]); sq=dict(sy=sy,sx=sy**-0.4)
            dy=-kf(i,[(58,0),(61,2),(64,0)])
        fr.append((comp(shadow(-dy),img,xform(p,dx,dy,**sq),fx),70 if i>=28 else 35))
    k=ts.index(31); fr[k]=(fr[k][0],300); fr[-1]=(fr[-1][0],300)
    return fr

# ---------- Yawn · 打哈欠 ----------
CAP=["...........ww",".........bbww",".......bbbb..","....bbbbbb...","..bbbbbbbb...","wwwwwwwwwww.."]
def sleep_scene(i,born=None,cap=0,eyes='shut'):
    """Frame i of Good Night. born: only z's at most this many frames old exist yet; cap: nightcap raised
    this many cells; eyes: 'open', 'half' (squinting) or 'shut' (the sleeping lines)."""
    p=base(); face(p,'n',blink=eyes=='half')
    if eyes=='shut':
        clear(p,[(4,8),(4,9),(10,8),(10,9)]); put(p,[(4,8),(4,9),(10,8),(10,9)],BODY)
        put(p,[(3,9),(4,9),(10,9),(11,9)],K)
    p.update(spr(CAP,2,-cap,{'b':'#4C6EF5','w':'#C9D3F2'}))
    sy=1-0.035*(1+math.sin(TAU*i/30))
    img=canvas()
    for k in range(3):
        a=(i+k*20)%60; t=a/60
        if born is not None and a>born: continue
        text(img,'z',round(cx(-3)+t*24),round(cy(5)-t*110),[3,4,5,6][min(3,int(t*4))],'#7C8FD9')
    return comp(shadow(),xform(p,0,0,sy=sy),img)
def yawn():
    """Drowsy like Overtime: the eyes squint, fight to stay open, squint again and shut; then the nightcap
    drops on and the z's start. Breathing runs on Good Night's clock throughout, so the last frame leads
    straight into its frame 0, which the theme plays next."""
    EYES=[(0,'open'),(8,'half'),(12,'open'),(14,'half'),(20,'shut')]
    fr=[]
    for i in range(24):
        eyes=[e for k,e in EYES if i>=k][-1]
        fr.append((sleep_scene(i-64,born=-1,cap=16,eyes=eyes),90))
    for j in range(40):   # lead-in: Good Night frames -40..-1, cap falling, z's appearing one by one
        fr.append((sleep_scene(j-40,born=j,cap=round(kf(j,[(0,16),(9,0)]))),90))
    return fr

# ---------- Wake · 醒来 ----------
MUG=["wwww.","wrrwh","wwwwh","wwww."]; MUG_PAL={'w':'#4F7BD9','r':'#FFFFFF','h':'#3A5FB0'}
def wake():
    """From the Good Night pose the eyes crack open, the nightcap lifts away and the mug slides in,
    landing on frame 0 of Coffee Break, which then plays through."""
    fr=[]
    for j in range(14):
        cap=round(kf(j,[(5,0),(13,16)])); mx=round(kf(j,[(5,24),(13,14)]))
        scene=sleep_scene(min(8+j,22.5),born=-1,cap=cap,eyes='shut' if j<4 else 'half')
        fr.append((comp(scene,spr(MUG,mx,8,MUG_PAL)),70))
    return fr+coffee()

# ---------- /exit · 拜拜, extended ----------
def bye_long():
    """/exit, except Clawd comes back: the terminal closes, a shadow grows on the ground and Clawd drops from
    the sky, lands flat, shakes off the stars and ends on the idle pose."""
    fr=[]; N=84; FG='#E6E1DA'; ORG='#E8845F'
    for i in range(N):
        img=canvas(); X0,Y0,X1,Y1=cx(-3),cy(-6),cx(18),cy(1); mid=(Y0+Y1)//2
        h=round(kf(i,[(52,(Y1-Y0)//2),(56,0)]))
        if h>2: term(img,X0,mid-h,X1,mid+h)
        if i<52:
            tx,ty,px=X0+14,Y0+14,4
            x=text(img,'> ',tx,ty,px,ORG); x=text(img,'/exit'[:clamp((i-2)//2,0,5)],x,ty,px,FG)
            if i<14 and (i//4)%2==0: box(img,x+px,ty,x+4*px,ty+5*px,FG)
            if i>=42:
                x=text(img,'bye!',tx,ty+36,px,FG)
                if (i//4)%2==0: box(img,x+px,ty+36,x+4*px,ty+36+5*px,FG)
        p=base(); ch=None; sh=None; fx={}
        if i<14:
            face(p,'n',0,-1)
            if 2<=i<12: arms(p,UP if i%2 else MID,MID if i%2 else UP)
            ch=xform(p); sh=shadow()
        elif i<30:
            face(p,'hap'); arms(p,DOWN,UP if (i//3)%2 else MID); ch=xform(p,0,0,rot=3*math.sin(TAU*i/12)); sh=shadow()
        elif i<42:
            face(p,'hap'); arms(p,UP,UP)
            cs=round(kf(i,[(30,12),(41,1)])); ch=render(p,cs,138,kf(i,[(30,264),(41,108)]))
        elif 57<=i<69:
            sh=shadow(kf(i,[(57,3.5),(69,0)]))
            if i>=64:
                face(p,'x'); arms(p,UP,UP); ch=xform(p,0,-22*(1-((i-64)/5)**2),sy=1.1,sx=0.95)
        elif i>=69:
            sh=shadow()
            if i<74:
                face(p,'x'); ch=xform(p,0,0,**squash(kf(i,[(69,0.62),(71,1.12),(74,1)])))
                if i<72: fx={(-1,14):'#D9D2CB',(0,13):'#D9D2CB',(-2,13):'#D9D2CB',(15,14):'#D9D2CB',(14,13):'#D9D2CB',(16,13):'#D9D2CB'}
            else:
                dizzy_=i<80; face(p,'x' if dizzy_ else 'n')
                ch=xform(p,0,0,rot=5*math.sin(TAU*(i-74)/4) if dizzy_ else 0)
                if dizzy_:
                    for k in range(3):
                        a=TAU*(i/6+k/3); fx[(round(7.5+5*math.cos(a)),round(4+1.2*math.sin(a)))]='#F2C14E'
        fr.append((comp(sh,ch,fx,img),60))
    fr[13]=(fr[13][0],200)
    return fr

# ---------- Team · 多人协作 (2 and 3 sessions) ----------
# Two Clawds at 2/3 size work side by side at their own screens; with 3 sessions a third stands on top of the
# screens, so nothing else moves between the two. Both loop every 72 frames.
CS=8; FOOT=cy(15); LEFT,RIGHT,TOP=72,204,138; DESK=106   # DESK: top edge of the screens, where the third stands
LINES=[(13,'#E8845F'),(8,'#9A9AA6'),(12,'#2FB15A'),(6,'#9A9AA6'),(10,'#7FB2E5'),(13,'#9A9AA6')]
FAILS=4   # which of the six tests goes red
def screen(ax):
    img=canvas(); term(img,ax-58,DESK,ax+58,DESK+70)
    return img
def ground(ax):
    img=canvas(); box(img,ax-36,FOOT,ax+36,FOOT+CS,'#D9D2CB')
    return img
def coder(i):
    img=screen(LEFT); x=LEFT-46
    for r in range(3):
        w,c=LINES[(i//12+r)%6]
        if r==2: w*=(i%12+1)/12   # the bottom line is the one being typed
        box(img,x,DESK+14+r*16,x+w*7,DESK+24+r*16,c)
    q=base(); face(q,'n',0,-1,blink=i%32<2); tap=(i//2)%2; arms(q,UP if tap else MID,MID if tap else UP)
    return img,ground(LEFT),render(q,CS,LEFT,FOOT)
def tester(i):
    """Runs the tests one by one and panics for a moment when one fails."""
    img=screen(RIGHT); x=RIGHT-46; s=i//12
    for r in range(3):
        k=(s+r)%6; y=DESK+14+r*16; running=r==2 and i%12<8
        col='#E8845F' if running else '#E5484D' if k==FAILS else '#2FB15A'
        if not (running and (i//2)%2): box(img,x,y,x+10,y+10,col)
        box(img,x+18,y+2,x+18+(LINES[k][0]*6),y+8,'#9A9AA6')
    q=base(); h=0; fx=canvas()
    if 32<=i<44:
        face(q,'x'); arms(q,UP,UP); h=round(10*abs(math.sin(math.pi*(i-32)/6)))
        if (i//2)%2: box(fx,RIGHT+64,FOOT-74,RIGHT+68,FOOT-58,BANG); box(fx,RIGHT+64,FOOT-54,RIGHT+68,FOOT-50,BANG)
    else: face(q,'n',0,-1,blink=(i+11)%40<2); arms(q,MID,MID)
    return img,ground(RIGHT),render(q,CS,RIGHT,FOOT-h),fx
def lookout(i):
    """Stands on the screens sipping coffee while the other two work."""
    c=i%36; sip=14<=c<26; my=round(kf(c,[(10,9),(14,5),(26,5),(30,9)]))
    q=base(); face(q,'n',0,1,blink=sip); arms(q,UP if sip else MID,DOWN)
    q.update(spr(MUG,-3,my,MUG_PAL))
    img=canvas()
    if not sip:
        for k in range(2):
            t=((c+k*9)%18)/18; x=TOP-74+k*12+round(3*math.sin(t*6)); y=DESK+(my-16)*CS-round(t*20)
            box(img,x,y,x+CS,y+CS,'#D8D2CA')
    return render(q,CS,TOP,DESK),img
def team2():
    return [(comp(*coder(i),*tester(i)),60) for i in range(72)]
def team3():
    return [(comp(*coder(i),*tester(i),*lookout(i)),60) for i in range(72)]
