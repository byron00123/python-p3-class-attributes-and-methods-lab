class Song:
    count = 0
    genres = []
    artists = []
    artist_count = {}  # Add artist_count attribute

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_artist_count()  # Add method to update artist_count

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_artist_count(self):
        if self.artist not in Song.artist_count:
            Song.artist_count[self.artist] = 1
        else:
            Song.artist_count[self.artist] += 1
