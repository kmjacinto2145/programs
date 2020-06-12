#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random as rd
import statistics as stats
import sys


# In[2]:


cases = list(range(1,27))


# In[3]:


amounts = [1,2,3,5,10,
           20,50,100,150,200,
           250,500,750,1000,2000,
           3000,4000,5000,10000,15000,
           20000,30000,50000,75000,100000,200000]


# In[4]:


rd.shuffle(amounts)


# In[5]:


final_cases = dict(zip(cases,amounts))


# In[6]:


cases_to_open = [6,5,4,3,2,1,1,1,1]


# In[7]:


def dialogue(cases):
    print("Enter the case number to open it! Enter 0 to see the remaining values on the board.")
    i = 0
    while i < len(cases):
        print("%d" % list(cases.keys())[i])
        i += 1


# In[8]:


def print_remaining_values(cases):
    values = [1,2,3,5,10,
           20,50,100,150,200,
           250,500,750,1000,2000,
           3000,4000,5000,10000,15000,
           20000,30000,50000,75000,100000,200000]
    print("The remaining values are:")
    global personal_case
    for i in values:
        for j in list(cases.values()) + [personal_case]:
            if i == j:
                print("%d" % i)


# In[9]:


def round(cases, to_open):
    i = 0
    while i < to_open:
        print("You have %d cases remaining this round." % (to_open - i))
        dialogue(cases)
        command = ""
        while (command not in list(cases.keys())) and (command != 0):
            command = input()
            if str.isdigit(command) == False:
                print('Try again.')
                continue
            else:
                command = int(command)
        if command == 0:
            print_remaining_values(cases)
            continue
        print("You opened case %d" % command)
        value = cases.pop(command)
        print("It contains $%d!" % value)
        i += 1
    return cases


# In[10]:


def calculate_offer(cases, personal_case):
    offer = 0.5 * stats.median(list(final_cases.values()) + [personal_case]) + 0.5 * sum(list(final_cases.values()) + [personal_case]) / len(cases)
    print("The Banker offers you $%d" % offer)
    print("Deal or No Deal?")
    print("D: Deal")
    print("N: No Deal")
    print("S: See Remaining Values")
    command = ""
    action_completed = False
    while action_completed is False:
        if command == "D":
            print("You chose to Deal.")
            print("Let's open your case.")
            input("Press any key to open your case.")
            print("It contains $%d!" % personal_case)
            end_game(offer)
        elif command == "N":
            action_completed = True
        elif command == "S":
            print_remaining_values(cases)
            print("Deal or No Deal?")
            print("D: Deal")
            print("N: No Deal")
            print("S: See Remaining Values")
            command = input()
        else:
            command = input()


# In[11]:


def end_game(winnings):
    print("Congratulations, you won $%d!" % winnings)
    input("Enter any key to finish.")
    sys.exit(0)


# In[12]:


print("Hello, and welcome to Deal or No Deal!")
print("Choose a case from 1 to 26. Enter 0 to quit.")
command = ""
while (command not in range(1,27)) and (command != 0):
    command = input()
    if str.isdigit(command) == False:
        print('Try again.')
        continue
    else:
        command = int(command)
if command == 0:
    end_game(0)
else:
    print("You chose case %d." % command)
    personal_case = final_cases.pop(command)
    
for i in cases_to_open:
    print("New round!")
    final_cases = round(final_cases,i)
    calculate_offer(final_cases, personal_case)
    
print("Let's open your case.")
input("Press any key to open your case.")
print("It contains $%d!" % personal_case)
end_game(personal_case)


# In[ ]:





# In[ ]:




