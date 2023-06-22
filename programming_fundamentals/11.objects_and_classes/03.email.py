class Email:
    def __init__(self,sender,receiver,content,is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent
    
    def send(self):
        self.is_sent = True
    
    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'
    
cmd = input()
emails = []
while cmd!='Stop':
    cmd = cmd.split()
    emails.append(Email(cmd[0],cmd[1],cmd[2],cmd[3] if len(cmd) > 3 else False))
    cmd = input()
    
sent_indices = list(map(int,input().split(', ')))

for i in sent_indices:
    emails[i].send()

for email in emails:
    print(email.get_info())