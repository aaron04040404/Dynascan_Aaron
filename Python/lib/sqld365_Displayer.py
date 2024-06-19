from lib.imports import *
from lib.SyntaxKiosK import SyntaxKiosK
from lib.DatabasePool import MySQLDatabaseProc
from lib.db_connection import MySQLConnection
from lib.ReturnData import ReturnData
from lib.CheckData import CheckData
from lib.sqlQuery import sqlQuery

class d365_Displayer():

    def Displayer_realtime():
        try:
            conn = MySQLConnection.db_connection()
            with conn.cursor() as cursor:

                bonding = request.json.get('bonding')
                command = sqlQuery.sqlDisplayer_realtime(bonding)
                cursor.execute(command)
                
                data = cursor.fetchall()
                column_names = [i[0] for i in cursor.description]
                df = pd.DataFrame(data, columns = column_names)

            print(command)
        finally:
            conn.close()

        
        return ReturnData.jsonify_return(df)