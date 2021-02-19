import artwork_db
import controls_utils
from artist import Artist


def add_new_artist():
    artist_name = input("What is the name of the artist you would like to add? ")
    if controls_utils.artist_already_in_db(artist_name):
        print('This artist is already in database')
    else:
        artist_email = input('Please enter artist\'s email: ')
        if controls_utils.artist_email_not_unique(artist_email):
            print('Artist email must not be the same as another artist ')
        else:
            new_artist = Artist(artist_name, artist_email)
            artwork_db.add_artist(new_artist)
