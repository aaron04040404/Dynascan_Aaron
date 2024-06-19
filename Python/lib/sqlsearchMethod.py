from lib.imports import *
from lib.SyntaxKiosK import SyntaxKiosK
from lib.DatabasePool import MySQLDatabaseProc
from lib.db_connection import MySQLConnection
from lib.ReturnData import ReturnData
from lib.CheckData import CheckData
from lib.sqlQuery import sqlQuery


class sqlsearchMethod():

    def sqlsearchMethod_main(command):
        try:
            conn = MySQLConnection.db_connection()
            with conn.cursor() as cursor:

                #command = sqlQuery.sqldisplayerVersion()
                cursor.execute(command)
                
                data = cursor.fetchall()
                column_names = [i[0] for i in cursor.description]
                df = pd.DataFrame(data, columns = column_names)
            
            return ReturnData.jsonify_return(df)
        except Exception as e:
            status = json.dumps(0)
            json_status = json.loads(status) 
            return jsonify({'status': json_status, 'message':"無效或錯誤的查詢: " + str(e)})

        finally:
            conn.close()
        
        
    

    def sqlsearchMethod_client(command):
        try:
            conn = MySQLConnection.db_connection_client()
            with conn.cursor() as cursor:
                
                cursor.execute(command)
                
                data = cursor.fetchall()
                column_names = [i[0] for i in cursor.description]
                df = pd.DataFrame(data, columns = column_names)
            return ReturnData.jsonify_return(df)
        except Exception as e:
            status = json.dumps(0)
            json_status = json.loads(status) 
            return jsonify({'status': json_status, 'message':"無效或錯誤的查詢: " + str(e)})
        finally:
            conn.close()
        print(df)
        

