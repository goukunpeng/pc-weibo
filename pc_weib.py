#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import requests
import time
import base64
from urllib import parse
from user_agent import getUserAgent


class PcWeiboLogin(object):

    def __init__(self, user, passwd):
        urlencode_user = parse.urlencode(user)
        base64_encode_user = base64.b64encode(urlencode_user)
        self.__user = base64_encode_user
        self.passwd = passwd

    def user(self):
        print(self.__user)

    def pre_login():
        pre_url = 'https://login.sina.com.cn/sso/prelogin.php?'
        params = {
            'entry': 'account',
            'callback': 'sinaSSOController.preloginCallBack',
            'su': 'MTExMQ==',   # 用户账号，先urlencode，再base64 encode
            'rsakt': 'mod',
            'client': 'ssologin.js(v1.4.15)',
            '_': '1527149300954'
        }
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'login.sina.com.cn',
            'Referer': 'https://login.sina.com.cn/signup/signin.php',
            'User-Agent': getUserAgent()
        }
        data = {
        'entry': 'sso',
        'gateway': '1',
        'from': 'null',
        'savestate': '30',
        'useticket': '0',
        'pagerefer': 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)',
        'vsnf': '1',
        'su': 'Z291a3VucGVuZw==',    # 用户名,先urlencode，再使用base64 Encode
        'service': 'sso',
        'servertime': '1527146988',   # 请求服务时间戳(s)
        'nonce': 'QMD967',
        'pwencode': 'rsa2',
        'rsakv': '1330428213',
        'sp': '7dd9e629d577b7565b305fc90c08116ed565b93c875abfec0a1fe51c7272de92b4087d9ce00cec136ce83f4b0ed3ad127c7939976cdd'
              '23985096052ae9dc1e009b1509e6a0aa4cf9d6a7bce938bfe7a9427b03da734e0d79c86b36b1c47b28f0468ea5595a39c42c3bf4537'
              'e6194a503d1db4b57f86c1290409c53308db2d7b5',  # 密码
        'sr': '1536*864',
        'encoding': 'UTF-8',
        'cdult': '3',
        'domain': 'sina.com.cn',
        'prelt': '152',
        'returntype': 'TEXT'
        }


gkp = PcWeiboLogin('goukunpeng@sina.cn', '111')
gkp.user()

