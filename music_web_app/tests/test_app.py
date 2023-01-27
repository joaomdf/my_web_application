"""
GET/ albums
before running POST route
return In rainbows records, response == 200
"""
def test_get_album_before_post(web_client, db_connection):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Album(1, Doolittle, 1989, 1)\nAlbum(2, Surfer Rosa, 1988, 1)\nAlbum(3, Waterloo, 1974, 2)\nAlbum(4, Super Trouper, 1980, 2)\nAlbum(5, Bossanova, 1990, 1)\nAlbum(6, Lover, 2019, 3)\nAlbum(7, Folklore, 2020, 3)\nAlbum(8, I Put a Spell on You, 1965, 4)\nAlbum(9, Baltimore, 1978, 4)\nAlbum(10, Here Comes the Sun, 1971, 4)\nAlbum(11, Fodder on My Wings, 1982, 4)\nAlbum(12, Ring Ring, 1973, 2)'

"""
POST /albums
No return, expected response == 200

AND 

GET/ albums
after running POST route
return In rainbows and Voyage records, response == 200
"""
def test_post_album_and_check_new_get(web_client, db_connection):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.post('/albums', data={"title": "Voyage", "release_year": 2022, "artist_id": 2})
    assert response.status_code == 200
    response_two = web_client.get('/albums')
    assert response_two.status_code == 200
    assert response_two.data.decode('utf-8') == 'Album(1, Doolittle, 1989, 1)\nAlbum(2, Surfer Rosa, 1988, 1)\nAlbum(3, Waterloo, 1974, 2)\nAlbum(4, Super Trouper, 1980, 2)\nAlbum(5, Bossanova, 1990, 1)\nAlbum(6, Lover, 2019, 3)\nAlbum(7, Folklore, 2020, 3)\nAlbum(8, I Put a Spell on You, 1965, 4)\nAlbum(9, Baltimore, 1978, 4)\nAlbum(10, Here Comes the Sun, 1971, 4)\nAlbum(11, Fodder on My Wings, 1982, 4)\nAlbum(12, Ring Ring, 1973, 2)\nAlbum(13, Voyage, 2022, 2)'

"""
raises 400 error if body parameters are missing
"""
def test_post_album_no_parameters(web_client, db_connection):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.post('/albums')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'Bad request!'


"""
GET/ artists
before running POST route
return complete list of albums, response == 200
"""

"""
POST /artists
No return, expected response == 200
adds new artist with name: Wild Nothing and genre: Indie
"""

"""
GET/ artists
after running POST route
return complete list of artists including new artist Wild Nothing
response == 200
"""

"""
POST /artists
Return "Bad Request", expected response == 400
When POST request is made without the necessary body parameters, name/genre
"""