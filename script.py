import pickle
from sklearn.feature_extraction.text import CountVectorizer
#import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import re
import numpy as np

from socialreaper import Twitter
from socialreaper.tools import to_csv
import re
import tqdm
import os
import pandas as pd
cEXT = pickle.load( open( "models/cEXT.p", "rb"))
cNEU = pickle.load( open( "models/cNEU.p", "rb"))
cAGR = pickle.load( open( "models/cAGR.p", "rb"))
cCON = pickle.load( open( "models/cCON.p", "rb"))
cOPN = pickle.load( open( "models/cOPN.p", "rb"))
vectorizer_31 = pickle.load( open( "models/vectorizer_31.p", "rb"))
vectorizer_30 = pickle.load( open( "models/vectorizer_30.p", "rb"))

twt = Twitter(app_key="", 
              app_secret="", 
              oauth_token="", 
              oauth_token_secret="")
    

def get_tweets_as_string(user_name):
    tweets = twt.user(user_name, 
                    count=500, 
                    exclude_replies=False, 
                    include_retweets=True)
        
    to_csv(list(tweets), filename=user_name+'_tweets.csv')
    tweets_df = pd.read_csv(user_name+"_tweets.csv")
    just_tweets=tweets_df.loc[:, ["text"]]
    no_urls = just_tweets.loc[:, ["text"]].apply(lambda x: re.split('https:\/\/.*', str(x))[0])
    tweets_string = ""
    for idx,row in (no_urls.iteritems()):
        tweets_string += (str(row) + '.')

    clean_text = re.sub("[^A-Za-z0-9. ]"," ",tweets_string)
    clean_text.strip()
    return(clean_text)

def predict_personality(text):
    sentences = re.split("(?<=[.!?]) +", text)
    text_vector_31 = vectorizer_31.transform(sentences)
    text_vector_30 = vectorizer_30.transform(sentences)
    EXT = cEXT.predict(text_vector_31)
    NEU = cNEU.predict(text_vector_30)
    AGR = cAGR.predict(text_vector_31)
    CON = cCON.predict(text_vector_31)
    OPN = cOPN.predict(text_vector_31)
    return [np.mean(EXT), np.mean(NEU), np.mean(AGR), np.mean(CON), np.mean(OPN)]

user_name="narendramodi"
text = get_tweets_as_string(user_name)
predictions = predict_personality(text)

df = pd.DataFrame(dict(r=predictions, theta=['EXT','NEU','AGR', 'CON', 'OPN']))
attrs = list(df['r'])
plt.rcParams["figure.figsize"] = (12, 6)
plt.style.use('ggplot')
plt.bar([' Extroversion','Neuroticism','Agreeableness', 'Conscientiousness', 'Openness'],attrs, color ='green', alpha=0.5)
plt.xlabel("Attribute")
plt.ylabel("Tendency")
plt.title(user_name+"'s Personality Report")
plt.show()
