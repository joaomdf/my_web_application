# User story

Add a route GET /artists/<id> which returns an HTML page showing details for a single artist.
Add a route GET /artists which returns an HTML page with the list of artists. This page should contain a link for each artist listed, linking to /artists/<id> where <id> needs to be the corresponding artist id.

# app.py changes
    route GET /artists/<id>
        returns html page with details for single artist

    route GET /artists
        returns html page with list of all artists
        with link for artist listed linking to /artists/<id>
        <id> is the artist id

# tests

"""
Check that route GET /artists/2 returns HTML page with records for artist ABBA
"""

"""
Check that route GET /artists returns HTML page with list of all artists
"""

"""
Check that route GET /artists can connect to /artists/2 via the ABBA record in list
and that subsequently GET /artists/2 returns HTML page with records for artist ABBA
"""
