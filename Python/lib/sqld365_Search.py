#from lib.db_connection import conn
#from lib.config import get_connection_main
from lib.imports import *
from lib.SyntaxKiosK import SyntaxKiosK
from lib.DatabasePool import MySQLDatabaseProc
from lib.db_connection import MySQLConnection
from lib.ReturnData import ReturnData
from lib.CheckData import CheckData
from lib.sqlQuery import sqlQuery
from lib.sqlsearchMethod import sqlsearchMethod


class d365_Search:
    def MainDisplayer():
        try:
            #在config裡面做連接function
            #引用Class實例要加括號()
            
            #conn = MySQLDataBase().connection(read_db_config())
            conn = MySQLConnection.db_connection()
            with conn.cursor() as cursor:
        
                command = f"""SELECT b.id, b.mount, b.condition_flg, b.bonding, b.lcm_id, b.sn, b.model
                                FROM displayer_realtime AS b
                                INNER JOIN 
                                (SELECT {SyntaxKiosK.sqlBondingMainId()} 
                                FROM displayer AS a
                                INNER JOIN displayer_realtime AS b ON a.id = b.id
                                INNER JOIN displayer_model AS dm ON dm.model = b.model) AS main_id_tab ON main_id_tab.main_id = b.id"""
                
                cursor.execute(command)
                
                
                data = cursor.fetchall()
                column_names = [i[0] for i in cursor.description]
                df = pd.DataFrame(data, columns = column_names)
            
                print(df)
                

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
                #df.to_csv("我要的錯誤資料.csv")-->只能在地端轉換
                #print(df)
            #print(command)        
        finally:
            
            conn.close()
        
        return ReturnData.jsonify_return(df)

    def displayer_version():

        return sqlsearchMethod.sqlsearchMethod_main(sqlQuery.sqldisplayerVersion())
    
    def displayer_run():
        
        return sqlsearchMethod.sqlsearchMethod_main(sqlQuery.sqldisplayerRun())
    
    def displayer_inconsistent():#有可能會用到client資料庫連接 需要時再回來修改 2024-06-13
        
        return sqlsearchMethod.sqlsearchMethod_main(sqlQuery.sqldisplayer_inconsistent())
    
    def model_different():

        return sqlsearchMethod.sqlsearchMethod_client(sqlQuery.sqlmodelDifferent())
    
    def new_display_tab():
        return sqlsearchMethod.sqlsearchMethod_main(sqlQuery.sqlNewdisplayTable())