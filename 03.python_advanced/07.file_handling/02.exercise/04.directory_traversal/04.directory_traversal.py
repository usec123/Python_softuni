import os

def file_checker(dir):
    for file in os.listdir(dir):
        f = os.path.join(dir,file)
        if os.path.isfile(f):
            ext = file.split('.')[-1]
            if ext not in files:
                files[ext] = []
            files[ext].append(file)
        else:
            file_checker(os.path.join(dir,f))

files = {}
starting_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))

file_checker(starting_directory)

for key, value in files.items():
    print(f'.{key}')
    for file in value:
        print(f'- - - {file}')