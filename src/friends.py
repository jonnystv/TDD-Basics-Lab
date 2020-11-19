# 1
def get_name(person):
        return person['name']

#2
def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

#3
def likes_to_eat(person, food):
    return food in person['favourites']['snacks']

# 3.2
# def like_to_eat(person, food):
#     for snack in person["favourites"]["snacks"]
#         if snack == food:
#             return True
#         return False

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

    
#7

def l_money(ler, lee, amount):
    ler['monies'] -= amount
    lee["monies"] += amount
    # print (ler["monies"])
    # print (lee["monies"])

#8
def all_favourite_foods(people):
    favourite_snacks = []
    for person in people:
        favourite_snacks.extend(person["favourites"]["snacks"])
    
    return favourite_snacks
#  can also do it with +=

# # 8.2
# def all_favourite_foods(people):
#     favourite_snacks = []
#     for person in people:
#         for snack in person["favouties"]["snacks"]:
#             favourite_foods.append(snack)
#     return favourite_foods

def find_no_friendends(people):
    losers = []

    for person in people:
        if person["friends"] == []:
            losers.append(person)
    return losers
