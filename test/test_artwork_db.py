import sqlite3
import unittest

from unittest import TestCase
import os

from artist import Artist
from artwork import Artwork
import config

db_path = os.path.join('test_database', 'test_artwork_catalog.db')
config.db_path = db_path
import artwork_db


class TestArtWorkDB(TestCase):

    def setUp(self):
        artwork_db.create_tables()
        conn = sqlite3.connect(db_path)
        conn.execute('DELETE FROM artists')
        conn.execute('DELETE FROM artwork')
        conn.commit()
        conn.close()

    def test_get_all_artists_empty_db(self):
        results = artwork_db.get_all_artists()
        self.assertEquals(0, len(results))

    def test_add_artist(self):
        old_results = artwork_db.get_all_artists()
        a1 = Artist('Sven Jonis', 'sven@fake.com')
        artwork_db.add_artist(a1)
        results = artwork_db.get_all_artists()
        self.assertEquals(len(old_results) + 1, len(results))

    def test_get_all_artists_one_artist(self):
        a1 = Artist('Sven Jonis', 'sven@fake.com')
        artwork_db.add_artist(a1)
        result = artwork_db.get_all_artists()
        self.assertEquals(1, len(result))

    def test_artist_already_exists(self):
        a1 = Artist('Sven Jonis', 'sven@fake.com')
        artwork_db.add_artist(a1)
        a2 = Artist('Sven Jonis', 'sven@fake.com')
        with self.assertRaises(artwork_db.ArtDbError):
            artwork_db.add_artist(a2)

    def test_artist_no_name(self):
        a1 = Artist(None, 'sven@fake.com')
        with self.assertRaises(artwork_db.ArtDbError):
            artwork_db.add_artist(a1)

    def test_delete_artwork_in_db(self):
        a1 = Artwork('sven', 'sven nude', 8311, True)
        artwork_db.add_artwork(a1)
        old_results = artwork_db.get_all_artwork()
        artwork_db.delete_artwork(a1.artwork_name)
        results = artwork_db.get_all_artists()
        self.assertEquals(len(old_results) - 1, len(results))

    def test_delete_artwork_not_in_db(self):
        a1 = Artwork('Captain NoFun', 'the cap', 1138, True)
        with self.assertRaises(artwork_db.ArtDbError):
            artwork_db.delete_artwork(a1.artwork_name)

    def test_get_all_artwork_empty_db(self):
        results = artwork_db.get_all_artists()
        self.assertEquals(0, len(results))

    def test_add_new_artwork(self):
        old_results = len(artwork_db.get_all_artwork())
        aw1 = Artwork('Banksy', 'Mcdonald\'s is stealing your children', 138, True)
        artwork_db.add_artwork(aw1)
        results = len(artwork_db.get_all_artwork())
        self.assertEquals(old_results + 1, results)

    def test_get_all_artwork_one_artwork_in_db(self):
        aw1 = Artwork('Art Dood', 'Overpriced still life', 1138, True)
        artwork_db.add_artwork(aw1)
        result = artwork_db.get_all_artwork()
        self.assertEquals(1, len(result))

    def test_get_all_work_sold_and_unsold(self):

        aw1 = Artwork('Banksy', 'Rats', 138831, True)
        aw2 = Artwork('Banksy', 'Rats2', 138831, False)
        aw3 = Artwork('Banksy', 'Rats3', 138831, True)
        artwork_db.add_artwork(aw1)
        artwork_db.add_artwork(aw2)
        artwork_db.add_artwork(aw3)
        total_arts = artwork_db.get_all_artwork_from_one_artist('Banksy')
        self.assertEquals(3, len(total_arts))

    def test_get_all_available_art(self):
        aw1 = Artwork('Baanksy', 'Rats1', 138831, True)
        aw2 = Artwork('Baanksy', 'Rats21', 138831, False)
        aw3 = Artwork('Baanksy', 'Rats31', 138831, True)
        artwork_db.add_artwork(aw1)
        artwork_db.add_artwork(aw2)
        artwork_db.add_artwork(aw3)
        total_arts = artwork_db.get_available_artwork_from_one_artist('Baanksy')
        self.assertEquals(2, len(total_arts))


if __name__ == '__main__':
    unittest.main()
