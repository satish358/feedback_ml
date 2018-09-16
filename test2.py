import tokenHandle
import requests
from textblob import TextBlob

token = tokenHandle.getToken()

URL = "https://lostfound2.000webhostapp.com/api/sendData.php"
PARAMS = {'token': token}
i = j = 0
pos = 0
neg = 0
neu = 0
tempData = {}
x = {}

r = requests.get(url=URL, params=PARAMS)
data = r.json()
name = len(data['data'])

for dt in data['data']:
    finalData = {}
    grpFeed = TextBlob(dt['feed'])
    finalData['name'] = dt['name']
    finalData['app_name'] = dt['app_name']
    finalData['app_id'] = dt['app_id']
    finalData['feed'] = dt['feed']
    finalData['polarity'] = grpFeed.sentiment.polarity
    if grpFeed.sentiment.polarity == 0:
        finalData['sentiment'] = 'neutral'
        finalData['bg'] = 'bg-primary'
        neu = neu+1
    elif grpFeed.sentiment.polarity > 0:
        finalData['sentiment'] = 'positive'
        finalData['bg'] = 'bg-success'
        pos = pos+1
    elif grpFeed.sentiment.polarity < 0:
        finalData['sentiment'] = 'negative'
        finalData['bg'] = 'bg-danger'
        neg = neg+1
    tempData[i] = finalData
    i += 1
chart_data = { 'pos': pos,'neg':neg,'neu':neu }
tempData['chart'] = chart_data

print(tempData)
