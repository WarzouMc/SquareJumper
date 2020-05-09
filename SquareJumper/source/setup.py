import sys
from cx_Freeze import setup, Executable

base = None

# Necessary for 32-bit systems
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("main.py", base=base, targetName="SquareJumper.exe")]

setup(
    # EXE NAME HERE
    name="Report Cards",
    version="VERSION_NUMBER e.g. 0.1",
    description='report card generator',
    executables=executables, requires=['pygame']
)