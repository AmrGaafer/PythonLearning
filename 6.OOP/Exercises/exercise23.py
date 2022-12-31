# --------------------------------------------------------------------------------------------------
# Exercise #23: Object Oriented Programming
# Developer:    Amr Gaafer
# Date:         31.12.2022
# --------------------------------------------------------------------------------------------------
import os
os.system('cls')        # cls command

print("Task#1: class creation:")

class Game:
    def __init__(self, name, developer, year, price_in_pounds):
        self.name = name
        self.developer = developer
        self.year = year
        self.price = price_in_pounds
    def price_in_pounds(self):
        return f'{24.5*self.price} Egyptian Pounds'

game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()}")

print("Task#2: class creation:")
class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    def full_details(self):
        if self.gender == 'Male':
            return f'Hello Mr {self.first_name} {self.last_name.capitalize()[0]}. [{str(40-self.age).zfill(2)}] Years To Reach 40'
        elif self.gender == 'Female':
            return f'Hello Mrs {self.first_name} {self.last_name.capitalize()[0]}. [{str(40-self.age).zfill(2)}] Years To Reach 40'

user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40

print("Task#3: class methods:")
class Message:
    @classmethod
    def print_message(cls):
        return 'Hello From Class Message'

print(Message.print_message())  # Hello From Class Message

print("Task#4: class with different input types:")
class Games:
    def __init__(self, input):
        self.input = input
    def show_games(self):
        if isinstance(self.input, str):
            print(f'I Have One Game Called "{self.input}"')
        elif isinstance(self.input, list):
            my_text = '\n'.join('-- {}'.format(element) for element in self.input)
            print(f'I Have Many Games:\n{my_text}')
        elif isinstance(self.input, int):
            print(f'I Have {self.input} Game.')

my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()            # I Have One Game Called "Shadow Of Mordor"

my_games_names.show_games()     # I Have Many Games:
                                # -- Ys II
                                # -- Ys Oath In Felghana
                                # -- YS Origin

my_games_count.show_games()     # I Have 80 Game.

print("Task#5: inheritance:")
class Members:
    def __init__(self, n, p):
        self.name = n
        self.permission = p
    def show_info(self):
        return f"Your Name Is {self.name} And You Are {self.permission}"

# Create Admin Class Here
class Admins(Members):
    def __init__(self, n, p):
        super().__init__(n, p)

# Create Moderators Class Here
class Moderators(Members):
    def __init__(self, n, p):
        Members.__init__(self, n, p)

member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())   # Your Name Is Osama And You Are Admin
print(member_two.show_info())   # Your Name Is Ahmed And You Are Moderator

print("Task#6: inheritance:")
class A:
    def __init__(self, one):
        self.one = one
class B:
    def __init__(self, two):
        self.two = two
class C:
    def __init__(self, three):
        self.three = three

# Write The Class Called "Text" Here
class Text(A, B, C):
    def __init__(self, one, two, three):
        A.__init__(self, one)
        B.__init__(self, two)
        C.__init__(self, three)
    def show_name(self):
        return self.one + self.two + self.three

the_name = Text("El", "ze", "ro")
print(the_name.show_name())     # The Name Is Elzero
