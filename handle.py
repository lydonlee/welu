# -*- coding: utf-8 -*-
# filename: handle.py
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
import hashlib
import web

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = 'tokenweilu' #请按照公众平台官网\基本配置中信息填写
            print("handle/GET func: signature: ,token ,echostr,timestamp,nonce",signature,token,echostr,timestamp,nonce)

            check_signature(token, signature, timestamp, nonce):  # 检查验证请求的签名
            return echostr
        except InvalidSignatureException as Argument:
            return Argument