import artwork_db


def artist_already_in_db(artist_name):
    current_artists = artwork_db.get_all_artists()
    names = []
    for artist in current_artists:
        names.append(artist.artist_name)
    if artist_name.upper() in names:
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


def artist_has_work_in_db(artist_name):
    current_artwork = artwork_db.get_all_artwork()
    names =[]
    for artwork in current_artwork:
        names.append(artwork.artist_name)
    if artist_name in names:
        return True
    else:
        return False


def artwork_name_is_unique(artwork_name):

    current_artwork = artwork_db.get_all_artwork()
    titles = []
    for artwork in current_artwork:
        titles.append(artwork.artwork_name.upper())
    if artwork_name.upper() in titles:
        return False
    else:
        return True


def price_is_right(price):
    if price.isdigit():
        return True
    else:
        return False


def artwork_exists(artwork_query):
    current_artwork = artwork_db.get_all_artwork()
    titles = []
    for artwork in current_artwork:
        titles.append(artwork.artwork_name.upper())
    if artwork_query.upper() in titles:
        return True
    else:
        return False


def name_of_artist(artwork_to_delete):
    current_artwork = artwork_db.get_all_artwork()
    for artwork in current_artwork:
        if artwork.artwork_name == artwork_to_delete:
            return artwork.artist_name


def response_affirmative(response):
    if response.upper() == 'Y':
        return True
    elif response.upper() == 'X':
        print('exiting ')
        return False
    else:
        return False


def artwork_available(artwork_name, artist):
    currently_available = artwork_db.get_available_artwork_from_one_artist(artist)
    titles = []
    for artwork in currently_available:
        titles.append(artwork.artwork_name.upper())
    if artwork_name.upper() in titles:
        print(artwork)
        return True
    else:
        return False








