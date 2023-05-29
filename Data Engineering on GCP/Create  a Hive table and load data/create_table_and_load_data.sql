--show available databases
show databases;

--create new database hive_db
create database if not exists hive_db;

--drop table if already available
drop table if exists hive_db.customers;

--create table customers in database hive_db
create table if not exists hive_db.customers( 
customer_id int, 
customer_name string,  
contact_name string, 
address string, 
city string, 
postal_code string, 
country string) 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '~';

use hive_db;

--show headers in output
set hive.cli.print.header=true;

--check record count in table
select count(*) from hive_db.customers;

--load data from local file
load data local inpath 'customers-local.csv' into table hive_db.customers;

select count(*) from hive_db.customers;

select * from hive_db.customers limit 2;

--load data from hdfs file
load data inpath '/data/customers-hdfs.csv' into table hive_db.customers; 

--check record count
select count(*) from hive_db.customers;

select customer_id from hive_db.customers;
