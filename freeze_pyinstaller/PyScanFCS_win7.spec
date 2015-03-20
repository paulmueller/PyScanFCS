# -*- mode: python -*-
import codecs
import os
import sys

if not os.path.exists("freeze_pyinstaller"):
    raise Exception("Please go to `PyScanFCS` directory.")

    
name = "PyScanFCS"
DIR = os.path.realpath(".")
PyInstDir = os.path.join(DIR, "freeze_pyinstaller")
PCFDIR = os.path.join(DIR, "pyscanfcs")
ProgPy = os.path.join(PCFDIR,"PyScanFCS.py")
ChLog = os.path.join(DIR,"ChangeLog.txt")
DocPDF = os.path.join(DIR,"doc/PyScanFCS_doc.pdf")
ICO = os.path.join(PyInstDir,"PyScanFCS.ico")

sys.path.append(DIR)

## Create inno setup .iss file
import pyscanfcs
version = pyscanfcs.__version__
issfile = codecs.open(os.path.join(PyInstDir,"win7_innosetup.iss.dummy"), 'r', "utf-8")
iss = issfile.readlines()
issfile.close()
for i in range(len(iss)):
    if iss[i].strip().startswith("#define MyAppVersion"):
        iss[i] = '#define MyAppVersion "{:s}"\n'.format(version)
nissfile = codecs.open("win7_innosetup.iss", 'wb', "utf-8")
nissfile.write(u"\ufeff")
nissfile.writelines(iss)
nissfile.close()


a = Analysis([ProgPy],
             pathex=[DIR],
             hiddenimports=["sympy.assumptions.handlers", # sympy
                            "sympy.assumptions.handlers.common",
                            "scipy.special._ufuncs_cxx"],
             hookspath=None)
a.datas += [('doc\\ChangeLog.txt', ChLog, 'DATA'),
            ('doc\\PyScanFCS_doc.pdf', DocPDF, 'DATA')]

pyz = PYZ(a.pure)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name=name+'.exe',
          debug=False,
          strip=None,
          upx=True,
          icon=ICO,
          console=False )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name=name)