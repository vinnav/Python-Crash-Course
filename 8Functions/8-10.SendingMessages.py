messages = ["Message 1", "Message 2", "Message 3"]
sent_messages = []
def sendMessages(msg, sentMsg):
    while msg:
        current = msg.pop()
        sentMsg.append(current)

sendMessages(messages, sent_messages)
print(messages)
print(sent_messages)
