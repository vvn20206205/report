import os
import glob
root_dir = os.path.join(os.getcwd(), r"..\\..\\..\\")
root_dir=r"c:\Users\vvn20206205\Pictures"
ext=".py"
ext=".srt"
ext=".tex"
ext=".md"
ext=".mp4"
files=glob.glob(os.path.join(  root_dir, f'**/*{ext}'), recursive=True) 
print(len(files))
for f in files:
    print(f) 