from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('E:\py') if isfile(join('E:\py', f))]
print(files_list);
