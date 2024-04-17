###############################################################################
# Done: 1. (3 pts)
#
#   For this module, we are going to create a basic program to handle movie
#   times at a movie theater. For our purposes, a movie is going to be defined
#   as a dictionary with these keys:
#       - title
#       - duration
#       - start_time
#       - theater_num
#       - num_of_tickets
#
#   For this __todo__, write a function called show_movies() that takes one
#   argument:
#       - movies     <-- list of dictionaries (movies)
#
#   First, it should print the line:
#       Movies:
#   
#   Then, This function should loop through the list of movies and, for each
#   movie, print information about the movie like so:
#
#       Title: Braveheart
#       Duration: 170 minutes
#       Start Time: 2:15 PM
#       Theater: 8
#       Tickets Available: 20
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def show_movies(movies):
    print("\nMovies:")
    for movie in movies:
        print(f"Title: {movie["title"]}")
        print(f"Duration: {movie["duration"]}")
        print(f"Start Time: {movie["start_time"]}")
        print(f"Theater: {movie["theater_num"]}")
        print(f"Tickets Available: {movie["num_of_tickets"]}")

###############################################################################
# Done: 2. (3 pts)
#
#   For this _todo_, write a function called get_ticket() that takes one
#   parameter:
#       - movie      <-- dictionary (movie)
#
#   This function should behave like this:
#
#       - If the movie has tickets available (that is, it is greater than 0), it
#         should set the value of num_of_tickets to one less than what it was
#         before and print:
#           "Success! You know have a ticket for <MOVIE TITLE HERE>!"
#       - If the movie's num_of_tickets value is not greater than 0 (that is,
#         it is there are not tickets available), it should print:
#           "There are currently no tickets available for that movie."
#
#   HINT: Remember that you will need to convert the number of tickets to an
#   integer
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def get_ticket(movie):
    num_of_tickets = 0
    if movie["num_of_tickets"] > 0:
        movie["num_of_tickets"] = movie["num_of_tickets"] - 1
        print(f"Success! You now have a ticket for {movie["title"]}!")
    else:
        print("There are currently no tickets available for that movie.")

###############################################################################
# Done: 3. (9 pts)
#
#   Now, let's create our movie showtimes system.
#
#   For this _todo_, write a function called main() that will start things off.
#   This function should do these things in order:
#
#       1. Print a welcome message to the user
#       2. Continually ask the user for information about movies (title,
#          duration (in minutes), start time, theater number, tickets
#          available). If the user types "end" for any of the fields, the
#          program should stop asking for movie information. (HINT: I used a
#          while loop)
#       3. For each movie, create a dictionary to hold the movie's information.
#          The dictionary should have all of this information: title, duration,
#          start_time, theater_num, num_of_tickets.
#       4. It should keep track of all the movies in a list.
#       5. Once the user stops entering movie information, the program should
#          use the show_movies() function to print the list of movies and their
#          information.
#       6. Then, the program should continually prompt the user like so:
#           "Which movie would you like to buy a ticket for? "
#       7. If the user types a movie title that is in the list of movies, it
#          should get a ticket for the user (using the get_ticket() function)
#          and reprint the list of movies with the updated information. It
#          should keep asking the user for more movies to get tickets for until
#          they type "end".
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def main():

    print("Hello! Do you want to watch a movie?")

    movies = []

    while True:
        title = input("Please enter the movie's title: ")
        if title == "end":
            break
        duration = input("Please enter the movie's duration in minutes: ")
        if duration == "end":
            break
        start_time = input("Please enter the movie's start time: ")
        if start_time == "end":
            break
        theater_num = input("Please enter the theater's number: ")
        if theater_num == "end":
            break
        num_of_tickets = int(input("How many tickets would you like? "))
        if num_of_tickets == "end":
            break

        movieinformation = {
            "title": title,
            "duration": duration,
            "start_time": start_time,
            "theater_num": theater_num,
            "num_of_tickets": num_of_tickets
        }
    
        movies.append(movieinformation)

    show_movies(movies)

    while True:
            movie_chosen = input("Which movie would you like to buy a ticket for? ")
            if movie_chosen == "end":
                break
            for x in movies:
                if x["title"] == movie_chosen:
                    get_ticket(x)
                    show_movies(movies)
main()