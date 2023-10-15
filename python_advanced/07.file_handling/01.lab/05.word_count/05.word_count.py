import os, re

FILE_PATH_WORDS = os.path.join(os.path.dirname(os.path.abspath(__file__)), '05.words.txt')
FILE_PATH_READ = os.path.join(os.path.dirname(os.path.abspath(__file__)), '05.input.txt')
FILE_PATH_OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '05.output.txt')

words = dict()

with open(FILE_PATH_WORDS) as f:
    words = {key:0 for key in f.readline().split()}


    
with open(FILE_PATH_READ) as f:
    text = f.read()
    for word in words:
        pattern = rf'\b{word}\b'
        result = re.findall(pattern, text, re.IGNORECASE)
        words[word] = len(result)

with open(FILE_PATH_OUTPUT,'w') as f:
    for key,value in dict(sorted(words.items(), key=lambda x: -x[1])).items():
        f.write(f'{key} - {value}\n')