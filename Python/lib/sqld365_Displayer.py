from lib.imports import *
from lib.sqlQuery import sqlQuery
from lib.DataProcess import DataProc

class d365_Displayer():

    def Displayer_realtime():
        bonding = request.json.get('bonding')
        result = DataProc.sqlsearchMethod_main(sqlQuery.sqlDisplayer_realtime(bonding))
        if isinstance(result, pd.DataFrame):
            return DataProc.jsonify_return(result)
        else:
            return result
    