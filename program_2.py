# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.
# David Stalmakov 9/25/2025 "Number of Tickets for Movies"
def main():
    ######################
    total_tickets = 0
    count = 0
    number_of_movies = int(input("Enter the number of movies you want to buy tickets for: "))

    while count < number_of_movies:
        movie = input("Enter the movie title: ")
        tickets = int(input("Enter the number of tickets: "))
        total_tickets += tickets
        count += 1

    print("Total tickets: ", total_tickets)
    ######################


if __name__ == '__main__':
    main()