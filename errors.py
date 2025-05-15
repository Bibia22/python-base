#!/urs/bin/env python3
import os
import sys

try:
    raise RuntimeError("Ocorreu um erro")
except Exception as e:
    print(str(e))


try:
    names = open("names.txt").readlines()
  
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
else:
    print("Sucesso!")
finally:
    print("Execute isso sempre!")

try::
    print(names[2])
except:
    print("[Error:] Missing name in the list")
    sys.exit(1)
