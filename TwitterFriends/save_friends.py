# export TWITTER_CONSUMER_KEY=s6ngzSsznfKlAVrOzf7PVxJki
# export TWITTER_CONSUMER_SECRET=0sxA71SgHXVfJIdin5LhoQ9XxNKug0qzh8OBVbFP2MqWsaolJU
# export TWITTER_ACCESS_TOKEN=480616828-HHfeoAO1P4GNwddR2OSybjxveatw41k6EeEAE9jB
# export TWITTER_ACCESS_TOKEN_SECRET=cFFi3OzlapGCEQo4JTDLSSC4YOqT5XtDBvRQ4VaUlZDMX
from os import environ
environ.setdefault("DJANGO_SETTINGS_MODULE", "TwitterFriends.settings")
import django
django.setup()
import tweepy
from findfriends.models import TwitterUser

def save_user(user):
    if not TwitterUser.objects.filter(user_id=user.id).exists():
        print("Saving: ",user.screen_name)
        u = TwitterUser()
        u.user_id = user.id
        u.screen_name = user.screen_name
        u.is_verified = user.verified
        u.location = user.location
        u.save()
    else:
        print(user.screen_name, " is already on the data base")


def get_and_save_friends(user_id):
    global n_calls
    for friend in tweepy.Cursor(api.friends, user_id=user_id, count=200).items():
        save_user(friend)

auth = tweepy.OAuthHandler(environ["TWITTER_CONSUMER_KEY"], 
                           environ["TWITTER_CONSUMER_SECRET"])
auth.set_access_token(environ["TWITTER_ACCESS_TOKEN"], 
                      environ["TWITTER_ACCESS_TOKEN_SECRET"])
api = tweepy.API(auth_handler=auth, wait_on_rate_limit_notify=True, 
    wait_on_rate_limit=True)

me = api.me()
save_user(me)

get_and_save_friends(user_id=me.id)
amigos = api.friends_ids(user_id=me.id)
for amigo in amigos:
    get_and_save_friends(user_id=amigo)
