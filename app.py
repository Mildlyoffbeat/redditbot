import praw

reddit = praw.Reddit(
    client_id="my client id"
    client_secret="my client secret"
    user_agent="my user agent"
)
print(reddit.read_only)
# Output: True

for submission in reddit.subreddit("learnpython").hot(limit=10):
    print(submission.title)

# Output: 10 submissions