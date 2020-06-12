#!/usr/bin/env python
# coding: utf-8

# In[44]:


#Imports required libraries
import random
import sys
import time
from PIL import Image
import os
#import getpass


# In[45]:


#Sets working directory
os.chdir(sys.path[0]) 


# In[46]:


#Sets the length of the roulette
roulette_length = 37


# In[47]:


#Creates the list of odd numbers
odds = []

i = 0
while i < roulette_length:
    if i % 2 == 1:
        odds.append(i)
    i += 1
    


# In[48]:


#Creates the list of even numbers
evens = []

i = 0
while i < roulette_length:
    if i % 2 == 0:
        evens.append(i)
    i += 1
    


# In[49]:


#List of red numbers
reds = [
    1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
]


# In[50]:


#List of black numbers
blacks = []
i = 1
while i < roulette_length:
    if i not in reds:
        blacks.append(i)
    i += 1


# In[51]:


#Creates the other groupings of numbers
dozens = [
    list(range(1,13)), 
    list(range(13,25)), 
    list(range(25,37))
]

first18 = list(range(1,19))
second18 = list(range(19,37))

basket = list(range(0,4))

cols = [
    list(range(1,37,3)),
    list(range(2,37,3)),
    list(range(3,37,3))
]

streets = []
i = 1
while i < roulette_length:
    streets.append(list(range(i, i + 3)))
    i += 3

j = 1
corners = []
while j < roulette_length - 4:
    if j % 3 != 0:
        corners.append([j, j + 1, j + 3, j + 4])
    j += 1


# In[52]:


#Opens an image of the roulette board for the player's reference
def show_table():
    img = Image.open("Roulette Board.png")
    img.show()


# In[53]:


#Initialises the random number generator
random.seed()


# In[54]:


#Dictionary of possible actions the user can take in the main menu
games = {
    1: 'Single Number',
    2: '1 to 18',
    3: '19 to 36',
    4: 'Red',
    5: 'Black',
    6: 'Odd',
    7: 'Even',
    8: 'Columns',
    9: 'Streets',
    10: 'Dozens',
    11: 'Corners',
    12: 'Basket',
    13: 'Show Roulette Board',
    14: 'Help',
    15: 'Exit'
}


# In[55]:


#Prints a dialogue asking the user what action they will take
def roulette_dialogue():
    print('\nEnter: ')
    for i in games:
        print('{0}: {1}'.format(i, games[i]))


# In[56]:


#Dictionary of base payouts
payouts = {
    'Single Number': 36,
    '1 to 18': 2,
    '19 to 36': 2,
    'Red': 2,
    'Black': 2,
    'Odd': 2,
    'Even': 2,
    'Columns': 3,
    'Streets': 12,
    'Dozens': 3,
    'Corners': 9,
    'Basket': 9
}


# In[57]:


#Allows the user to set how much they would like to bet per round
def set_bet_amount(money):
    print('How much would you like to wager?')
    print('Balance: $%d' % money)
    wager = ''
    while wager not in range(1, money + 1):
        wager = input()
        if str.isdigit(wager) == False:
            print('Try again.')
        elif (int(wager) <= 0) or (int(wager) > money):
            print('Try again.')
        else:
            wager = int(wager)
    return wager


# In[58]:


#User bets on a single number
def single_number(money):
    wait_t_seconds(1)
    wager = 1
    #wager = set_bet_amount(money)
    print('Choose a number from 0 to 36.')
    print('Enter any other key to return to the main menu.')
    choice = input()
    if str.isdigit(choice) == False:
        print('Returning to main menu.')
        wait_t_seconds(1)
        return money
    else:
        choice = int(choice)
    if choice not in range(0, roulette_length):
        print('Returning to main menu.')
        wait_t_seconds(1)
        return money
    
    global turn_count
    turn_count += 1    
    money -= wager
    number = random.randrange(0, roulette_length)
    wait_t_seconds(1)
    print('The roulette returned %d.' % number)
    wait_t_seconds(1)
    if choice == number:
        print('It\'s a match!')
        money += payouts['Single Number'] * wager
    else:
        print('Better luck next time.') 
    wait_t_seconds(1)
    return money


# In[59]:


#User bets on the numbers 1-18
def one_eighteen(money):
    global turn_count
    turn_count += 1
    wager = 1
    #wager = set_bet_amount(money)
    money -= wager 
    number = random.randrange(0, roulette_length)
    wait_t_seconds(1)
    print('The roulette returned %d.' % number)
    wait_t_seconds(1)
    if number in first18:
        print('It\'s a match!')
        money += payouts['1 to 18'] * wager
    else:
        print('Better luck next time.') 
    wait_t_seconds(1)
    return money


# In[60]:


#User bets on the numbers 19-36
def nineteen_thirtysix(money):
    global turn_count
    turn_count += 1
    wager = 1
    #wager = set_bet_amount(money)
    money -= wager 
    number = random.randrange(0, roulette_length)
    wait_t_seconds(1)
    print('The roulette returned %d.' % number)
    wait_t_seconds(1)
    if number in second18:
        print('It\'s a match!')
        money += payouts['19 to 36'] * wager
    else:
        print('Better luck next time.')
    wait_t_seconds(1)
    return money    


# In[61]:


#User bets on the red numbers
def red(money):
    global turn_count
    turn_count += 1
    wager = 1
    #wager = set_bet_amount(money)
    money -= wager  
    number = random.randrange(0, roulette_length)
    wait_t_seconds(1)
    print('The roulette returned %d.' % number)
    wait_t_seconds(1)
    if number in reds:
        print('It\'s a match!')
        money += payouts['Red'] * wager
    else:
        print('Better luck next time.')
    wait_t_seconds(1)
    return money        


# In[62]:


#User bets on the black numbers
def black(money):
    global turn_count
    turn_count += 1
    wager = 1
    #wager = set_bet_amount(money)
    money -= wager  
    number = random.randrange(0, roulette_length)
    wait_t_seconds(1)
    print('The roulette returned %d.' % number)
    wait_t_seconds(1)
    if number in blacks:
        print('It\'s a match!')
        money += payouts['Black'] * wager
    else:
        print('Better luck next time.')
    wait_t_seconds(1)
    return money   


# In[63]:


#User bets on the odd numbers
def odd(money):
    global turn_count
    turn_count += 1
    wager = 1
    #wager = set_bet_amount(money)
    money -= wager  
    number = random.randrange(0, roulette_length)
    wait_t_seconds(1)
    print('The roulette returned %d.' % number)
    wait_t_seconds(1)
    if number in odds:
        print('It\'s a match!')
        money += payouts['Odd'] * wager
    else:
        print('Better luck next time.')
    wait_t_seconds(1)
    return money       


# In[64]:


#User bets on the even numbers
def even(money):
    global turn_count
    turn_count += 1
    wager = 1
    #wager = set_bet_amount(money)
    money -= wager 
    number = random.randrange(0, roulette_length)
    wait_t_seconds(1)
    print('The roulette returned %d.' % number)
    wait_t_seconds(1)
    if number in evens:
        print('It\'s a match!')
        money += payouts['Even'] * wager
    else:
        print('Better luck next time.')
    wait_t_seconds(1)
    return money        


# In[65]:


#Prints out a list of columns. Used within the function column()
def print_columns():
    print('Choose a column:')
    print('1: 1,4,7,...,34')
    print('2: 2,5,8,...,35')
    print('3: 3,6,9,...,36')    


# In[66]:


#User bets on a (vertical) column of numbers
def column(money):
    wait_t_seconds(1)
    wager = 1
    #wager = set_bet_amount(money)
    print_columns()
    print('Enter any other key to return to the main menu.')
    choice = input()
    if str.isdigit(choice) == False:
        print('Returning to main menu.')
        wait_t_seconds(1)
        return money
    else:
        choice = int(choice)
    if choice not in [1,2,3]:
        print('Returning to main menu.')
        wait_t_seconds(1)
        return money
    
    global turn_count
    turn_count += 1
    money -= wager 
    number = random.randrange(0, roulette_length)
    wait_t_seconds(1)
    print('The roulette returned %d.' % number)
    wait_t_seconds(1)
    if number in cols[choice - 1]:
        print('It\'s a match!')
        money += payouts['Columns'] * wager
    else:
        print('Better luck next time.')
    wait_t_seconds(1)
    return money            


# In[67]:


#Prints out a list of streets. Used within the function street()
def print_streets():
    print('Choose a street:')
    i = 1
    for i in range(1, 13):
        print('{0}: {1}'.format(i, streets[i - 1]))


# In[68]:


#User bets on a (horizontal) row of numbers
def street(money): 
    wait_t_seconds(1)
    wager = 1
    #wager = set_bet_amount(money)
    print_streets()
    print('Enter any other key to return to the main menu.')
    choice = input()
    if str.isdigit(choice) == False:
        print('Returning to main menu.')
        wait_t_seconds(1)
        return money
    else:
        choice = int(choice)
    if choice not in list(range(1,13)):
        print('Returning to main menu.')
        wait_t_seconds(1)
        return money
    
    global turn_count
    turn_count += 1
    money -= wager 
    number = random.randrange(0, roulette_length)
    wait_t_seconds(1)
    print('The roulette returned %d.' % number)
    wait_t_seconds(1)
    if number in streets[choice - 1]:
        print('It\'s a match!')
        money += payouts['Streets'] * wager
    else:
        print('Better luck next time.')
    wait_t_seconds(1)
    return money         


# In[69]:


#Prints out a list of dozens. Used within the function doz()
def print_dozens():
    print('Choose a dozen:')
    print('1: 1,2,3,...,12')
    print('2: 13,14,15,...,24')
    print('3: 25,26,27,...,36')    


# In[70]:


#User bets on a series of twelve consecutive numbers
def doz(money):
    wait_t_seconds(1)
    wager = 1
    #wager = set_bet_amount(money)
    print_dozens()
    print('Enter any other key to return to the main menu.')
    choice = input()
    if str.isdigit(choice) == False:
        print('Returning to main menu.')
        wait_t_seconds(1)
        return money
    else:
        choice = int(choice)
    if choice not in [1,2,3]:
        print('Returning to main menu.')
        wait_t_seconds(1)
        return money
    
    global turn_count
    turn_count += 1
    money -= wager
    number = random.randrange(0, roulette_length)
    wait_t_seconds(1)
    print('The roulette returned %d.' % number)
    wait_t_seconds(1)
    if number in dozens[choice - 1]:
        print('It\'s a match!')
        money += payouts['Dozens'] * wager
    else:
        print('Better luck next time.')
    wait_t_seconds(1)
    return money         


# In[71]:


#User bets on the basket (0, 1, 2, 3)
def bask(money):
    global turn_count
    turn_count += 1
    wager = 1
    #wager = set_bet_amount(money)
    money -= wager  
    number = random.randrange(0, roulette_length)
    wait_t_seconds(1)
    print('The roulette returned %d.' % number)
    wait_t_seconds(1)
    if number in basket:
        print('It\'s a match!')
        money += payouts['Basket'] * wager
    else:
        print('Better luck next time.')
    wait_t_seconds(1)
    return money   


# In[72]:


#Prints out a list of corners. Used within the function corner()
def print_corners():
    print('Choose a corner:')
    j = 1
    for i in range(1,33):
        if i % 3 != 0:
            print(
                "{0}: {1},{2},{3},{4}".format(j, i, i + 1, i + 3, i + 4)
            )
            j += 1


# In[73]:


#User bets on a square of four numbers
def corner(money):
    wait_t_seconds(1)
    wager = 1
    #wager = set_bet_amount(money)
    print_corners()
    print('Enter any other key to return to the main menu.')
    choice = input()
    if str.isdigit(choice) == False:
        print('Returning to main menu.')
        wait_t_seconds(1)
        return money
    else:
        choice = int(choice)
    if choice not in range(1, len(corners) + 1):
        print('Returning to main menu.')
        wait_t_seconds(1)
        return money    
    
    global turn_count
    turn_count += 1
    money -= wager
    number = random.randrange(0, roulette_length)
    wait_t_seconds(1)
    print('The roulette returned %d.' % number)
    wait_t_seconds(1)
    if number in corners[choice - 1]:
        print('It\'s a match!')
        money += payouts['Corners'] * wager
    else:
        print('Better luck next time.')
    wait_t_seconds(1)
    return money             


# In[74]:


def e_to_exit():
    print('Press E to exit.')
    command = ''
    while (command != 'E') and (command != 'e'):
        command = input()
    return


# In[75]:


#Displays a help page for new users
def help_page():
    print('Rules:')
    print('-On the main menu, enter a number from 1 to 12 to bet on a certain number or group of numbers.')
    print('-There are 37 numbers, from 0 to 36.')
    print('-You will always start with $10 and lose $1 with each bet.\n')
    
    print('Special groups:')
    print('-Red: 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36')
    print('-Black: 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35')
    print('-Basket: 0, 1, 2, 3\n')
    
    print('Payouts:')
    for k, v in payouts.items():
        print('%s: ' % k + '$' + '%d' % v)
    print('\n')
    e_to_exit()


# In[76]:


#Prints a warning and controls asking the user if they are certain they want to exit the simulator.
def display_exit_controls():
    print('Are you sure you want to exit?')
    print('Y: Yes')
    print('N: No') 


# In[77]:


#Delays the program for t seconds.
def wait_t_seconds(t):
    now = time.time()
    future = now + t
    while time.time() < future:
        pass


# In[78]:


#Exits the game
def game_exit(money, turns):
    display_exit_controls()
    command = input()
    while (command != 'N') and (command != 'n'):
        if (command == 'Y') or (command == 'y'):
            if turns == 1:
                print('You played for 1 turn and finished with $%d.' % money)
            else:
                print('You played for {0} turns and finished with ${1}.'.format(turns, money))
            wait_t_seconds(1)
            print('Goodbye!')
            wait_t_seconds(1.5)
            sys.exit(0)
        command = input()
    print('Returning to main menu.') 


# In[79]:


'''
class accounts:
    def __init__(self, username, password):
        for k in self.keys():
            if username == k:
                print("Username already taken")
                return False
        self.password = password
        self.money = 10
        self.turn_count = 0
    
    def check_account(self, username, password):
        for k in self.keys():
            if username == k:
                if password == self[k]:
                    print("Login successful. Welcome back, %s!" % username)
                    return True
                else:
                    print("Incorrect username or password")
                    return False
        print("No such username exists")
        return False        
        
    def get_money(self, username):
        return self.money[username]    
    
    def get_turn_count(self, username):
        return self.turn_count[username]
'''


# In[80]:


#Landing page. This will be the first thing users will see 
#upon starting the program.


'''
def landing():
    print("Press 1 for login")
    print("Press 2 to create a new account")
    print("Press 3 to exit")
    done = False
    while done is not True:
        command = input()
        if str.isdigit(command) == False:
            print('Try again.')
            continue
        else:
            command = int(command)
            
        if command == 1:
            username = input("Username: ")
            password = getpass.getpass(prompt = "Password: ")
            login = accounts.check_account(username, password)
            if login is True:
                return username
            else:
                continue
        elif command == 2:
            username = input("Username: ")
            password = getpass.getpass(prompt = "Password: ")
            accounts(username, password)
        elif command == 3:
            print("Goodbye!")
            wait_t_seconds(1.5)
            sys.exit(0)
        else:
            print("Try again.")
'''


# In[81]:


#Main program
print('Welcome to Roulette!')
turn_count = 0
money = 10
wait_t_seconds(1)
while money > 0:
    roulette_dialogue()
    print('Balance: $%d' % money)
    command = ''
    while command not in list(games.keys()):
        command = input()
        if str.isdigit(command) == False:
            print('Try again.')
            continue
        else:
            command = int(command)
            
        if command == 1:
            money = single_number(money)
        elif command == 2:
            money = one_eighteen(money)
        elif command == 3:
            money = nineteen_thirtysix(money)
        elif command == 4:
            money = red(money)
        elif command == 5:
            money = black(money)
        elif command == 6:
            money = odd(money)
        elif command == 7:
            money = even(money)
        elif command == 8:
            money = column(money)
        elif command == 9:
            money = street(money)
        elif command == 10:
            money = doz(money)
        elif command == 11:
            money = corner(money)
        elif command == 12:
            money = bask(money)
        elif command == 13:
            show_table()
        elif command == 14:
            help_page()
        elif command == 15:
            game_exit(money, turn_count)
        else:
            print('Try again.')
if turn_count == 1:
    print('You ran out of money after 1 turn!')
else:
    print('You ran out of money after %d turns!' % turn_count)
e_to_exit()


# In[46]:


'''
Future modifications:
-Allow the user to set the intial balance and bet amounts
-Add exotic bets
-Give the option to play American roulette
-Model the trajectories of a large number of simulated players (Monte Carlo)
'''


# In[132]:


'''
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline


turns = []

for i in range(0,1000):
    turn_count = 0
    money = 10
    while money > 0:
        money = red2(money)
        turn_count += 1
    turns.append(turn_count)

print("Average Turns survived: %.2f" % (sum(turns) / len(turns)))

plt.hist(x = turns, bins = 50, range = (0, 1000))


#User bets on the red numbers - SIMULATION ONLY!
def red2(money):
    money -= 1 
    number = random.randrange(0, roulette_length)
    if number in reds:
        money += 2
    return money   

'''


# In[ ]:




