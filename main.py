import artwork_db
import os
from artist import Artist
from config import db_path
from artwork import Artwork

db_path = os.path.join('database', 'test_artwork_catalog.db')


def main():
    #
    # artwork_db.create_tables()
    # artists_in_db = artwork_db.get_all_artists()
    # for name in artists_in_db:
    #     print(str(name))
    # name = input("Enter new artist name: ")
    # email = input("enter email: ")
    # new_artist = Artist(name, email)
    # artwork_db.add_artist(new_artist)
    # artwork_db.create_test_db()
    # artwork_db.delete_artist('johnny')
    aw1 = Artwork('Banksy', 'Mcdonald\'s is stealing your children', 138, True)
    # artwork_db.add_artwork(aw1)
    # results = artwork_db.get_all_artwork()
    # for piece in results:
    #     print(piece)

    artwork_db.update_artwork(aw1)
if __name__ == '__main__':
    main()
