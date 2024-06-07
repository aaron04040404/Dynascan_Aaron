
class SyntaxKiosK:
    db_settings = {
    "host" : "127.0.0.1",
    "port" : 3306,
    "user" : "root",
    "password" : "tn830120",
    "db" : "dynascan365_main",
    "charset" : "utf8"
    }
    


    #def sqlBondingMainSn():




    #SELECT 出 sqlBondingMainId2() 的值以 main_id的欄位輸出
    def sqlBondingMainId(mcb_main_tab='' , mcb_realtime_tab='',use_to_select = '' , output_alias = "main_id" ):
        
        return f""" {use_to_select} AS {output_alias}"""
            
    
    def test():
        
        sql = SyntaxKiosK.sqlBondingMainId()
        
        print(SyntaxKiosK.sqlBondingMainId())

#SyntaxKiosK.test()