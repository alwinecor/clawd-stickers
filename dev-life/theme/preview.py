# SPDX-License-Identifier: MIT
# License: ../../LICENSE
"""
Draws the 300x300 catalog thumbnail of each theme: a terminal sign reading "dev life" over Clawd with a coffee.

  python preview.py          # light theme -> previews/clawd-dev-life.webp
  python preview.py --dark   # dark theme -> previews/clawd-dev-life-dark.webp

The clawd-themes catalog shows it on the theme's card; a new theme version needs it again.
"""
import argparse, os, sys
THEME_DIR=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(THEME_DIR,'..','src'))
import clawd_dev
from clawd_dev import *
ORG='#E8845F'; STEAM='#D8D2CA'; SIZE=300

def held_mug(p,x0=14,y0=6):
    """Mug in Clawd's raised right claw: handle under the claw, cup just past it."""
    p.update(spr([r[::-1] for r in MUG],x0,y0,MUG_PAL)); arms(p,DOWN,UP)
    return {(x0+2,y0-1):STEAM,(x0+3,y0-2):STEAM}
def sign():
    img=canvas(); X0,Y0,X1,Y1=cx(-3),cy(-6),cx(18),cy(3); term(img,X0,Y0,X1,Y1)
    px=6; d=ImageDraw.Draw(img); title='dev life'
    w=7*px+text_w(title)*px; x=round((X0+X1-w)/2); y=Y0+20
    for sx,sy in SPIN[5]: d.rectangle([x+sx*px,y+sy*px,x+(sx+1)*px-1,y+(sy+1)*px-1],fill=ORG)   # Claude Code's ✻
    text(img,title,x+7*px,y,px,'#E6E1DA')
    y2=y+5*px+16; x2=text(img,'>',x,y2,px,'#9A9AA6')+2*px
    box(img,x2,y2,x2+3*px,y2+5*px,ORG)   # cursor
    p=base(); face(p,'hap'); steam=held_mug(p)
    return comp(shadow(),img,draw(canvas(),p),steam)
def preview(dark=False):
    set_dark(dark)
    img=sign(); tile=Image.new('RGBA',(SIZE,SIZE),(0,0,0,0))
    tile.alpha_composite(img,((SIZE-img.width)//2,(SIZE-img.height)//2))
    out=os.path.join(THEME_DIR,'previews'); os.makedirs(out,exist_ok=True)
    path=os.path.join(out,'clawd-dev-life'+('-dark' if dark else '')+'.webp')
    tile.save(path,lossless=True,method=6)
    print(f'preview -> {os.path.normpath(path)}')

if __name__=='__main__':
    ap=argparse.ArgumentParser(description='Draw the catalog thumbnail of a theme.')
    ap.add_argument('--dark',action='store_true',help='draw the dark theme thumbnail')
    preview(ap.parse_args().dark)
