from configparser import ConfigParser
import os


def read_db_config(filename='config.ini',section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    
    #把路徑設成此python file的路徑再往外三層到config.ini檔案位置
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    config_path = os.path.join(base_path, filename)
    #config_path = os.path.abspath(filename)
    #parser.read(os.path.abspath(r"D:\flaskvue3\vue-project\Python\config.ini"))
    parser.read(os.path.abspath(config_path))
    print(config_path)

    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception(
            '{0} not found in the {1} file'.format(
                section, filename))

    return db
