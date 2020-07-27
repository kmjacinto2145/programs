#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
import sys
import yfinance as yf
import datetime
import bs4
import requests


# In[8]:


fileDB = ''
start_date = datetime.datetime.today() - datetime.timedelta(weeks = 260)
end_date = datetime.datetime.today() - datetime.timedelta(days = 1)


# In[5]:


def extractYahoo_equity(asset):
    #call API routines specific to an asset
    equity = yf.download(asset,
                         start= start_date,
                         end= end_date,
                         progress=False,
                         auto_adjust=False)
    #drop extracts into ET fileDB
    equity.to_csv(fileDB + str(asset) + '.prices.csv')
    #equity.to_json(fileDB + str(asset) + 'prices.json')
    return equity


# In[92]:


def extract_all_assets():
    resp = requests.get('https://en.wikipedia.org/wiki/S%26P/ASX_200')
    soup = bs4.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    tickers = [s.replace('\n', '.AX') for s in tickers]
    equity = yf.download(tickers,
                         start= start_date,
                         end= end_date,
                         progress=False,
                         auto_adjust=False)
    #drop extracts into ET fileDB
    equity.to_csv(fileDB + 'all_prices.csv')
    #equity.to_json(fileDB + str(asset) + 'prices.json')
    return equity


# In[93]:


all_prices = extract_all_assets()

all_prices = all_prices['Adj Close']

all_prices = all_prices.dropna(axis = 1, how = 'all')


# In[78]:


menu_options = ['Exit', 'Settings', 'Buy', 'Sell', 'See Portfolio', 'See Current Prices', 'Graph Past Performance']
command_numbers = list(range(len(menu_options)))
menu_options = dict(zip(command_numbers, menu_options))


# In[26]:


#sets up the portfolio
try:
    portfolio = pd.read_csv("portfolio.csv")
except:
    portfolio = pd.DataFrame(data = [], columns = ['Stock','Price','Quantity','Total Amount'])


# In[49]:


cash = 10000


# In[70]:


def print_actions(options):
    for key in options:
        print(key, ":", options[key])


# In[90]:


def see_current_prices():
    current = all_prices.tail(1)
    for stock in current.columns:
        print(stock, ":", current[stock].item())


# In[83]:


def menu():
    
    print("Welcome, investor!")
    
    while True:
        
        portfolio_value = sum(portfolio['Total Amount'])
        print("You have $%.2lf in cash." % cash)
        print("Your portfolio value is $%.2lf." % portfolio_value)
        
        print_actions(menu_options)
        try:
            command = int(input("What do you want to do? "))
        except:
            continue
        
        if command == 0:
            portfolio.to_csv("portfolio.csv")
            input("Goodbye! Enter any key to continue. ")
            sys.exit(0)
        elif command == 1:
            settings()
        elif command == 2:
            buy()
        elif command == 3:
            sell()
        elif command == 4:
            see_portfolio()
        elif command == 5:
            see_current_prices()
        elif command == 6:
            ticker_found = False
            while not ticker_found:
                ticker = input("Which stock ticker do you want to visualise? ")
                if ticker in all_prices.columns:
                    ticker_found = True
                else:
                    print("Ticker not found. Try again.")
            
            print("Which date do you want to start graphing from?")
            start_date = input("Enter your date in the form YYYY-MM-DD. ")
                
            print("Which date do you want to graph to?")
            end_date = input("Enter your date in the form YYYY-MM-DD. ")            
            
            try:
                graph_past_performance(ticker, start_date, end_date)
            except:
                print("Something went wrong. Returning to main menu.")


# In[36]:


def graph_past_performance(ticker, start_date, end_date):
    plt.rcParams["figure.figsize"] = (12,8)
    plt.plot(all_prices[ticker][start_date: end_date])
    plt.title("Plot of {} from {} to {}".format(ticker, start_date, end_date))
    plt.xlabel("Date")
    plt.ylabel(ticker)
    plt.show()


# In[91]:


if __name__ == "__main__":
    menu()


# In[94]:


all_prices.head()


# In[ ]:




