# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 15:39:16 2024

@credit: daniel mimouni

This code automatizes the interaction with instagram on the behalf of olvero_france

Developped for Relinquo
contact: daniel bodenheimer - daniel@relinquo.fr
"""
#############
# IMPORTS:  #
#############

# Import codes:
# bot (instapy)
from instapy import InstaPy
# non necessary: control API to enable posting
# this has to be set for all new account and has not been 
# implemented for olvero_france
from meta_API import *
# general imports
import pandas as pd
import numpy as np
import random
import time


    ############################################
    ############# Personal imports #############
    ##### Has to be provided by the client #####
    ############################################
hashtags = list(pd.read_csv('hashtags.csv').hashtags)
commentaires = list(pd.read_csv('commentaires.csv').commentaires)
very_basic_comments = list(pd.read_csv('very_basic_comments.csv').very_basic_comments)
inspiring_users = ['giovannainparis', 'parislivingway', 'joaquim.santos.paris',
                   'parisisincredible', 'paristumemanques', 'secrets_de_paris', 'sightseekersparis']


##################
# LAUNCH INSTA:  #
##################

# Open my session  
session = InstaPy(username='paris_pics_aesthetic', password='azertyU@2023', headless_browser=False,
                  geckodriver_path=r'C:\Users\dan15\OneDrive\Bureau\projet insta\automate_insta-main\paris_pics_aesthetic\INTERACT_insta\geckodriver-v0.33.0-win32/geckodriver.exe',
                  browser_executable_path=r'C:\Program Files\Mozilla Firefox\firefox.exe')
# login
session.login(check_infos=False)

# Definitions
"""
set_skip_users: skip private accounts or no (note that it is not always easy to assess an account is private yet)
set_do_follow: follow (%=100 BLOC 2, 0 Bloc 3 because account from # are too large) the author of a post
set_do_like: like (%=100%) a post
set_do_comment: comment (%=30%) a post
set_user_interact: interact with a certain nb (2 in BLOC 2 but the most the better) of post of a user
interact_user_followers: follow a certain number of user's followers
interact_user_likers: interact with a certain nb of likers from a certain nb of post
like_by_tags: interact with a certain nb of post from a list of #
unfollow_users: unfollow a certain nb of users after a certain time following them
"""

# Initialize general settings
session.set_skip_users(skip_private = True)
session.set_do_follow(enabled=True, percentage=100)
session.set_user_interact(amount=1, percentage=100, randomize=True)


##################
# INTERACTIONS:  #
##################

    
## BLOC 2 : Follow and like posts of someone who liked a post of inspiring_users
# to limit the nb of requests sent to instagram it's better to grab more users per post than 
# go through a lot of posts from the inspiring_users
users = [inspiring_users[i] for i in random.sample(range(0, len(inspiring_users)), 1)]
session.set_comments(comments=very_basic_comments)
session.set_do_comment(enabled=True, comment_liked_photo=False, percentage=33) 
session.set_do_like(enabled=True, percentage=100)
session.set_do_follow(enabled=True, percentage=100)
session.set_user_interact(amount=2, percentage=100, randomize=True)
session.interact_user_likers(users, posts_grab_amount=1, interact_likers_per_post=5, randomize=True)
print('Bloc 2 is done')
