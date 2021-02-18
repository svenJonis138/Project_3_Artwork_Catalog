import sqlite3
import artist
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
            conn.execute('DELETE FROM artists WHERE artist_name LIKE ? COLLATE NOCASE', (artist_to_delete.artist_name,))
        conn.close()
    except sqlite3.IntegrityError as e:
        raise ArtDbError(f'Error - this artist was not found in the database. {artist}') from e


class ArtDbError(Exception):
    """for any db errors"""
    pass
