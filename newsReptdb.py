# Database code for the newsRept

import psycopg2
import bleach

DBNAME = "news"


def get_popular_articles():
    """Return 3 most popular aritcles, most popular first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = "SELECT art.title, count(log.path) as views "
    query = query + "FROM log INNER JOIN articles art "
    query = query + " ON art.slug = substring(log.path,10) "
    query = query + "WHERE path != '/' "
    query = query + "GROUP BY art.title "
    query = query + "ORDER BY views desc limit 3;"
    c.execute(query)
    articles = c.fetchall()
    db.close()
    return articles


def get_popular_authors():
    """Return authors and number of articles read, listing most
    popular first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = "SELECT authors.name as autName, count(log.id) as autViews "
    query = query + "FROM log INNER JOIN articles art "
    query = query + "on art.slug = substring(path,10) "
    query = query + "INNER JOIN authors on authors.id = art.author "
    query = query + "where path != '/' "
    query = query + "group by authors.name order by autViews desc;"
    c.execute(query)
    authors = c.fetchall()
    db.close()
    return authors


def get_perc_bad():
    """Return date and percent of date where the
    percentage of errors for the day was > 1% """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = "SELECT  dateVal, round(prcVal,2) as prcVal "
    query = query + "FROM (select dateVal, "
    query = query + "((cast(badNum as decimal)/TotalNum) * 100) as prcVal "
    query = query + "FROM (select a.dateVal, a.statCount as goodNum, "
    query = query + "b.statCount as badNum, "
    query = query + "(a.statCount + b.statCount) as TotalNum "
    query = query + "FROM vw_date_statCount a join vw_date_statCount b "
    query = query + "on a.dateVal = b.dateVal "
    query = query + "and a.statCount > b.statCount) as percQ) "
    query = query + " as summQ WHERE prcVal > 1.0;"
    c.execute(query)
    errors = c.fetchall()
    db.close()
    return errors
