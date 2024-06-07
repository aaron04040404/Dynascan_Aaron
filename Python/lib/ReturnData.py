from lib.imports import *


class ReturnData():
    def jsonify_return(df):
        
        json_data = df.to_dict(orient = 'records')#-->直接轉成dictionary
        #for item in json_data:-->有需要把bytearray轉換再用
            #item['content_id'] = int.from_bytes(item['content_id'], byteorder='big')
            
        #print(json_data)
        try:      
            status = json.dumps(1)
            json_status = json.loads(status)
            #json_obj = json.loads(json_data)-->用loads()將json格式字串轉成dictionary
            return jsonify({'status': json_status,'data':json_data})
            
        
        #When an error message occurs with jsonify, execute the except 
        except TypeError as e:
            status = json.dumps(0)
            json_status = json.loads(status)
            #json_obj = json_data
            return jsonify({'status': json_status, 'message':"An error occurred: " + str(e)})