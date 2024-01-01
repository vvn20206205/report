import os
import glob


def TimKiem(root_dir, ext):
 return glob.glob(os.path.join(
 root_dir, f'**/*{ext}'), recursive=True)


folder = os.path.join(os.getcwd(), r"..\\..\\..\\")
files = TimKiem(folder, '.md')
files = TimKiem(folder, '.py')
files = TimKiem(folder, '.srt')
files = TimKiem(folder, '.tex')
for f in files:
    print(f)


 