#!/usr/bin/env python
# coding: utf-8

#Version 07 12 2021
import json
import os
import requests
import argparse

def findID(token):
    print(token)
    if ':' in token: #checks if a valid Telegram token has been inputed
        method = 'getUpdates' #sets the telegram request status
        response = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(token, method) #reqets the updates with the token

        ).json()
        #print((response['result'][0]['message']['chat']))#['message'])['chat']))
        chatID = ((((response['result'][0])['message'])['chat'])['id']) #searches in the dict for the chat message token
        print('Your Chat ID is ' + str(chatID)) #shows it to the user
        return chatID
    else:
        print('Not the right Token :/')

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


####Setup config as dict
config = {'myuserid': findID(token),
        'token': token,
         }


##Writing JSON with established dict
try: 
    with open('config.json', 'w', encoding='utf-8') as f: #writing config.json in utf-8
        json.dump(config, f)
except:
    print('config file write error')

