# cerner_2^5_2019
# Author: joeratt (Joe Rattazzi)
# pull the most recent Reddit posts from the input subreddit - uses Python3
import requests
import datetime

sub_reddit =  input("input subreddit (don't include r/): ")
sub_reddit = 'cerner' if sub_reddit == '' else sub_reddit # just default to cerner if not picked
i = 0
while True:
    req = requests.get('https://api.reddit.com/r/' + sub_reddit) #This has limiting involved, which we hit
    i = i + 1
    if(req.status_code == 200 or i > 5):
      break

if i > 5:
    req.close()
    print("Could not get a valid connection")
    quit()
jdata = req.json()
children = jdata['data']['children']

for child in children:
    child_data = child['data']
    print("%s - %s\n\t%s\n" %(child_data['title'], datetime.datetime.fromtimestamp(child_data['created_utc']).strftime("%c"), child_data['url']))

req.close()