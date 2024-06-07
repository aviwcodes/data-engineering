import Order as o
import Product as p

import common_utils
import datetime
import os
import subprocess
import json
import pandas as pd

def _place_new_orders(logger):
    #Last customer Id
    max_customer_id = common_utils._get_last_generated_id('customer_id', logger)
    order_id = common_utils._get_last_generated_id('order_id', logger)
    
    logger.info("Last generated customer_id : {}".format(max_customer_id))
    logger.info("Last generated order_id : {}".format(order_id))
    
    tm=str(datetime.datetime.now()).replace(":","")
    
    base_path = f'resources/output/orders/dt={str(datetime.datetime.today()).split(" ")[0]}/hr={datetime.datetime.now().hour}/'
    file_name = 'orders-{}.json'.format(tm)
    isExist = os.path.exists(base_path)
    if not isExist:
        os.makedirs(base_path)
    
    file_name = base_path + file_name
    
    if os.path.exists(file_name):
        os.remove(file_name)
    
    lst_orders=[]
    #how many customers to generate
    for ordr_counter in range(0,common_utils._get_random_int(1,10)):
        #order for which customer
        random_number= common_utils._get_random_int(1,max_customer_id)
        logger.info("generating new order for customer_id :{}".format(random_number))
        
        customer_id = random_number
        order_id = order_id + 1
        
        order_date = datetime.datetime.now() - datetime.timedelta(days = common_utils._get_random_int(1,30))
        delivery_date = order_date + datetime.timedelta(days = common_utils._get_random_int(1,10))
        
        logger.info("New order id: {}".format(order_id))
        ord=o.Order(order_id,customer_id,order_date,delivery_date)
        
        item_count_in_order = common_utils._get_random_int(1,5)
        for i in range(0,item_count_in_order):    
            product_details = common_utils._get_random_name("dummy_product_name")            
            product_id=product_details.split("|")[0]
            product_name=product_details.split("|")[1]
            category_id=product_details.split("|")[2]
            category_name=product_details.split("|")[3]
            rate=product_details.split("|")[4]
            quantity=common_utils._get_random_int(1,5)
            product=p.Product(product_id,product_name,category_id,category_name,rate,quantity)
            ord._add_product(product.__dict__())
        
        logger.info(ord.__dict__())
        lst_orders.append(ord.__dict__())
        logger.info("---------------------------------")
    
    #with open(file_name, "a") as f:
    #    f.write(str(lst_orders).replace("'",""))
    pd.DataFrame(lst_orders).to_json(indent=False,lines=True,path_or_buf=file_name,orient='records')
    logger.info("_update_last_generated_id: {}".format(order_id))
    common_utils._update_last_generated_id('order_id',order_id,logger)

#_place_new_orders()
        
