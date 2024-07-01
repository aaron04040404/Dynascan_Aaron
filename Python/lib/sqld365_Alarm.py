from lib.imports import *
from lib.sqlQuery import sqlQuery
from lib.DataProcess import DataProc

class d365Alarm():

    def duplicate_alarm_event():
        date = request.json.get('end_on_date')
        result = DataProc.sqlsearchMethod_main(sqlQuery.sqlduplicate_alarm_event(date))
        print(sqlQuery.sqlduplicate_alarm_event(date))
        if isinstance(result, pd.DataFrame):
            return DataProc.jsonify_return(result)
        else:
            return result