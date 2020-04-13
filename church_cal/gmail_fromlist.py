from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import sys

#https://developers.google.com/gmail/api/quickstart/python
#Need to relook at token


# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'

def main():
    error = 0
    # Adding Arg parser.  Need credential file and token file location(s)
    # HELP: First file arg is crediential
    # HELP: Second file arg is token
    num_of_args = len(sys.argv)-1
    if num_of_args == 2:
        cred_file = sys.argv[1]
        token_file = sys.argv[2]
        print ("credential file: " + cred_file)
        print ("token file: " + token_file)
    else:
        error = 1
        print ("ERROR: Expected two input arguments.  python gmail_fromlist.py [credential_file_path] [token_file_path]")
        #TODO: throw an exception


    if error==0:
        store = file.Storage(token_file)
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(cred_file, SCOPES)
            creds = tools.run_flow(flow, store)

        service = build('gmail', 'v1', credentials=creds)
        #service = build('calendar', 'v3', http=creds.authorize(Http()))

        # Call the Gmail API
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
        else:
            print('Labels:')
            for label in labels:
                print(label['name'])

if  __name__ == '__main__':
    main()
