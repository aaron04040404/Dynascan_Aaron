#from lib.db_connection import conn
#from lib.config import get_connection_main
from lib.imports import *
from lib.SyntaxKiosK import SyntaxKiosK
from lib.DatabasePool import MySQLDatabaseProc
from lib.db_connection import MySQLConnection
from lib.ReturnData import ReturnData
from lib.CheckData import CheckData


def MainDisplayer():
    try:
        #在config裡面做連接function
        #引用Class實例要加括號()
        
        #conn = MySQLDataBase().connection(read_db_config())
        conn = MySQLConnection.db_connection()
        with conn.cursor() as cursor:
    
            command = f"""SELECT id, mount, condition_flg, b.bonding, lcm_id, sn, model
                            FROM
                            (SELECT bonding
                            FROM
                            (SELECT
                                b.*,
                                IF(b.bonding != '' AND b.bonding IS NOT NULL, b.bonding, a.sn) AS main_sn,
                                CONVERT( CASE
                                    WHEN ( dm.face_total_num ) IS NULL OR ( dm.face_total_num ) = 1 THEN 0
                                    WHEN ( dm.face_normal_num + dm.face_touch_num ) = ( dm.face_total_num ) AND ( dm.face_total_num ) >= 2 THEN 1
                                    ELSE 0
                                END, UNSIGNED INTEGER ) AS is_dual

                            FROM displayer AS a
                            INNER JOIN displayer_realtime AS b ON a.id = b.id
                            INNER JOIN displayer_model AS dm ON dm.model = b.model) AS standard_tab
                            INNER JOIN (SELECT {SyntaxKiosK.sqlBondingMainId(use_to_select='unnormalBondingId()')}) AS main_id_tab ON main_id_tab.main_id = standard_tab.id) AS bonding_tab
                            INNER JOIN displayer_realtime AS b ON b.bonding = bonding_tab.bonding"""
            
            cursor.execute(command)
            
            
            data = cursor.fetchall()
            column_names = [i[0] for i in cursor.description]
            df = pd.DataFrame(data, columns = column_names)
         
            print(df)
            

    finally:
        
        conn.close()
    
    return ReturnData.jsonify_return(df)
        
def sql_searching2():
    try:
    
        conn = MySQLConnection.db_connection()
    
        with conn.cursor() as cursor:
    
            #command = request.get_json()
            #print(command) #測試傳入的command是否正確
            mcb_id = request.json.get('mcb_id')
            start_date = request.json.get('startDate')
            end_date = request.json.get('endDate')
            print(mcb_id)
            print(start_date)
            print(end_date)

            # param -> '$.mcb_id' equal to JSON_EXTRACT(param, '$.mcb_id')
            command = f"""SELECT 
                        cast(param-> '$.mcb_id' as unsigned) as mcb_id, 
                        cast(param-> '$.alarm_type'as unsigned) as alarm_type, 
                        happen_on
                        FROM dynascan365_main.notification_contents
                        where JSON_EXTRACT(param, '$.mcb_id') = {mcb_id} and happen_on between "{start_date}" and "{end_date}" """
            print(command)
            cursor.execute(command)
            
            #cursor.callproc('test_proc')
            #result 獲取一次查詢
            data = cursor.fetchall()
            #for result in cursor.stored_results():
                    #data 回傳 result值
                #data = result.fetchall()
            column_names = [i[0] for i in cursor.description]
            #column_names = ['id', 'value', 'datetime']
            df = pd.DataFrame(data, columns = column_names)
            #print(df)
            
            #for row in result:
                #print(row)

    finally:
        conn.close()
    
    return ReturnData.jsonify_return(df)


def wrong_Bonding():
    try:
        #在config裡面做連接function
        #引用Class實例要加括號()
        
        #conn = MySQLDataBase().connection(read_db_config())
        """section = 'mysql'
        filename = 'config.ini'
        config = read_db_config(filename, section)
        if MySQLDatabaseProc.startCnxPool(config, section, 3):
            print(MySQLDatabaseProc.POOLS)
            conn = MySQLDatabaseProc.getConnection(section)"""
        conn = MySQLConnection.db_connection()
    
        with conn.cursor() as cursor:
    
            command = f"""SELECT id, mount, condition_flg, b.bonding, lcm_id, sn, b.model, dm.face_total_num, dm.face_normal_num, dm.face_touch_num,
                            CONVERT( CASE
                            WHEN ( dm.face_total_num ) IS NULL OR ( dm.face_total_num ) = 1 THEN 0
                            WHEN ( dm.face_normal_num + dm.face_touch_num ) = ( dm.face_total_num ) AND ( dm.face_total_num ) >= 2 THEN 1
                            ELSE 0
                        END, UNSIGNED INTEGER ) AS is_dual
                    FROM
                    (SELECT DISTINCT b.bonding
                    FROM
                    (SELECT bonding
                    FROM
                    (SELECT id, mount, condition_flg, bonding, lcm_id, sn, model, main_sn
                    FROM
                    (SELECT DISTINCT
                        IF(b.bonding != '' AND b.bonding IS NOT NULL, b.bonding, a.sn) AS main_sn	
                    FROM displayer AS a 
                    INNER JOIN displayer_realtime AS b ON b.id = a.id) AS bonding_tab
                    INNER JOIN displayer_realtime AS b ON b.bonding = bonding_tab.main_sn AND b.mount > 0) AS bonding_tab2
                    GROUP BY bonding_tab2.bonding
                    HAVING SUM(bonding_tab2.lcm_id) = 2 OR SUM(bonding_tab2.lcm_id) > 3) AS bonding_tab3
                    INNER JOIN displayer_realtime AS b ON b.bonding = bonding_tab3.bonding
                    UNION DISTINCT


                    SELECT DISTINCT b.bonding
                    FROM
                    (SELECT bonding
                    FROM
                    (SELECT bonding_tab2.*, isdual_tab.is_dual
                    FROM
                    (SELECT id, mount, condition_flg, bonding, lcm_id, sn, model, main_sn
                    FROM
                    (SELECT DISTINCT
                        IF(b.bonding != '' AND b.bonding IS NOT NULL, b.bonding, a.sn) AS main_sn	
                    FROM displayer AS a 
                    INNER JOIN displayer_realtime AS b ON b.id = a.id) AS bonding_tab
                    INNER JOIN displayer_realtime AS b ON b.bonding = bonding_tab.main_sn AND b.mount > 0) AS bonding_tab2
                    INNER JOIN 
                    (SELECT 
                    model,
                    CONVERT( CASE
                            WHEN ( displayer_model.face_total_num ) IS NULL OR ( displayer_model.face_total_num ) = 1 THEN 0
                            WHEN ( displayer_model.face_normal_num + displayer_model.face_touch_num ) = ( displayer_model.face_total_num ) AND ( displayer_model.face_total_num ) >= 2 THEN 1
                            ELSE 0
                        END, UNSIGNED INTEGER ) AS is_dual
                    FROM dynascan365_main.displayer_model ) AS isdual_tab ON isdual_tab.model = bonding_tab2.model AND is_dual = 1) AS bonding_isdual_tab
                    GROUP BY bonding_isdual_tab.bonding
                    HAVING SUM(bonding_isdual_tab.is_dual) < 2) AS final_isdual
                    INNER JOIN displayer_realtime AS b ON b.bonding = final_isdual.bonding
                    UNION DISTINCT


                    SELECT DISTINCT b.bonding
                    FROM
                    (SELECT bonding, 
                    CONVERT( CASE
                                WHEN MAX( dm.face_total_num ) IS NULL OR MAX( dm.face_total_num ) = 1 THEN MAX( b.condition_flg )
                                WHEN SUM( b.mount ) = MAX( dm.face_normal_num + dm.face_touch_num ) THEN (
                                    CASE
                                        WHEN MAX( ( IF( b.mount > 0, b.condition_flg, NULL ) ) ) = 1 AND
                                            MIN( ( IF( b.mount > 0, b.condition_flg, NULL ) ) ) = 1
                                        THEN 1
                                        WHEN MAX( ( IF( b.mount > 0, b.condition_flg, NULL ) ) ) = 3 AND
                                            MIN( ( IF( b.mount > 0, b.condition_flg, NULL ) ) ) = 3
                                        THEN 3
                                        WHEN MAX( ( IF( b.mount > 0, b.condition_flg, NULL ) ) ) = 0 AND
                                            MIN( ( IF(b.mount > 0, b.condition_flg, NULL ) ) ) = 0
                                        THEN 0
                                        ELSE 2
                                    END )
                                ELSE (
                                    MAX( b.condition_flg )
                                )
                            END, UNSIGNED INTEGER ) AS correct_condition_flg
                    FROM
                    (SELECT id, mount, condition_flg, bonding, lcm_id, sn, model, main_sn
                    FROM
                    (SELECT DISTINCT
                        IF(b.bonding != '' AND b.bonding IS NOT NULL, b.bonding, a.sn) AS main_sn	
                    FROM displayer AS a 
                    INNER JOIN displayer_realtime AS b ON b.id = a.id) AS bonding_tab
                    INNER JOIN displayer_realtime AS b ON b.bonding = bonding_tab.main_sn) AS b
                    INNER JOIN displayer_model AS dm ON dm.model = b.model
                    GROUP BY b.bonding) AS correct_tab
                    INNER JOIN displayer_realtime AS b ON b.bonding = correct_tab.bonding
                    WHERE b.condition_flg != correct_tab.correct_condition_flg
                    UNION DISTINCT


                    SELECT DISTINCT b.bonding
                    FROM
                    (SELECT bonding,
                    CONVERT( CASE
                                WHEN MAX( dm.face_total_num ) IS NULL THEN 0
                                WHEN SUM( b.mount ) = 0 THEN 100
                                WHEN SUM( b.mount ) = MAX( dm.face_normal_num + dm.face_touch_num ) THEN 0
                                WHEN SUM( b.mount ) < MAX( dm.face_normal_num + dm.face_touch_num ) THEN -1
                                WHEN SUM( b.mount ) > MAX( dm.face_normal_num + dm.face_touch_num ) THEN 1
                            END, SIGNED INTEGER ) AS mount_err
                    FROM
                    (SELECT id, mount, condition_flg, bonding, lcm_id, sn, model, main_sn
                    FROM
                    (SELECT DISTINCT
                        IF(b.bonding != '' AND b.bonding IS NOT NULL, b.bonding, a.sn) AS main_sn	
                    FROM displayer AS a 
                    INNER JOIN displayer_realtime AS b ON b.id = a.id) AS bonding_tab
                    INNER JOIN displayer_realtime AS b ON b.bonding = bonding_tab.main_sn) AS b
                    INNER JOIN displayer_model AS dm ON dm.model = b.model
                    GROUP BY b.bonding) AS mount_err_tab
                    INNER JOIN displayer_realtime AS b ON b.bonding = mount_err_tab.bonding
                    WHERE mount_err_tab.mount_err != 0) AS all_err_bonding
                    INNER JOIN displayer_realtime AS b ON b.bonding = all_err_bonding.bonding
                    INNER JOIN displayer_model AS dm ON b.model = dm.model"""
            
            cursor.execute(command)
            
            
            data = cursor.fetchall()
            column_names = [i[0] for i in cursor.description]
            df = pd.DataFrame(data, columns = column_names)
            CheckData.CheckWrong_Bonding(df)
            #df.to_csv("我要的錯誤資料.csv")
            #print(df)
            
    finally:
        
        conn.close()
    
    return ReturnData.jsonify_return(df)