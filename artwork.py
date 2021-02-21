"""Artwork class"""


class Artwork:
    def __init__(self, artist_name, artwork_name, price, available):
        self.artist_name = artist_name
        self.artwork_name = artwork_name
        self.price = price
        self.available = available

    def __str__(self):

        return f'{self.artist_name}, {self.artwork_name}, ' \
               f'{self.price}, available = {self.available}.'
