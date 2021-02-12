import os
import sqlite3

db = os.path.join('database', 'artwork_catalog.db')


def create_artwork_table():
    """create the artwork table"""
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS artwork '
                     '(artist_name TEXT, '
                     'art_work_name TEXT UNIQUE, '
                     'price INTEGER, '
                     'available BOOLEAN)')
    conn.close()


def create_artists_table():
    """create the artists table"""
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS artists '
                     '(artist_name TEXT, '
                     'email TEXT UNIQUE)')
    conn.close()
