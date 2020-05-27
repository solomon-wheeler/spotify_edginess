# import sys
import spotipy
import spotipy.util as util
import requests
import json



def user_auth():
    f = open("credentials.txt","r")
    creds= []
    for x in f:
        creds.append((x.strip()).split("=")[1])
    client_id = creds[0]
    client_secret = creds[1]
    dev_username = creds[2]
    scope = "user-top-read"

    redirect = "http://localhost:8080"
    user_token = util.prompt_for_user_token(username=dev_username,   #developer account username not client
                                            scope=scope,
                                            client_id=client_id,
                                            client_secret=client_secret,
                                            redirect_uri=redirect)
    return user_token

#not used in this program
def client_auth():
    grant_type = 'client_credentials'
    url = 'https://accounts.spotify.com/api/token'
    response = requests.post(url,
                             data={'grant_type': grant_type},
                             auth=(client_id, client_secret))
    client_token_raw = json.loads(response.text)
    client_token = client_token_raw["access_token"]
    return client_token

