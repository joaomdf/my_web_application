# User story:

Create a new Flask application called music_web_app.

Test-drive a route POST /albums to create a new album:
    # Request:
    POST /albums

    # With body parameters:
    title=Voyage
    release_year=2022
    artist_id=2

    # Expected response (200 OK)
    (No content)

Your test should assert that the new album is present in the list of records returned by GET /albums


SINGLE TABLE DESIGN
-----

# Extract nouns from the user stories or specification

Nouns:

album, title, release year, artist_id

# Infer the Table Name and Columns

Record	Properties
album	title, release year, artist_id

Name of the table: albums
Column names: title, release_year, artist_id

# Decide the column types.

id: SERIAL
title: text
release_year: int
artist_id: int

# Write the SQL.

-- file: music_library.sql

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int
);

5. Create the table.

psql -h 127.0.0.1 music_web_app_db < music_library.sql


ROUTE DESIGN
-----

# Design the Route Signature

POST /albums

With body parameters:
title = string
release_year = integer
artist_id = integer


GET /albums
no query or path parameters
Expected response == 200

# Create Examples as Tests

"""
POST /albums
No return, expected response == 200
"""

"""
GET/ albums
before running POST route
return In rainbows records, response == 200
"""

"""
GET/ albums
after running POST route
return In rainbows and Voyage records, response == 200
"""

"""
POST /albums
Return "Bad Request", expected response == 400
When POST request is made without the necessary body parameters
"""

class layout 
-----
class Album:
    method __init__()
    arg - title, release_year, artist_id

    method __repr__()

    method __eq__()
    arg - other

"""
Album constructs with an id, title, release_year and artist_id
"""

"""
Album can format albums to strings nicely
"""

"""
Album can compare two identical albums
And have them be equal
"""

class AlbumRepository:
    method __init__()
    arg - connection

    method all()

    method create()
    arg - album

"""
When we call AlbumRepository.all()
We get a list of all Album objects reflecting the seed data
"""

"""
Given a new album record
when using the create() method to add these records to the album table in the database
are the new records also listed when the all() method is used to gather all the existing records
"""