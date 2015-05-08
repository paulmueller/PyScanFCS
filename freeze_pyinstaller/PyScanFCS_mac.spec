# -*- mode: python -*-

hiddenimports = ["scipy.optimize",
                 "scipy.special._ufuncs_cxx"]


a = Analysis(['pyscanfcs/PyScanFCS.py'],
              hiddenimports=hiddenimports,
              hookspath=None)
a.datas += [('doc/ChangeLog.txt', 'ChangeLog.txt', 'DATA'),
            ('doc/PyScanFCS_doc.pdf', 'doc/PyScanFCS_doc.pdf', 'DATA')]
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='PyScanFCS',
          debug=False,
          strip=None,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='PyScanFCS')
app = BUNDLE(coll,
             name='dist/PyScanFCS.app',
             icon='freeze_pyinstaller/PyScanFCS.icns')
