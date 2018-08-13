#from django.shortcuts import render
from django.http import HttpResponse

from ciscosparkapi import CiscoSparkAPI
import feedparser
import config
import hashlib

from .models import Feed, Link

SENDER_ID = config.SENDER_ID
ROOM_ID = config.ROOM_ID

api = CiscoSparkAPI(access_token=SENDER_ID)

def output():
  myFeeds = Feed.objects.all()
  for feed in myFeeds:
    URL = feed.linkFile
    c = feedparser.parse(URL)
    numLinks = min(5, len(c.entries))
    i = 0
    while i < numLinks:
      print(i)
      title = c.entries[i].title
      print(title)
      link = c.entries[i].link
      print(link)
      linkId = hashlib.md5(c.entries[i].id.encode()).hexdigest()
      print(linkId)
      newLink = False
      try:
        l = Link.objects.get(linkId = linkId)
        newLink = False
      except:
        l = Link(parentFeed = feed, linkId=linkId)
        l.save()
        newLink = True
      print(newLink)
      if newLink:
        mdown = "[" + title + "](" + link + ")"
        api.messages.create(roomId=ROOM_ID, markdown=mdown)
      i += 1
  return HttpResponse(status=200)
