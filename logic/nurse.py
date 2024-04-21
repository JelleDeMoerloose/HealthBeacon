class Nurse:
    def __init__(self, id):
        self.id = id
        self.notifications = {}
        self.get_status = False
        self.latest = []
    
    def notify(self, chatEl, id):
        self.get_status = True
        if id not in self.notifications:
            self.notifications[id] = []
        self.notifications[id].append(chatEl)
        
        self.latest = [chatEl, id]

    def get_latest(self):
        self.get_status = False
        return self.latest

    def get_all_notifications(self):
        serialized_notifications = {}
        for id, chats in self.notifications.items():
            serialized_chats = [chat.serialize() for chat in chats]
            serialized_notifications[id] = serialized_chats
        return serialized_notifications
       
        