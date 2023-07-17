import re

title_pattern = r'<title>([^\n]*)</title>'
body_pattern = r'<body>(.*)</body>'
body_remover_pattern = r'<[^>]*>|\\.'

html = input()
title = re.search(title_pattern,html).group(1)
content = re.sub(body_remover_pattern,'',re.search(body_pattern,html).group(1))

print(f'Title: {title}')
print(f'Content: {content}')