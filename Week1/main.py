import random

def print_date(month, day, year='2026'):
    print(f'{year}-{month}-{day}')
    print(year + '-' + month + '-' + day)


ROCK = 'R'
PAPER = 'P'
SCISSORS = 'S'

def get_user_throw():
    choice = ''
    while choice not in (ROCK, PAPER, SCISSORS):
        choice = input("Enter R for rock, P for Paper, S for scissors").upper()
    return choice

def get_computer_throw():
    return random.choice((ROCK, PAPER, SCISSORS))

def display_winner(users_throw, computer_throw):
    if users_throw == computer_throw:
        print("tie")
    elif users_throw == ROCK and computer_throw == SCISSORS \
        or users_throw == PAPER and computer_throw == ROCK \
        or users_throw == SCISSORS and computer_throw == PAPER:
        print("win")
    else:
        print("lose")


users_throw = get_user_throw()
computer_throw = get_computer_throw()




display_winner(users_throw, computer_throw)



# random.seed(10)
random_number = random.randint(1, 10)


guess = int(input("Guess a number 1-10"))

if guess == random_number:
    print("You win! You can go home")
else:
    print("You have to stay")




def our_function():
    print("hello there")
    print("another line")
    print("done")
    # functions without a return will implicitly return None
    # return None

our_function()
print(our_function)

# optional type hint : type you are expecting
# optional return type hint -> expected type
def double(number : int ) -> int:
    return number * 2

print(double(10))
print(double("ten"))




some_number = 42
print(type(some_number))

floating_point = 7.7
print(type(floating_point))

some_word = "O\'Neil"
other_word = 'Charnesky'

name = some_word + " " + other_word

print(type(some_word))

favorite_number = input("Enter your favorite number")
print(type(favorite_number))
# you can multiply a string and it just gets repeated
print(favorite_number * 2)

try:
    favorite_number = int(favorite_number)
    print(type(favorite_number))
except ValueError as ex:
    print(ex)
    print("That's not a numeric value!")

print(favorite_number * 2)

# 2^3
print(2**3)

some_value = 5

other_value = int(input("Enter 10"))

some_value += 5

print(some_value == other_value)

some_list = [1, 2, 3]
another_list = [1, 2, 3]


print(some_list is another_list)

some_list = another_list

print(some_list is another_list)


if some_value:
    print("It's not 0")

some_string = ""

if some_string: # {
    print("Has text") # }
else:
    print("empty")

score = int(input("Enter your score 0 - 100"))

if score > 93:
    print("A")
elif score >= 90:
    print("A-")
# can sandwich values between relational operators
elif 90 > score >= 87:
    print("B+")

money = int(input("How much money do you have for lunch?"))

# if money > 10:
#     lunch = 'Picasso wrap'
# else:
#     lunch = 'ramen noodles'
#
# print(lunch)

lunch = 'Picasso wrap' if money > 10 else 'ramen noodles'
print(lunch)

