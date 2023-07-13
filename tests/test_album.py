from lib.album import Album

"""
album constructs with an id, title, release year and artist_id
"""
def test_album_constructs():
    album = Album(1, "Test title", "Test release_year", "test artist_id")
    assert album.id == 1
    assert album.title == "Test title"
    assert album.release_year == "Test release_year"
    assert album.artist_id == "test artist_id"

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1, "Test title", "Test release_year", "test artist_id")
    assert str(album) == "Album(1, Test title, Test release_year, test artist_id)"
    # Try commenting out the `__repr__` method in lib/album.py
    # And see what happens when you run this test again.

"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1, "Test title", "Test release_year", "test artist_id")
    album2 = Album(1, "Test title", "Test release_year", "test artist_id")
    assert album1 == album2
    # Try commenting out the `__eq__` method in lib/album.py
    # And see what happens when you run this test again.
