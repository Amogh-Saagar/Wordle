from cx_Freeze import setup, Executable

setup(name = "wordle",

      version = 1,

      executables = [Executable("wordle.py")])
