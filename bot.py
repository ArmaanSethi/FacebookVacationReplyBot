import fbchat
from user_info import MY_ID,MY_PASSWORD
#https://scontent-iad3-1.xx.fbcdn.net/v/t1.0-1/c1.0.160.160/p160x160/13124855_1178970508810332_7106922968667891819_n.jpg?oh=1bee7925ee7d3ca916240d6231729eb3&oe=599CF92F
client = fbchat.Client(MY_ID, MY_PASSWORD)

friends = []
friends.append(client.getUsers("Vamsi")[0])
friends.append(client.getUsers("Harshal")[0])

#sent = client.send(friend.uid, "Yo im sending this through a my terminal lol...wsup")
for f in friends:
    #print(f)
    #print(client.getUserInfo(f.uid))

    # sent = client.send(f.uid, "This be a message to multiple ppls from a ...idek what this is")
    # if sent:
    #     print(f, "Message sent successfully!")
