from lib.imports import *
from lib.config.python_mysql_dbconfig import read_db_config
from lib.config.db_lib import MySQLDataBase
from lib.db_connection import MySQLConnection

def use_data():
    database = request.json.get('database')
    if database == 'dynascan365_main':
        conn = MySQLConnection.db_connection()
    elif database == 'dynascan365_client':
        conn = MySQLConnection.db_connection()
    #print(database)
    try:
        #conn = mysql.connector.connect(**db_settings)
        
        with conn.cursor() as cursor:
            command = request.json.get('sql')
            print(command)
            
            cursor.execute(command)
            data = cursor.fetchall()
            column_names = [i[0] for i in cursor.description]
            df = pd.DataFrame(data, columns = column_names)
            print(df)
    
    finally:
        conn.close()
    
    json_data = df.to_dict(orient = 'records')
    
    try:      
        status = json.dumps(1)
        json_status = json.loads(status)
        return jsonify({'status': json_status,'data':json_data})
        
    #except json.JSONDecodeError:
    
    #When an error message occurs with jsonify, execute the except 
    except TypeError as e:
        status = json.dumps(0)
        json_status = json.loads(status)        
        return jsonify({'status': json_status, 'message':"An error occurred: " + str(e)})