# -------------------------------
# User Class
# -------------------------------

class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    # joining chatroom
    def join_chatroom(self, chatroom):
        if self.chatroom is not None:
            print(f"{self.username} is already in a chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")

    # leaving chatroom
    def leave_chatroom(self):
        if self.chatroom is None:
            print(f"{self.username} is not in any chatroom.")
        else:
            room = self.chatroom
            room.remove_user(self)
            self.chatroom = None
            print(f"{self.username} left {room.name}")

    # sending messages 
    def send_message(self, content):
        if self.chatroom is None:
            print(f"{self.username} cannot send a message.")
        else:
            self.chatroom.send_message(self, content)


# -------------------------------
# Message Class
# -------------------------------

class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def __str__(self):
        return f"{self.sender.username}: {self.content}"


# -------------------------------
# ChatRoom Class
# -------------------------------

class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def send_message(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)

        print(message)

    def show_chat_history(self):
        print(f"\n--- Chat History: {self.name} ---")

        for message in self.messages:
            print(message)


# -------------------------------
# Main Program
# -------------------------------

room = ChatRoom("Python Lounge")

bhavesh = User("Bhavesh")
bob = User("Bob")
charlie = User("Charlie")

bhavesh.join_chatroom(room)
bob.join_chatroom(room)

bhavesh.send_message("Hello everyone!")
bob.send_message("Hi Bhavesh!")

charlie.join_chatroom(room)
charlie.send_message("Hey guys!")

room.show_chat_history()

bhavesh.leave_chatroom()
bob.leave_chatroom()
charlie.leave_chatroom()