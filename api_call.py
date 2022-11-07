# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 13:05:51 2022

@author: avanjavakam
"""
# code to save all data to a single file

import pandas as pd
import glob

path = './*.json'
files = glob.glob(path)

data_frames = []

for file in files:
    f = open(file, 'r', encoding="utf8")
    data_frames.append(pd.read_json(f))
    f.close()

pd.concat(data_frames).to_csv("data.csv")


with open('platforms.json', encoding='utf8') as f_input:
    df = pd.read_json(f_input)

df.to_csv('platforms.csv', encoding='utf-8', index=False)


with open('involved_companies.json', encoding='utf8') as f_input:
    df = pd.read_json(f_input)

df.to_csv('involved_companies.csv', encoding='utf-8', index=False)



with open('player_perspectives.json', encoding='utf8') as f_input:
    df = pd.read_json(f_input)

df.to_csv('player_perspectives.csv', encoding='utf-8', index=False)


with open('themes.json', encoding='utf8') as f_input:
    df = pd.read_json(f_input)

df.to_csv('themes.csv', encoding='utf-8', index=False)



from igdb.wrapper import IGDBWrapper
wrapper = IGDBWrapper("xxxxx", "xxxxx")


#querying game data. This is the dataset I will be using for analysis.
for i in range(0, 210000, 500):

    '''With a wrapper instance already created'''
    # JSON API request
    byte_array = wrapper.api_request(
            'games',
            'fields age_ratings,aggregated_rating,aggregated_rating_count,category,created_at,dlcs,expanded_games,expansions,external_games,first_release_date,follows,forks,franchise,franchises,game_engines,game_modes,genres,hypes,involved_companies,multiplayer_modes,name,parent_game,platforms,player_perspectives,ports,rating,rating_count,release_dates,remakes,remasters,screenshots,similar_games,slug,standalone_expansions,status,storyline,summary,tags,themes,total_rating,total_rating_count,updated_at,url,version_parent,version_title,videos,websites; limit 500; offset' + str(i) + ';'            
          )

    data = json.loads(byte_array)
    data_1 = pd.json_normalize(data)
    data_frames.append(pd.DataFrame(data_1))


pd.concat(data_frames).to_csv("data_200K.csv")


# querying genres mappings
data_frames = []
'''With a wrapper instance already created'''
# JSON API request
byte_array = wrapper.api_request(
            'genres',
            'fields *; limit 500;'            
          )
df = pd.read_json(byte_array)
df.to_csv('genres.csv', encoding='utf-8', index=False)


# querying companies mappings

data_frames = []
for i in range(0, 50000, 500):

    '''With a wrapper instance already created'''
    # JSON API request
    byte_array = wrapper.api_request(
            'companies',
            'fields *; limit 500; offset' + str(i) + ';'            
          )

    data = json.loads(byte_array)
    data = pd.json_normalize(data)
    data_frames.append(pd.DataFrame(data))


pd.concat(data_frames).to_csv("companies.csv")

# querying involved_companies mappings
data_frames = []
for i in range(0, 200000, 500):

    '''With a wrapper instance already created'''
    # JSON API request
    byte_array = wrapper.api_request(
            'involved_companies',
            'fields *; limit 500; offset' + str(i) + ';'            
          )

    data = json.loads(byte_array)
    data = pd.json_normalize(data)
    data_frames.append(pd.DataFrame(data))


pd.concat(data_frames).to_csv("involved_companies.csv")


# querying age_ratings mappings
data_frames = []
for i in range(0, 200000, 500):

    '''With a wrapper instance already created'''
    # JSON API request
    byte_array = wrapper.api_request(
            'age_ratings',
            'fields *; limit 500; offset' + str(i) + ';'            
          )

    data = json.loads(byte_array)
    data = pd.json_normalize(data)
    data_frames.append(pd.DataFrame(data))


pd.concat(data_frames).to_csv("age_ratings.csv")

#age_rating_content_descriptions
data_frames = []
for i in range(0, 100000, 500):

    '''With a wrapper instance already created'''
    # JSON API request
    byte_array = wrapper.api_request(
            'age_rating_content_descriptions',
            'fields *; limit 500; offset' + str(i) + ';'            
          )

    data = json.loads(byte_array)
    data = pd.json_normalize(data)
    data_frames.append(pd.DataFrame(data))

pd.concat(data_frames).to_csv("age_rating_content_descriptions.csv")