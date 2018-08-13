#from django.shortcuts import render
from django.http import HttpResponse

from ciscosparkapi import CiscoSparkAPI
import feedparser
import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context
import config
import hashlib
import logging

from .models import Feed, Link

LOG_LEVEL = config.LOG_LEVEL
LOG_FILE = config.LOG_FILE
logging.basicConfig(
    filename=LOG_FILE,
    level=LOG_LEVEL,
    format="%(asctime)s:%(levelname)s:%(message)s"
    )

SENDER_ID = config.SENDER_ID
ROOM_ID = config.ROOM_ID

api = CiscoSparkAPI(access_token=SENDER_ID)

def output():
  logging.debug('Looking through feeds...')
  myFeeds = Feed.objects.all()
  logging.debug('Found ' + str(myFeeds.count()) + ' feeds...')
  for feed in myFeeds:
    URL = feed.linkFile
    logging.debug('Found this URL: ' + str(URL))
    c = feedparser.parse(URL)
    numLinks = min(5, len(c.entries))
    logging.debug('Will go through ' + str(numLinks) + ' entries')
    i = 0
    while i < numLinks:
      logging.debug('-----Iteration ' + str(i) + ' -----')
      title = c.entries[i].title
      logging.debug(title)
      link = c.entries[i].link
      logging.debug(link)
      linkId = hashlib.md5(c.entries[i].id.encode()).hexdigest()
      logging.debug(linkId)
      newLink = False
      try:
        l = Link.objects.get(linkId = linkId)
        newLink = False
      except:
        l = Link(parentFeed = feed, linkId=linkId)
        l.save()
        newLink = True
      logging.debug(newLink)
      if newLink:
        mdown = "[" + title + "](" + link + ")"
        api.messages.create(roomId=ROOM_ID, markdown=mdown)
      i += 1
  return HttpResponse(status=200)
