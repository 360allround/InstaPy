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

# Hashtag Databases
hashtagdb_Store = ["urbanwear","streetwear","fashion","streetstyle","streetfashion","style","hiphop","urbanstyle","urbanfashion","mensfashion","urban","menswear","clothing","design","rap","photography","ootd","urbanclothing","instagood","supreme","streetclothing","clothingbrand","art","streetwearfashion","skateboarding","tshirt","apparel","clothes","skate","bhfyp"]
hashtagdb = ["hiphop","xxxtentacion","worldstar","trap","rap","rapper","soundcloud","producer","newsong","instamusic","studio","hiphopculture","losangeles","beat"]

# Neem deze accounts niet mee in de script
excludeaccounts = ["kaije5","krisrobertson","360allround"]

# define session and get
  session = InstaPy(username=insta_username,
                    password=insta_password,
                    headless_browser=True)

def job_Unfollow():
  print("Started unfollow")

  with smart_run(session):
    # Exclude these accounts
    session.set_dont_include(excludeaccounts)
    # Unfollow non Followers
    session.unfollow_users(amount=100, nonFollowers=True, style="FIFO", unfollow_after=3*24*60*60, sleep_delay=0)

def job_LikeByHashtags():
  print("Started Like by hashtag")
  
  with smart_run(session):
    # Exclude these accounts
    session.set_dont_include(excludeaccounts)
    # like by hashtag then like their account
    session.set_user_interact(amount=3, randomize=True, percentage=100)
    session.like_by_tags(hashtagdb, amount=10, interact=True)

def job_FollowByAccount():
  print("Started Follow by account")

  with smart_run(session):
    # Exclude these accounts
    session.set_dont_include(excludeaccounts)
    # Follow someone elses Follower

def job_CommentActivity():
  print("Started Commenting")

  with smart_run(session):
    # Exclude these accounts
    session.set_dont_include(excludeaccounts)
    # comment

# Schedules
schedule.every().hour.do(job_Unfollow)


while True:
  schedule.run_pending()
  time.sleep(10)