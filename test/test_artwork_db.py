import sqlite3
import unittest
from unittest import TestCase
import os
import artwork_db
from artist import Artist


class TestArtWorkDB(TestCase):
    db = os.path.join('database', 'test_artwork.db')

    def setUp(self):
        # Overwrite the miles db_url with the test database URL
        artwork_db.db_path = self.db

        # drop everything from the DB to always start with an empty database
        conn = sqlite3.connect(self.db)
        conn.execute('DELETE FROM artwork')
        conn.commit()
        conn.close()

    def test_add_artist(self):
        test_name1 = 'Sven Jonis'
        test_email1 = 'sven@fake.org'
        test_artist1 = Artist(test_name1, test_email1)
        artwork_db.add_artist(test_artist1)