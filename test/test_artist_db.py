import sqlite3
import unittest

from unittest import TestCase
import os

from artist import Artist
# from config import db_path
import config
db_path = os.path.join('database', 'test_artwork_catalog.db')
config.db_path = db_path
import artwork_db


class TestArtWorkDB(TestCase):

    def setUp(self):
        artwork_db.create_tables()
        conn = sqlite3.connect(db_path)
        conn.execute('DELETE FROM artists')
        conn.commit()
        conn.close()

    def test_add_artist(self):
        print('database being used is ' + db_path)

        test_name1 = 'Sven Jonis'
        test_email1 = 'sven@fake.org'
        test_artist1 = Artist(test_name1, test_email1)
        print(test_artist1)
        artwork_db.add_artist(test_artist1)


if __name__ == '__main__':
    unittest.main()
