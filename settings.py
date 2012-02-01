# -*- coding: utf-8 -*-#
#
# Copyright 2011 nerdhurders hurd@nerhurder.com
#

import calendar

try:
    import simplejson as json
except:
    import json

json_data = open('people.json')
NERDS = json.load(json_data)

LUNCH_HOUR = 13
LUNCH_WEEKDAY = calendar.THURSDAY

# brace for ugly ass comprehension:
WHO = [ nerd['name'] for nerd in NERDS if nerd['rsvp']==True ]
GUESTS = sum([ nerd['guests'] for nerd in NERDS if nerd['rsvp']==True ])

# Keep track of overall number of people
COUNT = len(WHO) + GUESTS

# this WHEN override doesn't really work yet
WHEN = ''
WHERE = "Artichoke Basille's Pizza http://maps.google.com/maps/place?cid=9417195867123786812"
