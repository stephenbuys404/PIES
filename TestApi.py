#requests
import requests
import json

host_url=''

def GET():
    response_code=requests.get(host_url+'/todos')
    print(response_code)
    response_result=(json.dumps(response_code.json(),indent=4))
    print(response_result)

def POST():
    body={'userId':11,'id':201,'title':'hello','completed':False}
    response_code=requests.post(host_url+'/todos',data=body)
    print(response_code)
    response_result=(json.dumps(response_code.json(),indent=4))
    print(response_result)

def PUT():
    body={'userId':11,'id':201,'title':'hello','completed':False}
    response_code=requests.post(host_url+'/todos/1',data=body)
    print(response_code)
    response_result=(json.dumps(response_code.json(),indent=4))
    print(response_result)

def DELETE():
    response_code=requests.delete(host_url+'/todos/200')
    print(response_code)
    response_result=(json.dumps(response_code.json(),indent=4))
    print(response_result)

GET()