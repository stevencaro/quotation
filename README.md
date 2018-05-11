# quotation
A library and console application to display a quote in German, Spanish, or Latin to the user. Similar to the fortune program in Unix. https://en.wikipedia.org/wiki/Fortune_(Unix)

## Introduction
This project shows basic object oriented design in action. It also uses unittest as the testing framework. The project includes the following files:

* Quotation.py is the main library file.
* show-quote.py is the command line application.
* quotation.cfg is the configuration file.
* german-history-file is a persistent dictionary used by the GermanQuote subclass.
* README.md contains this documentation.

The three .json files contain the data.

* german-quotes.json
* spanish-quotes.json
* latin-quotes.json

## Dependencies

To search the quotation files, the API uses the [third-party regex](https://pypi.org/project/regex/) module instead of the Python re module.

## Basic usage
Run the show-quote.py program to see a quote. If you don't specify one of l, q, or s on the command line, the program chooses the language at random.

```
~/git/quotation❯ show-quote.py
in principio erat Verbum : in the beginning was the Word (Logos)

Another quote?
obscuris vera involvens : the truth being enveloped by obscure things

Another quote? ^C⏎
~/git/quotation❯
```

## Search
The Quotation API includes a search method that you can use to search the quotation files. The method uses Python regular expression syntax. The search method is best used from within an interactive iPython session. For example:

```
In [7]: run -n Quotation.py

In [8]: gq = GermanQuote()

In [9]: gq.search('Hund')

Out[9]:
[['Bellende Hunde beißen nicht.', "Barking dogs don't bite."],
 ['Der Hund bellt und die Karawane geht vorüber.',
  'The dogs bark and the caravan moves on.',
  'Let the world say what it will.'],
 ['Man findet bald einen Stecken, wenn man einen Hund schlagen will.',
  'You will soon find a stick, if you want to beat a dog.',
  'Someone who wants to be mean will find things to be mean about no matter what.'],
 ['Nicht alle sind Diebe die der Hund anbellt.',
  'All are not thieves that dogs bark at.'],
 ['Schlafende Hunde soll man nicht wecken.',
  'English Equivalent: Let sleeping dogs lie.'],
 ['Wer mich liebt, der libt auch meinen Hund.', 'Love me, love my dog.']]

In [12]: lq.search('\mamor\M')
Out[12]:
[['Tempus fugit, amor manet.', 'Time flees, love stays'],
 ['Crescit amor nummi, quantum ipsa pecunia crevit',
  'The love of wealth grows as the wealth itself grew. (Juvenalis)'],
 ...
```

## Rationale
I love studying languages, so I made a console app to show quotations in the languages I've studied.
Although the project is a bit contrived, I feel it is a good and brief display of my coding style. And my documentation style.
