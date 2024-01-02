import os
import glob


def TimKiem(root_dir, ext):
 return glob.glob(os.path.join(
 root_dir, f'**/*{ext}'), recursive=True)


folder = os.path.join(os.getcwd(), r"..\\..\\..\\")
files = TimKiem(folder, '.py')
for f in files:
    print(f)
files = TimKiem(folder, '.srt')
for f in files:
    print(f)
files = TimKiem(folder, '.tex')
for f in files:
    print(f)
files = TimKiem(folder, '.md')
for f in files:
    print(f)


 