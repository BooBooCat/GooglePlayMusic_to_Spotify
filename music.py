import csv
import pprint
import spotipy
from gmusicapi import Mobileclient
from spotipy.oauth2 import SpotifyClientCredentials

pp = pprint.PrettyPrinter(indent=4)

# GooglePlay Auth
mc = Mobileclient()
mc.perform_oauth() 
#outhres = mc.oauth_login(oauth_credentials = './outh.txt',device_id = mc.FROM_MAC_ADDRESS) #in case you want to use auth file 
#print(outhres)

# Spotify Auth
scope = "user-library-read user-library-modify"
token = spotipy.util.prompt_for_user_token(client_id='<FILL ME>', client_secret='<FILL ME>', redirect_uri='http://example.com/', scope=scope)
sp = spotipy.Spotify(auth=token)

f = csv.writer(open("myMusic.csv", "w"))

# Write CSV Header
f.writerow([ 'Artist', 'Title', 'Album', 'Year','Spotify_UID'])

for SongDict in mc.get_top_songs():
    try:
        artist = SongDict['artist'] 
        title = SongDict['title']
        album = SongDict['album']
        year = SongDict['year']
        SPID = sp.search(q='track:' + title, type='track')
        SP_trackID = SPID['tracks']['items'][0]['id']
        f.writerow([artist, title, album, year, SP_trackID])
        pp.pprint(title)
        #pp.pprint(SP_trackID)
        gogo = sp.current_user_saved_tracks_contains([SP_trackID])[0]
        pp.pprint(gogo)
        if gogo == False:
            goga = sp.current_user_saved_tracks_add([SP_trackID])
            #pp.pprint('Добавил ' + artist + ' - ' + title)
    except LookupError:
        f.writerow([artist,
                    title,
                    album,
                    year])
    
    #pp.pprint(SongDict.get(['title', 'artist', 'composer', 'album','year'],None))