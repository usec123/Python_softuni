title = input()
article = input()

comments = []

cmd = input()
while cmd!='end of comments':
    comments.append(cmd)
    cmd=input()

div_text = '\n'.join([f'<div>\n\t{comment}\n</div>' for comment in comments])

print(f'<h1>\n\t{title}\n</h1>\n<article>\n\t{article}\n</article>\n{div_text}')