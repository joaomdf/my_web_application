from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository.all()
We get a list of all Album objects reflecting the seed data
"""
def test_album_repository_all(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repo = AlbumRepository(db_connection)
    assert repo.all() == [
        Album(1, "Doolittle", 1989, 1),
        Album(2,"Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, "Bossanova", 1990, 1),
        Album(6, "Lover", 2019, 3),
        Album(7, "Folklore", 2020, 3),
        Album(8, "I Put a Spell on You", 1965, 4),
        Album(9, "Baltimore", 1978, 4),
        Album(10, "Here Comes the Sun", 1971, 4),
        Album(11, "Fodder on My Wings", 1982, 4),
        Album(12, "Ring Ring", 1973, 2)
    ]

"""
Given a new album record
when using the create() method to add these records to the album table in the database
are the new records also listed when the all() method is used to gather all the existing records
"""

def test_album_create(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repo = AlbumRepository(db_connection)
    repo.create(Album(None, 'In Rainbows', 2007, 5))
    assert repo.all() == [
        Album(1, "Doolittle", 1989, 1),
        Album(2,"Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, "Bossanova", 1990, 1),
        Album(6, "Lover", 2019, 3),
        Album(7, "Folklore", 2020, 3),
        Album(8, "I Put a Spell on You", 1965, 4),
        Album(9, "Baltimore", 1978, 4),
        Album(10, "Here Comes the Sun", 1971, 4),
        Album(11, "Fodder on My Wings", 1982, 4),
        Album(12, "Ring Ring", 1973, 2),
        Album(13, "In Rainbows", 2007, 5)
    ]