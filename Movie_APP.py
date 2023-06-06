class MovieApp:
    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        self._storage.list_movies()

    def _command_update_movie(self):
        title = input("what film would you like to update? : ")
        user_notes = input("Anything to of note about this film? : ")
        self._storage.update_movie(title, user_notes)

    def _command_delete_movie(self):
        title = input("what film would you like to delete? : ")
        self._storage.delete_movie(title)

    def _command_movie_stats(self):
        self._storage.stats()

    def _command_add_movie(self):
        title = input("what film would you like to add? : ")
        user_notes = input("Anything to of note about this film? : ")
        self._storage.add_movie(title, user_notes)

    def _generate_website(self):
        self._storage.generate_website()

    def _command_random_movie(self):
        return self._storage.random_movie()

    def _command_search_movie(self):
        title = input("what film would you like to search for? : ")
        return self._storage.search_movie(title)

    def run(self):

        while True:

            print("Movie App Menu")

            print("----------")

            print("1. List movies")
            print('2. Add movies')
            print('3. Update movies')
            print('4. Delete movies')
            print('5. Stats')
            print("6. Random movie")
            print("7. search for movie")
            print('8. Generate Website')
            print('9. Quit')

            try:
                user_input = int(input("Please chose a number : "))
                if user_input > 9:
                    print("Please input a number between 1-9")
                    continue
            except (TypeError, ValueError) as e:
                print(f"there seems to be a problem : {e}")
                continue

            # lists all products
            if user_input == 1:
                self._command_list_movies()
                continue

            # Adds movie
            elif user_input == 2:
                self._command_add_movie()
                continue

            # Updates movie
            elif user_input == 3:
                self._command_update_movie()
                continue

            # Deletes movie
            elif user_input == 4:
                self._command_delete_movie()
                continue

            # Shows the statistics for movies
            elif user_input == 5:
                self._command_movie_stats()
                continue
            #Gives a random choice of film
            elif user_input == 6:
                print(f"Your random choice is {self._command_random_movie()} ")
                continue
            #Gives a search of films
            elif user_input == 7:
                print(f"{self._command_search_movie()}")
                continue

            # Generates a website
            elif user_input == 8:
                self._generate_website()
                continue

                # exits the program
            elif user_input == 9:
                print(
                    "--------- Program Terminated ---------" "\n" "\n" "         Thank you take care          " "\n" "\n" "--------------------------------------")
                exit()
