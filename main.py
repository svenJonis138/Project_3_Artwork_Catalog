import artwork_db
import os
from artist import Artist
from config import db_path

db_path = os.path.join('database', 'test_artwork_catalog.db')


def main():
    #
    # artwork_db.create_tables()
    artists_in_db = artwork_db.get_all_artists()
    for name in artists_in_db:
        print(str(name))
    name = input("Enter new artist name: ")
    email = input("enter email: ")
    new_artist = Artist(name, email)
    artwork_db.add_artist(new_artist)
    # artwork_db.create_test_db()


if __name__ == '__main__':
    main()
