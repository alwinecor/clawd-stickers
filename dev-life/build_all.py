# SPDX-License-Identifier: MIT
# License: ../LICENSE
"""
Generates every sticker, theme and catalog thumbnail, light and dark, in one go.

  python dev-life/build_all.py
"""
import os, sys
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'theme'))
from build import theme   # also puts ../src on the path
from preview import preview
from clawd_dev import build_stickers, set_dark

if __name__=='__main__':
    for dark in (False,True):
        set_dark(dark); build_stickers(); theme(dark); preview(dark)
