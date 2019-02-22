"""
360 Insta Schedule
"""

# imports
from instapy import InstaPy
from instapy.util import smart_run
from instapy import set_workspace
import schedule
import time

# login credentials
insta_username = 'drip.wear'
insta_password = 'ThreeSixty30'

#-Hashtag Databases-
#hashtagdb = ["urbanwear","streetwear","fashion","streetstyle","streetfashion","style","hiphop","urbanstyle","urbanfashion","mensfashion","urban","menswear","clothing","design","rap","photography","ootd","urbanclothing","instagood","supreme","streetclothing","clothingbrand","art","streetwearfashion","skateboarding","tshirt","apparel","clothes","skate","bhfyp"]
hashtagdb = ["hiphop","xxxtentacion","worldstar","trap","rap","rapper","soundcloud","producer","newsong","instamusic","studio","hiphopculture","losangeles","beat"]

# Neem deze accounts niet mee in de script
excludeaccounts = ["kaije5","krisrobertson","360allround"]

ef job_Unfollow():
  # get an InstaPy session!
  session = InstaPy(username=insta_username,
                    password=insta_password,
                    headless_browser=True)

  with smart_run(session):
      session.set_dont_include(excludeaccounts)
          #Unfollow non Followers
          session.unfollow_users(amount=100, nonFollowers=True, style="FIFO", unfollow_after=3*24*60*60, sleep_delay=0)
ef job_LikeByHashtags():
  # get an InstaPy session!
  session = InstaPy(username=insta_username,
                    password=insta_password,
                    headless_browser=True)

with smart_run(session):

# Te gebruiken Hashtags

# activities

#--Interact--
#like by hashtag then like their account
session.set_user_interact(amount=3, randomize=True, percentage=100)
session.like_by_tags(hashtagdb, amount=10, interact=True)

schedule.every().day.at("6:35").do(job)
schedule.every().day.at("16:22").do(job)

while True:
  schedule.run_pending()
  time.sleep(10)

""""
with smart_run(session):



    # Like our feed
    session.like_by_feed(amount=100, randomize=False, unfollow=True, interact=True)


    #Follow someone elses Follower

    #comment
""""
