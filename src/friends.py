# 1
def get_name(person):
        return person['name']

#2
def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

#3
def likes_to_eat(person, food):
    return food in person['favourites']['snacks']