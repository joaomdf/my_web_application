from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist
from lib.artist_repository import ArtistRepository
from flask import Flask, request
import os

app = Flask(__name__)


@app.route('/albums', methods=['POST'])
def create_album():
    if 'title' not in request.form or 'release_year' not in request.form or 'artist_id' not in request.form:
        return 'Bad request!', 400
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(None, request.form['title'], request.form['release_year'], request.form['artist_id'])
    album = repository.create(album)
    return "", 200

@app.route('/albums', methods=['GET'])
def get_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    final = []
    for album in repository.all():
        final.append(str(album))
    return "\n".join(final)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

