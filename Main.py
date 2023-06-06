from Movie_APP import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv

storage = StorageCsv('Movie_data.csv')
movie_app = MovieApp(storage)
movie_app.run()