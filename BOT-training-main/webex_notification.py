import requests
import json
import time

def send_webex_message(token,text):
    token = 'Bearer '+token
    m={
#   "roomId": whole_json["data"]["roomId"],
   "text" : text,
   "toPersonEmail":"adarshpreddy18@gmail.com"
#    "parentId" : whole_json['data']['id'],
}
    r = requests.post('https://webexapis.com/v1/messages', data=json.dumps(m),
                  headers={'Authorization': token,'Content-Type': 'application/json'})
    
    return r

token='YmRmNjM4ZGMtZDExNS00MTM0LTk2MTctMjljN2ZkODgxYTVjYTU1ODQ3MTYtNDg4_P0A1_ff715326-fd83-4783-a6df-1d61fb6babb3'

while True:
    time.sleep(30)
    send_webex_message(token,"Heyyy, its time to drink water")