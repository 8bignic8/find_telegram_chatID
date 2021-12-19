#!/usr/bin/env python
# coding: utf-8

#Version 10 12 2021
import json
import os
import requests
import argparse

json_config_path = "config.json"
def findLastChat(res):
    try:
        i = 1
        lastGroupID = 0
        mID = 0
        #print(res[2]['message']!= None)
        #print((((res[0])['message'])))#['chat'])['id'])
        res = res['result']
        res = res[len(res)-1] # gets last message

        res = res['message']
        print('Send from: ' + res['from']['first_name'] +' '+ res['from']['last_name'])
        print('In chat: ' + res['chat']['title'])
        myid = res['chat']['id']
    except:
        print('Message was send Not in a valid Group Chat')

    return myid



#### Parser argument part
try:
    parser = argparse.ArgumentParser(description='Input of the Telegram_Bot token')
    parser.add_argument('API_Bot_Token', metavar='T', type=str,
                        help='A string seperated by a : ')
    args = parser.parse_args()
    if(args):
        token = args.API_Bot_Token
    else:
        print('Error_parse')
except:
    print('Fail to get argument [Token] switching to inputMode')

    ##Input part
    print('You need to setup your Telegram bot and add it to a group with you!! Than you need to send a /start message in the group to initialize the connection')
    token = input('Set your BOT TOKEN e.g.: 213477740:ssf.......wfVg --> ') or 'ERR'



#### HTTP Request Part
print(str(token))
if ':' in token: #checks if a valid Telegram token has been inputed
    method = 'getUpdates' #sets the telegram request status
    response = requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(token, method) #reqets the updates with the token
    ).json()


else:
    print('Not the right Token :/')



####Setup config as dict
try:
    if(response['ok']):
        numb = findLastChat(response)
    else:
        print('No response from the Bot')
    config = {'myuserid': numb,
            'token': token,
             }
except:
    print('Error while getting the ID ')
    print(response['result'][len(response['result'])-1])


##Writing JSON with established dict
try:
    with open(json_config_path, 'w', encoding='utf-8') as f: #writing config.json in utf-8
        json.dump(config, f)
    print('Chat ID is ' + str(numb) + ' saved to ==> config.json')
except:
    print('config file write error')

