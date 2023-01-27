from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
def test_get_emoji(page, test_web_address): # Note new parameters
    # We load a virtual browser and navigate to the /emoji page
    page.goto(f"http://{test_web_address}/emoji")

    # We look at the <strong> tag
    strong_tag = page.locator("strong")

    # We assert that it has the text ":)"
    expect(strong_tag).to_have_text(":)")

# === End Example Code ===

def test_get_albums(db_connection, page, test_web_address):
    # We seed our database with the book store seed file
    db_connection.seed("seeds/music_library.sql")

    # We load a virtual browser and navigate to the /books page
    page.goto(f"http://{test_web_address}/albums")

    # We look at all the <li> tags
    list_titles = page.locator("h2")
    list_release_date = page.locator("p")
    # We assert that it has the books in it
    expect(list_titles).to_have_text([
        "Doolittle",
        "Surfer Rosa",
        "Waterloo",
        "Super Trouper",
        "Bossanova",
        "Lover",
        "Folklore",
        "I Put a Spell on You",
        "Baltimore",
        "Here Comes the Sun",
        "Fodder on My Wings",
        "Ring Ring"])
    expect(list_release_date).to_have_text([
        "Release year: 1989",
        "Release year: 1988",
        "Release year: 1974",
        "Release year: 1980",
        "Release year: 1990",
        "Release year: 2019",
        "Release year: 2020",
        "Release year: 1965",
        "Release year: 1978",
        "Release year: 1971",
        "Release year: 1982",
        "Release year: 1973"
    ])

def test_get_album(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/2")
    title_element = page.locator("h1")
    expect(title_element).to_have_text("Surfer Rosa")
    release_year_element = page.locator(".t-release_year")
    expect(release_year_element).to_have_text("Release year: 1988")
    artist_element = page.locator(".t-artist")
    expect(artist_element).to_have_text("Artist: Pixies")

def test_get_album_link(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Surfer Rosa'")
    title_element = page.locator("h1")
    expect(title_element).to_have_text("Surfer Rosa")
    release_year_element = page.locator(".t-release_year")
    expect(release_year_element).to_have_text("Release year: 1988")
    artist_element = page.locator(".t-artist")
    expect(artist_element).to_have_text("Artist: Pixies")

def test_return_main_album_index(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/2")
    page.click("text='Back to all albums'")
    list_titles = page.locator("h2")
    list_release_date = page.locator("p")
    # We assert that it has the books in it
    expect(list_titles).to_have_text([
        "Doolittle",
        "Surfer Rosa",
        "Waterloo",
        "Super Trouper",
        "Bossanova",
        "Lover",
        "Folklore",
        "I Put a Spell on You",
        "Baltimore",
        "Here Comes the Sun",
        "Fodder on My Wings",
        "Ring Ring"])
    expect(list_release_date).to_have_text([
        "Release year: 1989",
        "Release year: 1988",
        "Release year: 1974",
        "Release year: 1980",
        "Release year: 1990",
        "Release year: 2019",
        "Release year: 2020",
        "Release year: 1965",
        "Release year: 1978",
        "Release year: 1971",
        "Release year: 1982",
        "Release year: 1973"
    ])

"""
Check that route GET /artists/2 returns HTML page with records for artist ABBA
"""

def test_get_artist(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/2")
    artist_name = page.locator("h1")
    expect(artist_name).to_have_text("ABBA")
    genre_tag = page.locator(".t-genre")
    expect(genre_tag).to_have_text("Genre: Pop")

"""
Check that route GET /artists returns HTML page with list of all artists
"""

def test_get_list_artist(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    list_artists = page.locator("li")
    expect(list_artists).to_have_text([
        'Pixies',
        'ABBA',
        'Taylor Swift',
        'Nina Simone',
        'Radiohead'
    ])

"""
Check that route GET /artists can connect to /artists/2 via the ABBA record in list
and that subsequently GET /artists/2 returns HTML page with records for artist ABBA
"""
def test_get_list_artist_from_id_page(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Nina Simone'")
    artist_name = page.locator("h1")
    expect(artist_name).to_have_text("Nina Simone")
    genre_tag = page.locator(".t-genre")
    expect(genre_tag).to_have_text("Genre: Jazz")

def test_get_index_page_from_id_page(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists/4")
    page.click("text='Back to all artists'")
    list_artists = page.locator("li")
    expect(list_artists).to_have_text([
        'Pixies',
        'ABBA',
        'Taylor Swift',
        'Nina Simone',
        'Radiohead'
    ])

"""
When we create a new album
We see it in the albums index
"""
def test_create_album(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add a new album")
    page.fill("input[name='title']", "The Sun's Tirade")
    page.fill("input[name='release_year']", "2016")
    page.fill("input[name='artist']", "Isaiah Rashad")
    page.click("text=Add album")
    title_element = page.locator("h1")
    release_year_element = page.locator(".t-release_year")
    artist_element = page.locator(".t-artist")
    expect(title_element).to_have_text("The Sun's Tirade")
    expect(release_year_element).to_have_text("Release year: 2016")
    expect(artist_element).to_have_text("Artist: Isaiah Rashad")

"""
If we create a new album without a title, release year or artist
We see an error message
"""
def test_create_album_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add a new album")
    page.click("text=Add Album")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Title can't be blank, Release year can't be blank, Artist can't be blank")



"""
When we create a new artist
We see it in the artists index
"""
def test_create_artist(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Add a new artist")
    page.fill("input[name='name']", "Father John Misty")
    page.fill("input[name='genre']", "Indie")
    page.click("text=Add Artist")
    artist_name = page.locator("h1")
    expect(artist_name).to_have_text("Father John Misty")
    genre_tag = page.locator(".t-genre")
    expect(genre_tag).to_have_text("Genre: Indie")

"""
If we create a new artist without a name or genre
We see an error message
"""
def test_create_artist_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Add a new artist")
    page.click("text=Add Artist")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Name can't be blank, Genre can't be blank")