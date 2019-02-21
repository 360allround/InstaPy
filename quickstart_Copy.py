"""
360 Insta Schedule
"""

# imports
from instapy import InstaPy
from instapy.util import smart_run

# login credentials
insta_username = 'drip.wear'
insta_password = 'ThreeSixty30'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
    # Neem deze accounts niet mee in de script
    excludeaccounts = ["kaije5","krisrobertson","360allround"]
    session.set_dont_include(excludeaccounts)
    # Te gebruiken Hashtags
    hashtagdb = ["urbanwear","streetwear","fashion","streetstyle","streetfashion","style","hiphop","urbanstyle","urbanfashion","mensfashion","urban","menswear","clothing","design","rap","photography","ootd","urbanclothing","instagood","supreme","streetclothing","clothingbrand","art","streetwearfashion","skateboarding","tshirt","apparel","clothes","skate","bhfyp"]


    # activities

    #like by hashtag then like their account
    #session.set_user_interact(amount=3, randomize=True, percentage=100)
    #session.like_by_tags(hashtagdb, amount=10, interact=True)

    # Like our feed
    #session.like_by_feed(amount=100, randomize=False, unfollow=True, interact=True)

    #Unfollow non Followers
    session.unfollow_users(amount=100, nonFollowers=True, style="FIFO", unfollow_after=3*24*60*60, sleep_delay=655)
