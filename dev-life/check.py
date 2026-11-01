# SPDX-License-Identifier: MIT
# License: ../LICENSE
"""
Rebuilds every sticker and theme in a temporary copy of this folder and compares the result with the
committed files, so a source change that was never regenerated gets caught. Files here are only read.

  python dev-life/check.py

Compare with the Pillow version pinned in ../requirements.txt: another version can change the bytes.
"""
import os, shutil, subprocess, sys, tempfile
HERE=os.path.dirname(os.path.abspath(__file__))
OUTPUTS=('gif','gif-dark','theme/clawd-dev-life','theme/clawd-dev-life-dark')
def read(path):
    data=open(path,'rb').read()
    return data.replace(b'\r\n',b'\n') if path.endswith(('.json','.svg')) else data   # git may check out either
def outputs(root):
    """{path relative to root: contents} for every generated file under root."""
    found={}
    for sub in OUTPUTS:
        for d,_,names in os.walk(os.path.join(root,sub)):
            for nm in names:
                path=os.path.join(d,nm)
                found[os.path.relpath(path,root).replace(os.sep,'/')]=read(path)
    return found
def check():
    with tempfile.TemporaryDirectory() as tmp:
        copy=os.path.join(tmp,'dev-life')
        shutil.copytree(HERE,copy,ignore=shutil.ignore_patterns('__pycache__'))
        for sub in OUTPUTS: shutil.rmtree(os.path.join(copy,sub))   # so a file with no source shows up too
        subprocess.run([sys.executable,'build_all.py'],cwd=copy,check=True,stdout=subprocess.DEVNULL,
                       env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
        built=outputs(copy)
    have=outputs(HERE)
    return sorted(k for k in have.keys()|built.keys() if have.get(k)!=built.get(k)),len(built)
if __name__=='__main__':
    stale,n=check()
    if stale:
        print(f'{len(stale)} of {n} generated files are out of date:')
        for k in stale: print(' ',k)
        print('Run python dev-life/build_all.py to regenerate them.')
        sys.exit(1)
    print(f'{n} generated files are up to date')
