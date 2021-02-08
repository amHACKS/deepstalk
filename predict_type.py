import pickle
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from profilescraper import get_profile
from socialreaper import Twitter
from socialreaper.tools import to_csv
import re, os
import getopt, sys
import warnings
warnings.filterwarnings("ignore")


def tweet(user_name):
    twt = Twitter(app_key="PDz1fZLoCEHcOx035TtLsrcWS", 
              app_secret="Ok1aJBP4nM6g87F3hFiPFY0R0a7qnUNsdIoKZteaAuzYF2yTuF", 
              oauth_token="1292034807057149952-3Mlqa59ZAoqRdACgnW6z4goXUy3vUs", 
              oauth_token_secret="ZZlu7jF3mymeapDxwj19MkqCYF3osQjp48xYEuIL4wRM1")

    tweets = twt.user(user_name, 
                    count=1000, 
                    exclude_replies=False, 
                    include_retweets=False)
        
    to_csv(list(tweets), filename='profile_data/'+user_name+'_tweets.csv')

    tweets_df = pd.read_csv('profile_data/'+user_name+"_tweets.csv")
    just_tweets=tweets_df[["text"]]
    ##remove urls 
    no_urls = just_tweets['text'].apply(lambda x: re.split('https:\/\/.*', str(x))[0])
    no_urls=no_urls.to_frame()

    # convert rows to a string
    tweets_string = ""
    for idx,row in no_urls.iterrows():
        tweets_string += (row['text'] + '. ')

    clean_text = re.sub("[^A-Za-z0-9. ]"," ",tweets_string)
    clean_text.strip()
    return clean_text

def fetch_usernames(filename, count):
    list_from_names = []
    i = 0
    print(f'Fetching profiles from {filename}')
    with open(filename) as f:
        if i < count:
            list_from_names = [line.rstrip() for line in f]
            i += 1
    usernames = []
    for person in list_from_names:
        usernames.append(get_profile(person)['twitter'])
    return usernames

def fetch_tweets(usernames):
    tweets = []
    op_file = open('information.txt','a')
    print('Fetching summaries => information.txt')
    for u in usernames:
        summary = tweet(u)
        op_file.write(summary + '\n')
    op_file.close()


def predict_personality(text):
    sentences = re.split("(?<=[.!?]) +", text)
    text_vector_31 = vectorizer_31.transform(sentences)
    text_vector_30 = vectorizer_30.transform(sentences)
    EXT = cEXT.predict(text_vector_31)
    NEU = cNEU.predict(text_vector_30)
    AGR = cAGR.predict(text_vector_31)
    CON = cCON.predict(text_vector_31)
    OPN = cOPN.predict(text_vector_31)
    st = f'EXT = {np.mean(EXT)}, NEU = {np.mean(NEU)}, AGR = {np.mean(AGR)}, CON = {np.mean(CON)}, OPN = {np.mean(OPN)}'
    return st

""""
----- VISUALISATION OF THE RESULTS ------
predictions = predict_personality(text)
print("predicted personality:", predictions)
df = pd.DataFrame(dict(r=predictions, theta=['EXT','NEU','AGR', 'CON', 'OPN']))
attrs = list(df['r'])

plt.rcParams["figure.figsize"] = (12, 6)
plt.style.use('ggplot')
plt.bar(['EXT','NEU','AGR', 'CON', 'OPN'],attrs, color ='green', alpha=0.5)
plt.xlabel("Attribute")
plt.ylabel("Tendency")
plt.title(user_name+"'s Personality Report")
plt.show() 
"""

def fetch_predictions():
    prediction_list = []
    summaries = []
    with open('information.txt','r') as f:
        summaries = [line.rstrip() for line in f]
    op_file = open('predictions.txt','a')
    for s in summaries:
        op_file.write(predict_personality(s) + '\n')
    print('Generated predictions => predictions.txt')
    op_file.close()


if __name__ == '__main__':

    #LOADING PRETRAINED MODELS
    cEXT = pickle.load( open( "models/cEXT.p", "rb"))
    cNEU = pickle.load( open( "models/cNEU.p", "rb"))
    cAGR = pickle.load( open( "models/cAGR.p", "rb"))
    cCON = pickle.load( open( "models/cCON.p", "rb"))
    cOPN = pickle.load( open( "models/cOPN.p", "rb"))
    vectorizer_31 = pickle.load( open( "models/vectorizer_31.p", "rb"))
    vectorizer_30 = pickle.load( open( "models/vectorizer_30.p", "rb"))

    #COMMAND LINE INPUT
    argumentList = sys.argv[1:]
    if len(argumentList) == 0:
        print('Please provide valid inputs\n FORMAT => $python3 predict_type.py --testcase <#> --inputfile <filename>')
        exit(0)
    long_options = ['testcase=', 'inputfile=']
    options = 't:i'
    count = 0
    filename = ''
    try:
    # Parsing argument
        arguments, values = getopt.getopt(argumentList, options,  long_options)
     
    # checking each argument
        for currentArgument, currentValue in arguments:
    
            if currentArgument in ('-t','--testcase'):
                count = int(currentValue)
            elif currentArgument in ('-i','--inputfile'):
                filename = currentValue
             
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))

    #DRIVER CODE
    usernames = fetch_usernames(filename, count)
    fetch_tweets(usernames)
    fetch_predictions()
