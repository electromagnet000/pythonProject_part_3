from Movie_APP import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv

while True:
    try:
        print("who is using this device?")
        user_input = int(input("1 : John.json, 2 : Ashely.csv,  : "))
        if user_input > 2:
            raise ValueError
        break
    except (ValueError, TypeError) as e:
        print(f"user not recognised : {e}")
        continue

if user_input == 1:
    storage = StorageJson('John.json')
    movie_app = MovieApp(storage)
    movie_app.run()

elif user_input == 2:
    storage = StorageCsv('Ashley.csv')
    movie_app = MovieApp(storage)
    movie_app.run()