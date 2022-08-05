class Email:

    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return print(f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}")

emails = []
while True:
    command = input()
    if command == 'Stop':
        break

    message = command.split(' ')
    email = Email(message[0], message[1], message[2])
    emails.append(email)

indices = list(int(x) for x in input().split(', '))
for i in indices:
    emails[i].send()

for j in emails:
    j.get_info()

