import fbchat
import random

from user_info import MY_ID,MY_PASSWORD

# subclass fbchat.Client and override required methods
class EchoBot(fbchat.Client):

    def __init__(self,email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self,email, password, debug, user_agent)

    def on_message(self, mid, author_id, author_name, message, metadata):
        self.markAsDelivered(author_id, mid) #mark delivered
        self.markAsRead(author_id) #mark read
        print("%s said: %s"%(author_id, message))
        #if you are not the author, echo
        message +=  "\nthis was sent from a bot cuz Armaan doesn't feel like responding"
        message = list(message)

        #send the message recived back to the sender with the case of the letters randomized
        for idx, c in enumerate(message):
            if random.random() > 0.6:
                print c
                if c.isupper():
                    message[idx] = c.lower()
                else:
                    message[idx] = c.upper()
        message = "".join(message)

        if str(author_id) != str(self.uid):
            # self.send(author_id,message)
            self.sendRemoteImage(author_id, message = message, image="https://usatftw.files.wordpress.com/2017/05/spongebob.jpg")

#client = fbchat.Client(MY_ID, MY_PASSWORD)
bot = EchoBot(MY_ID,MY_PASSWORD)
bot.listen()
