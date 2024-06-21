#from lib.db_connection import conn
#from lib.config import get_connection_main
from lib.imports import *
from lib.SyntaxKiosK import SyntaxKiosK
from lib.db_connection import MySQLConnection
from lib.CheckData import CheckData
from lib.sqlQuery import sqlQuery
from lib.DataProcess import DataProc

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
        
        return DataProc.jsonify_return(df)
    


    def wrong_Bonding():
        #result回傳一個查詢後的結果，有可能是成功的dataframe或失敗的字串訊息，如果是dataframe就利用jsonify_return來回傳最後結果
        result = DataProc.sqlsearchMethod_main(sqlQuery.sqlWrongBonding())
        print(sqlQuery.sqlWrongBonding())
        
        if isinstance(result, pd.DataFrame):
            #如果有需要檢查的資料就塞在這裡做檢查
            if(CheckData.CheckWrong_Bonding(result)):
                return DataProc.jsonify_return(result)
        else:
            return result


    def displayer_version():
        result = DataProc.sqlsearchMethod_main(sqlQuery.sqldisplayerVersion())
        if isinstance(result, pd.DataFrame):
            return DataProc.jsonify_return(result)
        else:
            return result
    
    def displayer_run():
        result = DataProc.sqlsearchMethod_main(sqlQuery.sqldisplayerRun())
        if isinstance(result, pd.DataFrame):
            return DataProc.jsonify_return(result)
        else:
            return result
    
    def displayer_inconsistent():#有可能會用到client資料庫連接 需要時再回來修改 2024-06-13
        
        result = DataProc.sqlsearchMethod_main(sqlQuery.sqldisplayer_inconsistent())
        if isinstance(result, pd.DataFrame):
            return DataProc.jsonify_return(result)
        else:
            return result
    
    def model_different():

        result = DataProc.sqlsearchMethod_client(sqlQuery.sqlmodelDifferent())
        if isinstance(result, pd.DataFrame):
            return DataProc.jsonify_return(result)
        else:
            return result
    
    def new_display_tab():
        result = DataProc.sqlsearchMethod_main(sqlQuery.sqlNewdisplayTable())
        if isinstance(result, pd.DataFrame):
            return DataProc.jsonify_return(result)
        else:
            return result