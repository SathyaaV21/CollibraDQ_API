import requests
import json

#Login API to get the JWT token.
body={
  "username": "sathyaav",
  "password": "Lucid@123",
  "iss": "public"
}
url="http://192.168.169.90:9000/v3/auth/signin"
r=requests.post(url, json=body, verify=False)
token= r.json()
myToken=token[ "token"]





#Generating JWT token with "Bearer" as prefix.
head = {'Authorization': 'Bearer ' +myToken}

print(head)




#Fetching all the rules
get_rules_url="http://192.168.169.90:9000/v3/rules"
#getRules=requests.get(get_rules_url,headers=head, verify=False)
#print(getRules.text)




#Creating a new simple rule for a specific data set(Using V2 of the APIs..because the latest V3 is not working fine).

create_rule_url = "http://192.168.169.90:9000/v2/createrule"

with open("C:/Users/sathy/Downloads/DQRules.json", 'r') as file:
  rulesSet=json.load(file)

query_params={
    "dataset": "birthplace_2018_census_csv_csv_1",
    "rulenm": "newPythonRule3",
    "ruletype": "SQLF",
    "where": "Birthplace is not Null;",
    "points": 1,
    "perc": 1
    
   
    }
count=0
for key,value in rulesSet.items():
  query_params["rulenm"]=key
  query_params["where"]=value
  response = requests.post(create_rule_url,params=query_params,headers=head,verify=False)
  count+=1
  print(count, "hi",response.text)
