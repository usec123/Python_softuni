class Party:
    def __init__(self):
        self.people = []

p = Party()
cmd = input()
while cmd!='End':
    p.people.append(cmd)
    cmd = input()

print(f'Going: {", ".join(p.people)}')
print(f'Total: {len(p.people)}')