## SmartScrapes
Predicting the personality of the user based on their social activity

## Workflow of the project ##
### 1. Searching a profile ###

``` python
from googlesearch import search
import re

def get_profile(keyword):
  results = list(search(keyword, num=10))
  profiles = {
      'twitter': '',
    #   'facebook': '',
    #   'linkedin':''
  }
  for r in results:
    if r.find('twitter') != -1 and profiles['twitter'] == '':
      r = re.search(r'https://twitter.com/([^/?]+)', r).group(1)
      profiles['twitter'] = r
    # if r.find('facebook') != -1 and profiles['facebook'] == '':
    #   r = re.search(r'https://www.facebook.com/([^/?]+)', r).group(1)
    #   profiles['facebook'] = r
    # if r.find('linkedin') != -1 and profiles['linkedin'] == '':
    #   r = re.search(r'https://in.linkedin.com/in/([^/?]+)', r).group(1)
    #   profiles['linkedin'] = r
  return profiles
```
### 2. Getting text from user tweets ###
``` python
def get_text_from_tweets(user_name):
    tweets = twt.user(user_name, 
                    count=1000, 
                    exclude_replies=False, 
                    include_retweets=True)
        
    to_csv(list(tweets), filename=user_name+'_tweets.csv')

    tweets_df = pd.read_csv(user_name+"_tweets.csv")
    just_tweets=tweets_df[["text"]]
    ##remove urls 
    no_urls = just_tweets['text'].apply(lambda x: re.split('https:\/\/.*', str(x))[0])
    #just_text_from_tweets.head(50)
    no_urls=no_urls.to_frame()

    # convert rows to a string
    tweets_string = ""
    for idx,row in no_urls.iterrows():
        tweets_string += (row['text'] + '. ')

    clean_text = re.sub("[^A-Za-z0-9. ]"," ",tweets_string)
    clean_text = clean_text.strip()
    return(clean_text)
```
### 3. Predicting Personality ###
``` python
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
```
### 4. Displaying Results ###
``` python
def display_results(text, user_name):
    predictions = predict_personality(text)
    #print("predicted personality:", predictions)
    df = pd.DataFrame(dict(r=predictions, theta=['EXT','NEU','AGR', 'CON', 'OPN']))
    attrs = list(df['r'])
    plt.rcParams["figure.figsize"] = (12, 6)
    plt.style.use('ggplot')
    plt.bar(['EXT','NEU','AGR', 'CON', 'OPN'],attrs, color ='green', alpha=0.5)
    plt.xlabel("Attribute")
    plt.ylabel("Tendency")
    plt.title(user_name+"'s Personality Report")
    plt.show()
```
## Setup ##
1. Clone the project
```
git clone https://github.com/Mainakdeb/e_summit.git
```
2. Go to specific Directory 
```
cd e_summit
```
3. Install the requirements from / requirements.txt file
``` python
pip install -r requirements.txt
```
## Usage ##
### 1.  via CLI ###  

   Add desired names in names.txt along with some keywords(Already some have been included).
   
   Run the command down below  
   
   ```
   python3 predict_type.py --testcase 7 --inputfile "names.txt"
   ```
   See the output using:
   ```
   cat predictions.txt
   ```
### 2. Run on Google Collab ###
   Link for collab
## Tasks completed ##


## What's next? ##

