import requests
import json
from authenticate_spotify import user_auth
import time

def get_top_artists(user_token):
    url = "https://api.spotify.com/v1/me/top/artists"
    time_range = "medium_term"
    artist_limit = 50
    headers = {"Authorization": "Bearer "+ user_token}
    payload = {"time_range": time_range, "limit": artist_limit}
    spotify_response = requests.get(url, headers= headers, params = payload )
    parsed_top_artists = json.loads(spotify_response.content)
    return parsed_top_artists

def get_overall_popularity_data(top_artists):
    overall_popularity = 0
    amount_done = 0
    all_artist_data = []
    for individual_artist in top_artists['items']:
        #print(individual_artist['popularity'])
        overall_popularity += individual_artist['popularity']
        amount_done += 1 # Always 50 at the moment but could be change in future
        this_artist_data = [individual_artist['name'], individual_artist['popularity']]
        all_artist_data.append(this_artist_data)
    average_popularity = int(overall_popularity/amount_done)
    top_bot_artists = get_top_bot_5(all_artist_data,amount_done)
    top_5_artists = top_bot_artists[1]
    bot_5_artists = top_bot_artists[0]
    output_data(average_popularity,top_5_artists,bot_5_artists)

def get_top_bot_5(all_artist_data,amount_done):
    top5_artists = []
    bot5_artists = []
    sorted_all_artist_data = sorted(all_artist_data,key=lambda x: x[1])
    for each_number in range(0,5):
        bot5_artists.append(sorted_all_artist_data[each_number])
        top5_artists.append(sorted_all_artist_data[amount_done - (each_number + 1)]) # need to check this works proparly
    return top5_artists, bot5_artists

def output_data(average_popularity,top_5_artists,bot_5_artists):
    print("I'm about to reveal you're score on the edgeometer ...")
    time.sleep(1)
    print("100 is the least edgey, and 0 is the most edgey")
    time.sleep(2)

    print("Your score on the edge-ometer was " , average_popularity ," out of 100")
    time.sleep(1)

    edge_responses = [[90,"You need to get of the top 40 playlist , there's a world of music out there!" ],[80,"You didn't really know them before they were popular did you? "],
                      [70,"A bit basic but respectable, you have the edge-o-meters approval" ], [60,"Very impressive, you're music is far of the beaten track" ],
                      [50, "Wow someone's hip. Do you even know what capital is?" ], [40, "Your music taste is so far underground it's in china"],
                      [30,"Really? You are clearly the definition of hipster, please teach me your ways"], [20,"Maybe there's a reason the music you listen to is so unpopular?"],
                      [10, "be honest. Have you been listening to your own songs on spotify?"]]
    response_found = False
    responses_done = 0
    while not response_found:
        responses_done += 1
        if average_popularity > edge_responses[responses_done][0]:
            print(edge_responses[responses_done][1])
            response_found = True
    time.sleep(2)

    print("The artists you listen to that are most edgy are:")
    time.sleep(1)

    for each_in_list in range(0,5):
        print(str(each_in_list + 1 ) + ". " + str(top_5_artists[each_in_list][0]) + " Popularity : " + str(top_5_artists[each_in_list][1]))
        time.sleep(0.5)

    print("The artists you listen to that are most popular are:")
    time.sleep(1)

    for each_in_list in range(0,5):
        print(str(each_in_list + 1 ) + ". " + str(bot_5_artists[each_in_list][0]) + " Popularity  : " + str(bot_5_artists[each_in_list][1]))
        time.sleep(0.5)












##main##
user_token = user_auth()
top_artists = get_top_artists(user_token)
#print(json.dumps(top_artists,indent=4, sort_keys=True))
#print(top_artists)
get_overall_popularity_data(top_artists)