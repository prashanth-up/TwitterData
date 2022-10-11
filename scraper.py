import twint
import csv
import pandas as pd
import time

# setup twint
c = twint.Config()
c.Search = "Biden pardons marijuana"
c.Store_csv = True
c.Output = "biden_pardons_marijuana.csv"
c.Since = "2022-10-1"
c.Until = "2022-10-11"
c.Hide_output = True

# run search
twint.run.Search(c)

# read csv file
df = pd.read_csv("biden_pardons_marijuana.csv")

# make a dataframe
df = pd.DataFrame(df)

# #Drop all columns except for the tweet and date
# df = df.drop(columns=['id', 'conversation_id', 'created_at', 'date', 'time', 'timezone', 'user_id', 'username', 'name', 'place', 'tweet', 'language', 'mentions', 'urls', 'photos', 'replies_count', 'retweets_count', 'likes_count', 'hashtags', 'cashtags', 'link', 'retweet', 'quote_url', 'video', 'thumbnail', 'near', 'geo', 'source', 'user_rt_id', 'user_rt', 'retweet_id', 'reply_to', 'retweet_date', 'translate'])

# Print all the attributes of the dataframe
print(df.columns)

# Keep only the tweet and date and time columns
df = df[['tweet', 'date', 'time']]

# Sort the dataframe by date and time
df = df.sort_values(by=['date', 'time'])
