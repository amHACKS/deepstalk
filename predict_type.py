import pickle
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
#from data_prep import DataPrep
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from profilescraper import get_profile
from socialreaper import Twitter
from socialreaper.tools import to_csv
import re, os
import getopt, sys
from glob import glob
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
    return {'usernames':usernames, 'names':list_from_names}

def fetch_tweets(usernames):
    tweets = []
    op_file = open('information.txt','a')
    print('Fetching summaries => information.txt')
    for u in usernames:
        summary = tweet(u)
        op_file.write(summary + '\n')
    op_file.close()


def predict_personality(X):
        X=[X]
        predictions = {}
        traits = ['OPN', 'CON', 'EXT', 'AGR', 'NEU']
        for trait in traits:
            pkl_model = models[trait]
            trait_scores = pkl_model.predict(X, regression=True).reshape(1, -1)
            # scaler = MinMaxScaler(feature_range=(0, 50))
            # print(scaler.fit_transform(trait_scores))
            # scaled_trait_scores = scaler.fit_transform(trait_scores)
            predictions['pred_s'+trait] = trait_scores.flatten()[0]
            # predictions['pred_s'+trait] = scaled_trait_scores.flatten()

            trait_categories = pkl_model.predict(X, regression=False)
            predictions['pred_c'+trait] = str(trait_categories[0])
            # predictions['pred_c'+trait] = trait_categories

            trait_categories_probs = pkl_model.predict_proba(X)
            predictions['pred_prob_c'+trait] = trait_categories_probs[:, 1][0]
            # predictions['pred_prob_c'+trait] = trait_categories_probs[:, 1]
        return predictions

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

def fetch_predictions(usernames):
    prediction_list = []
    summaries = []
    with open('information.txt','r') as f:
        summaries = [line.rstrip() for line in f]
    op_file = open('predictions.txt','a')
    for s in range(len(summaries)):
        op_file.write(usernames[s] + ' => [' + str(predict_personality(summaries[s])) + ']' + '\n')
    print('Generated predictions => predictions.txt')
    op_file.close()


if __name__ == '__main__':

    #LOADING PRETRAINED MODELS

    class Model():
        def __init__(self):
            self.rfr = RandomForestRegressor(bootstrap=True,
            max_features='sqrt',
            min_samples_leaf=1,
            min_samples_split=2,
            n_estimators= 200)
            self.rfc = RandomForestClassifier(max_features='sqrt', n_estimators=110)
            self.tfidf = TfidfVectorizer(stop_words='english', strip_accents='ascii')

        def fit(self, X, y, regression=True):
            X = self.tfidf.fit_transform(X)
            if regression:
                self.rfr = self.rfr.fit(X, y)
            else:
                self.rfc = self.rfc.fit(X, y)

        def predict(self, X, regression=True):
            X = self.tfidf.transform(X)
            if regression:
                return self.rfr.predict(X)
            else:
                return self.rfc.predict(X)

        def predict_proba(self, X, regression=False):
            X = self.tfidf.transform(X)
            if regression:
                raise ValueError('Cannot predict probabilites of a regression!')
            else:
                return self.rfc.predict_proba(X)

    M = Model()
    models={}
    traits = ['OPN', 'CON', 'EXT', 'AGR', 'NEU']
    for trait in traits:
        with open('models/' + trait + '_model.pkl', 'rb') as f:
            models[trait] = pickle.load(f)

    #CLEAR PREVIOUS OUTPUTS
    if os.path.exists('information.txt'):
        os.remove('information.txt')
    if os.path.exists('predictions.txt'):
        os.remove('predictions.txt')
    files = glob('profile_data/*')
    for f in files:
        os.remove(f)

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
    profile_dict = fetch_usernames(filename, count)
    usernames = profile_dict['usernames']
    fetched_names = profile_dict['names']
    names = []
    for f in fetched_names:
        name = f.split(',')[0]
        names.append(name)
    fetch_tweets(usernames)
    fetch_predictions(names)
