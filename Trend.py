def Trend(Checking_Condition,Live_Data1,Live_Data2):
    max_Chek = max(Checking_Condition)
    max_Live1 = max(Live_Data1)
    max_Live2 = max(Live_Data2)
    #This is the Condition for the down trand
    if (max_Chek > max_Live1) or (max_Live1 > max_Live2) or (max_Chek > max_Live1 and max_Live1 > max_Live2):
        return 1
    #This is the condition for the up trand
    elif (max_Chek < max_Live1) or (max_Live1 < max_Live2) or (max_Chek < max_Live1 and max_Live1 < max_Live2):
            return 0
    else:
        return 2
            
            
