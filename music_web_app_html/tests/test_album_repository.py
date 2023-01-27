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
        Album(1, "Doolittle", 1989, "Pixies"),
        Album(2,"Surfer Rosa", 1988, "Pixies"),
        Album(3, "Waterloo", 1974, "ABBA"),
        Album(4, "Super Trouper", 1980, "ABBA"),
        Album(5, "Bossanova", 1990, "Pixies"),
        Album(6, "Lover", 2019, "Taylor Swift"),
        Album(7, "Folklore", 2020, "Taylor Swift"),
        Album(8, "I Put a Spell on You", 1965, "Nina Simone"),
        Album(9, "Baltimore", 1978, "Nina Simone"),
        Album(10, "Here Comes the Sun", 1971, "Nina Simone"),
        Album(11, "Fodder on My Wings", 1982, "Nina Simone"),
        Album(12, "Ring Ring", 1973, "ABBA"),
    ]

"""
Given a new album record
when using the create() method to add these records to the album table in the database
are the new records also listed when the all() method is used to gather all the existing records
"""

def test_album_create(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repo = AlbumRepository(db_connection)
    repo.create(Album(None, 'In Rainbows', 2007, "Radiohead"))
    assert repo.all() == [
        Album(1, "Doolittle", 1989, "Pixies"),
        Album(2,"Surfer Rosa", 1988, "Pixies"),
        Album(3, "Waterloo", 1974, "ABBA"),
        Album(4, "Super Trouper", 1980, "ABBA"),
        Album(5, "Bossanova", 1990, "Pixies"),
        Album(6, "Lover", 2019, "Taylor Swift"),
        Album(7, "Folklore", 2020, "Taylor Swift"),
        Album(8, "I Put a Spell on You", 1965, "Nina Simone"),
        Album(9, "Baltimore", 1978, "Nina Simone"),
        Album(10, "Here Comes the Sun", 1971, "Nina Simone"),
        Album(11, "Fodder on My Wings", 1982, "Nina Simone"),
        Album(12, "Ring Ring", 1973, "ABBA"),
        Album(13, "In Rainbows", 2007, "Radiohead")
    ]

def test_find_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    assert repository.find(1) == Album(1, "Doolittle", 1989, "Pixies")