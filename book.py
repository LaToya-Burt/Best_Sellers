# TODO: Create a Book class with the following instance variables:
# name
# author
# user_rating
# number_of_reviews
# price
# year
# genre
class Book:

    def __init__(self, dict_object):
        self.name = dict_object['name']
        self.author = dict_object['author']
        self.user_rating = dict_object['user_rating']
        self.price = dict_object['price']
        self.year = dict_object['year']
        self.genre = dict_object['genre']
        self.number_of_reviews = dict_object['number_of_reviews']
        
