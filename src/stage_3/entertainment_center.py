# IPND Stage 3 Final Project - Siddhant Prakash Pardeshi
# Entertainment center - uses media and fresh_tomatoes classes to generate a movie webpage with a list of movie objects

import media
import fresh_tomatoes

the_transporter = media.Movie("The Transporter", "https://upload.wikimedia.org/wikipedia/en/6/68/Transporterposter.jpg", "https://youtu.be/0poXFSvX0_4")

the_avengers = media.Movie("The Avengers", "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg", "https://www.youtube.com/watch?v=eOrNdBpGMv8")

the_terminator = media.Movie("The Terminator", "https://upload.wikimedia.org/wikipedia/en/7/70/Terminator1984movieposter.jpg", "https://youtu.be/k64P4l2Wmeg")

movies = [the_transporter, the_avengers, the_terminator]
fresh_tomatoes.open_movies_page(movies)
