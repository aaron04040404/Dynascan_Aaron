from lib.imports import *
from lib.SyntaxKiosK import SyntaxKiosK
from lib.DatabasePool import MySQLDatabaseProc
from lib.db_connection import MySQLConnection
from lib.ReturnData import ReturnData
from lib.CheckData import CheckData
from lib.sqlQuery import sqlQuery


class d365_Notification_Search():

    def Notification_between_date():
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