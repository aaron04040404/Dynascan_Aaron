from lib.imports import *
from lib.db_connection import MySQLConnection

class DataProc():

    def downloadcsv():
        data = request.json.get('data')
        df = pd.DataFrame(data)
        print(df)
        response = make_response(df.to_csv(index=False))
        response.headers["Content-Disposition"] = "attachment; filename=data.csv"
        response.headers["Content-Type"] = "text/csv"

        return response
    

    #檢查是否有bytearray如果有就轉換
    def convert_bytearray_fields(data):
        if isinstance(data, dict):
            return {k: (v.hex() if isinstance(v, bytearray) else v) for k, v in data.items()}
        elif isinstance(data, list):
            return [DataProc.convert_bytearray_fields(item) for item in data]
        return data
    
    
    #進行main查詢動作
    def sqlsearchMethod_main(command):
        try:
            conn = MySQLConnection.db_connection()
            with conn.cursor() as cursor:

                #command = sqlQuery.sqldisplayerVersion()
                cursor.execute(command)
                
                data = cursor.fetchall()
                column_names = [i[0] for i in cursor.description]
                df = pd.DataFrame(data, columns = column_names)
            return(df)
        except Exception as e:
            status = json.dumps(0)
            json_status = json.loads(status) 
            return jsonify({'status': json_status, 'message':"無效或錯誤的查詢: " + str(e)})

        finally:
            conn.close()

    #進行client查詢動作
    def sqlsearchMethod_client(command):
        try:
            conn = MySQLConnection.db_connection_client()
            with conn.cursor() as cursor:
                
                cursor.execute(command)
                
                data = cursor.fetchall()
                column_names = [i[0] for i in cursor.description]
                df = pd.DataFrame(data, columns = column_names)
            return(df)
        except Exception as e:
            status = json.dumps(0)
            json_status = json.loads(status) 
            return jsonify({'status': json_status, 'message':"無效或錯誤的查詢: " + str(e)})
        finally:
            conn.close()


    #查詢成功形成dataframe後才會進到這裡決定回傳給前端
    def jsonify_return(df):
        json_data = df.to_dict(orient = 'records')
        json_data_finally =  DataProc.convert_bytearray_fields(json_data)
        try:      
            status = json.dumps(1)
            json_status = json.loads(status)
            #json_obj = json.loads(json_data)-->用loads()將json格式字串轉成dictionary
            return jsonify({'status': json_status,'data':json_data_finally})
            
        
        #When an error message occurs with jsonify, execute the except 
        except TypeError as e:
            status = json.dumps(0)
            json_status = json.loads(status)
            #json_obj = json_data
            return jsonify({'status': json_status, 'message':"An error occurred: " + str(e)})
    
    
    
    
    
