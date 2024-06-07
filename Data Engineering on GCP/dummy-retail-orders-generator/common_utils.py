from random import randint
import pandas as pd
import json
import os
import sf_utils

def _get_random_int(min_n, max_n):
    return randint(min_n, max_n)

def _is_file_available(file_path):
    return os.path.exists(file_path)

def get_sf_conn_details(logger):
    #read connection details
    file_path="resources/config/connection.json"
    if _is_file_available(file_path):        
        logger.info("path exists : {}".format(file_path))
        with open(file_path,'r') as f:            
            conn_details = json.load(f)                
        return conn_details["SNOWFLAKE"]
    else:
        return None

def _get_random_name(dummy_tbl_name):
    
    df=pd.read_csv("resources/data/" + dummy_tbl_name +".csv")
    
    lst_name = df[df.columns[0]].tolist()
    rn=  _get_random_int(0,len(lst_name))  
    if rn == len(lst_name):
        rn= len(lst_name)-1
        
    return lst_name[rn]

def _get_last_generated_id(entity_id_type, logger):
    #local test
    
    try:
        sf_conn_details=get_sf_conn_details(logger)
        sql_query = "select * from dev_db.dg.data_generator_ctrl_tbl where entity_type_id='{}';".format(entity_id_type)
            
        cur=sf_utils.run_sql_on_sf_and_get_result_as_pandas_df(sf_conn_details['USER'],sf_conn_details['PASSWORD'],
                                                        sf_conn_details['ACCOUNT'],sf_conn_details['WAREHOUSE'],sf_conn_details['DATABASE'],sf_conn_details['SCHEMA'],sql_query,logger)
        df=cur.fetch_pandas_all()
        logger.info(df.head())
        last_id = df[df['ENTITY_TYPE_ID']==entity_id_type]['LAST_GENERATED_ID'][0]
        logger.info("result from snowflake:{}".format(last_id))
        return last_id
    except Exception as e:
        logger.info(e)
        #if any issue with Snowflake get details from local
        logger.info("Execption while getting details from snowflake....trying to get from local...")
        file_path="resources/data/data_generator_ctrl_tbl.csv"
        if _is_file_available(file_path):
            df=pd.read_csv(file_path)    
            last_id = df[df['ENTITY_TYPE_ID']==entity_id_type]['LAST_GENERATED_ID'][0]
            return last_id
        
def _update_last_generated_id(entity_id_type,id, logger):        
    sf_conn_details=get_sf_conn_details(logger)
    sql_query = """update dev_db.dg.data_generator_ctrl_tbl
                   set LAST_GENERATED_ID={}
                   where entity_type_id='{}';""".format(id,entity_id_type)
            
    cur=sf_utils.run_sql_on_sf_and_get_result_as_pandas_df(sf_conn_details['USER'],sf_conn_details['PASSWORD'],
                                                        sf_conn_details['ACCOUNT'],sf_conn_details['WAREHOUSE'],sf_conn_details['DATABASE'],sf_conn_details['SCHEMA'],sql_query,logger)    
    logger.info("Returned result:{}".format(cur._result))
#print(_get_random_int())

#for i in range(1, 30):
#    print(_get_random_name("dummy_first_name"))

#print(_get_random_name("dummy_first_name"))
    