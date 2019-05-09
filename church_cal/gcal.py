from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
#https://developers.google.com/calendar/quickstart/python
import sys

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'

def main():
    error = 0
    # Adding Arg parser.  Need credential file and token file location(s)
    # HELP: First file arg is crediential
    # HELP: Second file arg is token
    num_of_args = len(sys.argv)-1
    if num_of_args == 2:
        cred_file = sys.argv[1]
        print ("credential file: " + cred_file)
        print ("token file: " + token_file)
    else:
        error = 1
        print ("ERROR: Expected two input arguments.  python church_cal.py [credential_file_path] [token_file_path]")
        #TODO: throw an exception 


    if error==0:
        store = file.Storage(token_file)
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(cred_file, SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('calendar', 'v3', http=creds.authorize(Http()))

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

if  __name__ == '__main__':
    main()

