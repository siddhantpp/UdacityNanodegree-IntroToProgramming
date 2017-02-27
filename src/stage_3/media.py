# IPND Stage 3 Final Project - Siddhant Prakash Pardeshi

import webbrowser

class Movie():
    # This class provides a way to store movie related information

    def __init__(self, movie_title, movie_poster_url, movie_trailer_url):
        # initializes instances of class Movie with title, poster url and trailer url
	self.title = movie_title
	self.poster_image_url = movie_poster_url
	self.trailer_youtube_url = movie_trailer_url

    def show_trailer(self):
        # shows the trailer of this instance of class movie
        webbrowser.open(self.trailer_youtube_url)
