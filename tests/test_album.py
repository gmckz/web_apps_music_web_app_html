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

"""
We can check if an album object is valid 
and return true if it is or false otherwise
"""
def test_album_valid():
    album1 = Album(1, "", "", "")
    album2 = Album(2, "test title", "2000", "1")
    album3 = Album(3, None, None, None)
    album4 = Album(4, "title", "", "")
    album5 = Album(5, None, "", "3")
    assert album1.is_valid() == False
    assert album2.is_valid() == True
    assert album3.is_valid() == False
    assert album4.is_valid() == False
    assert album5.is_valid() == False

"""
We get an error message when Album#is_valid is False
"""
def test_get_error_message():
    album1 = Album(1, "", "", "")
    assert album1.get_error_message() == "Title can't be blank, Release year can't be blank, Artist ID can't be blank"
    album2 = Album(2, "title", None, "")
    assert album2.get_error_message() == "Release year can't be blank, Artist ID can't be blank"
    album3 = Album(3, "title", "release year", None)
    assert album3.get_error_message() == "Artist ID can't be blank"
