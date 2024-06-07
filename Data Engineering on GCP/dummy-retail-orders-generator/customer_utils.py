import common_utils
import Customer as cust
import os
import subprocess
import datetime
import json
import pandas as pd

def _generate_new_customers(logger):
    #Last customer Id
    customers_lst = []
    customer_id = common_utils._get_last_generated_id('customer_id',logger)
    logger.info("Last generated customer_id : {}".format(customer_id))
    #how many customers to generate
    random_number= common_utils._get_random_int(1,10)

    tm=str(datetime.datetime.now()).replace(":","")
    base_path = f'resources/output/customers/dt={str(datetime.datetime.today()).split(" ")[0]}/hr={datetime.datetime.now().hour}/'
    file_name = 'customer-{}.json'.format(tm)
    isExist = os.path.exists(base_path)
    if not isExist:
        os.makedirs(base_path)
    
    file_name = base_path + file_name
    
    if os.path.exists( file_name):
        os.remove(file_name)
    
    logger.info("generating {} new customers".format(random_number))
    
    for c_cntr in range(1,random_number+1):
        customer_id = customer_id + 1
        first_name = common_utils._get_random_name("dummy_first_name")
        last_name = common_utils._get_random_name("dummy_last_name")
        city_country = common_utils._get_random_name("dummy_city_name")
        email_domain = common_utils._get_random_name("dummy_email_name")
        email = "{}.{}@{}".format(first_name,last_name,email_domain)
        city=city_country.split("|")[0]
        country=city_country.split("|")[1]
        unit_no= common_utils._get_random_int(1,100)
        building_no= common_utils._get_random_int(1,10000)
        address = "Unit #{}, {}".format(unit_no,building_no)    
        if c_cntr % 2 ==0:
            gender="M"
        else:
            gender="F"
        c1=cust.Customer(customer_id,first_name,last_name,email,gender,address,city,country)
        logger.info(c1.__dict__())
        customers_lst.append(c1.__dict__())
        
        logger.info("---------------------------------")

    #with open(file_name, "a") as f:
    #    f.write(str(customers_lst).replace("'",""))
    pd.DataFrame(customers_lst).to_json(indent=False,lines=True,path_or_buf=file_name,orient='records')
    logger.info("_update_last_generated_id: {}".format(customer_id))
    common_utils._update_last_generated_id('customer_id',customer_id,logger)

#_generate_new_customers()
        
