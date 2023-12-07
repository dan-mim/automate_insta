# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 16:12:28 2023

@author: mimounid

tests for my own instapy version
"""

from instapy import InstaPy
import pandas as pd
import numpy as np
import random
import time


# import data
hashtags = list(pd.read_csv('hashtags.csv').hashtags)
commentaires = list(pd.read_csv('commentaires.csv').commentaires)
very_basic_comments = list(pd.read_csv('very_basic_comments.csv').very_basic_comments)
inspiring_users = ['giovannainparis', 'parislivingway', 'joaquim.santos.paris',
                   'parisisincredible', 'paristumemanques', 'secrets_de_paris', 'sightseekersparis']

# Open my sesssion  paris_pics_aesthetic  azertyU@2023
session = InstaPy(username='paris_pics_aesthetic', password='azertyU@2023', headless_browser=False,
                  geckodriver_path=r'C:\Users\mimounid\Desktop\perso\instaloader\insta_automation\geckodriver-v0.33.0-win32/geckodriver.exe',
                  browser_executable_path=r'C:\Users\mimounid\AppData\Local\Mozilla Firefox\firefox.exe')
# login
session.login()

# General settings
session.set_skip_users(skip_private = True)
session.set_do_follow(enabled=True, percentage=100)
session.set_user_interact(amount=1, percentage=100, randomize=True)


for i in range(1):
    # Unfollow some followings
    session.unfollow_users(amount=100, delay_followbackers=172800) #aproximatelly 2 days
        
    time.sleep(60*30)

l = []
for i in range(3):
    st = time.time()
    
    # Follow followers of some accounts
    session.set_do_like(enabled=False, percentage=0)
    # check the time spent to choose if instagram let me do a quick_follow routine or not:
    # start = time.time()
    # # Quick follow routine: (does not work well unfortunately)
    # session.interact_user_followers(usernames=['giovannainparis'], amount=100, randomize=True, quick_follow=True,)
    # print(time.time() - start)
    # if time.time() - start < 60: # it means I could not use quick_follow
    users = [inspiring_users[i] for i in random.sample(range(0, len(inspiring_users)), 1)]
    session.interact_user_followers(usernames=users, amount=20, randomize=True, quick_follow=False,)
    
    time.sleep(60*10)
    
    # Follow and like posts of someone who liked a post of a similar account
    session.set_comments(comments=very_basic_comments)
    session.set_do_comment(enabled=True, comment_liked_photo=False, percentage=30)
    session.set_do_like(enabled=True, percentage=100)
    users = [inspiring_users[i] for i in random.sample(range(0, len(inspiring_users)), 1)]
    session.interact_user_likers(users, posts_grab_amount=2, interact_likers_per_post=10, randomize=True)
    
    
    time.sleep(60*10)
    users = [inspiring_users[i] for i in random.sample(range(0, len(inspiring_users)), 1)]
    session.interact_user_followers(usernames=users, amount=20, randomize=True, quick_follow=False,)
    
    time.sleep(60*30)
    
    # Like and comment relatable hashtags:
    nb_hashtags = 2
    list_hashtags = [hashtags[i] for i in random.sample(range(0, len(hashtags)), nb_hashtags)]
    session.set_do_follow(enabled=True, percentage=100)
    session.set_comments(comments=commentaires)
    session.set_do_comment(enabled=True, comment_liked_photo=False,percentage=30)
    session.set_user_interact(amount=2, randomize=True, percentage=100)
    session.like_by_tags(list_hashtags, amount=3, randomize=True, interact=False) # it is better not to interact because it could lead to comment irrelevantly pictures
    
    
    
    time.sleep(60*30)
    
    end = time.time()
    l.append(np.round((end-st)/60, 2))
    df = pd.DataFrame({'l_tps':l})
    df.to_csv('l_tps.csv')
    
    

    