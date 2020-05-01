from plexapi.server import PlexServer
import os
import time
from requests.exceptions import ConnectionError

baseurl = 'http://192.168.1.2:32400'
token = '<MY TOKEN HERE>'

def get_sessions(plex): 
    sessions = plex.sessions()

    if len(sessions) != 0:
        return True
        print("session exists")
    else:
        return False
        print("no session")

def shutting_down():
    os.system('sudo shutdown now')

if __name__ == "__main__":
    try:
        plex = PlexServer(baseurl, token)

        while True:
            if get_sessions(plex):
                print('plex session active, not shutting down for now')
            else: 
                print('shutting down')
                shutting_down()
                break
            time.sleep(60)

    except ConnectionError:
        print("no plex running, shutting down")
        shutting_down()
