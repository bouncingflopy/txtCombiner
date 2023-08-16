import sys
import os

files = sys.argv[1:]
folder = "\\".join(files[0].split("\\")[:-1])

with open(f'{folder}\\combined.txt', 'w') as combined:
    for file in files:
        with open(file, 'r') as f:
            combined.writelines(f.readlines())
            combined.write("\n")
        os.remove(file)