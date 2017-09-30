#!/usr/bin/env python3
# A small program to display 3 reports:
# 1) most popular articles,
# 2) most popular authors, and
# 3) date(s) with > 1% error

from flask import Flask, request, redirect, url_for
from newsReptdb import get_popular_articles, get_popular_authors, get_perc_bad

app = Flask(__name__)
articles = get_popular_articles()
authors = get_popular_authors()
errors = get_perc_bad()

print " "
print "Article data: "

for article in articles:
    print "  \"", article[0], "\" -- ", article[1], " views"

print " "
print "Author data: "

for author in authors:
    print "   ", author[0], " -- ", author[1], " views"

print " "
print "Error data: "

for error in errors:
    print "    ", error[0], " -- ", error[1], " % errors"

print "  "
