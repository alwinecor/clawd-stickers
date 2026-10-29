# SPDX-License-Identifier: MIT
"""
Animated 3:4 pages (1080x1440) for sharing the set on Xiaohongshu:
the 40 stickers split over two pages, 5 x 4 each, with their English names.

  python dev-life/promo/make_covers.py                # both pages, dark terminal theme
  python dev-life/promo/make_covers.py 2              # just page 2
  python dev-life/promo/make_covers.py --light 1 2    # cream theme

Output: page-N-{dark,light}.gif, plus page-N-{dark,light}-static.png, a still
built from a hand-picked key frame per sticker (KEY below) rather than one
moment of the whole page.

The dark theme uses the dark-background set in dev-life/gif-dark/,
the cream theme the regular set in dev-life/gif/.

Every sticker plays once and holds its last frame, so the page loops cleanly.
Stickers are scaled by whole pixels so the pixel art stays crisp.
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont
HERE=os.path.dirname(os.path.abspath(__file__))
SET=os.path.join(HERE,'..')
OUT=os.path.join(HERE,'covers')

CW,CH=1080,1440
ORANGE='#D77757'; TERM_TXT='#EDE6DE'; TERM_DIM='#8C827A'
THEMES={
    'dark': dict(bg='#161412',ink='#E8E1D9',bar='#26211E',bar_hi='#332D29',mono=True,suffix='-dark',gif='gif-dark'),
    'light':dict(bg='#FBF6EE',ink='#2B2522',bar='#211D1B',bar_hi='#2E2926',mono=False,suffix='-light',gif='gif'),
}
TH=THEMES['dark']
BAR=76   # height of the terminal bars at the top and bottom
FONTS='C:/Windows/Fonts'
def font(px,bold=True,mono=False):
    names=('consolab.ttf','courbd.ttf') if mono else \
          ('segoeuib.ttf','arialbd.ttf') if bold else ('segoeui.ttf','arial.ttf')
    for nm in names:
        p=os.path.join(FONTS,nm)
        if os.path.exists(p): return ImageFont.truetype(p,px)
    return ImageFont.load_default(px)

STICKERS=[('hello','hello, world'),('thinking','Thinking'),('ultrathink','ultrathink'),('plan','Plan Mode'),('todo','Todo List'),
    ('simple',"It's Simple"),('subagents','Subagents'),('proceed','Yes, Proceed'),('lgtm','LGTM'),('right',"You're Absolutely Right!"),
    ('compact','/compact'),('clear','/clear'),('limit','Usage Limit'),('esc','Esc'),('banned','Banned'),
    ('clone','git clone'),('stash','git stash'),('cherry','cherry-pick'),('conflict','Merge Conflict'),('forcepush','Force Push'),
    ('blame','git blame'),('rmrf','rm -rf'),('detached','detached HEAD'),('notfound','404 Not Found'),('error','Error'),
    ('bug','Bug Hunt'),('duck','Rubber Duck'),('loop','while(true)'),('overflow','Stack Overflow'),('leak','Memory Leak'),
    ('works','Works on My Machine'),('passed','Tests Passed'),('deploy','Friday Deploy'),('deadline','Deadline'),('overtime','Overtime'),
    ('coffee','Coffee Break'),('fish','Slacking Off'),('offwork','Clock Out'),('sleep','Good Night'),('bye','/exit')]
# frame index of each sticker's punchline, for the stills (same in gif/ and gif-dark/)
KEY={'hello':36,'thinking':15,'ultrathink':44,'plan':24,'todo':20,
     'simple':20,'subagents':40,'proceed':25,'lgtm':6,'right':40,
     'compact':24,'clear':16,'limit':35,'esc':18,'banned':29,
     'clone':30,'stash':10,'cherry':12,'conflict':14,'forcepush':10,
     'blame':8,'rmrf':27,'detached':16,'notfound':7,'error':30,
     'bug':29,'duck':26,'loop':20,'overflow':31,'leak':30,
     'works':15,'passed':22,'deploy':20,'deadline':15,'overtime':5,
     'coffee':31,'fish':14,'offwork':7,'sleep':20,'bye':22}

# ---------- loading ----------
_cache={}
def load(nm):
    """[(RGBA frame cropped to the 23x24-cell drawing, duration ms)]"""
    if nm not in _cache:
        im=Image.open(os.path.join(SET,TH['gif'],nm+'.gif')); fr=[]
        for i in range(im.n_frames):
            im.seek(i); fr.append((im.convert('RGBA').crop((6,0,282,288)),im.info['duration']))
        _cache[nm]=fr
    return _cache[nm]
def scaled(nm,b):
    """Frames scaled so each sticker cell is b px (sticker is 23b x 24b)."""
    key=(nm,b)
    if key not in _cache:
        _cache[key]=[(f.resize((23*b,24*b),Image.NEAREST),d) for f,d in load(nm)]
    return _cache[key]
def frame_at(fr,t):
    for f,d in fr:
        if t<d: return f
        t-=d
    return fr[-1][0]
def length(nm): return sum(d for _,d in load(nm))

# ---------- page layout: (static background, [(sticker, b, x, y)]) ----------
def label(d,s,cx,y,maxw,px=28):
    """Centered label; names too long for the column wrap onto two lines."""
    fit=lambda lines,px: max(d.textlength(ln,font=font(px,mono=TH['mono'])) for ln in lines)<=maxw
    lines=[s]
    if not fit(lines,24):
        words=s.split()
        k=min(range(1,len(words)),key=lambda k:abs(len(' '.join(words[:k]))-len(' '.join(words[k:]))))
        lines=[' '.join(words[:k]),' '.join(words[k:])]; px=25
    while not fit(lines,px) and px>18: px-=1
    f=font(px,mono=TH['mono'])
    for i,ln in enumerate(lines):
        w=d.textlength(ln,font=f); d.text((cx-w/2,y+i*(px+3)),ln,font=f,fill=TH['ink'])
def terminal_bars(d):
    """Window title bar on top, a shell prompt on the bottom; returns the cursor box."""
    d.rectangle([0,0,CW,BAR],fill=TH['bar']); d.rectangle([0,BAR-4,CW,BAR],fill=TH['bar_hi'])
    for k,c in enumerate(('#FF5F57','#FEBC2E','#28C840')):
        x=44+k*44; d.ellipse([x-13,BAR//2-15,x+13,BAR//2+11],fill=c)
    f=font(28,mono=True); s='~/clawd-stickers'
    w=d.textlength(s,font=f); d.text(((CW-w)/2,BAR//2-18),s,font=f,fill=TERM_DIM)
    y0=CH-BAR; d.rectangle([0,y0,CW,CH],fill=TH['bar']); d.rectangle([0,y0,CW,y0+4],fill=TH['bar_hi'])
    f=font(30,mono=True); x=40; ty=y0+BAR//2-15
    for s,c in (('> ',ORANGE),('git clone ',TERM_TXT),('github.com/alwinecor/clawd-stickers',TERM_DIM)):
        d.text((x,ty),s,font=f,fill=c); x+=d.textlength(s,font=f)
    return (round(x)+6,ty+2,round(x)+22,ty+32)
def page(n):
    img=Image.new('RGB',(CW,CH),TH['bg']); d=ImageDraw.Draw(img)
    cursor=terminal_bars(d)
    b=9; sw,sh=23*b,24*b; cols=5; cw=CW//cols; rh=sh+80
    gy=BAR+(CH-2*BAR-4*rh)//2+24; items=[]
    for k,(nm,name) in enumerate(STICKERS[20*(n-1):20*n]):
        c,r=k%cols,k//cols; x0=c*cw; y0=gy+r*rh
        items.append((nm,b,x0+(cw-sw)//2,y0))
        label(d,name,x0+cw/2,y0+sh+6,cw-16)
    return img,items,cursor

# ---------- timeline + GIF ----------
BLINK=500
def timeline(names,hold=700,minf=40):
    """Frame start times where any sticker or the cursor changes, merged to >= minf ms apart."""
    ts={0}
    for nm in names:
        t=0
        for _,d in load(nm): t+=d; ts.add(t)
    end=-(-(max(length(nm) for nm in names)+hold)//(2*BLINK))*2*BLINK   # whole blink cycles
    ts|=set(range(0,end,BLINK))
    out=[]
    for t in sorted(ts):
        if t<end and (not out or t-out[-1]>=minf): out.append(t)
    return out,end
def render(n):
    bg,items,cursor=page(n)
    names=[nm for nm,*_ in items]
    times,end=timeline(names)
    # one shared palette: every sticker colour exactly, plus the static background
    cols=set()
    for nm in set(names):
        for f,_ in load(nm):
            cols|={c[:3] for _,c in f.getcolors(1<<16) if c[3]==255}
    cols=sorted(cols)[:200]
    bgq=bg.quantize(256-len(cols),dither=Image.Dither.NONE).convert('RGB')
    cols+=[c for _,c in bgq.getcolors(1<<16) if c not in cols]
    flat=[v for c in cols[:256] for v in c]; flat+=[0]*(768-len(flat))
    palimg=Image.new('P',(1,1)); palimg.putpalette(flat)
    frames=[]
    for t in times:
        im=bgq.copy()
        for nm,b,x,y in items:
            f=frame_at(scaled(nm,b),t); im.paste(f,(x,y),f)
        if t//BLINK%2==0: ImageDraw.Draw(im).rectangle(cursor,fill=TERM_TXT)
        frames.append(im.quantize(palette=palimg,dither=Image.Dither.NONE))
    durs=[b-a for a,b in zip(times,times[1:]+[end])]
    os.makedirs(OUT,exist_ok=True)
    path=os.path.join(OUT,f"page-{n}{TH['suffix']}.gif")
    frames[0].save(path,save_all=True,append_images=frames[1:],duration=durs,loop=0,optimize=False)
    print(f'page {n}: {len(frames)} frames, {end/1000:.1f}s, {os.path.getsize(path)//1024}KB')
    still(n,bg,items,cursor)
def still(n,bg,items,cursor):
    """Static version: every sticker at its key frame, cursor shown."""
    im=bg.copy()
    for nm,b,x,y in items:
        f=scaled(nm,b)[KEY[nm]][0]; im.paste(f,(x,y),f)
    ImageDraw.Draw(im).rectangle(cursor,fill=TERM_TXT)
    im.save(os.path.join(OUT,f"page-{n}{TH['suffix']}-static.png"))

if __name__=='__main__':
    args=sys.argv[1:]
    if '--light' in args: args.remove('--light'); TH=THEMES['light']
    for n in (args or ['1','2']): render(int(n))
