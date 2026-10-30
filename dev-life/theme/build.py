# SPDX-License-Identifier: MIT
# License: ../../LICENSE
"""
Builds the clawd-on-desk themes in this folder from the sticker GIFs in ../gif/ (../gif-dark/ with --dark),
plus the theme-only animations in animations.py and svg.py.

  python build.py          # light theme -> clawd-dev-life/
  python build.py --dark   # dark theme -> clawd-dev-life-dark/

Run ../src/clawd_dev.py first if a sticker has changed.
https://github.com/rullerzhou-afk/clawd-on-desk/blob/main/docs/guides/guide-theme-creation.md
"""
import json, os, sys
THEME_DIR=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(THEME_DIR,'..','src'))
from clawd_dev import *
from animations import banned_long, detached_long, dizzy, passed_long, team2, team3, wake, yawn
from svg import SVGS

# viewBox is in body cells, the same grid as the built-in Clawd theme (body x 0..15, feet at y=15).
THEME_ID='clawd-dev-life'+('-dark' if DARK_MODE else '')
THEME={
 'states':{'idle':['idle'],'thinking':['thinking','ultrathink','plan'],'working':['todo','simple','bug','loop','deadline'],
           'juggling':['subagents'],'sweeping':['compact'],'carrying':['clone'],'notification':['proceed'],
           'attention':['passed_long','lgtm'],'error':['error'],'sleeping':['sleep'],'roam':['roam'],
           'dizzy':['dizzy'],
           'yawning':['yawn'],'dozing':['sleep'],'collapsing':['sleep'],'waking':['wake']},
 'workingTiers':[(3,['team3']),(2,['team2','conflict']),(1,['todo','simple','bug','loop','deadline'])],
 'idleAnimations':['fish','coffee','duck','hello','works','blame','deploy','overtime','offwork'],
 'hitBoxes':{'conflict':{'x':-4,'y':5,'w':23,'h':11},'team2':{'x':-3,'y':2,'w':21,'h':14},'team3':{'x':-3,'y':-4,'w':21,'h':20}},   # wider than one Clawd
 'reactions':{'drag':'drag','clickLeft':'hello','clickRight':'right','annoyed':'notfound','double':['rmrf','detached_long','banned_long']},
}
ONESHOT=['attention','error','notification','carrying','dizzy']   # hold until the animation has played once
HOLD=300   # ms of extra stillness on the last frame of an animation played once for a fixed time
ANIMATIONS={f.__name__:f for f in (banned_long,detached_long,dizzy,passed_long,team2,team3,wake,yawn)}
def to_apng(frames,path):
    frames[0][0].save(path,format='PNG',save_all=True,append_images=[im for im,_ in frames[1:]],
                      duration=[d for _,d in frames],loop=0,disposal=0,blend=0)
    return os.path.getsize(path)
def sticker(nm):
    im=Image.open(os.path.join(OUT,nm+'.gif')); fr=[]
    for k in range(im.n_frames):
        im.seek(k); c=im.convert('RGBA')   # blank the colour under transparent pixels, which GIF leaves behind
        fr.append((Image.composite(c,Image.new('RGBA',c.size),c.getchannel('A')),im.info['duration']))
    return fr
def frames(nm): return square(ANIMATIONS[nm]()) if nm in ANIMATIONS else sticker(nm)
def theme():
    out=os.path.join(THEME_DIR,THEME_ID); ad=os.path.join(out,'assets')
    os.makedirs(ad,exist_ok=True)
    names=list(dict.fromkeys(n for v in THEME['states'].values() for n in v))
    names+=[n for _,ns in THEME['workingTiers'] for n in ns]+THEME['idleAnimations']
    names+=[n for v in THEME['reactions'].values() for n in ([v] if isinstance(v,str) else v)]
    vb={'x':-OX-(H-W)/2,'y':-OY,'width':H,'height':H}
    for nm,fn in SVGS.items():
        with open(os.path.join(ad,nm+'.svg'),'w',encoding='utf-8') as fp: fp.write(fn(vb))
    st=THEME['states']; first=lambda s:ms[st[s][0]]
    # Animations clawd-on-desk plays once for a fixed time. Each gets HOLD ms of extra stillness on its
    # last frame, so a timer firing a little late never shows the loop restart. A reaction or state pool
    # shares one duration, so its shorter members hold their last frame until the longest one ends.
    once=set(THEME['idleAnimations'])|{n for s in ONESHOT+['yawning','waking'] for n in st[s]}
    once|={n for k,v in THEME['reactions'].items() if k!='drag' for n in ([v] if isinstance(v,str) else v)}
    pools=[v for v in THEME['reactions'].values() if not isinstance(v,str)]+[st[s] for s in ONESHOT if len(st[s])>1]
    ms={}; pending={}; f=lambda n:n+('.svg' if n in SVGS else '.apng')
    def write(nm,fr,pad=0):
        if nm in once: fr[-1]=(fr[-1][0],fr[-1][1]+pad+HOLD)
        n=to_apng(fr,os.path.join(ad,f(nm)))
        print(f'{nm}: {len(fr)} frames, {ms[nm]}ms'+(f' (+{pad}ms hold)' if pad else '')+f', {n//1024}KB')
    for nm in dict.fromkeys(n for n in names if n not in SVGS):
        fr=frames(nm)
        ms[nm]=sum(d for _,d in fr)
        if any(nm in p for p in pools): pending[nm]=fr
        else: write(nm,fr)
    for p in pools:
        T=max(ms[n] for n in p)
        for n in p: pad=T-ms[n]; ms[n]=T; write(n,pending[n],pad)
    cfg={
     'schemaVersion':1,
     'name':'Dev Life · 克码人生'+(' (Dark)' if DARK_MODE else ''),
     'author':'alwinecor','version':'1.0.0',
     'description':'Clawd Stickers 的 Dev Life 主题：思考、写码、压缩上下文、报错都有对应的小剧场。'
                   '非官方同人作品，与 Anthropic 无关。'+('适合深色桌面。' if DARK_MODE else ''),
     'preview':f('idle'),
     'viewBox':vb,
     'layout':{'contentBox':{'x':0,'y':6,'width':15,'height':10},'centerX':7.5,'baselineY':16,
               'visibleHeightRatio':0.29,'baselineBottomRatio':0.05},
     # Same values as the built-in Clawd; the ratios place the eyes (7.5, 9) inside our viewBox.
     'eyeTracking':{'enabled':True,'states':['idle'],
                    'eyeRatioX':(7.5-vb['x'])/vb['width'],'eyeRatioY':round((9-vb['y'])/vb['height'],3),
                    'maxOffset':3,'bodyScale':0.33,'shadowStretch':0.15,'shadowShift':0.3,
                    'ids':{'eyes':'eyes-js','body':'body-js','shadow':'shadow-js'},'shadowOrigin':'7.5px 15px'},
     'customization':{'petTint':False},
     'states':{s:[f(n) for n in v] for s,v in st.items()},
     # yawning hands over to dozing/collapsing/sleeping, which all show Good Night: the yawn ends on its
     # first frame, and deepSleepTimeout/collapseDuration move on at once so the picture never changes.
     'sleepSequence':{'mode':'full'},
     'workingTiers':[{'minSessions':k,'file':f(ns[0]),**({'files':[f(n) for n in ns]} if len(ns)>1 else {})}
                     for k,ns in THEME['workingTiers']],
     'idleAnimations':[{'file':f(n),'duration':ms[n]} for n in THEME['idleAnimations']],
     'reactions':{k:({'file':f(v)} if k=='drag' else {'file':f(v),'duration':ms[v]} if isinstance(v,str) else
                     {'files':[f(n) for n in v],'duration':max(ms[n] for n in v)})
                  for k,v in THEME['reactions'].items()},
     'timings':{'minDisplay':{**{s:first(s) for s in ONESHOT},'sweeping':first('sweeping'),
                              'working':1000,'thinking':1000},
                'autoReturn':{**{s:first(s) for s in ONESHOT},'sweeping':300000},
                'mouseIdleTimeout':20000,'mouseSleepTimeout':60000,
                'yawnDuration':first('yawning'),'deepSleepTimeout':60000+first('yawning'),'collapseDuration':100,
                'wakeDuration':first('waking')},
     'hitBoxes':{'default':{'x':-1,'y':5,'w':17,'h':11}},
     'fileHitBoxes':{f(n):b for n,b in THEME['hitBoxes'].items()},
     'miniMode':{'supported':False},
    }
    with open(os.path.join(out,'theme.json'),'w',encoding='utf-8') as fp:
        json.dump(cfg,fp,ensure_ascii=False,indent=2); fp.write('\n')
    print(f'theme -> {os.path.normpath(out)}')

if __name__=='__main__':
    theme()
