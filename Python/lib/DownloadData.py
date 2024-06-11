from lib.imports import *

class DownloadData():

    def downloadcsv():
        data = request.json.get('data')
        df = pd.DataFrame(data)
        print(df)
        response = make_response(df.to_csv(index=False))
        response.headers["Content-Disposition"] = "attachment; filename=data.csv"
        response.headers["Content-Type"] = "text/csv"

        return response