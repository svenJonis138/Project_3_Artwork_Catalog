import artwork_db
import os
from artist import Artist
from config import db_path
from artwork import Artwork
import menu

db_path = os.path.join('database', 'test_artwork_catalog.db')


def main():
    artwork_db.create_tables()
    while True:
        menu.display_menu()


if __name__ == '__main__':
    main()
