import tweepy
from textblob import TextBlob

consumer_key = 'ZClYUeSxmYLdvviONTjX0iSKH'
consumer_secret = 'GLx8OiHyceexXIPijquOkuKyOaBPwnMrS3SGZU497GyaloYA0h'

access_token = '842243345145556992-MGb9KP1aei9x3fT4dkZI7vOVxN1mpHE'
access_token_secret = '9Ho0UJw6paMxoyfYZbcVJoQn98NBd9ukb1jiZ5LUGm0Qd'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
