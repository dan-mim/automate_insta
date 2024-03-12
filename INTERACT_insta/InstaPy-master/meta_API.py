# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 20:31:12 2023

@author: mimounid
"""
import requests
import json
import pandas as pd
import numpy as np

# data
df_posts = pd.read_excel('00_pics_to_post_all.xlsx')
df_posts = df_posts[['caption_to_post', 'image_urls']]

# data to post with instagram API
access_token_meta = 'EAAC3MDg6OKcBO6SjtRcDsBegEKph3ONn37DQlkO53oKOdE8p6ZAHvpM4fZAkMb2NCfWw8yjoCKUAas01sbPvCjOZC3yQLvEJcZCSHImUFFUA6NfD3PjAtN67ExylyMRgUG3BB1P8oH4N0soI1ZCo6AkP1WPeuZCwWfdHDHTDncs0dlshQ2nwObQsGaZBlHwnPny'
#'EAAC3MDg6OKcBO7EiJvnNRpEw0kc12AiktoOcrWSCEhFCFVLxExcz4Repi2amdBdEk7HhyFMIo7m8ZBVxG7S9Aw3QR7JbTVEoZAuhD5XjTKrST5f2K6V5xNNqFpJgwiVZCh88xVEIn4TVgnDntAEiSu1OgdKzlzLXIooakEo2ltC41oX7JGZB3zeiwZCZBEeiD5'
#'EAAC3MDg6OKcBO7XiGglpTIZCra9szJZBie6pZBvXb8ZBJG8p7o2B74yXqnhPyriJi1YYLhitQkomGN0gNs1qnyvD18KUoEyymGGZBZBZBU58KZB5QMleWl5i8WDT0gKGs6EwJXaleg61ZBn26V0QwKBslJPSuZChhEFzKuABqJTVRGZANZCIs9THLMTA6IGqMCEGj8m6'
insta_ID = '17841456369812963'
insta_code = 'azertyU@2023'
graph_url = 'https://dan-mim.github.io/'



def publish_image(image_url1, caption_pic):
    
    access_token = access_token_meta
    ig_user_id = insta_ID
    image_url = image_url1
    
    # cant make the location work :()
    # list_locations = ['6889842', '4883504', '542498473',  '1860258650870020']
    # location_id = '1423220914594882'  #list_locations[np.random.randint(len(list_locations))]
    # dans le payload: 'location_id':location_id,
    
    post_url = f'https://graph.facebook.com/v18.0/{ig_user_id}/media'
    
    caption_pic.replace('_x000D_', '')  # c'est un beug de saut de ligne et d 'emoji que je corrige
    payload = {
        'image_url' :image_url,
        'caption': caption_pic,
        'access_token':access_token
        }
    r = requests.post(post_url, data=payload)
    print(r.text)
    print('Media uploaded successfully')
    
    results = json.loads(r.text)
    
    if 'id' in results:
        creation_id = results['id']
        second_url =  f'https://graph.facebook.com/v18.0/{ig_user_id}/media_publish'
        second_payload = {
            'creation_id':creation_id,
            'access_token':access_token
            }
        r  = requests.post(second_url, data=second_payload)
        print(r.text)
        print("Image published to instagram")
    
    else:
        print('Image posting is not possible')

# post a pic
# nb = 76
# image_url1 = df_posts.iloc[nb].image_urls
# caption_pic = df_posts.iloc[nb].caption_to_post
# publish_image(image_url1, caption_pic)

# #%% Get the data of another account
# """
# Limitations of the method:
# 1. The user should have an Instagram business account.
# 2. The user account should be public.
# """

# graph_url = 'https://graph.facebook.com/v18.0/'
# def func_get_business_account_deatils(search_id ,ig_user_id ,access_token):
#     url = graph_url + ig_user_id 
#     param = dict()
#     param['fields'] = f'business_discovery.username({search_id})'+'{followers_count,follows_count,name,biography,username,profile_picture_url,id, media_count,media{comments_count,like_count,media_url,permalink,user_name,caption,timestamp,media_type,media_product_type}}'
#     param['access_token'] = access_token
#     response = requests.get(url, params=param)
#     response = response.json()
#     return response

# datas = func_get_business_account_deatils('lesfacadesdeparis' ,insta_ID ,access_token_meta)
# # print(datas)
# print(f" followers_count =  {datas['business_discovery']['followers_count']}")
# media_urls = []
# for media in datas['business_discovery']['media']['data']:
#     media_urls.append(media['media_url'])
