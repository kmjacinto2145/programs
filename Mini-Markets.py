#!/usr/bin/env python
# coding: utf-8

# In[205]:


import numpy as np
import pandas as pd
import random
import sys


# In[206]:


stocks = {"A": 100, "B": 100, "C": 100}
stock_vars = {"A": 0.5, "B": 1, "C": 3}
annual_stock_growth = 0.1
daily_stock_growth = (1 + annual_stock_growth) ** (1 / 365) - 1
funds = 10000
annual_funds_growth = 0.018
daily_fund_growth = (1 + annual_funds_growth) ** (1 / 365) - 1
portfolio_value = 0
portfolio = {"A": 0, "B": 0, "C": 0}
actions = {0: "Buy", 
           1: "Sell", 
           2: "See prices", 
           3: "Next day", 
           4: "Quit simulator",
           5: "See portfolio",
           6: "Stock info"}
stock_descriptions = {"A": "A low-risk stock. Nice and safe for youngblood noobs like you.",
                      "B": "A medium-risk stock. Perfect for the risk-neutral individual.",
                      "C": "A high-risk stock. Big d*ck energy!"}


# In[207]:


def adjust_daily():
    global funds
    global portfolio
    global portfolio_value
    global stocks
    
    portfolio_value = 0
    
    for i in portfolio:
        portfolio_value += portfolio[i] * stocks[i]
        
    funds += funds * daily_fund_growth


# In[208]:


def see_portfolio(funds, portfolio, portfolio_value, stocks):
    print("Portfolio value: $%.2lf" % portfolio_value)
    print("Funds value: $%.2lf" % funds)
    print("Quantities:", portfolio)
    print("Values:")
    for i in portfolio:
        print(i, ": $", portfolio[i] * stocks[i])
        
    profit = portfolio_value + funds - 10000
    if profit > 0:
        print("You have made a profit of $%.2lf." % profit)
    elif profit == 0:
        print("You have not made a profit or a loss.")
    else:
        print("You have made a loss of $%.2lf." % abs(profit))


# In[209]:


def print_actions():
    for i in actions:
        print(str(i) + ": " + actions[i])


# In[210]:


def see_prices(stocks):
    print("Here are today's stock prices:")
    for i, j in stocks.items():
        print(i, ": $", round(j,2))      


# In[211]:


def place_order():
    
    global funds
    global portfolio
    global portfolio_value
    global stocks
    
    print("You currently have $%.2lf in cash." % funds)
    
    for i, j in stocks.items():
        print(i, ": $", round(j,2))
    
    stock = input("Which stock do you want to buy? ")
    if stock in stocks:
        buy(stock)    
    
    return


# In[212]:


def buy(stock):
    
    global funds
    global portfolio
    global portfolio_value
    global stocks
    
    max_purchaseable = funds // stocks[stock]
    
    purchased = False
    
    while not purchased:
    
        number_purchased = int(input("How many do you want to buy? You can buy up to %d units. " % max_purchaseable))

        if number_purchased > max_purchaseable:
            print("Insufficient funds.")
        else:
            purchased = True
    
    print("Purchased {0} of stock {1} for a total of ${2}.".format(number_purchased, stock, round(number_purchased * stocks[stock], 2)))
    portfolio[stock] += number_purchased
    portfolio_value += number_purchased * stocks[stock]
    funds -= number_purchased * stocks[stock]


# In[213]:


def place_sell():
    global funds
    global portfolio
    global portfolio_value
    global stocks
    
    print("You currently have $%.2lf in cash." % funds)
    
    for i, j in portfolio.items():
        print(i, ":", round(j,2))
    
    stock = input("Which stock do you want to sell? ")
    if stock in stocks:
        sell(stock)     
    
    return


# In[214]:


def sell(stock):
    global funds
    global portfolio
    global portfolio_value
    global stocks
    
    sold = False
    
    while not sold:
    
        number_sold = int(input("How many do you want to sell? You can sell up to %d units. " % portfolio[stock]))

        if number_sold > portfolio[stock]:
            print("Insufficient units.")
        else:
            sold = True
    
    print("Sold {0} of stock {1} for a total of ${2}.".format(number_sold, stock, round(number_sold * stocks[stock], 2)))
    portfolio[stock] -= number_sold
    portfolio_value -= number_sold * stocks[stock]
    funds += number_sold * stocks[stock]


# In[215]:


def change_prices():
    global stocks
    global annual_growth
    global funds
    for i in stocks:
        stocks[i] += stocks[i] * daily_stock_growth + random.normalvariate(0,1)


# In[216]:


def day(i, sim_length):
    
    global funds
    global portfolio
    global portfolio_value
    global stocks
        
    print("Welcome to day %d out of %d, Investor!" % (i, sim_length))
    print("Your portfolio value is $%.2lf" % portfolio_value)
    print("You have $%.2lf in cash." % funds)
    print("\n")
            
    see_prices(stocks)
    print("\n")
        
    done = False
    while done is False:
        print_actions()
        command = int(input("What do you want to do? "))
        if command == 0:
            place_order()
        elif command == 1:
            place_sell()
        elif command == 2:
            see_prices(stocks)
        elif command == 3:
            done = True
        elif command == 4:
            sys.exit(0)
        elif command == 5:
            see_portfolio(funds, portfolio, portfolio_value, stocks)
        elif command == 6:
            stock_info(stock_descriptions)
            
    change_prices()
    adjust_daily()


# In[217]:


def stock_info(stock_descriptions):
    for i in stock_descriptions:
        print(i, ":", stock_descriptions[i])
    print("Note that all three stocks yield the same average return.")
    print("Happy investing!")


# In[218]:


def main():
    
    sim_length = int(input("How many days do you want to simulate for? ")) 
    
    for i in range(1, sim_length + 1):
        day(i, sim_length)
        
    see_portfolio(funds, portfolio, portfolio_value)


# In[219]:


if __name__ == "__main__":
    main()


# In[ ]:




