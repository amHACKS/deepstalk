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

