import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.artist import Artist
from lib.artist_repository import ArtistRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection()
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums/index.html', albums=albums)

    # GET /albums/<id>
@app.route('/albums/<int:id>', methods=['GET'])
def get_album(id):
    connection = get_flask_database_connection()
    repository = AlbumRepository(connection)
    album = repository.find(id)
    return render_template('albums/show.html', album=album)

@app.route('/artists/<id>', methods=['GET'])
def get_artist(id):
    connection = get_flask_database_connection()
    repository = ArtistRepository(connection)
    album_repository = AlbumRepository(connection)
    artist = repository.find(id)
    albums = album_repository.find_for_artist(artist.name)
    return render_template('artists/show.html', artist=artist, albums=albums)

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection()
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template('artists/index.html', artists=artists)

@app.route('/albums/new', methods=['GET'])
def get_new_album():
    return render_template('albums/new.html')

@app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection()
    repository = AlbumRepository(connection)
    title = request.form['title']
    release_year = request.form['release_year']
    artist = request.form['artist']
    album = Album(None, title, release_year, artist)
    if not album.is_valid():
        return render_template('albums/new.html', album=album, errors=album.generate_errors()), 400
    album = repository.create(album)
    return redirect(f"/albums/{album.id}")

@app.route('/artists/new', methods=['GET'])
def get_new_artist():
    return render_template('artists/new.html')

@app.route('/artists', methods=['POST'])
def create_artist():
    connection = get_flask_database_connection()
    repository = ArtistRepository(connection)
    name = request.form['name']
    genre = request.form['genre']
    artist = Artist(None, name, genre)
    if not artist.is_valid():
        return render_template('artists/new.html', artist=artist, errors=artist.generate_errors()), 400
    artist = repository.create(artist)
    return redirect(f"/artists/{artist.id}")

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
