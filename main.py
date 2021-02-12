import artwork_db
from artist import Artist


def main():
    # artwork_db.create_tables()
    name = input("Enter new artist name: ")
    email = input("enter email: ")
    new_artist = Artist(name, email)
    artwork_db.add_artist(new_artist)
    # artwork_db.create_test_db()


if __name__ == '__main__':
    main()
