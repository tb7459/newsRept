#!/usr/bin/env python3
# A small program to display 3 reports:
# 1) most popular articles,
# 2) most popular authors, and
# 3) date(s) with > 1% error

from newsReptdb import get_popular_articles, get_popular_authors, get_perc_bad

if __name__ == "__main__":
    articles = get_popular_articles()
    authors = get_popular_authors()
    errors = get_perc_bad()

    print(" ")
    print("Article data: ")

    for(article, views) in articles:
        print("    {} - {} views".format(article, views))
    print("-" * 70)
    print(" ")
    print("Author data: ")

    for(author, views) in authors:
        print("    {} - {} views".format(author, views))
    print("-" * 70)
    print(" ")
    print("Error data: ")

    for(date, erPerc) in errors:
        print("    {} - {}%".format(date, erPerc))
    print("  ")
