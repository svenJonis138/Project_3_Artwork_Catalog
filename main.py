import artwork_db
import os
from artist import Artist
from config import db_path

db_path = os.path.join('database', 'test_artwork_catalog.db')


def main():

    artwork_db.create_tables()
    name = input("Enter new artist name: ")
    email = input("enter email: ")
    new_artist = Artist(name, email)
    artwork_db.add_artist(new_artist)
    # artwork_db.create_test_db()


if __name__ == '__main__':
    main()
