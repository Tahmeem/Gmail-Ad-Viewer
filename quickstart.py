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


labels = service.users().labels().get(userId='tahmeemmahedi@gmail.com',id='CATEGORY_PERSONAL').execute()

def findEmail(email):
    email = email[1:len(email)-1]
    return email

messagesRead = service.users().messages().list(userId='tahmeemmahedi@gmail.com',labelIds=['CATEGORY_PROMOTIONS']).execute()
for i in messagesRead['messages']:
    msgFirst = service.users().messages().get(userId='tahmeemmahedi@gmail.com',id=i['id'],format="full").execute()
    print(msgFirst['snippet'])
    headers = msgFirst['payload']['headers']
    for header in headers:
        if header['name'] == 'From':
            headerList = header['value'].split()
            headerEmail = headerList.pop(-1)
            headerEmail = findEmail(headerEmail)
            headerName = " ".join(headerList)
            print(headerName + ' Email' + ' ' + headerEmail)
    print('\n\n')

#print(messagesRead)


