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
    message_bytes = msg.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

labels = service.users().labels().get(userId='tahmeemmahedi@gmail.com',id='CATEGORY_PERSONAL').execute()


messagesRead = service.users().messages().list(userId='tahmeemmahedi@gmail.com',labelIds=['CATEGORY_PROMOTIONS']).execute()
for i in messagesRead['messages']:
    msgFirst = service.users().messages().get(userId='tahmeemmahedi@gmail.com',id=i['id']).execute()
    print(msgFirst['snippet'])
    print('\n\n')

#print(messagesRead)


