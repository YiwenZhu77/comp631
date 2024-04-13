# %%
# crawl data from wikipedia using wikipedia-api

import json
import re
import os

# %%
# iterate to get subcategories up to depth 4
def get_subcategories(cate, depth, level=0):
    url="https://en.wikipedia.org/w/api.php?action=query&format=json&list=categorymembers&cmtitle=" +cate + "&cmlimit=max"
    response = requests.get(url)
    data = response.json()

    members=data['query']['categorymembers']

    # if categorymembers is null, return
    if members == []:
        return

    # add categorymembers that are not subcategories to the list
    subcategories = [page['title'] for page in members if page['ns'] == 14]
    artTitles.extend([page['title'] for page in members if (page['ns'] == 0)or (page['ns'] == 2)])
    subcateTitles.extend(subcategories)
    
    # if level is less than depth, iterate to get subcategories
    if level < depth:
        for subcategory in subcategories:
            get_subcategories(subcategory, depth, level + 1)
    
# Retrieve all subcategories under the category "Space physics" up to subcategory depth of 4
artTitles=[]
subcateTitles=[]
get_subcategories("Category:Space_science",4 )

# %% save to pickle
import pickle
with open('subcateTitles.pkl', 'wb') as f:
    pickle.dump(subcateTitles, f)
with open('artTitles.pkl', 'wb') as f:
    pickle.dump(artTitles, f)