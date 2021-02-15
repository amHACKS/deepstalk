from googlesearch import search
import re
# pip install googlesearch-python  --ignore-installed certifi

def get_profile(keyword):
  print("getting profiles from google..")
  results = list(search(keyword, num_results=10))
  profiles = {
      'twitter': ''
  }
  for r in results:
    if r.find('twitter') != -1 and profiles['twitter'] == '':
      r = re.search(r'https://twitter.com/([^/?]+)', r).group(1)
      profiles['twitter'] = r

  return profiles
