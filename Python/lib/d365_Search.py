#from lib.db_connection import conn
#from lib.config import get_connection_main
from lib.imports import *
from lib.SyntaxKiosK import SyntaxKiosK
from lib.DatabasePool import MySQLDatabaseProc
from lib.db_connection import MySQLConnection
from lib.ReturnData import ReturnData
from lib.CheckData import CheckData
from lib.sqlQuery import sqlQuery


class d365_Search:
    def MainDisplayer():
        try:
            #在config裡面做連接function
            #引用Class實例要加括號()
            
            #conn = MySQLDataBase().connection(read_db_config())
            conn = MySQLConnection.db_connection()
            with conn.cursor() as cursor:
        
                command = f"""SELECT id, mount, condition_flg, b.bonding, lcm_id, sn, model
                                FROM
                                (SELECT bonding
                                FROM
                                (SELECT
                                    b.*                            
                                FROM displayer AS a
                                INNER JOIN displayer_realtime AS b ON a.id = b.id
                                INNER JOIN displayer_model AS dm ON dm.model = b.model) AS standard_tab
                                INNER JOIN (SELECT {SyntaxKiosK.sqlBondingMainId()}) AS main_id_tab ON main_id_tab.main_id = standard_tab.id) AS bonding_tab
                                INNER JOIN displayer_realtime AS b ON b.bonding = bonding_tab.bonding"""
                
                cursor.execute(command)
                
                
                data = cursor.fetchall()
                column_names = [i[0] for i in cursor.description]
                df = pd.DataFrame(data, columns = column_names)
            
                print(df)
                

        finally:
            
            conn.close()
        
        return ReturnData.jsonify_return(df)
            
    def sql_searching2():
        try:
        
            conn = MySQLConnection.db_connection()
        
            with conn.cursor() as cursor:
        
                #command = request.get_json()
                #print(command) #測試傳入的command是否正確
                mcb_id = request.json.get('mcb_id')
                start_date = request.json.get('startDate')
                end_date = request.json.get('endDate')
                print(mcb_id)
                print(start_date)
                print(end_date)

                # param -> '$.mcb_id' equal to JSON_EXTRACT(param, '$.mcb_id')
                command = sqlQuery.sqlNotification(mcb_id, start_date, end_date)
                print(command)
                cursor.execute(command)
                
                #cursor.callproc('test_proc')
                #result 獲取一次查詢
                data = cursor.fetchall()
                #for result in cursor.stored_results():
                        #data 回傳 result值
                    #data = result.fetchall()
                column_names = [i[0] for i in cursor.description]
                #column_names = ['id', 'value', 'datetime']
                df = pd.DataFrame(data, columns = column_names)
                #print(df)
                
                #for row in result:
                    #print(row)

        finally:
            conn.close()
        
        return ReturnData.jsonify_return(df)


    def wrong_Bonding():
        try:
            #在config裡面做連接function
            #引用Class實例要加括號()
            
            #conn = MySQLDataBase().connection(read_db_config())
            """section = 'mysql'
            filename = 'config.ini'
            config = read_db_config(filename, section)
            if MySQLDatabaseProc.startCnxPool(config, section, 3):
                print(MySQLDatabaseProc.POOLS)
                conn = MySQLDatabaseProc.getConnection(section)"""
            conn = MySQLConnection.db_connection()
        
            with conn.cursor() as cursor:
        
                command = sqlQuery.sqlWrongBonding()
                
                cursor.execute(command)
                
                
                data = cursor.fetchall()
                column_names = [i[0] for i in cursor.description]
                df = pd.DataFrame(data, columns = column_names)
                CheckData.CheckWrong_Bonding(df)
                #df.to_csv("我要的錯誤資料.csv")
                #print(df)
                
        finally:
            
            conn.close()
        
        return ReturnData.jsonify_return(df)

    def displayer_version():

        try:
            conn = MySQLConnection.db_connection()
            with conn.cursor() as cursor:

                command = sqlQuery.sqldisplayerVersion()
                cursor.execute(command)
                
                data = cursor.fetchall()
                column_names = [i[0] for i in cursor.description]
                df = pd.DataFrame(data, columns = column_names)
        finally:
            conn.close()
        
        return ReturnData.jsonify_return(df)