

class CheckData():

    @staticmethod
    def CheckWrong_lcm_id(subset):
            sum_lcm_id = subset[subset['mount'] > 0]['lcm_id'].sum() #lcm_id值做相加
            if sum_lcm_id == 3 or sum_lcm_id == 1:
                return True
            else:
                return False

    @staticmethod
    def CheckWrong_model(subset):
            sum_isdual = subset['is_dual'].sum()
            if sum_isdual >= 2:
                return True
            else:
                return False
            

    @staticmethod
    def CheckWrong_condition_flg(subset):
            max_condition_flg = subset[subset['mount'] > 0]['condition_flg'].max()
            min_condition_flg = subset[subset['mount'] > 0]['condition_flg'].min()
            if max_condition_flg == min_condition_flg:
                return True
            else:
                return False
    
    @staticmethod
    def CheckWrong_mount(subset):
            sum_mount = subset['mount'].sum()
            if sum_mount == (subset['face_normal_num']+subset['face_touch_num']).max():
                return True
            else:
                return False
    @staticmethod        
    def CheckWrong_Bonding(df):
        bonding_values = df['bonding'].unique() #classify the bonding
        for bonding_value in bonding_values:
            subset = df[df['bonding'] == bonding_value]
            if CheckData.CheckWrong_lcm_id(subset):
                if CheckData.CheckWrong_model(subset):
                    if CheckData.CheckWrong_condition_flg(subset):
                        if CheckData.CheckWrong_mount(subset):
                            print(f"{bonding_value} is no problem")
        return ("Check Complete!!")