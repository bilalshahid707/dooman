def create_messages(history):
    messages = []

    for message in history:
        messages.append({"role": message.role, "content": message.content})

    return messages
