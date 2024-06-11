from lib.imports import *
from lib.SyntaxKiosK import SyntaxKiosK

class sqlQuery():

    def sqlWrongBonding():
        return f"""SELECT id, mount, condition_flg, b.bonding, lcm_id, sn, b.model, b.android_v, b.dsservice_v, b.dsm365_v,
                         dm.face_total_num, dm.face_normal_num, dm.face_touch_num,
                        {SyntaxKiosK.sqlisDual()}
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
                    {SyntaxKiosK.sqlisDual()}
                    FROM displayer_model AS dm) AS isdual_tab ON isdual_tab.model = bonding_tab2.model AND is_dual = 1) AS bonding_isdual_tab
                    GROUP BY bonding_isdual_tab.bonding
                    HAVING SUM(bonding_isdual_tab.is_dual) < 2) AS final_isdual
                    INNER JOIN displayer_realtime AS b ON b.bonding = final_isdual.bonding
                    UNION DISTINCT


                    SELECT DISTINCT b.bonding
                    FROM
                    (SELECT bonding, 
                    {SyntaxKiosK.sqlBondingConditionFlg()}
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
                    {SyntaxKiosK.sqlisMountError()}
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
    
    def sqlNotification(mcb_id, start_date, end_date):
        return f"""SELECT 
                cast(param-> '$.mcb_id' as unsigned) as mcb_id, 
                cast(param-> '$.alarm_type'as unsigned) as alarm_type, 
                happen_on
                FROM dynascan365_main.notification_contents
                where JSON_EXTRACT(param, '$.mcb_id') = {mcb_id} and happen_on between "{start_date}" and "{end_date}" """
    
    def sqldisplayerVersion():
        return """SELECT 
                    IF(a.sn != b.sn, 1, 0) AS sn_error, IF(a.model != b.model, 1, 0) AS model_error,
                    b.update_on, IF( DATE_ADD( b.update_on, INTERVAL 5 MINUTE ) < NOW(), 1, 0 ) AS off_line,
                    a.sn AS a_sn, a.model AS a_model, a.belong_to_name, b.bonding, b.sn AS b_sn, b.model AS b_model, b.android_v, b.dsservice_v, b.dsm365_v,
                    JSON_UNQUOTE( JSON_EXTRACT(b.status_tags, '$.ttc_ver') ) AS tcc_ver
                    
                FROM displayer AS a
                INNER JOIN displayer_realtime AS b ON b.id = a.id
                WHERE a.status != 'D' AND b.mount = 1"""
    
