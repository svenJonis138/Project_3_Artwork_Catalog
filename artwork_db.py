import sqlite3
import artist
from artwork import Artwork
from config import db_path
"""This module holds all database code"""


def create_tables():
    """create the artwork table"""
    with sqlite3.connect(db_path) as conn:
        print(db_path)
        conn.execute('CREATE TABLE IF NOT EXISTS artwork '
                     '(artist_name TEXT NOT NULL, '
                     'artwork_name TEXT UNIQUE, '
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


def delete_artwork(artwork_to_delete):
    """deletes specified artwork (must match spelling)"""
    delete_sql = 'DELETE FROM artwork WHERE artwork_name LIKE ? COLLATE NOCASE'

    with sqlite3.connect(db_path) as conn:
        deleted = conn.execute(delete_sql, (artwork_to_delete,))
        deleted_count = deleted.rowcount
    conn.close()
    if deleted_count == 0:
        raise ArtDbError(f'Artwork {artwork_to_delete} not found. ')


def add_artwork(new_artwork):
    """inserts an artwork into the database"""
    insert_sql = 'INSERT INTO artwork (artist_name, artwork_name, price, available) VALUES (?, ?, ?, ?)'
    try:
        with sqlite3.connect(db_path) as conn:
            res = conn.execute(insert_sql, (new_artwork.artist_name, new_artwork.artwork_name, new_artwork.price,
                                            new_artwork.available))
            new_id = res.lastrowid  # Get the ID of the new row in the table
            artist.id = new_id  # Set this artist's ID
        conn.close()
    except sqlite3.IntegrityError as e:
        raise ArtDbError(f'Error - this artwork is already in the database. {new_artwork}') from e


def get_all_artwork():
    """this will return all artwork in db for use in data validation"""
    con = sqlite3.connect(db_path)
    artwork_cursor = con.execute('SELECT * FROM artwork')
    artwork = [Artwork(*row) for row in artwork_cursor.fetchall()]
    con.close()
    return artwork


def update_artwork(sold_artwork):
    """this will update an artwork object's availability to sold"""
    update_sql = 'UPDATE artwork SET available = ? WHERE artwork_name = ?'
    try:
        with sqlite3.connect(db_path) as conn:
            conn.execute(update_sql, (False, sold_artwork))
        conn.close()
    except sqlite3.IntegrityError as e:
        raise ArtDbError(f'Error - this artwork is already marked as sold in the database. {sold_artwork}') from e


def get_all_artwork_from_one_artist(given_artist):
    """this will return all works by a given artist regardless of availability"""
    con = sqlite3.connect(db_path)
    artwork_cursor = con.execute('SELECT * FROM artwork WHERE artist_name LIKE ? COLLATE NOCASE', (given_artist,))
    artwork = [Artwork(*row) for row in artwork_cursor.fetchall()]
    con.close()
    return artwork


def get_available_artwork_from_one_artist(given_artist):
    """this will return all artwork from a given artist that is available"""
    con = sqlite3.connect(db_path)
    artwork_cursor = con.execute('SELECT * FROM artwork WHERE (artist_name LIKE ? COLLATE NOCASE'
                                 ' AND available = true )', (given_artist,))
    artwork = [Artwork(*row) for row in artwork_cursor.fetchall()]
    con.close()
    return artwork


class ArtDbError(Exception):
    """for any db errors"""
    pass
