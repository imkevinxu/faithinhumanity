# Threading the tweet_scraper command in the same process as the web app
import threading
from faithinhumanity_app.management.commands.tweet_scraper import Command as tweet_scraper

t = threading.Thread(target=tweet_scraper().handle)
t.setDaemon(True)
t.start()