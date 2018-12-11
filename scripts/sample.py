from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

store = file.Storage('token_rw.json')
creds = store.get()

if not creds or creds.invalid:
  ## this code will trigger a transfer to the browser, requiring user to authenticate.
  flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
  creds = tools.run_flow(flow, store)

service = build('sheets', 'v4', http=creds.authorize(Http()))
sheet = service.spreadsheets()
sv = sheet.values()

##
## documentation implies that range should be specified twice.
##
x = sv.update(spreadsheetId="18exg34zO7wvuRz8qvVLtHTMOGJtlcA05zjNi9J810EM",range='Sheet1!b20:c21', body={'range':'Sheet1!b20:c21','majorDimension':'ROWS','values':[[99,1],['c','d']]}, valueInputOption='RAW')
x.execute()

