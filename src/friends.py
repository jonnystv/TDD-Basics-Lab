# 1
def get_name(person):
        return person['name']

#2
def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

#3
def likes_to_eat(person, food):
    return food in person['favourites']['snacks']

#4
def add_friend(person, friend):
    person["friends"].append(friend)
#return len(person["friends"])


#5
def remove_friend(person, friend):
    person["friends"].remove(friend)

#6

def total_money(people_dictionaries):
    money = 0
    for person in people_dictionaries:
        money += person['monies']
    return money

