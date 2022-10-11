# imports
import twint
import csv
import pandas as pd
import time

# load the biden_pardons_marijuana.csv file
df = pd.read_csv("biden_pardons_marijuana.csv")

# make a dataframe
df = pd.DataFrame(df)

# setup twint
c = twint.Config()
c.Search = "Biden pardons marijuana"
c.Store_csv = True
# append the output to the existing csv file
c.Output = "biden_pardons_marijuana.csv"

# set the since datetime to the exact date and time of the last tweet in the csv file
c.Since = df['date'].iloc[-1] + " " + df['time'].iloc[-1]

# set the until date to the current date tiem so that the bot will only scrape new tweets
c.Until = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

c.Hide_output = True

# run search
twint.run.Search(c)
