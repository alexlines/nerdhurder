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

# this WHEN override doesn't really work yet
WHEN = ''
WHERE = "bill's bar and burger http://bit.ly/n3ga4p"
