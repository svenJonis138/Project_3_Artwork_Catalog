class Artist:
    def __init__(self, artist_name, email, id=None):
        self.artist_name = artist_name
        self.email = email
        self.id = id

    def __str__(self):
        return f'{self.artist_name}, {self.email}'
