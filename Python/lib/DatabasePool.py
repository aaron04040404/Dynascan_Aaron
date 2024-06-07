import mysql.connector
from mysql.connector import pooling
import json
import hashlib
from configparser import ConfigParser
import os

class MySQLDatabaseProc (object):
    POOL_SIZE = 3

    POOLS={}
    # pools{
    #      pool_1:{
    #         "pool":
    #         "config":   
    # 
    # }
    
    
    # }




    @staticmethod
    def startCnxPool( config, name, size = POOL_SIZE ):
        if len( MySQLDatabaseProc.POOLS ) > 0:
            for poolname in MySQLDatabaseProc.POOLS:
                if poolname == name:
                    new_config = hashlib.md5( json.dumps( config ).encode("utf-8") ).hexdigest()
                    # if the pool config is changed, set config again.
                    if MySQLDatabaseProc.POOLS[ poolname ]["config"] != new_config: 
                        MySQLDatabaseProc.POOLS[ poolname ]["pool"].set_config( **config )
                        MySQLDatabaseProc.POOLS[ poolname ]["config"] = new_config
                    
                    #print ("DB [%s] pool has been ready" % name)
                    #print ("Now pools are(%s):" % len(MySQLDatabaseProc.POOLS))
                    #print (str( MySQLDatabaseProc.POOLS.keys() )[1:-1])
                    return True
        pool = None
        try:
            pool = mysql.connector.pooling.MySQLConnectionPool( pool_name = name, pool_size = size, **config )
        except mysql.connector.PoolError as err:
            print ("MySQL connection pooling error: %s" % err)
            
        if not pool:
            return False
        
        MySQLDatabaseProc.POOLS[ name ] = { 
            "pool": pool, 
            "config": hashlib.md5( json.dumps( config ).encode("utf-8") ).hexdigest() 
        }
        
        #print ("DB [%s] pool is ready now" % name)
        #print ("Now pools are(%s):" % len(MySQLDatabaseProc.POOLS))
        #print (str( MySQLDatabaseProc.POOLS.keys() )[1:-1])
        return True
    
    def __init__(self):
        raise Exception("Please use static method StartCnxPool()...")
    
    def __del__(self):
        for key in MySQLDatabaseProc.POOLS:
            if "pool" in MySQLDatabaseProc.POOLS[ key ]:
                MySQLDatabaseProc.POOLS[ key ]["pool"].close()
                del MySQLDatabaseProc.POOLS[ key ]["pool"]
            if "config" in MySQLDatabaseProc.POOLS[ key ]:
                del MySQLDatabaseProc.POOLS[ key ]["config"]
            del MySQLDatabaseProc.POOLS[ key ]
        del MySQLDatabaseProc.POOLS
        
        print ("db connecting pool clear.")

    @staticmethod
    def getConnection(pool_name):
        if len(MySQLDatabaseProc.POOLS) == 0:
            raise Exception("MySQL connector pooling is empty!")
        
        try:
            conn = MySQLDatabaseProc.POOLS[pool_name]["pool"].get_connection()
            if conn.is_connected() is False:
                conn.reconnect(attempts = 1, delay = 0) #attempts 重新連線次數
                if(conn.is_connected() is False):
                    raise Exception("Connection error!!!")
            return conn
        except mysql.connector.PoolError as err:
            raise Exception(f"Database get connection error {err}")
        
    