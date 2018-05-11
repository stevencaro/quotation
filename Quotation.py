
#from collections import defaultdict
#from inspect import
from itertools import chain
from random import choice

import configparser as cfg
import json
import regex as re
import shelve
import string
import sys
import unittest

import arrow

class Quotation():

    def __init__(self, language):
        self.config = cfg.ConfigParser(interpolation=cfg.ExtendedInterpolation() )
        self.config.read('quotation.cfg')

        quotefile = self.config['Languages'][language]

        try:
            f = open(quotefile, "r")
            self.quotes = json.load(f)
            f.close()
        except OSError:
            sys.exit("Quote file not found.")

    def __len__(self):
        "len() returns how many proverbs are in the collection."
        return len(self.quotes)

    def random_quote(self):
        self.quote = choice(self.quotes)

    def search(self, pattern, flags=0):
        results = []
        for q in self.quotes:
            concatenated = ""
            for s in list(chain(q)):
                concatenated += s
            if re.search(pattern, concatenated, flags):
                results.append(q)
        return results

    def show(self):
        self.random_quote()
        quote = self.quote
        q = quote[0]
        print (q, "\n")
        for l in quote[1:]:
            print("    ", l)


class LatinQuote(Quotation):

    def __init__(self):
        super().__init__('Latin')

    ### The LatinQuote subclass prompts the user to display another quote
    def show(self):
        self.random_quote()
        try:
            while True:
                print ( self.quote[0] + ' : ' + self.quote[1] )
                ans = input("\nAnother quote? ")
                self.random_quote()
        except KeyboardInterrupt:
            sys.exit()

class GermanQuote(Quotation):

    def __init__(self):
        super().__init__('German')

        self.history_file = self.config['ShelfFiles']['GermanShelfFile']

    ### The GermanQuote subclass logs the date and time a quote was displayed.
    ### It uses a persistent dictionary via the shelve module.
    def random_quote(self):
        super().random_quote()

        with shelve.open(self.history_file) as history:
            history[self.quote[0]] = arrow.utcnow()


class SpanishQuote(Quotation):

    def __init__(self):
        super().__init__('Spanish')

    ### The SpanishShow subclass uses a Template to display its quotation.
    ### However, this approach is overkill.
    def show(self):
        self.random_quote()
        values = { 'quote': self.quote[0],
                   'trans': self.quote[1],
                   'note' : self.quote[2] if len (self.quote) > 2 else '' }

        template = '''$quote

    $trans
    $note'''
        t = string.Template(template)
        print( t.safe_substitute(values), end='')

if __name__ == '__main__':

    class TestQuotationObjects(unittest.TestCase):

        def test_basics(self):
            lq = LatinQuote()
            gq = GermanQuote()
            sq = SpanishQuote()

            for obj in [lq, gq, sq]:
                self.assertTrue(issubclass(obj.__class__, Quotation))

            self.assertTrue(len(lq) == 3575)
            self.assertTrue(len(gq) == 299)
            self.assertTrue(len(sq) == 284)

    unittest.main()

