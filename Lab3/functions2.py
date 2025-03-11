movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

# 1) Check IMDB score
def is_good_imdb(movie):
    """Checks if a movie has an IMDB score above 5.5.

    Args:
        movie: A dictionary representing a movie.

    Returns:
        True if the IMDB score is above 5.5, False otherwise.
    """
    return movie["imdb"] > 5.5

# 2) Sublist of movies with good IMDB score
def filter_good_imdb(movies):
    """Returns a sublist of movies with an IMDB score above 5.5.

    Args:
        movies: A list of movie dictionaries.

    Returns:
        A list of movies with IMDB score above 5.5.
    """
    return [movie for movie in movies if is_good_imdb(movie)]

# 3) Filter movies by category
def filter_by_category(movies, category):
    """Returns a sublist of movies in a given category.

    Args:
        movies: A list of movie dictionaries.
        category: The category to filter by.

    Returns:
        A list of movies in the specified category.
    """
    return [movie for movie in movies if movie["category"] == category]

# 4) Average IMDB score
def average_imdb(movies):
    """Calculates the average IMDB score of a list of movies.

    Args:
        movies: A list of movie dictionaries.

    Returns:
        The average IMDB score.
    """
    if not movies:
        return 0
    return sum(movie["imdb"] for movie in movies) / len(movies)

# 5) Average IMDB score by category
def average_imdb_by_category(movies, category):
    """Calculates the average IMDB score for movies in a given category.

    Args:
        movies: A list of movie dictionaries.
        category: The category to calculate the average for.

    Returns:
        The average IMDB score for the specified category.
    """
    movies_in_category = filter_by_category(movies, category)
    return average_imdb(movies_in_category)