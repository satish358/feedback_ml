import tokenHandle
import requests
from textblob import TextBlob


def getFeedData(token):

    URL = "https://lostfound2.000webhostapp.com/api/sendData.php"
    PARAMS = {'token': token}
    i = 0
    pos = 0
    neg = 0
    neu = 0
    tempData = {}

    r = requests.get(url=URL, params=PARAMS)

    data = r.json()

    for dt in data['data']:
        finalData = {}
        grpFeed = TextBlob(dt['feed'])
        finalData['name'] = dt['name']
        finalData['app_name'] = dt['app_name']
        finalData['app_id'] = dt['app_id']
        finalData['feed'] = dt['feed']
        finalData['polarity'] = grpFeed.sentiment.polarity
        if grpFeed.sentiment.polarity == 0:
            finalData['sentiment'] = 'Neutral'
            finalData['bg'] = 'bg-primary'
            neu = neu+1
        elif grpFeed.sentiment.polarity > 0:
            finalData['sentiment'] = 'Positive'
            finalData['bg'] = 'bg-success'
            pos = pos+1
        elif grpFeed.sentiment.polarity < 0:
            finalData['sentiment'] = 'Negative'
            finalData['bg'] = 'bg-danger'
            neg = neg+1
        tempData[i] = finalData
        i += 1
    
    chart_data = { 'pos': pos,'neg':neg,'neu':neu }
    tempData['chart'] = chart_data
    return tempData


def sortFeedsByAppID(data,app_id):
    result_data = {}
    j = 0
    neu = 0
    pos = 0
    neg = 0
    for i in range(len(data)-1):
        if data[i]['app_id'] == str(app_id):
            result_data[j] = data[i]
            j+=1

            if data[i]['polarity'] == 0:
                neu = neu+1
            elif data[i]['polarity'] > 0:
                pos = pos+1
            elif data[i]['polarity'] < 0:
                neg = neg+1
    chart_data = {'pos': pos, 'neg': neg, 'neu': neu}
    result_data['chart'] = chart_data
    return result_data

