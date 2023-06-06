import json
import requests
import random
from Istorage import IStorage


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.filepath = file_path

    def list_movies(self):
        with open(self.filepath, "r") as test_file:
            movie_data = json.load(test_file)
            movies_len = len(movie_data)
            print(f"total movies : {movies_len}")
            for movie in movie_data:
                print(movie["Title"])

    def add_movie(self, title, user_notes):
        """
            Creates a movie for the movie database using an api.
            Loads the information from the Api, adds the movie to the data,
            and saves the data in a new file.
            """
        with open(self.filepath, "r") as file_obj:
            movies_data = json.load(file_obj)

            API_KEY = "ae79a6f6"
            # sends a get request to gather specific information from Movies API
            api_url = "http://www.omdbapi.com/?t={}&apikey={}".format(title, API_KEY)
            response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
            # if the response status is 200 then it proceeds with the request
            if response.status_code == requests.codes.ok:
                # creates a variable for the text repsonse

                fetched_data = response.json()

                # creates an empty dict
                requested_data = {}
                # creates the parameters we need to get
                requested_parameters = ['Title', 'Year', 'imdbRating', 'Poster', 'imdbID']

                # iterates through the keys to get the correct parameters and stores them in requested_data
                for key, value in fetched_data.items():
                    if key in requested_parameters:
                        requested_data[key] = value

                # checks if anything was acutally added into the requested data dict
                if not bool(requested_data):
                    print(f"Movie {title} not found in API")
                    return False

                requested_data["Notes"] = user_notes

                # creats a new file with all the added information
                with open(self.filepath, "w") as new_file:
                    movies_data.append(requested_data)
                    json.dump(movies_data, new_file)
                    print(f"Movie {title} successfully added")

    def delete_movie(self, title):

        with open(self.filepath, "r") as data:
            movie_data = json.load(data)

            nothing_found = 1

            for movie in range(len(movie_data)):
                if movie_data[movie]["Title"].upper() == title.upper():
                    del movie_data[movie]
                    print(f"{title} deleted from database")
                    nothing_found = 2
                    break

            if nothing_found == 1:
                print(f"{title} : was not found in the database please try again")

                # creates a new file based on the appended data
            with open(self.filepath, "w") as new_file:
                json.dump(movie_data, new_file)

    def update_movie(self, title, notes):
        with open(self.filepath, "r") as file_obj:
            movie_data = json.load(file_obj)

            # checks the movie in the dict and changes the rating
            for movie in range(len(movie_data)):
                if title in movie_data[movie]['Title']:
                    movie_data[movie]["Notes"] = notes

            with open(self.filepath, "w") as new_file:
                json.dump(movie_data, new_file)

    def stats(self):
        """
        gathers information from the movie database.
        Loads the information from the JSON file, shows the movie
        """
        with open(self.filepath, "r") as file_obj:

            movies_data = json.load(file_obj)

            # creates an empty rating list
            movie_ratings = []

            for movie in range(len(movies_data)):
                movie_ratings.append(float(movies_data[movie]["imdbRating"]))

            avg_rating = sum(movie_ratings) / len(movie_ratings)

            # helps the median formula
            n = 0 if len(movies_data) % 2 == 0 else 1
            # calculates the median
            median = (len(movies_data) + n) / 2

            # calculates the top value
            top_value = 0
            for values in movie_ratings:
                if top_value <= values:
                    top_value = values

            # compiles all the top values into a list
            top_values = []

            for movie in range(len(movies_data)):
                if top_value == float(movies_data[movie]["imdbRating"]):
                    top_values.append(movies_data[movie])

            # calculates all the bottom values
            bottom_value = 10
            for values in movie_ratings:
                if bottom_value >= values:
                    bottom_value = values

            # complies all the bottom values into a list
            bottom_values = []
            for movie in range(len(movies_data)):
                if bottom_value == float(movies_data[movie]["imdbRating"]):
                    bottom_values.append(movies_data[movie])

            # prints stats
            print(f"The average rating is : {avg_rating}")
            print(f"The median is : {median}")
            # prints multiple movies of same value:
            print("Top rated movie/s")
            for movie in range(len(top_values)):
                print(f"Title : {top_values[movie]['Title']}, Rating : {top_values[movie]['imdbRating']}")
            print("Bottom rated movie/s")
            for movie in range(len(top_values)):
                print(f"Title : {bottom_values[movie]['Title']}, Rating : {bottom_values[movie]['imdbRating']}")

    def movie_serialisation(self):
        with open(self.filepath, "r") as file_obj:
            movies_data = json.load(file_obj)

            output = ""

            for movie in movies_data:
                # try:
                output += '<li>\n'
                output += '<div class="movie">\n'
                output += f'<a href="https://www.imdb.com/title/{movie["imdbID"]}"><img class="movie-poster" alt="movie-poster" title="{movie["Notes"]}" \n src="{movie["Poster"]}"/></a>\n'
                output += f'<div class="movie-title">{movie["Title"]}</div>\n'
                output += f'<div class="movie-year">{movie["Year"]}</div>\n'
                output += f'<div class="movie-rating">{movie["imdbRating"]}</div>\n'
                output += '</div>\n'
                output += '</li>\n'

            return output

    def generate_website(self):

        file_path_split = self.filepath.split(".")
        name_file_path = file_path_split[0]

        website_title = "My Movie Database"
        website_owner = f"{name_file_path}_database_showcase.html"

        open_file = open("index_html.html", "r")
        read_file = open_file.read()

        updated_title = read_file.replace("__TEMPLATE_TITLE__", website_title)

        if self.movie_serialisation():
            updated_template = updated_title.replace("__TEMPLATE_MOVIE_GRID__", self.movie_serialisation())
        else:
            updated_template = read_file.replace("__TEMPLATE_MOVIE_GRID__", f"<h2>No movie data found</h2>")

        with open(website_owner, "w") as file_html:
            file_html.write(updated_template)
            print(f"successfully generate website : {website_title}")



    def random_movie(self):
        with open(self.filepath, "r") as file_obj:
            movies_data = json.load(file_obj)

            random_choice = random.choice(movies_data)
            return f": {random_choice['Title']}, {random_choice['imdbRating']}"

    def search_movie(self, title):

        with open(self.filepath, "r") as file_obj:
            movies_data = json.load(file_obj)

            for movie in movies_data:
                if title.lower() in movie['Title'].lower():
                    print("Movie found !")
                    print()

                    return f"Title : {movie['Title']}, Rating : {movie['imdbRating']}, Year of realease : {movie['Year']}"

            return f"Movie : {title} not found in database"
