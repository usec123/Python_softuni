import os
FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),'text.txt')

with open(FILE_PATH) as file:
    lines = file.readlines()
    for x in range(len(lines)):
        chars = lines[x].count(".")+lines[x].count(",")+lines[x].count("?")+lines[x].count("!")+lines[x].count("\'")+lines[x].count("-")
        print(f'Line {x+1}: {lines[x]} ({len([letter for letter in lines[x] if letter.isalpha()])})({chars})')