import sys
import os
import shutil
from pathlib import Path

if len(sys.argv) == 3:
    path_to = sys.argv[2]
else:
    path_to = 'dist'
path_from = sys.argv[1]

if path_to not in os.listdir():
    os.mkdir(path_to)

def copy_tree(path1: Path, path2: Path) -> None:

    for child in Path(path1).iterdir():
        print(child)
        if child.is_dir():
            copy_tree(child, path2)
        else: 
            dir_name = str(child).split('.')[-1]
            if dir_name not in os.listdir(path2):
                os.mkdir(os.path.join(path2, dir_name))
                shutil.copy2(child, os.path.join(path2, dir_name))
            else:
                shutil.copy2(child, os.path.join(path2, dir_name))
            
try:
    copy_tree(path_from, path_to)
except:
    print("Щось пішло не так!")