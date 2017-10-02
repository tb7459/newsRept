Description: 
  A python program to run 3 queries and return:
   1) 3 most popular articles, most popular first.
   2) most popular authors in order of popularity.
   3) Date(s) and percentage of errors where errors 
      happened

Prerequisites:

--- Virtual Machine ---

  download virtual machine:
    https://www.virtualbox.org/wiki/Downloads - follow directions on page

  Install Vagrant:
    https://www.vagrantup.com/downloads.html

  Download configuration:
    https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip

  Once all downloaded and installed, cd into vagrant
  and start vagrant by typing following command:

    vagrant up

  login using: 
    vagrant ssh

    cd /vagrant


--- database ---
  Get a copy of the database by running:
  vagrant@vagrant:/vagrant$ psql -d news -f newsdata.sql


  Create view as follows:

 create view vw_date_statCount as select date(time) as dateVal, status, count(status) as statCount 
 from log group by date(time), status;
  
  newsRept.sql has been provided
  and can be run from psql as follows:


  cd /vagrant
  cd /newsRept

  vagrant@vagrant:/vagrant/newsRept$ psql news -f newsRept.sql
  (this will create the view to run the percent errors query.

Final step:
  run newsRept.py as follows:

  $ python3 newsRept.py

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


