from lib.imports import *
#from lib.config import get_connection_main
from lib.SyntaxKiosK import SyntaxKiosK
from lib.config.python_mysql_dbconfig import read_db_config
from lib.config.db_lib import MySQLDataBase
from lib.DatabasePool import MySQLDatabaseProc


conn = None

class MySQLConnection():
    
    
    def db_connection():
        section = 'mysql'
        filename='config.ini'
        config = read_db_config(filename, section)
        if MySQLDatabaseProc.startCnxPool(config, section, 3):
            print(MySQLDatabaseProc.POOLS)
            conn = MySQLDatabaseProc.getConnection(section)
        return conn