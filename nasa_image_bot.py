import requests
import os
import random
from tweepy import OAuthHandler,API
from lxml import html
import time

def twitter_api():
    consumer_key = "66aAZNNolxt08Q9QUg5NqVNDI"
    consumer_secret = "s09Ksoe5tnnxGhQWbGa6WI90r32hKl4qS1kjBrvk1yGobFErFY"
    access_token = "853723635340648450-m8JMNPzU98ZhvhM5i1TStEXyn8dLomh"
    access_token_secret = "0mPKEpGEbRJOredapreGO4YdL1fB5aunI3IyOVRhsgAU4"

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = API(auth)
    return api


def tweet_image(url, message):
    api = twitter_api()
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        #print("Unable to download image")

while True:
    try:
        image_num=str(random.randint(1,30000)).zfill(5)
        url = "https://photojournal.jpl.nasa.gov/jpegMod/PIA"+image_num+"_modest.jpg"
        pageurl="https://photojournal.jpl.nasa.gov/catalog/PIA"+image_num
        page=requests.get(pageurl)
        content=page.content.decode()
        caption=content.split('<b>')[1].split('</b>')[0].split(': ')[1]
        message = caption+' '+pageurl
        #print('Tweeting: '+message)
        tweet_image(url,message)
        keepgoing=0
        time.sleep(60*15)
    except:
        #print("Image not found!")
