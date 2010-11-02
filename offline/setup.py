# setup.py
from distutils.core import setup
import py2exe

setup(name="XiboOfflineDownload",
options = {"py2exe": { "compressed": 1,
                           "optimize": 2,
                           "bundle_files": 1,
                           "includes": [ "encodings.utf_8",],
						   "dll_excludes":["MSVCP90.dll"],}},
      windows=["XiboOfflineDownload.py",],
      data_files=[(".",
                   ["logo.jpg","defaults.cfg"])],
)

