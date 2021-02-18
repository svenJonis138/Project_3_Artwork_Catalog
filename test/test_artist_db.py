import sqlite3
import unittest

from unittest import TestCase
import os

from artist import Artist

import config

db_path = os.path.join('test_database', 'test_artwork_catalog.db')
config.db_path = db_path
import artwork_db


class TestArtWorkDB(TestCase):

    def setUp(self):
        artwork_db.create_tables()
        conn = sqlite3.connect(db_path)
        conn.execute('DELETE FROM artists')
        conn.commit()
        conn.close()

    def test_get_all_artists_empty_db(self):
        artwork_db.get_all_artists()
        self.assertRaises(artwork_db.ArtDbError)

    def test_add_artist(self):
        a1 = Artist('Sven Jonis', 'sven@fake.com')
        artwork_db.add_artist(a1)

    def test_get_all_artists_one_artist(self):
        a1 = Artist('Sven Jonis', 'sven@fake.com')
        artwork_db.add_artist(a1)
        counter = 0
        result = artwork_db.get_all_artists()
        for artist in result:
            print(artist)
            counter += 1
        self.assertEquals(1, counter)

    def test_artist_already_exists(self):
        a1 = Artist('Sven Jonis', 'sven@fake.com')
        artwork_db.add_artist(a1)
        self.assertRaises(artwork_db.ArtDbError)

    def test_artist_no_name(self):
        a1 = Artist('', 'sven@fake.com')
        artwork_db.add_artist(a1)
        self.assertRaises(artwork_db.ArtDbError)

    def test_delete_artist_in_db(self):
        a1 = Artist('', 'sven@fake.com')
        artwork_db.add_artist(a1)
        artwork_db.delete_artist(a1)

    def test_delete_artist_not_in_db(self):
        a1 = Artist('Captain NoFun', 'thecap@nofun.com')
        artwork_db.delete_artist(a1)
        self.assertRaises(artwork_db.ArtDbError)


if __name__ == '__main__':
    unittest.main()
