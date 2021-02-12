import artwork_db as db


def main():
    db.create_artwork_table()
    db.create_artists_table()


if __name__ == '__main__':
    main()
