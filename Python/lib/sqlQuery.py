from lib.imports import *
from lib.SyntaxKiosK import SyntaxKiosK

class sqlQuery():

    def sqlWrongBonding():
        return f"""SELECT id, mount, condition_flg, b.bonding, lcm_id, sn, b.model, b.android_v, b.dsservice_v, b.dsm365_v,
                         dm.face_total_num, dm.face_normal_num, dm.face_touch_num,
                        {SyntaxKiosK.sqlisDual()}
                    FROM displayer_realtime AS b
                    INNER JOIN displayer_model AS dm ON b.model = dm.model
                    INNER JOIN 
                    (SELECT DISTINCT b.bonding
                    FROM displayer_realtime AS b
                    INNER JOIN
                    (SELECT
                        DISTINCT bonding,
                        IF(SUM(lcm_id) = 2 OR SUM(lcm_id) > 3, 1, 0) AS err_lcm_id
                    FROM displayer_realtime AS b
                    WHERE mount > 0 AND bonding != ''
                    GROUP BY bonding) AS err_lcm_id_tab ON b.bonding = err_lcm_id_tab.bonding AND err_lcm_id_tab.err_lcm_id = 1
                    UNION DISTINCT


                    SELECT DISTINCT b.bonding
                    FROM displayer_realtime AS b
                    INNER JOIN (
                        SELECT DISTINCT

                            IF(bonding != '' AND bonding IS NOT NULL, bonding, a.sn) AS main_sn
                        FROM displayer AS a
                        INNER JOIN displayer_realtime AS b ON b.id = a.id
                        
                    ) AS bonding_tab ON b.bonding = bonding_tab.main_sn AND b.mount > 0
                    INNER JOIN (
                        SELECT 
                            model,
                    {SyntaxKiosK.sqlisDual()}
                        FROM displayer_model AS dm
                    ) AS isdual_tab ON isdual_tab.model = b.model AND is_dual = 1
                    GROUP BY b.bonding
                    HAVING SUM(is_dual) < 2
                    UNION DISTINCT


                    SELECT DISTINCT b.bonding
                    FROM displayer_realtime as b
                    INNER JOIN
                    (SELECT 
                        b.bonding,
                        {SyntaxKiosK.sqlBondingConditionFlg()} 
                    FROM displayer_realtime as b 
                    INNER JOIN displayer_model as dm ON b.model = dm.model
                    GROUP BY b.bonding) AS correct_tab ON b.bonding = correct_tab.bonding
                    WHERE b.bonding != '' AND b.condition_flg != correct_tab.correct_condition_flg
                    UNION DISTINCT


                    SELECT DISTINCT b.bonding
                    FROM displayer_realtime as b
                    INNER JOIN
                    (SELECT b.bonding,
                    {SyntaxKiosK.sqlisMountError()}
                    FROM displayer_realtime as b
                    INNER JOIN displayer_model as dm ON b.model = dm.model
                    WHERE b.bonding != ''
                    group by b.bonding) as mount_err_tab ON b.bonding = mount_err_tab.bonding
                    WHERE mount_err_tab.mount_err != 0) AS all_err_bonding ON b.bonding = all_err_bonding.bonding"""
    
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
    

    def sqldisplayerRun():
        return """SELECT * 
                    FROM dynascan365_main.displayer AS a
                    INNER JOIN displayer_realtime AS b ON b.id = a.id
                    WHERE a.belong_to = 3 and b.update_on >= '2023-07-11 07:00:00'"""
    
    
    def sqldisplayer_inconsistent():
        return """select a.id, a.sn,
                    a.`condition_flg`   , b.`condition_flg` as b_condition_flg, 
                    a.`a_pw_supply`     , b.`a_pw_supply` as b_a_pw_supply,
                    a.`a_lcm_pw`        , b.`a_lcm_pw` as b_a_lcm_pw, 
                    a.`a_lan_switch_pw` , b.`a_lan_switch_pw` as b_a_lan_switch_pw, 
                    a.`a_player_pw`     , b.`a_player_pw` as b_a_player_pw, 
                    a.`a_thermal`       , b.`a_thermal` as b_a_thermal, 
                    a.`a_failover`      , b.`a_failover` as b_a_failover, 
                    a.`a_flood`         , b.`a_flood` as b_a_flood, 
                    a.`a_overheat`      , b.`a_overheat` as b_a_overheat, 
                    a.`a_bright_h`      , b.`a_bright_h` as b_a_bright_h, 
                    a.`a_lcm_stick`     , b.`a_lcm_stick` as b_a_lcm_stick, 
                    a.`a_nosignal`      , b.`a_nosignal` as b_a_nosignal, 
                    a.`a_powerstate`    , b.`a_powerstate` as b_a_powerstate, 
                    a.`a_fan`           , b.`a_fan` as b_a_fan, 
                    a.`a_lcm_mount`     , b.`a_lcm_mount` as b_a_lcm_mount, 
                    a.`a_kiosk_mcb`     , b.`a_kiosk_mcb` as b_a_kiosk_mcb,  
                    a.`s_door`          , b.`s_door` as b_s_door, 
                    a.`s_lightbox`      , b.`s_lightbox` as b_s_lightbox, 
                    a.`s_reboot`        , b.`s_reboot` as b_s_reboot, 
                    a.`s_osdlock`       , b.`s_osdlock` as b_s_osdlock, 
                    a.`s_amb_bright`    , b.`s_amb_bright` as b_s_amb_bright, 
                    a.`s_amb_temp`      , b.`s_amb_temp` as b_s_amb_temp, 
                    a.`s_cab_temp`      , b.`s_cab_temp` as b_s_cab_temp
                from
                    dynascan365_main.displayer_realtime as a,
                    dynascan365_client.displayer_realtime_sync as b
                where a.id = b.id and 
                (
                    a.`condition_flg`   != b.`condition_flg` or 
                    a.`a_pw_supply`     != b.`a_pw_supply` or 
                    a.`a_lcm_pw`        != b.`a_lcm_pw` or 
                    a.`a_lan_switch_pw` != b.`a_lan_switch_pw` or 
                    a.`a_player_pw`     != b.`a_player_pw` or 
                    a.`a_thermal`       != b.`a_thermal` or 
                    a.`a_failover`      != b.`a_failover` or 
                    a.`a_flood`         != b.`a_flood` or 
                    a.`a_overheat`      != b.`a_overheat` or 
                    a.`a_bright_h`      != b.`a_bright_h` or 
                    a.`a_lcm_stick`     != b.`a_lcm_stick` or 
                    a.`a_nosignal`      != b.`a_nosignal` or 
                    a.`a_powerstate`    != b.`a_powerstate` or 
                    a.`a_fan`           != b.`a_fan` or 
                    a.`a_lcm_mount`     != b.`a_lcm_mount` or 
                    a.`a_kiosk_mcb`     != b.`a_kiosk_mcb` or 
                    a.`s_door`          != b.`s_door` or 
                    a.`s_lightbox`      != b.`s_lightbox` or 
                    a.`s_reboot`        != b.`s_reboot` or 
                    a.`s_osdlock`       != b.`s_osdlock`
                );"""
    

    def sqlmodelDifferent():
        return """SELECT a.id, a.sn AS signup_sn, a.model AS signup_model, c.name, b.sn, b.model, b.bonding, b.update_on
                    FROM displayer AS a
                    INNER JOIN displayer_realtime_sync AS b ON b.id = a.id
                    LEFT JOIN company AS c ON c.id = a.belong_to
                    WHERE b.model != a.model AND a.id != 1"""

    def sqlNewdisplayTable():
        return"""SELECT t1.*, a2.belong_to_name, a2.descp
                    FROM
                    (
                        SELECT IF( b.bonding = '', a.sn, b.bonding ) AS sn,
                                ( CASE
                                    WHEN (
                                        MAX( DISTINCT( CASE
                                            WHEN JSON_UNQUOTE( JSON_EXTRACT( b.status_tags, '$.lcm_id' ) ) = 1 THEN a.id
                                            ELSE 0
                                        END ) ) = 0
                                    ) THEN MAX( a.id )
                                    ELSE (
                                        MAX( DISTINCT( CASE
                                            WHEN JSON_UNQUOTE( JSON_EXTRACT( b.status_tags, '$.lcm_id' ) ) = 1 THEN a.id
                                            ELSE 0
                                        END ) )
                                    )
                                END ) AS main_id,
                                GROUP_CONCAT( DISTINCT( a.id ) ) AS bonding
                        FROM displayer AS a
                        INNER JOIN displayer_realtime AS b ON b.id = a.id
                        WHERE a.status != 'D'
                        GROUP BY sn
                    ) t1
                    INNER JOIN displayer          AS a2 ON a2.id = t1.main_id
                    INNER JOIN displayer_realtime AS b2 ON b2.id = t1.main_id
                    WHERE a2.status != 'D' """
    
    def sqlDisplayer_realtime(bonding):
        return f"""SELECT * 
                    FROM displayer_realtime
                    WHERE MATCH(bonding, sn)
                    AGAINST('{bonding}*' IN BOOLEAN MODE);"""
    

    def sqlduplicate_alarm_event(date):
        return f"""WITH batch AS (
                    SELECT *
                    FROM mcb_alarm_events
                    WHERE end_on = '{date}'
                    ORDER BY mcb_id
                    LIMIT 3000000
                )
                SELECT mcb_id, alarm_type, COUNT(*) AS num
                FROM batch
                GROUP BY mcb_id, alarm_type
                HAVING COUNT(*) > 1
                ORDER BY num, mcb_id;"""