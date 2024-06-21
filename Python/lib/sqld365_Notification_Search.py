from lib.imports import *
from lib.sqlQuery import sqlQuery
from lib.DataProcess import DataProc

class d365_Notification_Search():

    def Notification_between_date():
        mcb_id = request.json.get('mcb_id')
        start_date = request.json.get('startDate')
        end_date = request.json.get('endDate')
        result = DataProc.sqlsearchMethod_main(sqlQuery.sqlNotification(mcb_id, start_date, end_date))
        print(sqlQuery.sqlNotification(mcb_id, start_date, end_date))
        if isinstance(result, pd.DataFrame):
            return DataProc.jsonify_return(result)
        else:
            return result