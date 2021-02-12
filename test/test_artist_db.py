import sqlite3
import unittest
from unittest import TestCase
import os

from artist import Artist
import config
config.db_path = os.path.join('database', 'test_artwork_catalog.db')
import artwork_db


class TestArtWorkDB(TestCase):
    # config.db_path = os.path.join('database', 'test_artwork_catalog.db')
    # db_path = config.db_path
    #
    # def setUp(self):
    #     # Overwrite the miles db_url with the test database URL
    #     # artwork_db.db_path = self.db_path
    #
    #     # drop everything from the DB to always start with an empty database
    #     conn = sqlite3.connect(self.db_path)
    #     conn.execute('DELETE FROM artwork')
    #     conn.commit()
    #     conn.close()

    def test_add_artist(self):
        print('database being used is ' + config.db_path)

        test_name1 = 'Sven Jonis'
        test_email1 = 'sven@fake.org'
        test_artist1 = Artist(test_name1, test_email1)
        print(test_artist1)
        artwork_db.add_artist(str(test_artist1))

