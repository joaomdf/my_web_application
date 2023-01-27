from lib.album import Album

"""
Album constructs with an id, title, release_year and artist_id
"""
def test_album_constructs():
    album = Album(1, 'OK Computer', 1999, 'Radiohead')
    assert album.id == 1
    assert album.title == 'OK Computer'
    assert album.release_year == 1999
    assert album.artist == "Radiohead"

"""
Album can format albums to strings nicely
"""
def test_album_formatting():
    album = Album(1, 'OK Computer', 1999, 'Radiohead')
    assert str(album) == 'Album(1, OK Computer, 1999, Radiohead)'
"""
Album can compare two identical albums
And have them be equal
"""

def test_compare_two_albums():
    album1 = Album(1, 'OK Computer', 1999, 'Radiohead')
    album2 = Album(1, 'OK Computer', 1999, 'Radiohead')
    assert album1 == album2