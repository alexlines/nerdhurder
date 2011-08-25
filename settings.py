# -*- coding: utf-8 -*-#
#
# Copyright 2011 nerdhurders hurd@nerhurder.com
#

import calendar
from people import NERDS

LUNCH_HOUR = 13
LUNCH_WEEKDAY = calendar.THURSDAY

# brace for ugly ass comprehension:
WHO = [ nerd['name'] for nerd in NERDS if nerd['rsvp']==True ]
GUESTS = sum([ nerd['guests'] for nerd in NERDS if nerd['rsvp']==True ])

# Keep track of overall number of people
COUNT = len(WHO) + GUESTS

# this WHEN override doesn't really work yet
WHEN = ''
WHERE = "Rye House http://maps.google.com/maps/place?cid=6127367641255397477"
