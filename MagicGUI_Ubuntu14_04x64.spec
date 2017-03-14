# -*- mode: python -*-

block_cipher = None


a = Analysis(['programs/magic_gui.py'],
             pathex=['/home/kevin/Code/Paleomag/PmagPy'],
             binaries=None,
             datas=[('./pmagpy/data_model','./data_model')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='MagicGUI_Ubuntu14_04x64',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='programs/images/PmagPy.ico')
