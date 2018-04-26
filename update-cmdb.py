#!/usr/bin/python3.6
from time import sleep
import requests
import json
from collections import namedtuple
from datetime import datetime

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

		"Building" : "Australia South East",

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

def getDateTime():
    timeOffset = datetime.utcnow()
    now = timeOffset.strftime("%H:%M:%S")
    nowDay = timeOffset.strftime("%Y-%m-%d")
    res = nowDay+'T'+now
    return res

def getInfraChangeID():
    id=''
    file = open("cr.txt", "r")
    for line in file:
        id=line
    file.close()
    # print(cr)
    return id


def getCrNo(InfraChangeID,token,url):
    headers = {
        'Content-Type':'application/json',
        'Authorization':'AR-JWT '+token
    }
    url=url+"?q='Infrastructure Change ID' = \""+InfraChangeID+"\"&fields=values(Request ID)"
    resp=requests.get(url,headers=headers)
    data=json.loads(resp.content.decode('utf-8'))['entries']
    return data[0]['values']['Request ID']



def getCrJson():
    res = {
        "values" : {
		"z1D_Action" : "MODIFY",
        "Outage?": "No",
        "Change Request Status": "Closed",
        "Status Reason": "Successful",
        "Scheduled Start Date": "2018-04-01T10:00:00",
        "Scheduled End Date" : "2018-04-02T15:00:00",
        "Actual Start Date" : "2018-04-01T10:00:00",
        "Actual End Date" : "2018-04-02T15:00:00"
        }
        }
    res['values']['Scheduled Start Date']=getDateTime()
    res['values']['Actual Start Date']=getDateTime()
    sleep(10)
    res['values']['Scheduled End Date']=getDateTime()
    res['values']['Actual End Date']=getDateTime()
    return res

def closeCR(crNo,url,token,data):
    headers = {
        'Content-Type':'application/json',
        'Authorization':'AR-JWT '+token
    }
    url=url+crNo
    resp = requests.get(url,data=data,headers=headers)
    return (resp.content.decode('utf-8'))

###############main####################

url = "http://glawi1283.agl.int:8008/api/jwt/login"
password = "remedyapi"
username = "remedyapi"

cmdbUrl = "http://glawi1283.agl.int:8008/api/arsys/v1/entry/AST:ComputerSystem"

crURL= "http://glawi1283.agl.int:8008/api/arsys/v1/entry/CHG:ChangeInterface/"

token = getToken(username,password,url).decode('utf-8')
print('Token Generated...\n')


data=getCMDBJson()

status=updateCMDB(data,token,cmdbUrl)




if status==204:
    print("CMDB Updated Successfully....\n")
    id=getInfraChangeID()
    print('Attempting to get Infrastructure Change ID...\n')
    print('Infrastructure Change ID='+id+'\n')
    print('Attempting to get CR Number...')
    cr=getCrNo(id,token,crURL)
    print('CR Number='+cr+'\n')

    print('Attempting to close CR...')
    print(closeCR(cr,crURL,token,getCrJson()))


else:
    print('CMDB Update Error:',status)
