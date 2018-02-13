import media
import fresh_tomatoes

def main():

	"""Creation of Movie objects to be displayed on website."""

	iron_man = media.Movie(
		"Iron Man 3",
		"https://images-na.ssl-images-amazon.com/images/M/MV5BMTkzMjEzMjY1M" \
		"15BMl5BanBnXkFtZTcwNTMxOTYyOQ@@._V1_SY1000_SX700_AL_.jpg",
		"https://www.youtube.com/watch?v=oYSD2VQagc4")
	captain_america = media.Movie(
		"Captain America: Civil War",
		"https://images-na.ssl-images-amazon.com/images/M/MV5BMjQ0MTgyNjAxM" \
		"V5BMl5BanBnXkFtZTgwNjUzMDkyODE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
		"https://www.youtube.com/watch?v=dKrVegVI0Us")
	spiderman = media.Movie(
		"Spider-Man: Homecoming",
		"https://images-na.ssl-images-amazon.com/images/M/MV5BNTk4ODQ1MzgzN" \
		"l5BMl5BanBnXkFtZTgwMTMyMzM4MTI@._V1_SY1000_CR0,0,658,1000_AL_.jpg",
		"https://www.youtube.com/watch?v=DiTECkLZ8HM")

	movies = [iron_man, captain_america, spiderman]

	# Invoking function to generate HTML File
	fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':

    main()
