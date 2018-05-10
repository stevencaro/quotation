#!/usr/bin/python3

import random
import sys

from quotation.Quotation import LatinQuote, SpanishQuote, GermanQuote

### Create all the Quotation objects:
lq = LatinQuote()
sq = SpanishQuote()
gq = GermanQuote()

### Test for command-line input:
try:
    arg = sys.argv[1]
except IndexError:
    arg = ''

### One way to implement switch semantics in Python:
try:
    user_choice = { 'l': lq,
                    's': sq,
                    'g': gq
                  }[arg]
except KeyError:
    user_choice = random.choice( (lq,sq,gq) )

### Show the quote:
user_choice.show()

