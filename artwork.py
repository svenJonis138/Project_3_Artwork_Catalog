class Artwork:
    def __init__(self, artist_name, art_work_name, price, available):
        self.artist_name = artist_name
        self.art_work_name = art_work_name
        self.price = price
        self.available = available

    def __str__(self):

        return f'{self.artist_name}, {self.art_work_name}, ' \
               f'{self.price}, available = {self.available}.'
