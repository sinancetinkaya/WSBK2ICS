# -*- mode: python -*-

block_cipher = None


a = Analysis(['WSBK2ICS.py'],
             pathex=['C:\\Users\\sinan\\Desktop\\Python'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             cipher=block_cipher)
for d in a.datas:
    if 'pyconfig' in d[0]: 
        a.datas.remove(d)
        break
pyz = PYZ(a.pure,
             cipher=block_cipher)
			 
		
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='WSBK2ICS.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
