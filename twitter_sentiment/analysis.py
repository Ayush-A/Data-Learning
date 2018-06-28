import tweepy
import csv

# Natural Language Processing module
from textblob import TextBlob

# Authorizing with your API and ACCESS TOKEN to Twitter's API
access_token = 	'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_SECRET'
consumer_key = 	'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Extract all the tweets related to the topic in braces
tweets = api.search('FIFA2018')

# Opening a csv file to store the related tweets along with the sentiment associated with the tweet
file = open("savaData.csv", "a")
writer = csv.writer(file)

# Performing analysis of the tweet with the NLP module's function and writing to .csv file
for tweet in tweets:
    analysis = TextBlob(tweet.text)
    writer.writerow((tweet.text, 'positive' if analysis.sentiment.polarity > 0 else 'negative'))
