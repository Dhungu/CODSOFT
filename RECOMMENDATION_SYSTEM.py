"""
Simple Recommendation System

Internship Task 4

This project recommends movies using a simple
content-based filtering approach.

The recommendation is based on matching the user's
preferences with predefined item attributes.

Technologies Used:
- Python
- Lists
- Dictionaries
- Loops
- Functions
- Conditional Statements

No machine learning or external libraries are used.
"""

import random


# List of available movies
movies = [
    {"name": "Interstellar", "genre": "Sci-Fi", "language": "English", "rating": 8.6, "year": 2014, "mood": "Serious"},
    {"name": "The Dark Knight", "genre": "Action", "language": "English", "rating": 9.0, "year": 2008, "mood": "Exciting"},
    {"name": "The Hangover", "genre": "Comedy", "language": "English", "rating": 7.7, "year": 2009, "mood": "Happy"},
    {"name": "Parasite", "genre": "Drama", "language": "Korean", "rating": 8.6, "year": 2019, "mood": "Serious"},
    {"name": "Train to Busan", "genre": "Horror", "language": "Korean", "rating": 7.6, "year": 2016, "mood": "Exciting"},
    {"name": "Your Name", "genre": "Romance", "language": "Japanese", "rating": 8.4, "year": 2016, "mood": "Relaxing"},
    {"name": "Spirited Away", "genre": "Drama", "language": "Japanese", "rating": 8.6, "year": 2001, "mood": "Relaxing"},
    {"name": "La La Land", "genre": "Romance", "language": "English", "rating": 8.0, "year": 2016, "mood": "Happy"},
    {"name": "Titanic", "genre": "Romance", "language": "English", "rating": 7.9, "year": 1997, "mood": "Serious"},
    {"name": "Get Out", "genre": "Horror", "language": "English", "rating": 7.7, "year": 2017, "mood": "Exciting"},
    {"name": "The Conjuring", "genre": "Horror", "language": "English", "rating": 7.5, "year": 2013, "mood": "Exciting"},
    {"name": "Mad Max: Fury Road", "genre": "Action", "language": "English", "rating": 8.1, "year": 2015, "mood": "Exciting"},
    {"name": "John Wick", "genre": "Action", "language": "English", "rating": 7.4, "year": 2014, "mood": "Exciting"},
    {"name": "Inception", "genre": "Sci-Fi", "language": "English", "rating": 8.8, "year": 2010, "mood": "Serious"},
    {"name": "The Matrix", "genre": "Sci-Fi", "language": "English", "rating": 8.7, "year": 1999, "mood": "Exciting"},
    {"name": "Bridget Jones's Diary", "genre": "Romance", "language": "English", "rating": 6.7, "year": 2001, "mood": "Happy"},
    {"name": "Crazy Rich Asians", "genre": "Romance", "language": "English", "rating": 6.9, "year": 2018, "mood": "Happy"},
    {"name": "Oldboy", "genre": "Drama", "language": "Korean", "rating": 8.4, "year": 2003, "mood": "Serious"},
    {"name": "Extreme Job", "genre": "Comedy", "language": "Korean", "rating": 7.5, "year": 2019, "mood": "Happy"},
    {"name": "Miracle in Cell No. 7", "genre": "Drama", "language": "Korean", "rating": 8.1, "year": 2013, "mood": "Serious"},
    {"name": "Kikujiro", "genre": "Comedy", "language": "Japanese", "rating": 7.7, "year": 1999, "mood": "Relaxing"},
    {"name": "Weathering With You", "genre": "Romance", "language": "Japanese", "rating": 7.5, "year": 2019, "mood": "Relaxing"},
    {"name": "Ringu", "genre": "Horror", "language": "Japanese", "rating": 7.2, "year": 1998, "mood": "Exciting"},
    {"name": "Battle Royale", "genre": "Action", "language": "Japanese", "rating": 7.6, "year": 2000, "mood": "Exciting"},
    {"name": "Guardians of the Galaxy", "genre": "Sci-Fi", "language": "English", "rating": 8.0, "year": 2014, "mood": "Happy"},
    {"name": "Zombieland", "genre": "Comedy", "language": "English", "rating": 7.6, "year": 2009, "mood": "Exciting"},
    {"name": "The Grand Budapest Hotel", "genre": "Comedy", "language": "English", "rating": 8.1, "year": 2014, "mood": "Relaxing"},
    {"name": "A Silent Voice", "genre": "Drama", "language": "Japanese", "rating": 8.1, "year": 2016, "mood": "Serious"},
    {"name": "Along with the Gods", "genre": "Action", "language": "Korean", "rating": 7.3, "year": 2017, "mood": "Serious"},
    {"name": "Hana-bi", "genre": "Drama", "language": "Japanese", "rating": 7.7, "year": 1997, "mood": "Relaxing"},
]

# Valid options the user can choose from
valid_genres = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance"]
valid_languages = ["English", "Japanese", "Korean"]
valid_moods = ["Happy", "Serious", "Exciting", "Relaxing"]


# Display welcome message
def welcome():
    print("=" * 36)
    print(" SIMPLE RECOMMENDATION SYSTEM")
    print("=" * 36)
    print("This program recommends movies based on what you like.")
    print("You can choose a genre, language, mood and minimum rating,")
    print("and the program will find movies from its list that match.")
    print("You can also search by genre, view every movie, or get a")
    print("random suggestion whenever you want.")


# Show the main menu
def show_menu():
    print("\n------------------------------------")
    print("MENU")
    print("------------------------------------")
    print("1. Get Recommendations")
    print("2. View All Items")
    print("3. Search by Genre")
    print("4. Random Recommendation")
    print("5. Most Popular Items")
    print("6. Exit")
    print("------------------------------------")


# Print one movie in a neat format (used by several menu options)
def display_item(movie):
    print("Movie:", movie["name"])
    print("Genre:", movie["genre"])
    print("Language:", movie["language"])
    print("Rating:", movie["rating"])
    print("Year:", movie["year"])
    print("Mood:", movie["mood"])
    print("------------------------------------")


# Display all items in a neat format
def view_items():
    print("\nHere is the full movie list:\n")
    for movie in movies:
        display_item(movie)


# Check if the user's choice is in a valid list (case-insensitive)
def is_valid_choice(user_input, valid_list):
    for option in valid_list:
        if option.lower() == user_input.lower():
            return True
    return False


# Search movies by genre
def search_genre():
    print("\nAvailable genres: Action, Comedy, Drama, Horror, Sci-Fi, Romance")
    genre = input("Enter genre: ").strip()

    if not is_valid_choice(genre, valid_genres):
        print("\nInvalid genre. Please use one of the listed genres.")
        return

    print()
    found = False
    count = 0
    for movie in movies:
        if movie["genre"].lower() == genre.lower():
            display_item(movie)
            found = True
            count = count + 1

    if not found:
        print("No movies found in this genre.")
    else:
        print("Found", count, "movie(s) in this genre.")


# Ask the user a few simple questions about what they like
def get_preferences():
    print("\nPreferred Genre:")
    print("Action, Comedy, Drama, Horror, Sci-Fi, Romance")
    genre = input("Enter genre: ").strip()
    if not is_valid_choice(genre, valid_genres):
        print("Invalid genre entered. Using Action as default.")
        genre = "Action"

    print("\nPreferred Language:")
    print("English, Japanese, Korean")
    language = input("Enter language: ").strip()
    if not is_valid_choice(language, valid_languages):
        print("Invalid language entered. Using English as default.")
        language = "English"

    rating_text = input("\nMinimum Rating (example: 7.5): ").strip()
    if rating_text == "":
        min_rating = 0
    else:
        try:
            min_rating = float(rating_text)
        except ValueError:
            print("That did not look like a number. Using 0 instead.")
            min_rating = 0

    print("\nPreferred Mood:")
    print("Happy, Serious, Exciting, Relaxing")
    mood = input("Enter mood: ").strip()
    if not is_valid_choice(mood, valid_moods):
        print("Invalid mood entered. Using Happy as default.")
        mood = "Happy"

    preferences = {
        "genre": genre,
        "language": language,
        "min_rating": min_rating,
        "mood": mood,
    }
    return preferences


# Recommend matching movies based on user preferences
def recommend():
    preferences = get_preferences()

    # Look for movies that match every preference
    matches = []
    for movie in movies:
        if (movie["genre"].lower() == preferences["genre"].lower()
                and movie["language"].lower() == preferences["language"].lower()
                and movie["mood"].lower() == preferences["mood"].lower()
                and movie["rating"] >= preferences["min_rating"]):
            matches.append(movie)

    print()
    if len(matches) > 0:
        print("Here are your recommended movies:\n")
        for movie in matches:
            display_item(movie)
        return

    # No exact match, so look for movies that match at least 2 preferences
    print("Sorry, no exact match was found.")
    print()
    print("Here are some similar recommendations instead.")
    print()

    similar = []
    for movie in movies:
        score = 0
        if movie["genre"].lower() == preferences["genre"].lower():
            score = score + 1
        if movie["language"].lower() == preferences["language"].lower():
            score = score + 1
        if movie["mood"].lower() == preferences["mood"].lower():
            score = score + 1
        if movie["rating"] >= preferences["min_rating"]:
            score = score + 1

        if score >= 2:
            similar.append(movie)

    if len(similar) > 0:
        for movie in similar:
            display_item(movie)
    else:
        # Still nothing found, so suggest 3 different random movies
        print("Here are a few movies you might like instead:\n")
        picked = []
        while len(picked) < 3:
            movie = random.choice(movies)
            already_picked = False
            for chosen in picked:
                if chosen["name"] == movie["name"]:
                    already_picked = True
            if not already_picked:
                picked.append(movie)
                display_item(movie)


# Recommend one random movie
def random_pick():
    print("\nHere is a random movie for you:\n")
    movie = random.choice(movies)
    display_item(movie)


# Show the most popular movies (rating above 8.5)
def popular_items():
    print("\nMost Popular Movies (rating above 8.5):\n")
    found = False
    for movie in movies:
        if movie["rating"] > 8.5:
            display_item(movie)
            found = True

    if not found:
        print("No movies above this rating were found.")


# Main program loop
def main():
    welcome()

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            recommend()
        elif choice == "2":
            view_items()
        elif choice == "3":
            search_genre()
        elif choice == "4":
            random_pick()
        elif choice == "5":
            popular_items()
        elif choice == "6":
            print("\nThank you for using the Simple Recommendation System.")
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice.")
            print("Please try again.")


# Run the program
if __name__ == "__main__":
    main()
