import artwork_db
"""this module checks all user given data for validity before calling DB functions"""


def artist_already_in_db(artist_name):
    """checks if artist is already registered"""
    current_artists = artwork_db.get_all_artists()
    names = []
    for artist in current_artists:
        names.append(artist.artist_name)
    if artist_name.upper() in names:
        return True
    else:
        return False


def artist_email_not_unique(artist_email):
    """checks to ensure email is unique"""
    current_artists = artwork_db.get_all_artists()
    for artist in current_artists:
        if artist.email.upper() == artist_email.upper():
            return True
        else:
            return False


def artist_has_work_in_db(artist_name):
    """checks if a registered artist has any work in DB"""
    current_artwork = artwork_db.get_all_artwork()
    names =[]
    for artwork in current_artwork:
        names.append(artwork.artist_name)
    if artist_name in names:
        return True
    else:
        return False


def artwork_name_is_unique(artwork_name):
    """checks if an artwork name is unique"""
    current_artwork = artwork_db.get_all_artwork()
    titles = []
    for artwork in current_artwork:
        titles.append(artwork.artwork_name.upper())
    if artwork_name.upper() in titles:
        return False
    else:
        return True


def price_is_right(price):
    """checks to ensure string price input is actually a number safe to parse to int"""
    if price.isdigit():
        return True
    else:
        return False


def artwork_exists(artwork_query):
    """checks to ensure a piece of art is in the database"""
    current_artwork = artwork_db.get_all_artwork()
    titles = []
    for artwork in current_artwork:
        titles.append(artwork.artwork_name.upper())
    if artwork_query.upper() in titles:
        return True
    else:
        return False


def name_of_artist(artwork_to_change):
    """grabs the name of the artist associated with either selling a piece or deleting
    to use to confirm with user before updating the DB"""
    current_artwork = artwork_db.get_all_artwork()
    for artwork in current_artwork:
        if artwork.artwork_name == artwork_to_change:
            return artwork.artist_name


def response_affirmative(response):
    """checks the validity of yes no answers used to confirm updating DB"""
    if response.upper() == 'Y':
        return True
    elif response.upper() == 'X':
        print('exiting ')
        return False
    else:
        return False


def artwork_available(artwork_name, artist):
    """checks if an artwork is available"""
    currently_available = artwork_db.get_available_artwork_from_one_artist(artist)
    titles = []
    for artwork in currently_available:
        titles.append(artwork.artwork_name.upper())
    if artwork_name.upper() in titles:
        return True
    else:
        return False








