from lib.artist import *
"""
Artists constructs with an id, name, and genre
"""
def test_artist_constructs():
    artist1 = Artist(1, 'Pixies', 'Rock')
    assert artist1.id == 1
    assert artist1.name == 'Pixies'
    assert artist1.genre == 'Rock'



"""
Artist can format artists to strings nicely
"""
def test_artist_format():
    artist1 = Artist(1, 'Pixies', 'Rock')
    assert str(artist1) == "Artist(1, Pixies, Rock)"

"""
Artist can format artists to strings nicely
"""
def test_artist_format_2():
    artist1 = Artist(2, 'ABBA', 'Pop')
    assert str(artist1) == "Artist(2, ABBA, Pop)"


"""
Artist can compare two identical artists
And have them be equal
"""

def test_equality():
    artist1 = Artist(2, 'ABBA', 'Pop')
    artist2 = Artist(2, 'ABBA', 'Pop')
    assert artist1 == artist2