import random
from celeb_list import data
from celeb_art import logo, vs


def get_celeb():
    """Outputs random celebrity from list"""
    celeb = random.choice(data)
    return celeb


def celeb_information(celeb):
    """Prints celebrity A information"""
    name = celeb['name']
    description = celeb['description']
    country = celeb['country']
    print(f'A: {name}, a {description} from {country}')


def celeb_information_2(celeb):
    """Prints celebrity B information"""
    name = celeb['name']
    description = celeb['description']
    country = celeb['country']
    print(f'B: {name}, a {description} from {country}')


def check_followers(person_1, person_2):
    """Checks which celebrity has higher follower count and returns that
    celebrity"""
    celeb_1_follower = person_1['follower_count']
    celeb_2_follower = person_2['follower_count']
    if celeb_1_follower > celeb_2_follower:
        return 'A'
    else:
        return 'B'


def guess_celebrity():
    print(logo)

    celeb_1 = get_celeb()
    celeb_2 = get_celeb()

    score = 0
    while True:
        celeb_information(celeb_1)
        print(vs)
        celeb_information_2(celeb_2)
        user_guess = input(f'Who has more followers, A or B?: ')

        print(logo)

        if user_guess == check_followers(celeb_1, celeb_2):
            score += 1
            print(f'Good job! Your score: {score}')
            celeb_1 = celeb_2
            celeb_2 = get_celeb()
        else:
            print('Nope! Wrong guess. Your score: {score}')
            break


guess_celebrity()

