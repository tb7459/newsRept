#!/usr/bin/env python3
# 
# A small webserver to display 3 reports:
# 1) most popular articles, 
# 2) most popular authors, and 
# 3) date(s) with > 1% error


from flask import Flask, request, redirect, url_for

from newsReptdb import get_popular_articles, get_popular_authors, get_perc_bad

app = Flask(__name__)

# HTML template for the forum page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>News Report</title>
    <style>
      h1, form { text-align: center; }
      textarea { width: 400px; height: 100px; }
      div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; }
      hr.postbound { width: 50%%; }
      em.date { color: #999 }
    </style>
  </head>
  <body>
    <h1>News Report</h1>
    <div class="post">
      <h1>Most Popular Articles</h1>
 %s
    </div>
    <div class="post">
      <h1>Most Popular Authors</h1>
 %s
    </div>
  </body>
</html>
'''

# HTML template for an individual comment
ART = '''\
    <em class=date>%s</em> -- %s views <br>
'''
AUT = '''\
    <em class=date>%s</em> -- %s views <br>
'''

@app.route('/', methods=['GET'])
def main():
  '''Main page of the forum.'''
  arts = "".join(ART % (name,views) for name, views in get_popular_articles())
  html = HTML_WRAP % arts
  
  auts = "".join(AUT % (autName,autViews) for autName, autViews in get_popular_authors())
  html = HTML_WRAP % auts

  return html



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)

