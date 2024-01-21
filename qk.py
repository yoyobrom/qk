import requests



# 获取cookie 和 课程id就可以抢课


def qian1():
    data = 1159207
    # data 是找到的课程ID，因为python没学好，代码写的有点乱
    # 下面是地址 就是我们抓到的那个数据包的URL
    url = 'http://172.13.1.32/xsxklist!getSksj.action?kcrwdms=' + str(data)
    cookie = 'JSESSIONID=9EC12E50A166BADA9587A33E443016F4'
    header = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'Referer': 'http://172.13.1.32/xsxklist!xsmhxsxk.action',
        'cookie': cookie
    }

    # 一直抢！
    while True:
        # 设定5s服务器未应答就放弃这次，鬼知道是服务器炸了还是。。。。
        mes = requests.get(url, headers=header, timeout=5)
        # 打印返回的结果，就是弹出来的那个小窗口的内容
        print(str(1) + str(mes.status_code) + ':' + str(mes.text))


# 后面是不同的课，因为不能吊在一课树上！
def qian2():
    data = 1159208
    # data 是找到的课程ID，因为python没学好，代码写的有点乱
    # 下面是地址 就是我们抓到的那个数据包的URL
    url = 'http://172.13.1.32/xsxklist!getSksj.action?kcrwdms=' + str(data)
    cookie = 'JSESSIONID=BE1E36E19F7F932552C9320695C910B3'
    header = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'Referer': 'http://172.13.1.32/xsxklist!xsmhxsxk.action',
        'cookie': cookie
    }


    while True:
        # 设定5s服务器未应答就放弃这次，鬼知道是服务器炸了还是。。。。
        mes = requests.get(url, headers=header, timeout=5)
        # 打印返回的结果，就是弹出来的那个小窗口的内容
        print(str(1) + str(mes.status_code) + ':' + str(mes.text))


def qian3():
    data = 1159211


    url = 'http://172.13.1.32/xsxklist!getSksj.action?kcrwdms=' + str(data)
    cookie = 'JSESSIONID=1574E7968E06ED6ED01E5505305C669C'
    header = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'Referer': 'http://172.13.1.32/xsxklist!xsmhxsxk.action',
        'cookie': cookie
    }

    # 一直抢！
    
        # 设定5s服务器未应答就放弃这次，鬼知道是服务器炸了还是。。。。
    mes = requests.get(url, headers=header, timeout=5)
        # 打印返回的结果，就是弹出来的那个小窗口的内容
    print(str(1) + str(mes.status_code) + ':' + str(mes.text))

def qian4():
    data = 1159211
    # data 是找到的课程ID，因为python没学好，代码写的有点乱
    # 下面是地址 就是我们抓到的那个数据包的URL
    url = 'http://172.13.1.32/xsxklist!getSksj.action?kcrwdms=' + str(data)
    cookie = 'JSESSIONID=BE1E36E19F7F932552C9320695C910B3'
    header = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'Referer': 'http://172.13.1.32/xsxklist!xsmhxsxk.action',
        'cookie': cookie
    }

    # 一直抢！
    while True:
        # 设定5s服务器未应答就放弃这次，鬼知道是服务器炸了还是。。。。
        mes = requests.get(url, headers=header, timeout=5)
        # 打印返回的结果，就是弹出来的那个小窗口的内容
        print(str(1) + str(mes.status_code) + ':' + str(mes.text))

if __name__ == '__main__':
    qian3()