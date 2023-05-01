from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import Image
import re
# from post import Post

title = []
subreddit = []
poster = []
upvotes = []
link = []
image = []
tweet = []


url = "https://www.reddit.com/"
page = urlopen(url)
soup = BeautifulSoup(page.read(), 'lxml')

# Gets title, subreddit, poster, upvotes and link info from url
# Only gets top 8 posts currently
titles = soup.find_all('h3', {'class' : '_eYtD2XCVieq6emjKBH3m'}) 
for i in titles: # takes the titles of top 8 posts and stores them in the title list
    title.append(i)

# Gets subreddit name of each post, parses the string and stores in subreddit list
subreddits = soup.find_all('a', {'class' : '_3ryJoIoycVkA88fy40qNJc'})
for i in subreddits:
    subreddit.append(i['href'])

upvote = soup.find_all('div', {'class' : "_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo"})
for i in upvote:
    upvotes.append(i.string)

links = soup.find_all('a', {'class' : 'SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE'})
for i in links:
    link.append('https://www.reddit.com' + i['href'])

images = soup.find_all('img', {'alt' : 'Post image'})
for i in images:
    image.append((i['src']))

tweets = soup.find_all('a', {'aria-label' : "Visit this Tweet on Twitter"})
print(tweets)
for i in tweets:
    tweet.append(i['href'])

print('TITLE: ', title)
print('SUBREDDIT: ', subreddit)
print('POSTER: ', poster)
print('UPVOTES: ', upvotes)
print('LINK: ', link)
print('IMAGE: ', image)
print('TWEET', tweet)
