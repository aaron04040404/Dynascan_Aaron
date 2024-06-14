import os
from lib.imports import *
from lib.config.python_mysql_dbconfig import read_db_config
from lib.sqld365_Search import d365_Search #沒有變數的已知查詢(包含所有)
from lib.sqld365_Notification_Search import d365_Notification_Search #跟Notification相關的查詢
from lib.SQL_typing import use_data
from lib.DownloadData import DownloadData
from lib.db_connection import MySQLConnection


app = Flask(__name__,
            static_folder = "../dist/assets",
            template_folder = "../dist")

app.config['JSON_SORT_KEYS'] = False
            
cors = CORS(app, resources = {r"/*":{"origins":"*"}})

#bytearray 轉換
def convert_dict(data):
    if isinstance(data,str):
        return data
    elif isinstance(data,bytes):
        return data.decode()
    elif isinstance(data,dict):
        for key,val in data.items():
            if isinstance(key,bytes):
                data[key.decode()] = convert_dict(data[key])
            else:
                data[key] = convert_dict(data[key])
        return data
    elif isinstance(data,list):
        temp_list = []
        for dt in data:
            temp_list.append(convert_dict(dt))
        return temp_list
    else:
        return data
    


@app.route('/', defaults={'path': ''})
#動態路由傳入path都導向同個html
@app.route('/<path:path>')
def catch_all(path):
    
    return render_template("index.html")
    


#request後做Access-Control-Allow-Credentials的檢查
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    
    return response
    

@app.route('/sql_typing', methods = ['GET', 'POST'])    
def run_sql_typing():
    
    return use_data()   


@app.route('/maindisplayer', methods = ['GET', 'POST'])  
def run_MainDisplayer():
    
    return d365_Search.MainDisplayer()
    
@app.route('/Notification_between_date', methods = ['GET', 'POST'])  
def run_Notification_between_date():
    
    return d365_Notification_Search.Notification_between_date()


@app.route('/wrong_Bonding', methods = ['GET', 'POST'])
def run_wrong_bonding():
    
    return d365_Search.wrong_Bonding()

@app.route('/immediate_version', methods = ['GET', 'POST'])
def run_displayer_version(): 

    return d365_Search.displayer_version()

@app.route('/displayer_run', methods = ['GET', 'POST'])
def run_displayer_run(): 

    return d365_Search.displayer_run()

@app.route('/displayer_realtime', methods = ['GET', 'POST'])
def run_displayer_realtime(): 

    return d365_Search.displayer_realtime()

@app.route('/model_different', methods = ['GET', 'POST'])
def run_model_different(): 

    return d365_Search.model_different()

@app.route('/new_display_tab', methods = ['GET', 'POST'])
def run_new_display_tab(): 

    return d365_Search.new_display_tab()

@app.route('/download', methods = ['GET', 'POST'])
def run_download():
    return DownloadData.downloadcsv()    
        
if __name__ == '__main__':
    
    app.run(host ='0.0.0.0', port = '5000', debug = True)
