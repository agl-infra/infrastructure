import requests
import json
from collections import namedtuple

def getToken(username,passoword,url):
    headers = {
    'content-type': 'application/x-www-form-urlencoded'
    }
    params = {
    'username': username,
    'password': passoword
    }
    resp = requests.post(url, data=params, headers=headers)
    return resp.content

def getCMDBJson():
    data = json.load(open('vm-output.json'))
    # data = json.dumps(data)
    # try:
    #     x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys(),rename=False)(*d.values()))
    #     print(x.Business_Owner.value)
    # except ValueError as err:
    #     print(err)
    res = {"values":{ "Name": "",

        "Asset ID+": "",

        "Short Description": "",

        "Company": "AGL",

        "Primary Capability": "Server",

        "AssetLifecycleStatus": "Deployed",

        "Environment Specification": "Staging",

        "DNS Host Name": "",

        "Data Set Id" : "BMC.ASSET",

		"Building" : "'Australia South East'",

        "Serial Number" : ""}}
    res['values']['Name']=data['VM_Name']['value']
    res['values']['Asset ID+']=data['VM_Name']['value']
    res['values']['Short Description']=data['VM_Name']['value']
    res['values']['DNS Host Name']=data['VM_Name']['value']
    
    
    
    res = json.dumps(res)
    return res



def updateCMDB(data,token,url):
    headers = {
        'Content-Type':'application/json',
        'Authorization':'AR-JWT '+token
    }
    resp = requests.post(url,data=data,headers=headers)
    return resp.status_code

def closeCR(msg,url,token):
    headers = {
        'Content-Type':'application/json',
        'Authorization':'AR-JWT '+token
    }
    resp = requests.get(url,headers=headers)
    return (resp.content)


###############main####################

url = "http://glawi1283.agl.int:8008/api/jwt/login"
password = "remedyapi"
username = "remedyapi"

cmdbUrl = "http://glawi1283.agl.int:8008/api/arsys/v1/entry/AST:ComputerSystem"
cmURL = "http://glawi1283.agl.int:8008/api/arsys/v1/entry/CHG:ChangeInterface"

token = getToken(username,password,url).decode('utf-8')
print(token)
data=getCMDBJson()
print(data)
if updateCMDB(data,token,cmdbUrl)==204:
    #closeCR('',cmURL,token)
    print("CMDB Updated Successfully.")


