from lib.imports import *

class ConvertData():

    def convert_bytearray_fields(data):
        if isinstance(data, dict):
            return {k: (v.hex() if isinstance(v, bytearray) else v) for k, v in data.items()}
        elif isinstance(data, list):
            return [ConvertData.convert_bytearray_fields(item) for item in data]
        return data