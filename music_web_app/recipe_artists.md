# User story:

Test-drive a route GET /artists, which returns the list of artists:

Request:
GET /artists

Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone
Test-drive a route POST /artists, which creates a new artist in the database. Your test should verify the new artist is returned in the response of GET /artists.

Request:
POST /artists

With body parameters:
name=Wild nothing
genre=Indie

Expected response (200 OK)
(No content)

Then subsequent request:
GET /artists

Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing

SINGLE TABLE DESIGN
-----

# Extract nouns from the user stories or specification

Nouns:

artist, name, genre

# Infer the Table Name and Columns

Record	Properties
album	name, genre

Name of the table: artists
Column names: name, genre

# Decide the column types.

id: SERIAL
name: text
genre: text

# Write the SQL.

-- file: music_library.sql

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name text,
    genre text,
);

5. Create the table.

psql -h 127.0.0.1 music_web_app_db < music_library.sql


ROUTE DESIGN
-----

# Design the Route Signature

GET /artists
no query or path parameters
Expected response == 200


POST /artists
With body parameters:
name = string
genre = string


# Create Examples as Tests

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

class layout 
-----
class Artist:
    method __init__()
    arg - name, genre

    method __repr__()

    method __eq__()
    arg - other

"""
Artists constructs with an id, name, and genre
"""

"""
Artist can format artists to strings nicely
"""

"""
Artist can compare two identical artists
And have them be equal
"""

class ArtistRepository:
    method __init__()
    arg - connection

    method all()

    method create()
    arg - album

"""
When we call ArtistRepository.all()
We get a list of all Artist objects reflecting the seed data
"""

"""
Given a new artist record
when using create() to add these records to the artist table in the database
the new records are also listed when the all() method is used
"""