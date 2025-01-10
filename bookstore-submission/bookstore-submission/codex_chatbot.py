from transformers import pipeline
from transformers import Conversation
class Chatbot:
    def __init__(self):
       self.chatbot = pipeline(task="conversational",
                   model="facebook/blenderbot-400M-distill")
       self.conversation=Conversation("")
    def startchat(self,prompt):
        self.conversation = Conversation (prompt)
        self.conversation = self.chatbot(self.conversation)
        return self.conversation
    def continuechat(self,prompt):
        self.conversation.add_message({
            "role":"user","content":f"{prompt}"
            }
            )
        self.conversation = self.chatbot(self.conversation)
        return self.conversation
    