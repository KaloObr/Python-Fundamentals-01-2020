class Email:
    def __init__(self, sender, reciever, content):
        self.sender = sender
        self.reciever = reciever
        self.content = content
        self.is_sent = False

    def sent(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.reciever}: {self.content}. Sent: {self.is_sent}'


emails = []
line = input()

while line != 'Stop':
    sender, reciever, content = line.split(" ")
    email = Email(sender, reciever, content)
    emails.append(email)
    line = input()

sent_emails = list(map(int, [x for x in input().split(", ")]))

for x in sent_emails:
    emails[x].sent()

for email in emails:
    print(email.get_info())

