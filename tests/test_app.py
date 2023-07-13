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
"""
When we call GET /albums
we get a list of album titles and release years in html format
"""
def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed('seeds/record_store.sql')
    page.goto(f"http://{test_web_address}/albums")
    list_tag = page.locator("li")
    expect(list_tag).to_have_text([
        "Doolittle",
        "Surfer Rosa"
    ])

"""
When we call GET /albums/<id> 
we get the title, release year and artist for that album the expected format
"""
def test_get_single_album(page, test_web_address, db_connection):
    db_connection.seed('seeds/record_store.sql')
    page.goto(f"http://{test_web_address}/albums/1")
    h1_tag = page.locator("h1")
    paragraph_tag = page.locator("p")
    expect(h1_tag).to_have_text("Doolittle")
    expect(paragraph_tag).to_have_text("Release year: 1989\nArtist: Pixies")

"""
The page returned by GET /albums contains a link for each album listed
it should link to /albums/<id> where <id> is the corresponding albums id
that page should show information about the album
"""
def test_album_link_goes_to_page(page, test_web_address, db_connection):
    db_connection.seed('seeds/record_store.sql')
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Surfer Rosa'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Surfer Rosa")


"""
When we call GET /artists
we get a list of artist links
"""
def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed('seeds/record_store.sql')
    page.goto(f"http://{test_web_address}/artists")
    h1_tag = page.locator("h1")
    list_tag = page.locator("li")
    expect(h1_tag).to_have_text("Artists")
    expect(list_tag).to_have_text([
        "Pixies",
        "ABBA",
        "Taylor Swift",
        "Nina Simone"
    ])

# Add a route GET /artists/<id> which returns an HTML page showing details
#  for a single artist.
"""
When we call GET /artists/<id>
where <id> is the artist id 
we get a html page with the details of a single artist
"""
def test_get_artist_by_id(page, test_web_address, db_connection):
    db_connection.seed('seeds/record_store.sql')
    page.goto(f"http://{test_web_address}/artists/2")
    h1_tag = page.locator("h1")
    paragraph_tag = page.locator("p")
    expect(h1_tag).to_have_text("ABBA")
    expect(paragraph_tag).to_have_text("Genre: Pop")


# Add a route GET /artists which returns an HTML page with the list of artists. 
# This page should contain a link for each artist listed, linking to /artists/<id>
#  where <id> needs to be the corresponding artist id.
def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed('seeds/record_store.sql')
    page.goto(f"http://{test_web_address}/artists")
    h1_tag = page.locator("h1")
    list_tag = page.locator("li")
    expect(h1_tag).to_have_text("Artists")
    expect(list_tag).to_have_text([
        "Pixies",
        "ABBA",
        "Taylor Swift",
        "Nina Simone"
    ])

def test_artist_link_goes_to_page(page, test_web_address, db_connection):
    db_connection.seed('seeds/record_store.sql')
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=ABBA")
    paragraph_tag = page.locator("p")
    expect(paragraph_tag).to_have_text("Genre: Pop")