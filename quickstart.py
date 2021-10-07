from Google import Create_Service
import base64
CLIENT_FILE = 'credentials.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = Create_Service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)
profile = service.users().getProfile(userId='tahmeemmahedi@gmail.com').execute()
emailAddress = profile['emailAddress']
messages = profile['messagesTotal']

def parse_msg(msg):
    if msg.get("payload").get("body").get("data"):
        return base64.urlsafe_b64decode(msg.get("payload").get("body").get("data").encode("ASCII")).decode("utf-8")
    return msg.get("snippet")


labels = service.users().labels().get(userId='tahmeemmahedi@gmail.com',id='CATEGORY_PERSONAL').execute()
messages = service.users().messages().list(userId='tahmeemmahedi@gmail.com').execute()
for i in messages['messages']:
    msgid = i['id']
    msgContent = service.users().messages().get(userId='tahmeemmahedi@gmail.com',id=msgid).execute()
    #if 'CATEGORY_PROMOTIONS' in msgContent['labelIds']:
    newmsg= parse_msg(msgContent)
    print('Message Content:' + newmsg)

messageId = messages['messages'][0]['id']
messagesRead = service.users().messages().get(userId='tahmeemmahedi@gmail.com',id=messageId).execute()

#print(messagesRead)


