import sqlite3
import artist
from artwork import Artwork
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


def add_artist(new_artist):
    """adds a new artist's info into artist table if not already there"""
    insert_sql = 'INSERT INTO artists (artist_name, email) VALUES (?, ?)'
    try:
        with sqlite3.connect(db_path) as conn:
            res = conn.execute(insert_sql, (new_artist.artist_name, new_artist.email))
            new_id = res.lastrowid  # Get the ID of the new row in the table
            artist.id = new_id  # Set this artist's ID
        conn.close()
    except sqlite3.IntegrityError as e:
        raise ArtDbError(f'Error - this artist is already in the database. {new_artist}') from e


def get_all_artists():
    """Displays all artists currently in db"""
    con = sqlite3.connect(db_path)
    artists_cursor = con.execute('SELECT * FROM artists')
    artists = [artist.Artist(*row) for row in artists_cursor.fetchall()]
    con.close()
    return artists


def delete_artist(artist_to_delete):
    """deletes specified artist (must match spelling)"""
    try:
        with sqlite3.connect(db_path) as conn:
            conn.execute('DELETE FROM artists WHERE artist_name LIKE ? COLLATE NOCASE', (artist_to_delete,))
        conn.close()
    except sqlite3.IntegrityError as e:
        raise ArtDbError(f'Error - this artist was not found in the database. {artist}') from e


def add_artwork(new_artwork):
    insert_sql = 'INSERT INTO artwork (artist_name, art_work_name, price, available) VALUES (?, ?, ?, ?)'
    try:
        with sqlite3.connect(db_path) as conn:
            res = conn.execute(insert_sql, (new_artwork.artist_name, new_artwork.art_work_name, new_artwork.price,
                                            new_artwork.available))
            new_id = res.lastrowid  # Get the ID of the new row in the table
            artist.id = new_id  # Set this artist's ID
        conn.close()
    except sqlite3.IntegrityError as e:
        raise ArtDbError(f'Error - this artwork is already in the database. {new_artwork}') from e


def get_all_artwork():
    con = sqlite3.connect(db_path)
    artwork_cursor = con.execute('SELECT * FROM artwork')
    artwork = [Artwork(*row) for row in artwork_cursor.fetchall()]
    con.close()
    return artwork


def update_artwork(sold_artwork):
    # insert_sql = 'UPDATE artwork SET available = FALSE WHERE art_work_name = ?', (sold_artwork.art_work_name,)
    try:
        with sqlite3.connect(db_path) as conn:
            res = conn.execute('UPDATE artwork SET available = FALSE WHERE'
                               ' art_work_name = ?', (sold_artwork.art_work_name,))

        conn.close()
    except sqlite3.IntegrityError as e:
        raise ArtDbError(f'Error - this artwork is already in the database. {sold_artwork}') from e


class ArtDbError(Exception):
    """for any db errors"""
    pass
