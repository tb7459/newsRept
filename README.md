Description: 
  A python program to run 3 queries and return:
   1) 3 most popular articles, most popular first.
   2) most popular authors in order of popularity.
   3) Date(s) and percentage of errors where errors 
      happened

Prerequisites:
  Create view as follows:

 create view vw_date_statCount as select date(time) as dateVal, status, count(status) as statCount 
 from log group by date(time), status;
  
  newsRept.sql has been provided
  and can be run from psql as follows:

  login to virtual machine

  cd /vagrant
  cd /newsRept

  vagrant@vagrant:/vagrant/newsRept$ psql news -f newsRept.sql
  (this will create the view to run the percent errors query.

Final step:
  run newsRept.py as follows:

  $ python newsRept.py

output:

output should look like:

vagrant@vagrant:/vagrant/newsRept$ python newsRept.py

Article data:
  " Candidate is jerk, alleges rival " --  338647  views
  " Bears love berries, alleges bear " --  253801  views
  " Bad things gone, say good people " --  170098  views

Author data:
    Ursula La Multa  --  507594  views
    Rudolf von Treppenwitz  --  423457  views
    Anonymous Contributor  --  170098  views
    Markoff Chaney  --  84557  views

Error data:
     2016-07-17  --  2.26  % errors


