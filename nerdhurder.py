#!/usr/bin/python
# -*- coding: utf-8 -*-#
#
# Copyright 2011 nerdhurders hurd@nerhurder.com
#

''' python interface to lunch '''

__author__ = 'nerdhurder.com'
__BUGS__ = 'probably'
# annoying formatting below makes for nicer diffs. feel free to debate endlessly
__TODO__ = [ 
             'better output formatting',
             'geolocation',
             'choose a license',
             'not a single test',
             'does not catch a single exception',
             'the WHEN override does not really work yet',
           ]

from settings import WHO, COUNT, WHERE, WHEN
from lunchdates import next_lunch_date

class NerdHurd(object):

  def __init__(self):
      self.time = 'placeholder'

  def assemble(self, who=WHO, count=COUNT, when=WHEN, where=WHERE):
      when = next_lunch_date()
      attending = "\n\t".join(who)
      # hold your nose:
      print "who: \t%s\ncount: \t%s\nwhen: \t%s\nwhere: \t%s\n" % (attending, count, when, where)

  def format(self, args):
      pass

if __name__ == '__main__':
  NerdHurd().assemble()
