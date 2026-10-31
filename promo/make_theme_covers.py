# SPDX-License-Identifier: MIT
"""
Animated 3:4 pages (1080x1440) for sharing the clawd-on-desk theme, in the same
style as make_covers.py:

  1. Clawd next to a mock Claude Code session, changing with each step
  2. a grid of what triggers which animation
  3. the animations only the theme has

  python promo/make_theme_covers.py                # all pages, dark terminal theme
  python promo/make_theme_covers.py 1              # just page 1
  python promo/make_theme_covers.py --light 2 3    # cream theme

Output: theme-N-{dark,light}.gif, plus theme-N-{dark,light}-static.png.
The triggers follow the table in dev-life/README.md.
"""
import sys
from PIL import Image, ImageDraw
import make_covers as mc
from make_covers import CW,CH,BAR,BLINK,ORANGE,TERM_TXT,TERM_DIM,font,label

GREEN='#3FB96B'; BLUE='#6FA8DC'
DIM={'dark':TERM_DIM,'light':'#6F655E'}
NOTE='Unofficial fan project. Not affiliated with Anthropic.'
# frame index of each theme-only animation's punchline, for the stills
mc.KEY.update(passed_long=65,team2=30,team3=30,dizzy=40,yawn=30,wake=30)

def dim(): return DIM['dark' if mc.TH is mc.THEMES['dark'] else 'light']
def centered(d,s,y,px,fill):
    f=font(px,mono=True); d.text(((CW-d.textlength(s,font=f))/2,y),s,font=f,fill=fill)
def frame(heading=None,sub=None):
    """Page background: terminal bars and heading."""
    img=Image.new('RGB',(CW,CH),mc.TH['bg']); d=ImageDraw.Draw(img)
    cursor=mc.terminal_bars(d)
    if heading: centered(d,heading,BAR+38,54,ORANGE)
    if sub: centered(d,sub,BAR+108,28,dim())
    return img,d,cursor

# ---------- page 1: a mock session ----------
WIN=(60,250,1020,680)
TYPED='fix the flaky login test'
# (sticker, ms on screen, name, what happened, session lines this step adds)
SCENES=[
    ('thinking',3000,'Thinking','You send a prompt',
        [[('* ',ORANGE),('Thinking...',TERM_DIM)]]),
    ('todo',3400,'Todo List','It uses tools',
        [[('* ',GREEN),('Update(auth/session.py)',TERM_TXT)],
         [('  + ',GREEN),('retry on expired token',TERM_DIM)]]),
    ('proceed',3400,'Yes, Proceed','It needs your OK',
        [[('? ',BLUE),('Run npm test?',TERM_TXT)],
         [('> ',ORANGE),('Yes, proceed',TERM_TXT)]]),
    ('passed_long',4760,'Tests Passed','The job is done',
        [[('PASS ',GREEN),('42 tests',TERM_TXT)],
         [('* ',ORANGE),('Fixed. Your login is stable.',TERM_TXT)]]),
]
B=21; CLAWD=(CW-23*B-16,CH-BAR-70-24*B)
TYPE_MS=60
def window(d,k,chars):
    x0,y0,x1,y1=WIN; bar=mc.TH['bar']
    d.rectangle(WIN,fill='#1B1816',outline=mc.TH['bar_hi'],width=3)
    d.rectangle([x0,y0,x1,y0+46],fill=bar)
    for i,c in enumerate(('#FF5F57','#FEBC2E','#28C840')):
        cx=x0+30+i*30; d.ellipse([cx-9,y0+14,cx+9,y0+32],fill=c)
    f=font(24,mono=True); w=d.textlength('claude',font=f)
    d.text(((x0+x1-w)/2,y0+9),'claude',font=f,fill=TERM_DIM)
    f=font(30,mono=True); y=y0+66
    lines=[[('> ',ORANGE),(TYPED[:chars],TERM_TXT)]]
    for s in SCENES[:k+1]: lines+=s[4]
    for ln in lines:
        x=x0+28
        for s,c in ln:
            d.text((x,y),s,font=f,fill=c); x+=d.textlength(s,font=f)
        y+=44
_bg={}
def hero_bg(k,chars=len(TYPED)):
    """Background at step k, with the prompt typed up to chars."""
    if (k,chars) not in _bg:
        img,d,cursor=frame('Clawd Dev Life','a clawd-on-desk theme that reacts to Claude Code')
        centered(d,NOTE,CH-BAR-44,22,dim())
        window(d,k,chars)
        y=740
        for i,(_,_,name,what,_) in enumerate(SCENES):
            on=i==k
            if on: d.text((64,y+18),'>',font=font(36,mono=True),fill=ORANGE)
            d.text((104,y),what,font=font(28,mono=True),fill=mc.TH['ink'] if on else dim())
            d.text((104,y+38),name,font=font(34,mono=True),fill=ORANGE if on else dim())
            y+=128
        _bg[(k,chars)]=(img,cursor)
    return _bg[(k,chars)]
def hero():
    names=[s[0] for s in SCENES]
    starts=[sum(s[1] for s in SCENES[:i]) for i in range(len(SCENES)+1)]
    end=-(-starts[-1]//(2*BLINK))*2*BLINK   # whole blink cycles
    ts=set()
    for nm,t0,t1 in zip(names,starts,starts[1:]+[end]):
        t=t0; ts.add(t0)
        for _,dur in mc.load(nm):
            t+=dur
            if t<t1: ts.add(t)
    # sticker changes always get a frame; the typing and the cursor fit in around them,
    # or a dropped change would hold a short frame until the next one
    for t in sorted(set(range(0,end,BLINK))|set(range(0,TYPE_MS*len(TYPED),TYPE_MS))):
        if all(abs(t-k)>=40 for k in ts): ts.add(t)
    times=sorted(ts)
    steps=[hero_bg(k)[0] for k in range(len(SCENES))]
    sheet=Image.new('RGB',(CW,CH*len(steps)))
    for k,im in enumerate(steps): sheet.paste(im,(0,CH*k))
    _,palimg=mc.palette(names,sheet)
    frames=[]
    for t in times:
        k=max(i for i in range(len(SCENES)) if starts[i]<=t)
        bg,cursor=hero_bg(k,min(len(TYPED),t//TYPE_MS+1))
        im=bg.copy(); f=mc.frame_at(mc.scaled(names[k],B),t-starts[k]); im.paste(f,CLAWD,f)
        if t//BLINK%2==0: ImageDraw.Draw(im).rectangle(cursor,fill=TERM_TXT)
        frames.append(im.quantize(palette=palimg,dither=Image.Dither.NONE))
    mc.save_gif('theme-1',frames,times,end)
    bg,cursor=hero_bg(len(SCENES)-1)
    mc.still('theme-1',bg,[(names[-1],B,*CLAWD)],cursor)

# ---------- page 2: triggers ----------
GRID=[('ultrathink','ultrathink','You send a prompt'),('bug','Bug Hunt','It uses tools'),('subagents','Subagents','A subagent runs'),
    ('compact','/compact','Context compacts'),('proceed','Yes, Proceed','It needs your OK'),('error','Error','A tool fails'),
    ('lgtm','LGTM','The task is done'),('clone','git clone','Worktree created'),('fish','Slacking Off','You step away')]
def triggers():
    img,d,cursor=frame('A scene for every state','Clawd acts out what Claude Code is doing')
    b=12; sw=23*b; sh=24*b; cw=CW//3; rh=sh+70; gy=BAR+158; items=[]
    for k,(nm,name,what) in enumerate(GRID):
        x0=k%3*cw; y0=gy+k//3*rh
        items.append((nm,b,x0+(cw-sw)//2,y0))
        label(d,name,x0+cw/2,y0+sh-2,cw-16,px=28)
        f=font(23,mono=True); w=d.textlength(what,font=f)
        d.text((x0+(cw-w)/2,y0+sh+36),what,font=f,fill=dim())
    return img,items,cursor

# ---------- page 3: theme-only animations ----------
def caption(d,name,what,cx,y):
    label(d,name,cx,y,CW//3,px=30)
    f=font(24,mono=True); w=d.textlength(what,font=f)
    d.text((cx-w/2,y+44),what,font=f,fill=dim())
def exclusives():
    img,d,cursor=frame()
    d.text((60,BAR+36),'# new animations for desktop',font=font(32,mono=True),fill=dim())
    items=[]; b=20; sw=23*b; y=BAR+90
    for i,(nm,name,what) in enumerate((('team2','Team of Two','2 sessions at once'),('team3','Team of Three','3 or more sessions'))):
        cx=CW*(2*i+1)//4
        items.append((nm,b,cx-sw//2,y)); caption(d,name,what,cx,y+24*b+4)
    b=14; sw=23*b; y+=24*20+160
    for i,(nm,name,what) in enumerate((('dizzy','Dizzy','Circle the mouse'),('yawn','Yawn','Left alone'),('wake','Wake','Back to work'))):
        cx=CW*(2*i+1)//6
        items.append((nm,b,cx-sw//2,y)); caption(d,name,what,cx,y+24*b+4)
    return img,items,cursor

if __name__=='__main__':
    args=sys.argv[1:]
    if '--light' in args: args.remove('--light'); mc.TH=mc.THEMES['light']
    for n in (args or ['1','2','3']):
        if n=='1': hero()
        elif n=='2': mc.render('theme-2',*triggers())
        elif n=='3': mc.render('theme-3',*exclusives())
