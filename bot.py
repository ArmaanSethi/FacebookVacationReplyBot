from user_info import MY_ID,MY_PASSWORD
from fbchat import log, Client, Message, Attachment, ShareAttachment
from fbchat.models import *
import random

class VacationBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        # self.markAsRead(thread_id)
        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        if author_id != self.uid:
            m = Message()
            m.text = message_object.text
            text_msg =  "\nthis was sent from a bot cuz Armaan doesn't feel like responding"
            txt_msg = "".join(list(map(lambda x: x.upper() if random.random() > 0.5 else x.lower(), list(text_msg))))
            m.text = txt_msg
            self.reactToMessage(message_object.uid, MessageReaction.WOW)
            self.sendRemoteImage("https://usatftw.files.wordpress.com/2017/05/spongebob.jpg", thread_id=thread_id, thread_type=thread_type)
            self.send(m, thread_id=thread_id, thread_type=thread_type)
            
client = VacationBot(MY_ID, MY_PASSWORD)
client.listen()