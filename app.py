from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

class Application():
    def __init__(self):    
        # Connect to the database
        self._connection = DatabaseConnection()
        self._connection.connect()
        # Seed with some seed data
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        print("Welcome to the music library manager!")
        print("")
        print("What would yo u like to do?")
        print("1 - List all albums")
        print("2 - List all artists")
        print("")
        value = input("Enter your value:\n")
        value = int(value)


        artist_repository = ArtistRepository(self._connection)
        artists = artist_repository.all()
        album_repository = AlbumRepository(self._connection)
        albums = album_repository.all()
        
        if value == 2:
            print("")
            print("Here is the list of artists:")
            for artist in artists:
                print(artist)
        elif value == 1:
            print("")
            print("Here is the list of albums:")
            for album in albums:
                print(album)


if __name__ == '__main__':
    app = Application()
    app.run()