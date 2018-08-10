#from django.shortcuts import render
from django.http import HttpResponse

from ciscosparkapi import CiscoSparkAPI
import feedparser
import config

SENDER_ID = config.SENDER_ID
ROOM_ID = config.ROOM_ID

api = CiscoSparkAPI(access_token=SENDER_ID)

def index(request):
  URL = 'https://newsroom.cisco.com/data/syndication/rss2/enterprise_networking_20.xml'
  c = feedparser.parse(URL)
  print(c)
  title = c.entries[0].title
  print(title)
  link = c.entries[0].link
  print(link)
  mdown = "[" + title + "](" + link + ")"
  api.messages.create(roomId=ROOM_ID, markdown=mdown)
  return HttpResponse(status=200)
