#!/usr/bin/env python

import media
import fresh_tomatoes

#toy_story = media.Movie("Toy Story",
#                        "The story of a boy and his toys that come to life",
#                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
#                        "https://www.youtube.com/watch?v=4KPTXpQehio")

local_hero = media.Movie("Local Hero",
                         "The story of an employee of a Houston oil company who goes to Scotland",
                         "http://ia.media-imdb.com/images/M/MV5BMjExMzE1NDg2NV5BMl5BanBnXkFtZTcwNjg2ODIyMQ@@._V1_.jpg",
                         "https://www.youtube.com/watch?v=5sMs9T5sRSk")

crouching_tiger = media.Movie("Crouching Tiger, Hidden Dragon",
                         "Enlighted warrior action!",
                         "https://upload.wikimedia.org/wikipedia/en/9/97/Crouching_tiger_hidden_dragon_poster.jpg",
                         "https://www.youtube.com/watch?v=4xPC1lEJ6Mg")

chocolate = media.Movie("Chocolate",
                         "Yum!",
                         "http://www.impawards.com/2000/posters/chocolat.jpg",
                         "https://www.youtube.com/watch?v=JHncbMjbaqQ")

movies = [local_hero, crouching_tiger, chocolate]

print media.Movie.VALID_RATINGS
print media.Movie.__doc__
print media.Movie.__name__
print media.Movie.__module__

#fresh_tomatoes.open_movies_page(movies)
