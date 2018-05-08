#!/usr/bin/python3

from random import choice

from quotation.Quotation import LatinQuote, SpanishQuote, GermanQuote

lq = LatinQuote()
sq = SpanishQuote()
gq = GermanQuote()

quote = choice( (lq,sq,gq) )
quote.show()
