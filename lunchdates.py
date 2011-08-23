#!/usr/bin/python
# -*- coding: utf-8 -*-#
#
# Copyright 2011 nerdhurders hurd@nerhurder.com
#

from datetime import date, time, datetime
from dateutil import rrule, relativedelta

__TODO__ = ['make timezone aware']
__BUGS__ = ['maybe']

from settings import LUNCH_WEEKDAY, LUNCH_HOUR

def next_lunch_date():
  next_thursday = rrule.rrule(rrule.MONTHLY, 
                              byweekday=relativedelta.weekday(LUNCH_WEEKDAY),
                              byhour=LUNCH_HOUR,
                              dtstart=date.today(), 
                              count=2)
  next_date = next_thursday[0]
  # doing this check manually is an artifact of not (yet) correctly
  # handling the timezone
  if next_date < datetime.now():
      next_date = next_thursday[1]
  return next_date.ctime()

if __name__ == '__main__':
    print next_lunch_date()
