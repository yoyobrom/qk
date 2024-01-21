# -*- coding: utf-8 -*-
import base64
import json
import hashlib
import lxml.etree as etree
import requests
from PIL import Image


class CreateSession:
    def __init__(self, account, pwd):
        encodestr=base64.b64encode(pwd.encode('utf-8'))
        self.account = account
        self.pwd = encodestr
        self.session = requests.Session()
        self.session.get("http://172.13.1.32")

    def get_code(self):
        while True:
            figure_url = 'http://172.13.1.32/yzm?d='
            picture = self.session.get(figure_url).content
            with open('captcha.jpg', 'wb') as file:
                file.write(picture)
            picture = Image.open('captcha.jpg')
            picture.show()
            captcha = input('请输入验证码：')
            if len(captcha) != 0:
                break
        return captcha

    def login(self):
        post_url = "http://172.13.1.32/login!doLogin.action"
        bad_credit_url = "http://zhjw.scu.edu.cn/login?errorCode=badCredentials"
        bad_captcha_url = "http://zhjw.scu.edu.cn/login?errorCode=badCaptcha"
        data = {'account': self.account, 'pwd': self.pwd, 'verifycode': self.get_code()}
        resp = self.session.post(post_url, data=data)
        if resp.url == bad_captcha_url:
            print("验证码错误！")
            return self.login()
        elif resp.url == bad_credit_url:
            print("用户名或密码错误！")
            exit()
        else:
            print("登录成功！")
        selector = etree.HTML(resp.text)
        user_name = selector.xpath('''/html/body/div[@id="navbar"]/div[@id="navbar-container"]/div[@role="navigation"]/
        ul[@class="nav ace-nav"]//li[@class="light-blue"]//span[@class="user-info"]/text()''')
        print(user_name[1].strip())

    def query_score(self):
        # 成绩查询
        query_url = "http://zhjw.scu.edu.cn/student/integratedQuery/scoreQuery/allPassingScores/callback"
        response = self.session.get(query_url, cookies={"selectionBar": "1379870"})
        semester = json.loads(response.content.decode("utf-8"))["lnList"]
        for i in semester:
            for j in i["cjList"]:
                print(j["courseName"] + ": " + j["cj"])


if __name__ == '__main__':
    USERNAME = ""
    PASSWORD = ""
    f = CreateSession(USERNAME, PASSWORD)
    f.login()
    f.query_score()

