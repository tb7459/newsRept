# Database code for the newsRept

import psycopg2

DBNAME = "news"


def closeDB(db):
    db.close()


def get_popular_articles():
    """Return 3 most popular aritcles, most popular first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = ("""SELECT art.title, count(log.path) as views
                FROM log INNER JOIN articles art
                 ON art.slug = substring(log.path,10)
                WHERE path != '/'
                GROUP BY art.title
                ORDER BY views desc limit 3;""")
    c.execute(query)
    articles = c.fetchall()
    closeDB(db)
    return articles


def get_popular_authors():
    """Return authors and number of articles read, listing most
    popular first."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = ("""SELECT authors.name as autName, count(log.id) as autViews
                FROM log INNER JOIN articles art
                 ON art.slug = substring(path,10)
                INNER JOIN authors on authors.id = art.author
                WHERE path != '/'
                group by authors.name order by autViews desc;""")
    c.execute(query)
    authors = c.fetchall()
    closeDB(db)
    return authors


def get_perc_bad():
    """Return date and percent of date where the
    percentage of errors for the day was > 1% """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = ("""SELECT  dateVal, round(prcVal,2) as prcVal
                FROM (select dateVal,
                    ((cast(badNum as decimal)/TotalNum) * 100) as prcVal
                      FROM (select a.dateVal, a.statCount as goodNum,
                            b.statCount as badNum,
                           (a.statCount + b.statCount) as TotalNum
                      FROM vw_date_statCount a join vw_date_statCount b
                       on a.dateVal = b.dateVal
		       and a.status = '200 OK' 
                       and b.status = '404 NOT FOUND') as percQ)
                       as summQ WHERE prcVal > 1.0;""")
    c.execute(query)
    errors = c.fetchall()
    db.close()
    return errors
