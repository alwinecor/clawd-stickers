# SPDX-License-Identifier: MIT
# License: ../../LICENSE
"""Animations that exist only in the clawd-on-desk theme, drawn with the helpers in ../src/clawd_dev.py."""
import math
from clawd_dev import *

# ---------- Longer cuts of stickers ----------
def passed_long():
    """Tests Passed, hopping for as long as LGTM and ending on a full hop, with a second wave of confetti."""
    return passed(72,second_wave=True)
def detached_long():
    """detached HEAD, hopping with relief soon after the head is back instead of freezing."""
    return detached(90,hops=True,end=60)
def banned_long():
    """Banned, with the sign flashing and the tears falling for the whole double-click duration."""
    return banned(88,tears=80,end=60)

# ---------- Dizzy · 转晕 ----------
ROLL=[(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]   # eye offsets going round clockwise
def dizzy():
    """Usage Limit spun round by the mouse: no keyboard, the eyes roll round and Clawd sways as the battery drains."""
    fr=[]; N=72
    # i counts 70 ms steps; the spin runs at half steps so its eyes and sway move smoothly
    ts=[k/2 for k in range(56)]+list(range(28,N))
    for i in ts:
        img=canvas(); battery(img,i)
        p=base(); dy=0; sq={}; fx={}
        if i<28:
            ph=i if i<18 else 18+(i-18)/1.5   # spin winds down with the battery
            face(p,'n',*ROLL[int(ph)%8]); arms(p,MID,MID)
            rot=6*math.sin(TAU*ph/6)
            sq=dict(sy=kf(i,[(20,1),(28,0.92)]),sx=1,rot=rot)
        else: dy,sq,fx=melt(p,i)
        fr.append((comp(shadow(-dy),img,xform(p,0,dy,**sq),fx),70 if i>=28 else 35))
    hold(fr,{ts.index(31):300,-1:300})
    return fr

# ---------- Yawn · 打哈欠 ----------
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
    fr=[]; N=84
    for i in range(N):
        img=canvas(); X0,Y0,X1,Y1=cx(-3),cy(-6),cx(18),cy(1); mid=(Y0+Y1)//2
        h=round(kf(i,[(52,(Y1-Y0)//2),(56,0)]))
        if h>2: term(img,X0,mid-h,X1,mid+h)
        if i<52: exit_prompt(img,X0,Y0,i)
        p=base(); ch=None; sh=None; fx={}
        if i<42:
            ch=exit_clawd(p,i)
            if i<30: sh=shadow()
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
                        a=TAU*(i/6+k/3); fx[(round(7.5+5*math.cos(a)),round(4+1.2*math.sin(a)))]=GOLD
        fr.append((comp(sh,ch,fx,img),60))
    hold(fr,{13:200})
    return fr

# ---------- Team · 多人协作 (2 and 3 sessions) ----------
# Two Clawds at 2/3 size work side by side at their own screens; with 3 sessions a third stands on top of the
# screens, so nothing else moves between the two. Both loop every 72 frames.
CS=8; LEFT,RIGHT,TOP=72,204,MIDX; DESK=106   # DESK: top edge of the screens, where the third stands
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
    q=base(); face(q,'n',0,-1,blink=i%32<2); flap(q,(i//2)%2)
    return img,ground(LEFT),render(q,CS,LEFT,FOOT)
def tester(i):
    """Runs the tests one by one and panics for a moment when one fails."""
    img=screen(RIGHT); x=RIGHT-46; s=i//12
    for r in range(3):
        k=(s+r)%6; y=DESK+14+r*16; running=r==2 and i%12<8
        col='#E8845F' if running else RED if k==FAILS else '#2FB15A'
        if not (running and (i//2)%2): box(img,x,y,x+10,y+10,col)
        box(img,x+18,y+2,x+18+(LINES[k][0]*6),y+8,'#9A9AA6')
    q=base(); h=0; fx=canvas()
    if 32<=i<44:
        face(q,'x'); arms(q,UP,UP); h=round(10*abs(math.sin(math.pi*(i-32)/6)))
        if (i//2)%2: box(fx,RIGHT+64,FOOT-74,RIGHT+68,FOOT-58,RED); box(fx,RIGHT+64,FOOT-54,RIGHT+68,FOOT-50,RED)
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
