from flask import Flask, render_template


import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

@app.route("/")
def home():
   return render_template('desktop-1.html')

if __name__ == '__main__':
   app.run()

@app.route("/test")
def test():
    return render_template('results.html')

def func():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="56e38026bbc84e3ca3b71ff14ada6a3c",
                                                   client_secret="ec745f399faa4b09b119e51d06a18583",
                                                   redirect_uri="http://localhost:9090",
                                                   scope="user-library-read "
                                                         "user-top-read "
                                                         "user-read-recently-played "
                                                         "user-read-playback-state"))

    results = sp.current_user_top_tracks(limit=511, offset=0, time_range='long_term')
    genre = sp.recommendation_genre_seeds()
    saved_tracks = sp.current_user_saved_tracks()

    #currentSong = sp.currently_playing(market='US')

    #for item in results['items']:
    #print(item, "\n")

    #results = sp.current_user_saved_tracks()

    #for idx, item in enumerate(results['items']):
        #print(idx + 1, item['name'], ' - ', item['uri'],  "\n")

    for idn in enumerate(genre['genres']):
        print(idn)

    #recs = sp.recommendations()
    #dance = dance +
    #track = item['track']
    #print(item['track']['artists'][0]['name'], " – ", item['track']['name'])

    trackList = []
    #for i in range(0,50):
        #trackList.append(results['items'][i]['uri'])
        #print(trackList)
        #trackList.append(res)
    for track in saved_tracks['items']:
        print(track['track']['name'])
        trackList.append(track['track']['uri'])
    #print(res)

    #for t in range(0, 10):
    #song = results['items'][t]['uri']
    d = 0
    e = 0
    l = 0
    m = 0
    s = 0
    a = 0
    intr = 0
    liv = 0
    v = 0
    t = 0
    feat = sp.audio_features(tracks=trackList)
    for f in feat:
        d = d + f['danceability']
        e = e + f['energy']
        l = l + f['loudness']
        m = m + f['mode']
        s = s + f['speechiness']
        a = a + f['acousticness']
        intr = intr + f['instrumentalness']
        liv = liv + f['liveness']
        v = v + f['valence']
        t = t + f['tempo']
        dance = d/len(trackList)
        energy = e/len(trackList)
        loud = l/len(trackList)
        speechiness = s/len(trackList)
        acousticness = a/len(trackList)
        instrumentalness = intr/len(trackList)
        liveness =  liv/len(trackList)
        valence = v/len(trackList)
        tempo = t / len(trackList)


    topArtists = sp.current_user_top_artists()
    genres = []
    for artist in topArtists['items']:
        for art in artist['genres']:
            genres.append(art)
    #mode = max(set(genres), key=genres.count)
    print(genres)
    #sort by greatest to least


    print(" dance: ", d/len(trackList), "\n", "energy: ", e/len(trackList), "\n", "loud: ", l/len(trackList),"\n", "mode: ", m/len(trackList),
          "\n", "speechiness: ", s/len(trackList), "\n", "acousticness: ", a/len(trackList), "\n","instrumentalness: ", intr/len(trackList),
          "\n", "liveness: ", liv/len(trackList), "\n", "valence: ", v/len(trackList),"\n", "tempo: ", t/len(trackList))

    firstFiveTracks = []
    for tra in range(0, 5):
        firstFiveTracks.append(trackList[tra])

    recommendations = sp.recommendations(seed_artists=None, seed_genres=None, seed_tracks=firstFiveTracks, limit=20, country='US',
                                         target_danceability=dance,
                                         target_energy=energy,
                                         target_loudness=loud,
                                         target_speechiness=speechiness,
                                         target_acousticness=acousticness,
                                         target_instrumentalness=instrumentalness,
                                         target_liveness=liveness,
                                         target_valence=valence,
                                         target_tempo=tempo,
                                         max_popularity=33,
                                         target_popularity=20)

    print(sp.track('spotify:track:2E7W1X4maFFcjHrVrFA7Vs')['popularity'])

    rec = ''
    for item in recommendations['tracks']:
        rec += item['artists'][0]['name'] + " - " + item['name'] + "\n"
    return rec

    #get list of artists
    #get list of genres






        #d = d + feat[0]['danceability']
        #e = e + feat[0]['energy']
    #d = d/50
    #e = e/50

    #print(d)

    #d2 = 0
    #song2 = results['items'][0]['uri']
    #feat2 = sp.audio_features(tracks=song2)

    #print(feat2)

    #danceabilty,energy,loudness,mode,speechiness,acousticness,instrumentalness, liveness, valence, tempo,
    #recs = sp.recommendations(seed_tracks=trackList)

    #for a in recs:
        #print(a, "\n")
func()

if __name__ == "__main__":
    app.run(port=5000)