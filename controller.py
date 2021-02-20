import artwork_db
import controls_utils
from artist import Artist
from artwork import Artwork


def get_artist_name():
    artist_name = input('What is the name of the artist? ')
    return artist_name


def get_artist_email():
    artist_email = input('Please enter artist\'s email: ')
    while controls_utils.artist_email_not_unique(artist_email):
        print('Artist\'s email must be unique. ')
        artist_email = input('Please enter artist\'s email: ')
    return artist_email


def get_artwork_name():
    artwork_name = input("Please enter title of artwork: ")
    while not controls_utils.artwork_name_is_unique(artwork_name):
        print('Artwork name is taken')
        artwork_name = input("Please enter title of artwork: ")
    return artwork_name


def get_price():
    price = input('Please enter the price of the piece: ')
    while not controls_utils.price_is_right(price):
        print('Price must be a numerical value ')
        price = input('Please enter the price of the piece: ')
    return int(price)


def add_new_artwork():
    artist_name = get_artist_name()
    if not controls_utils.artist_already_in_db(artist_name):
        print('Artist not registered, creating new registration. ')
        email = get_artist_email()
        new_artist = Artist(artist_name, email)
        artwork_db.add_artist(new_artist)

    artwork_name = get_artwork_name()
    price = get_price()
    available = True
    new_artwork = Artwork(artist_name, artwork_name, price, available)
    artwork_db.add_artwork(new_artwork)


def add_new_artist(artist_name):
    if controls_utils.artist_already_in_db(artist_name):
        print('This artist is already in database')
    else:
        artist_email = get_artist_email()
        new_artist = Artist(artist_name, artist_email)
        artwork_db.add_artist(new_artist)


def display_artist_complete_portfolio(artist_name):
    if controls_utils.artist_has_work_in_db(artist_name):
        results = artwork_db.get_all_artwork_from_one_artist(artist_name)
        for piece in results:
            print(piece)
    else:
        print('Sorry, no artwork from this artist to display ')


def display_artist_available_portfolio(artist_name):
    if controls_utils.artist_has_work_in_db(artist_name):
        results = artwork_db.get_available_artwork_from_one_artist(artist_name)
        if results:
            for piece in results:
                print(piece)
        else:
            print('Sorry this artist does not have any available art at this time ')
    else:
        print('Sorry, no artwork from this artist to display ')


def get_artwork_to_delete():
    artwork = input('Which artwork would you like to delete? ')
    while not controls_utils.artwork_exists(artwork):
        artwork = input('Which artwork would you like to delete? ')
    artist = controls_utils.name_of_artist(artwork)
    response = input('Are you sure you want to delete ' + artwork + ' by ' + artist + ' ? ')
    while not controls_utils.response_affirmative(response):
        response = input('Are you sure you want to delete '
                         + artwork + ' by ' + artist + ' ? press X to escape')
    delete_artwork(artwork)


def delete_artwork(artwork):
    artwork_db.delete_artwork(artwork)
