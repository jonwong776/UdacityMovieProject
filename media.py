class Movie():

    """Represents a movie.

    Used by the entertainment_center.py file to create Movie objects.

    Attributes:
        title: A string of the movie title.
        poster_image_url: A string of the URL of the movie poster.
        trailer_youtube_url: A string of the URL of the movie trailer.
    """

    def __init__(self, movie_title, poster_image, trailer_youtube):

        # Initialization of Movie object attributes
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
