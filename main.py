from game_data import data
import random

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

# random selection from dicitonary
def random_selection():
    random_data = random.choice(data)
    return {
        'follower_count': random_data['follower_count'],
        'name': random_data['name'],
        'description': random_data['description'],
        'country': random_data['country']
    }

# comparing followers
def compare_followers(a, b):
    if a > b:
        return ("A")
    else:
        return ("B")

#loading random selected data_a to variables
data_a = random_selection()
followers_a = data_a['follower_count']
name_a = data_a['name']
description_a = data_a['description']
country_a = data_a['country'];


#loading random selected data_b to variables
data_b = random_selection()
followers_b = data_b['follower_count']
name_b = data_b['name']
description_b = data_b['description']
country_b = data_b['country']

score= 0
#first print out of comparing data
print(f"Compare A: {data_a['name']}, {data_a['description']}, {data_a['country']}")
print (vs)
print(f"Compare B: {data_b['name']}, {data_b['description']}, {data_a['country']}")


while True:
    #user guessing who has more followers
    player_selection = input("Who has more followers? Type 'A' or 'B' : ")
    player_selection = player_selection.upper()
    #if random choose same data, get new data
    if followers_a == followers_b:
        data_b = random_selection()
        followers_b = data_b['follower_count']
    #if user guessed right who has more follower then adding score and data_b are loaded to data_a to compare with new data
    if player_selection == compare_followers(followers_a,followers_b):
        score += 1
        print(f"You are right! Current score: {score}")
        data_a = data_b
        followers_a = followers_b
        data_b = random_selection()
        followers_b = data_b['follower_count']
        print(f"Compare A: {data_a['name']}, {data_a['description']}, {data_a['country']}")
        print(vs)
        print(f"Compare B: {data_b['name']}, {data_b['description']}, {data_b['country']}")
    #if user guessed wrong, stop game and print out final score
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break
