import praw
import time

from secret import client_id, client_secret, password

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent="<console:testbott:1.0>",
    username="test-bott",
    password=password
)

for submission in reddit.subreddit("learnpython").hot(limit=10):

    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        comment_lower = top_level_comment.body.lower()
        if " bot " in comment_lower:

            top_level_comment.reply("Did someone say my name? Oh, wait...sorry. My creator is still learning - don't be mad! :)")
            time.sleep(660)