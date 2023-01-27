from lib.album import Album

class AlbumRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * FROM albums')
        albums = []
        for row in rows:
            item = Album(row['id'], row['title'], row['release_year'], row['artist'])
            albums.append(item)
        return albums

    def create(self,album):
        rows = self.connection.execute('INSERT INTO albums ("title", "release_year", "artist") VALUES (%s, %s, %s) RETURNING id', [album.title, album.release_year, album.artist])
        row = rows[0]
        album.id = row['id']
        return album

    def find(self,album_id):
        rows = self.connection.execute('SELECT * FROM albums WHERE id = %s', [album_id])
        row = rows[0]
        return Album(row['id'], row['title'], row['release_year'], row['artist'])

    def find_for_artist(self,artist_name):
        rows = self.connection.execute('SELECT * FROM albums WHERE artist = %s', [artist_name])
        albums = []
        for row in rows:
            item = Album(row['id'], row['title'], row['release_year'], row['artist'])
            albums.append(item)
        return albums