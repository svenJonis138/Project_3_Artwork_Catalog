
import sqlite3

from config import db_path


def create_tables():
    """create the artwork table"""
    with sqlite3.connect(db_path) as conn:
        print(db_path)
        conn.execute('CREATE TABLE IF NOT EXISTS artwork '
                     '(artist_name TEXT NOT NULL, '
                     'art_work_name TEXT UNIQUE, '
                     'price INTEGER, '
                     'available BOOLEAN)')
        """create the artists table"""
        conn.execute('CREATE TABLE IF NOT EXISTS artists '
                     '(artist_name TEXT NOT NULL, '
                     'email TEXT UNIQUE)')
    conn.close()


# def create_test_db():
#     with sqlite3.connect(os.path.join('database', 'test_artwork.db')) as conn:
#         conn.execute('CREATE TABLE IF NOT EXISTS artwork '
#                      '(artist_name TEXT, '
#                      'art_work_name TEXT UNIQUE, '
#                      'price INTEGER, '
#                      'available BOOLEAN)')
#         """create the artists table"""
#         conn.execute('CREATE TABLE IF NOT EXISTS artists '
#                      '(artist_name TEXT, '
#                      'email TEXT UNIQUE)')
#     conn.close()


def add_artist(artist):

    insert_sql = 'INSERT INTO artists (artist_name, email) VALUES (?, ?)'
    try:
        with sqlite3.connect(db_path) as conn:
            res = conn.execute(insert_sql, (artist.artist_name, artist.email))
            new_id = res.lastrowid  # Get the ID of the new row in the table
            artist.id = new_id  # Set this artist's ID
        conn.close()
    except sqlite3.IntegrityError as e:
        raise ArtDbError(f'Error - this artist is already in the database. {artist}') from e
    # finally:



class ArtDbError(Exception):
    """for any db errors"""
    pass

