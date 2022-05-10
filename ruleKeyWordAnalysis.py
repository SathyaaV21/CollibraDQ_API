import csv
from Util_Class import Utils
import Util_Class
import json

util=Utils()

reader = util.csv_read("C:/Users/sathy/Downloads/Book4.csv")
keywords={"tostring","exists","matches_regex","in_reference_list" ,"<>"}
#reader= util.csv_read("Social_Network_Ads_SVM.csv")
#writer=util.csv_writerows("C:/Users/sathy/Downloads/csvexample/newOne.csv",reader)
#r=reader.json()
print(reader)
data_dict = {}
for rows in reader[1:]:
 
            #assuming a column named 'No'
            #to be the primary key
    rulename = rows[0]
    rulelogic=rows[1]
    st=rulelogic
    keys=[]
    for i in st.split():
        for j in keywords:
            if j in i:
                keys.append(j)

    data_dict[rulename] = keys
 
    #open a json file handler and use json.dumps
    #method to dump the data
    #Step 3
with open("C:/Users/sathy/Downloads/DQRulesKeywords4.json", 'w', encoding = 'utf-8') as json_file_handler:
        #Step 4
    json_file_handler.write(json.dumps(data_dict, indent = 2))
 

   



st='IF NTS."VT_FT_HOLD_FOR_EXDATE_RULE".INSTR_ID exists AND DBCDB1A.DB5ADB.NTS."FT_T_IAPR".PY_TMS > date()-3 AND NTS."VT_FT_T_ISSU_EX_DATE_COMPARE".INSTR_ID exists THEN left(tostring(NTS."VT_FIR_AST_FMST_FUTURE_NOTNULL".D_FRST_NXT_EX),10) >= left(tostring(DBCDB1A.DB5ADB.NTS."FT_T_IADC".EX_TMS),10)'
keywords={"tostring","exists","matches_regex","in_reference_list" ,"<>"}
for i in st.split():
    for j in keywords:
        if j in i:
            print(j)

# for i in range(1,len(st.split())):
#     print(st.split()[i-1])    