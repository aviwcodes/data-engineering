#to install python connector run below
#pip install snowflake-connector-python
#pip install "snowflake-connector-python[pandas]"

import snowflake.connector
import pandas as pd
import traceback

def run_sql_on_sf_and_get_result_as_pandas_df(user,password,account,warehouse,db,schema,sql_query, logger):
    df=None
    conn = snowflake.connector.connect(
        user=user,
        password=password,
        account=account,
        warehouse=warehouse,
        database=db,
        schema=schema
        )
    try:
        cur = conn.cursor()
        
        logger.info("Query being run:{}".format(sql_query))
        cur.execute(sql_query)
        return cur   
        return df
    except Exception as e:
        logger.info(e)        
    finally:
        conn.close()
