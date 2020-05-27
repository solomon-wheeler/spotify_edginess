# Spotify Edginess
A program that gets data on your top artists on spotify, and uses there popularity data to decide how edgy your music is. 
It also includes a file from another project which authenticates the user for the required scope to be able to see there top artists

# How does it work?
It uses the spotipy libary to authenticate the user for the "user-top-read" scope, which allows the program to request the users top artists from spotfiy
It then gets the data on how popular these artists are from spotfiy (from a scale of 0-100) and determines and average from this, aswell as outputting the users top 5 most and least popular artists


# How to get it working?
You will need to create an application from the spotify developer dasboard - https://developer.spotify.com/dashboard/
Once you have created an application you need to add a redirect adress, this can be anything, but spotipy will automaticaly get the credentials if you redirect to a local host
The application you have created will have a clinet_id and client secret which you will need to add into a text file in the same directoy as this code in the following format    
client_id =111111111111111  
client_secret =11111111111111111111   
dev_username =my-username                 (this is the username for the account you used to sign into the developer dasboard)

You then have to run the top_artists script, which will ask you to long into your account.
