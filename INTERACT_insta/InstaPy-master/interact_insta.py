# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 16:12:28 2023

@author: mimounid

tests for my own instapy version
"""

from instapy import InstaPy
import pandas as pd
import random
import time


# import data
hashtags = list(pd.read_csv('hashtags.csv').hashtags)
commentaires = list(pd.read_csv('commentaires.csv').commentaires)
very_basic_comments = list(pd.read_csv('very_basic_comments.csv').very_basic_comments)
inspiring_users = ['giovannainparis', 'parislivingway']

# My code using InstaPy package components goes here
session = InstaPy(username='paris_pics_aesthetic', password='azertyU@2023', headless_browser=False,
                  geckodriver_path=r'C:\Users\mimounid\Desktop\perso\instaloader\insta_automation\geckodriver-v0.33.0-win32/geckodriver.exe',
                  browser_executable_path=r'C:\Users\mimounid\AppData\Local\Mozilla Firefox\firefox.exe')

session.login()
#%%

session.set_skip_users(skip_private = False)
session.set_do_follow(enabled=True, percentage=100)
session.set_user_interact(amount=1, percentage=100, randomize=True)

# # Follow followers of some accounts
# session.set_do_like(enabled=False, percentage=0)
# session.interact_user_followers(usernames=['julieaucontraire'], amount=20, randomize=True)

# # Unfollow people:
# for i in range(5):
#     # session.set_dont_unfollow_active_users(enabled= True, posts= 4, boundary= 500) #doês not work yet
    # session.unfollow_users(amount=100, delay_followbackers=172800) #aproximatelly 2 days
    # time.sleep(60*15)

for i in range(3):
    
    # Follow followers of some accounts
    session.set_do_like(enabled=False, percentage=0)
    # check the time spent to choose if instagram let me do a quick_follow routine or not:
    # start = time.time()
    # session.interact_user_followers(usernames=['giovannainparis'], amount=100, randomize=True, quick_follow=True,)
    # print(time.time() - start)
    # if time.time() - start < 60: # it means I could not use quick_follow
    users = [inspiring_users[i] for i in random.sample(range(0, len(inspiring_users)), 1)]
    session.interact_user_followers(usernames=users, amount=50, randomize=True, quick_follow=False,)
    
    time.sleep(60*20)
    
    # Follow and like posts of someone who liked a post of a similar account
    session.set_comments(comments=very_basic_comments)
    session.set_do_comment(enabled=True, comment_liked_photo=False, percentage=30)
    session.set_do_like(enabled=True, percentage=100)
    users = [inspiring_users[i] for i in random.sample(range(0, len(inspiring_users)), 1)]
    session.interact_user_likers(users, posts_grab_amount=3, interact_likers_per_post=10, randomize=True)
    
    time.sleep(60*30)
    
    # Unfollow some followings
    session.unfollow_users(amount=100, delay_followbackers=172800) #aproximatelly 2 days
    
    time.sleep(60*15)
    
    
    # Like and comment relatable hashtags:
    nb_hashtags = 3
    list_hashtags = [hashtags[i] for i in random.sample(range(0, len(hashtags)), nb_hashtags)]
    session.set_do_follow(enabled=True, percentage=100)
    session.set_comments(comments=commentaires)
    session.set_do_comment(enabled=True, comment_liked_photo=False,percentage=30)
    session.set_user_interact(amount=2, randomize=True, percentage=100)
    session.like_by_tags(list_hashtags, amount=4, randomize=True, interact=False) # it is better not to interact because it could lead to comment irrelevantly pictures

    time.sleep(60*30)
    
    
    
    

    
#%%
    
# to make work:
# session.follow_user_followers(
#         self,
#         usernames: list,
#         amount: int = 10,
#         randomize: bool = False,
#         interact: bool = False,
#         sleep_delay: int = 600,
#     )


    
# session.like_by_feed_generator(
#     self,
#     amount: int = 50,
#     randomize: bool = False,
#     unfollow: bool = False,
#     interact: bool = False,
# )

    