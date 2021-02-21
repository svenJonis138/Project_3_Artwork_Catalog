import artwork_db
import controls_utils
from artist import Artist
from artwork import Artwork
"""this module handles all user input for functions, sends data to controls.utils for validation and
when cleared does all the database function calls"""


def get_artist_name():
    """returns artist name"""
    artist_name = input('What is the name of the artist? ')
    while not artist_name:
        artist_name = input('What is the name of the artist? ')
    return artist_name


def get_artist_email():
    """returns artist email if it is unique"""
    artist_email = input('Please enter artist\'s email: ')
    while controls_utils.artist_email_not_unique(artist_email):
        print('Artist\'s email must be unique. ')
        artist_email = input('Please enter artist\'s email: ')
    return artist_email


def get_new_artwork_name():
    """returns artwork name if it is unique for creating new records"""
    artwork_name = input('Please enter title of artwork: ')
    while not controls_utils.artwork_name_is_unique(artwork_name):
        print('Artwork name is taken')
        artwork_name = input('Please enter title of artwork: ')
    return artwork_name


def get_artwork_name():
    """returns artwork name already in db for accessing artwork for functions"""
    artwork_name = input('Please enter title of artwork: ')
    if not controls_utils.artwork_name_is_unique(artwork_name):
        return artwork_name
    else:
        print('artwork not found')


def get_price():
    """gets the price and checks that it is the correct data type, then parses it into int"""
    price = input('Please enter the price of the piece: ')
    while not controls_utils.price_is_right(price):
        print('Price must be a numerical value ')
        price = input('Please enter the price of the piece: ')
    return int(price)


def add_new_artwork():
    """checks if artist name is already registered and if not, registers them before adding new artwork"""
    artist_name = get_artist_name()
    if not controls_utils.artist_already_in_db(artist_name):
        print('Artist not registered, creating new registration. ')
        email = get_artist_email()
        new_artist = Artist(artist_name, email)
        artwork_db.add_artist(new_artist)
    artwork_name = get_new_artwork_name()
    price = get_price()
    available = True
    new_artwork = Artwork(artist_name, artwork_name, price, available)
    artwork_db.add_artwork(new_artwork)


def add_new_artist(artist_name):
    """adds new artist to db if they are not already in"""
    if controls_utils.artist_already_in_db(artist_name):
        print('This artist is already in database')

    else:
        artist_email = get_artist_email()
        new_artist = Artist(artist_name, artist_email)
        artwork_db.add_artist(new_artist)


def display_artist_complete_portfolio(artist_name):
    """checks if artist is in db, if so displays their works sold and unsold"""
    if controls_utils.artist_has_work_in_db(artist_name):
        results = artwork_db.get_all_artwork_from_one_artist(artist_name)
        for piece in results:
            print(piece)
    else:
        print('Sorry, no artwork from this artist to display ')


def display_artist_available_portfolio(artist_name):
    """checks if artist is in db, if so displays their works that are unsold"""
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
    """gets name of artwork to delete and checks to make sure before deleting"""
    artwork = input('Which artwork would you like to delete? ')
    while not controls_utils.artwork_exists(artwork):
        artwork = input('Which artwork would you like to delete? ')
    artist = controls_utils.name_of_artist(artwork)
    response = input('Are you sure you want to delete ' + artwork + ' by ' + artist + ' ? Y or N')
    if response.upper() == 'Y':
        delete_artwork(artwork)
    while not controls_utils.response_affirmative(response):
        response = input('Are you sure you want to delete '
                         + artwork + ' by ' + artist + ' ? Y or N or press X to escape ')
        if response.upper() == 'X':
            break
        elif response.upper() == 'N':
            break


def delete_artwork(artwork):
    """does the actual deletion, separated for testing"""
    artwork_db.delete_artwork(artwork)


def change_availability():
    """after confirming the artwork exists and is not already sold, changes status to sold"""
    artwork_sold = get_artwork_name()
    if not controls_utils.artwork_exists(artwork_sold):
        print('No record of that piece of art. ')
    else:
        artist = controls_utils.name_of_artist(artwork_sold)
        if not controls_utils.artwork_available(artwork_sold, artist):
            print('Sorry that piece has already been sold. ')
        else:
            response = input('Mark ' + artwork_sold + ' as sold? Y or N ')
            if response.upper() == 'Y':
                mark_as_sold(artwork_sold)
            while not controls_utils.response_affirmative(response):
                response = input('Are you sure you want to mark '
                                 + artwork_sold + ' by ' + artist + ' as sold? Y or N or press X to escape ')
                if response.upper() == 'X':
                    break
                elif response.upper() == 'N':
                    break


def mark_as_sold(artwork):
    """does the actual change in db, separated for testing"""
    artwork_db.update_artwork(artwork)
    print(artwork + ' has been marked as sold. ')


def display_all():
    """prints all artwork for testing purposes"""
    results = artwork_db.get_all_artwork()
    for artist in results:
        print(artist)
