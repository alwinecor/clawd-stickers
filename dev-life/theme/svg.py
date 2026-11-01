# SPDX-License-Identifier: MIT
# License: ../../LICENSE; the drawn SVGs are artwork, see ../../LICENSE-ART and ../../NOTICE.md
"""Vector animations of the clawd-on-desk theme, which play smoothly at the display refresh rate."""
from clawd_dev import *

# ---------- Idle · 待机, Roam · 散步, Drag · 拎起来 ----------
# SVG + CSS rather than frames: the browser animates them smoothly at sub-pixel steps.
# Coordinates are body cells, the same grid as base(); legs run up behind the torso so lifting them leaves no gap.
def svg_rect(x,y,w,h,c=None): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}"'+(f' fill="{c}"' if c else '')+'/>'
def svg_doc(vb,css,body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb["x"]} {vb["y"]} {vb["width"]} {vb["height"]}" width="{H*S}" height="{H*S}">\n'
            f'  <defs>\n    <style>\n{css}    </style>\n  </defs>\n{body}</svg>\n')
def svg_legs(cls=('','','','')):
    return ''.join(f'<g class="{c}">{svg_rect(x,11,1,4)}</g>' if c else svg_rect(x,11,1,4) for x,c in zip((3,5,9,11),cls))
# Limbs and eyes snap between poses like the stickers' frames; only whole-body motion eases.
# Blinks like face(): only the top row of each eye goes.
LID="""      .lid { animation: lid 5.4s infinite step-end; }
      @keyframes lid { 0% { opacity: 1; } 96.6% { opacity: 0; } }
"""
def svg_eyes(*xs):
    return '<g class="lid">'+''.join(svg_rect(x,8,1,1) for x in xs)+'</g>'+''.join(svg_rect(x,9,1,1) for x in xs)
# Eye tracking moves #eyes-js, #body-js and #shadow-js. Breathes on Good Night's clock at half its depth.
def idle_svg(vb):
    r=svg_rect
    return svg_doc(vb,LID+"""      .breath { transform-origin: 7.5px 15px; animation: breath 2.7s infinite ease-in-out; }
      #eyes-js, #body-js, #shadow-js { transition: transform 0.25s ease; }
      #shadow-js { transform-origin: 7.5px 15px; }
      @keyframes breath { 0%, 100% { transform: scaleY(1); } 50% { transform: scaleY(0.965); } }
""",f'''  <g id="shadow-js">{r(3,15,9,1,tc('#D9D2CB'))}</g>
  <g fill="{BODY}">{svg_legs()}</g>
  <g id="body-js">
    <g class="breath" fill="{BODY}">
      {r(2,6,11,7)}{r(0,9,2,2)}{r(13,9,2,2)}
      <g id="eyes-js" fill="{K}">{svg_eyes(4,10)}</g>
    </g>
  </g>
''')
# Walks right (clawd-on-desk mirrors it for leftward walks): legs and arms step in pairs, body bobs on each step.
def roam_svg(vb):
    r=svg_rect
    return svg_doc(vb,LID+"""      .bob { animation: bob 0.3s infinite ease-in-out; }
      .step-a, .step-b { animation: step 0.6s infinite step-end; }
      .step-b { animation-delay: -0.3s; }
      .shadow { transform-origin: 7.5px 15.5px; animation: shadow 0.3s infinite ease-in-out; }
      @keyframes bob { 0%, 100% { transform: translate(0, 0); } 50% { transform: translate(0, -0.6px); } }
      @keyframes step { 0% { transform: translate(0, -1px); } 50% { transform: none; } }
      @keyframes shadow { 0%, 100% { transform: scaleX(1); } 50% { transform: scaleX(0.9); } }
""",f'''  <g class="shadow">{r(3,15,9,1,tc('#D9D2CB'))}</g>
  <g class="bob" fill="{BODY}">
    {svg_legs(('step-a','step-b','step-a','step-b'))}
    {r(2,6,11,7)}<g class="step-a">{r(0,9,2,2)}</g><g class="step-b">{r(13,9,2,2)}</g>
    <g fill="{K}">{svg_eyes(5,11)}</g>
  </g>
''')
# Held up by the scruff: swings from the top, arms flail, legs kick, > < eyes and flying sweat.
def drag_svg(vb):
    r=svg_rect; eyes=''.join(r(x,y,1,1) for x,y in [(3,7),(4,8),(3,9),(11,7),(10,8),(11,9)])
    return svg_doc(vb,"""      .sway { transform-origin: 7.5px 4px; animation: sway 0.9s infinite alternate ease-in-out; }
      .kick-a, .kick-b, .flail-a, .flail-b { animation: kick 0.24s infinite step-end; }
      .kick-b, .flail-b { animation-delay: -0.12s; }
      .flail-a, .flail-b { animation-name: flail; }
      .drop-l, .drop-r { animation: drop-l 0.8s infinite ease-out; }
      .drop-r { animation-name: drop-r; animation-delay: -0.4s; }
      .shadow { transform-origin: 7.5px 15.5px; animation: shadow 0.9s infinite alternate ease-in-out; }
      @keyframes sway { 0% { transform: translate(0, -1px) rotate(-7deg); } 100% { transform: translate(0, -1px) rotate(7deg); } }
      @keyframes kick { 0% { transform: translate(0, -1px); } 50% { transform: none; } }
      @keyframes flail { 0% { transform: translate(0, -1px); } 50% { transform: translate(0, 1px); } }
      @keyframes drop-l { 0% { transform: none; opacity: 1; } 100% { transform: translate(-3px, 2px); opacity: 0; } }
      @keyframes drop-r { 0% { transform: none; opacity: 1; } 100% { transform: translate(3px, 2px); opacity: 0; } }
      @keyframes shadow { 0% { transform: translateX(-1px) scaleX(0.9); } 100% { transform: translateX(1px) scaleX(0.9); } }
""",f'''  <g class="shadow" opacity="0.6">{r(5,15,5,1,tc('#D9D2CB'))}</g>
  <g class="sway" fill="{BODY}">
    {svg_legs(('kick-a','kick-b','kick-a','kick-b'))}
    {r(2,6,11,7)}<g class="flail-a">{r(0,7,2,2)}</g><g class="flail-b">{r(13,7,2,2)}</g>
    <g fill="{K}">{eyes}</g>
    <g fill="{SWEAT}"><g class="drop-l">{r(0,4,1,1)}</g><g class="drop-r">{r(14,4,1,1)}</g></g>
  </g>
''')
SVGS={'idle':idle_svg,'roam':roam_svg,'drag':drag_svg}
