from googlesearch import search
import re

def get_profile(keyword):
  results = list(search(keyword))
  profiles = {
      'twitter': '',
      'facebook': '',
      'linkedin':''
  }
  for r in results:
    if r.find('twitter') != -1 and profiles['twitter'] == '':
      r = re.search(r'https://twitter.com/([^/?]+)', r).group(1)
      profiles['twitter'] = r
    if r.find('facebook') != -1 and profiles['facebook'] == '':
      r = re.search(r'https://www.facebook.com/([^/?]+)', r).group(1)
      profiles['facebook'] = r
    if r.find('linkedin') != -1 and profiles['linkedin'] == '':
      r = re.search(r'https://in.linkedin.com/in/([^/?]+)', r).group(1)
      profiles['linkedin'] = r
  return profiles
