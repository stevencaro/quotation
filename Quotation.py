
#from collections import defaultdict
#from inspect import
from itertools import chain
from random import choice

import configparser as cfg
import json
#import pickle
import re
import string
#import shelve
import sys
import unittest

class Quotation():

    def __init__(self, quotefile):
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
        return choice(self.quotes)

    def search(self, pattern, flags=0):
        for q in self.quotes:
            concatenated = ""
            for s in list(chain(q)):
                concatenated += s
            if re.search(pattern, concatenated, flags):
                print(q)

    def show(self):
        quote = self.random_quote()
        q = quote[0]
        print (q, "\n")
        for l in quote[1:]:
            print("    ", l)


class GermanQuote(Quotation):

    def __init__(self):
        config = cfg.ConfigParser()
        config.read('quotation.cfg')
        self.quotefile = config['Default']['GermanQuotesFile']

        super().__init__(self.quotefile)


class LatinQuote(Quotation):

    def __init__(self):
        config = cfg.ConfigParser()
        config.read('quotation.cfg')
        self.quotefile = config['Default']['LatinQuotesFile']

        super().__init__(self.quotefile)


class SpanishQuote(Quotation):

    def __init__(self):
        config = cfg.ConfigParser()
        config.read('quotation.cfg')
        self.quotefile = config['Default']['SpanishQuotesFile']

        super().__init__(self.quotefile)

    ### The SpanishShow subclass uses a Template to display its quotation.
    ### However, this approach is overkill.
    def show(self):
        quote = self.random_quote()
        values = { 'quote': quote[0],
                   'trans': quote[1],
                   'note' : quote[2] if len (quote) > 2 else '' }

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

