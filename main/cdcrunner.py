import time
import unittest
import logging
import re
import os
import requests
import hashlib

class RunTest(unittest.TestCase):
    def check_verify(self, url, uin):
        url = "https://ssl.ptlogin2.qq.com/check?regmaster=&pt_tea=2&pt_vcode=1&uin={uin}&appid=550011611&js_ver=10275&js_type=1&login_sig=ASW6ngk7eE*mTSu*C6pnC1h5bH2KfIJ4yZUo8rgjvsHchfC*cAW7lT2vfFk4AXvG&u1=https%3A%2F%2Fwj.qq.com%2Fmine.html&r=0.335048458681266&pt_uistyle=40&pt_jstoken=2926650633"
        check = url.replace('{uin}',uin)
        pattern = re.compile("ptui_checkVC\('(.*)','(.*)','(.*)','(.*)','(.*)'\);")
        result = requests.get(check)
        checked = pattern.search(result.text).groups()
        return checked
    def get_verify(self):
        verify = "https://ssl.captcha.qq.com/getimage?aid=1003903&r=0.6472875226754695&uin={QQ}&cap_cd=aSD-ZVcNEcozlZUurhNYhp-MBHf4hjbJ"
        verify = verify.replace('{QQ}', self.QQ)
        path = os.path.join(os.path.basename(os.path.realpath(__file__)),'code.jpg')
        data = requests.get(verify)
        with open(path,'wb') as f:
            f.write(data.content)
    def passwd_secret(self, password, verify_code, uidhex):
        password = self.md5hex(password).upper()
        length = len(password)
        temp = ''
        for i in range(0, length, 2):
            temp+=r'\x'+password[i:i+2]
        return self.md5hex(self.md5hex(self.hex2asc(temp)+self.hex2asc(uidhex)).upper()+verify_code).upper()
    def md5hex(self,s):
        md5 = hashlib.md5()
        md5.update(s.encode('utf-8'))
        return md5.hexdigest()
    def hex2asc(self, s):
        _str = "".join(s.split(r'\x'))
        length = len(_str)
        data = ''
        for i in range(0, length, 2):
            data += chr(int(_str[i:i + 2], 16))
        return data
