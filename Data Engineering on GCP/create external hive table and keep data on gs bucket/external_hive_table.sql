--create external table
create external table if not exists hive_db.customers_external( 
customer_id int, 
customer_name string,  
contact_name string, 
address string, 
city string, 
postal_code string, 
country string) 
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY '~'
location 'gs://aviwcodes-bucket/ext-tables/customers_external/';

select count(*) from hive_db.customers_external;

insert into hive_db.customers_external select * from hive_db.customers;



create external ive table and keep data on gs bucket





