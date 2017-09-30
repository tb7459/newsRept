drop view vw_date_statCount;

create view vw_date_statCount as select date(time) as dateVal, status, count(status) as statCount from log group by date(time), status;
