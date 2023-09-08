import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from lib.album import Album
# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums/index.html', albums=albums )

@app.route('/albums/<id>')
def get_single_album(id):
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    album = album_repository.find(id)
    artist_repository = ArtistRepository(connection)
    artist = artist_repository.find(album.artist_id)
    return render_template('albums/single_album.html', album=album, artist=artist)

@app.route('/artists')
def get_artists():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artists = artist_repository.all()
    return render_template('artists/index.html', artists=artists)

@app.route('/artists/<id>')
def get_single_artist(id):
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artist = artist_repository.find(id)
    return render_template('artists/artist_info.html', artist=artist)

@app.route('/albums/new')
def get_new_albums():
    return render_template('albums/new.html')

@app.route('/albums/new', methods=['POST'])
def create_new_album():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    title = request.form["title"]
    release_year = request.form["release_year"]
    artist_id = request.form["artist_id"]
    album = Album(None, title, release_year, artist_id)
    if album.is_valid() == True:
        album_repository.create(album)
        album_id = _get_album_id_by_title(album.title)
        return redirect(f"/albums/{album_id}")
    else:
        return render_template('albums/new.html', errors=album.get_error_message())
    

def _get_album_id_by_title(title):
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    albums = album_repository.all()
    for album in albums:
        if album.title == title:
            return album.id



# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
