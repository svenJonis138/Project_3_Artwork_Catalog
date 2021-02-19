import artwork_db


def artist_already_in_db(artist_name):
    current_artists = artwork_db.get_all_artists()
    for artist in current_artists:
        if artist.artist_name.upper() == artist_name.upper():
            return True
        else:
            return False


def artist_email_not_unique(artist_email):
    current_artists = artwork_db.get_all_artists()
    for artist in current_artists:
        if artist.email.upper() == artist_email.upper():
            return True
        else:
            return False
