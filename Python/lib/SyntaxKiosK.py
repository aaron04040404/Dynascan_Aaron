
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
    def sqlBondingMainId(mcb_main_tab='' , mcb_realtime_tab='',use_to_select = 'sqlBondingMainId2()' , output_alias = "main_id" ):
        
        return f""" {use_to_select} AS {output_alias}"""


    def sqlisDual(mcb_model_tab = 'dm', output_alias = 'is_dual'):

        return f"""CONVERT( CASE
                            WHEN ( {mcb_model_tab}.face_total_num ) IS NULL OR ( {mcb_model_tab}.face_total_num ) = 1 THEN 0
                            WHEN ( {mcb_model_tab}.face_normal_num + {mcb_model_tab}.face_touch_num ) = ( {mcb_model_tab}.face_total_num ) AND ( {mcb_model_tab}.face_total_num ) >= 2 THEN 1
                            ELSE 0
                    END, UNSIGNED INTEGER ) AS {output_alias}"""     
        

    def sqlBondingConditionFlg(mcb_model_tab = 'dm', mcb_realtime_tab = 'b', output_alias = 'correct_condition_flg'):

        return f"""CONVERT( CASE
                                WHEN MAX( {mcb_model_tab}.face_total_num ) IS NULL OR MAX( {mcb_model_tab}.face_total_num ) = 1 THEN MAX( {mcb_realtime_tab}.condition_flg )
                                WHEN SUM( {mcb_realtime_tab}.mount ) = MAX( {mcb_model_tab}.face_normal_num + {mcb_model_tab}.face_touch_num ) THEN (
                                    CASE
                                        WHEN MAX( ( IF( {mcb_realtime_tab}.mount > 0, {mcb_realtime_tab}.condition_flg, NULL ) ) ) = 1 AND
                                            MIN( ( IF( {mcb_realtime_tab}.mount > 0, {mcb_realtime_tab}.condition_flg, NULL ) ) ) = 1
                                        THEN 1
                                        WHEN MAX( ( IF( {mcb_realtime_tab}.mount > 0, {mcb_realtime_tab}.condition_flg, NULL ) ) ) = 3 AND
                                            MIN( ( IF( {mcb_realtime_tab}.mount > 0, {mcb_realtime_tab}.condition_flg, NULL ) ) ) = 3
                                        THEN 3
                                        WHEN MAX( ( IF( {mcb_realtime_tab}.mount > 0, {mcb_realtime_tab}.condition_flg, NULL ) ) ) = 0 AND
                                            MIN( ( IF({mcb_realtime_tab}.mount > 0, {mcb_realtime_tab}.condition_flg, NULL ) ) ) = 0
                                        THEN 0
                                        ELSE 2
                                    END )
                                ELSE (
                                    MAX( {mcb_realtime_tab}.condition_flg )
                                )
                    END, UNSIGNED INTEGER ) AS {output_alias}"""
    
    def sqlisMountError(mcb_model_tab = 'dm', mcb_realtime_tab = 'b', output_alias = 'mount_err'):

        return f"""CONVERT( CASE
                                WHEN MAX( {mcb_model_tab}.face_total_num ) IS NULL THEN 0
                                WHEN SUM( {mcb_realtime_tab}.mount ) = 0 THEN 100
                                WHEN SUM( {mcb_realtime_tab}.mount ) = MAX( {mcb_model_tab}.face_normal_num + {mcb_model_tab}.face_touch_num ) THEN 0
                                WHEN SUM( {mcb_realtime_tab}.mount ) < MAX( {mcb_model_tab}.face_normal_num + {mcb_model_tab}.face_touch_num ) THEN -1
                                WHEN SUM( {mcb_realtime_tab}.mount ) > MAX( {mcb_model_tab}.face_normal_num + {mcb_model_tab}.face_touch_num ) THEN 1
                    END, SIGNED INTEGER ) AS {output_alias}"""

            
    
    def test():
        
        sql = SyntaxKiosK.sqlBondingMainId()
        
        print(SyntaxKiosK.sqlBondingMainId())

#SyntaxKiosK.test()