import requests
import socket
import tkinter
import re
import asyncio
import threading
from os import path, mkdir, chdir
from getpass import getuser


def test():
    try:
        requests.get('https://baidu.com', proxies=proxies,timeout=3)
    except:
        print('无网络请检查插口或无线调制器')
        post_cy()



# 获取本机地址
proxies = {'http': None, 'https': None}
def get_host_ip():

    html = requests.get('http://1.1.1.1',proxies=proxies,verify=False)
    try:
        ips = re.findall(r'\d+.\d+.\d+.\d+',html.url)
        ip = ips[1]
    except:
        ip=''
        pass
    return ip




def init_timer_loop():
    new_loop = asyncio.new_event_loop()
    t = threading.Thread(target=start_loop, args=(new_loop,))  # 开启一个线程，在线程中开启一个loop
    t.start()
    asyncio.run_coroutine_threadsafe(net_ready(), new_loop)  # 在线程的loop中加入协程

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def net_ready():
    my_ts = 'C:\\Users\\' + getuser() + '\\Documents\\school\\my_user.txt'
    global el1,el2,statu1
    statu1=0
    try:
        with open(my_ts) as fp:
            user = fp.readlines()
            fp.close()
        el1=user[0]
        el2=user[1]
    except:
        pass
    while (1):
        test()
        await asyncio.sleep(5)


# 检测初始化用户文件夹和切换工作区
def test_user(id, pas,statu):
    # 检测文件夹和文件
    my_path = 'C:\\Users\\' + getuser() + '\\Documents\\school'
    my_tcs = 'C:\\Users\\' + getuser() + '\\Documents\\school\\my_user_cy.txt'
    my_ts = 'C:\\Users\\' + getuser() + '\\Documents\\school\\my_user.txt'



    try:
        mkdir(my_path)
    except(FileExistsError):
        chdir(my_path)

    chdir(my_path)
    print("第一次初始化\n")
    a = id
    if(statu==1):
        a = 'XYGY_S' + a + '@SCITC'
    b = pas
    with open('my_user_cy.txt', 'w+') as f:
        f.write(a)
        f.write(b)
        f.seek(0,0)
        info = f.read()
        with open('my_user.txt','w') as fb:
            fb.write(info)
            fb.close()
            f.close()
    return 111




# 手动获取路由器ip/滑稽
def get_rout_ip():


    return 'http://10.10.11.14/webauth.do?wlanuserip=' + get_host_ip() +'&wlanacname=XF_BRAS'


# 获取用户账号密码
def get_user():
    with open('my_user.txt', 'r') as f:
        user = f.readlines()
    return user

def inter(e1, e2, statu):
    global  el1, el2, statu1

    el1=e1
    el2=e2
    statu1=statu
    post_cy()



def post_cy():
    headrs = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '320',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': '10.10.11.14',
        'Origin': 'http://10.10.11.14',
        'Referer': 'http://10.10.11.14/webauth.do?wlanuserip=172.25.33.99&wlanacname=XF_BRAS&vlan=0&rand=fd501de91c262',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36}'}

    url = 'http://10.10.11.14/webauth.do?wlanuserip=' + get_host_ip() + '&wlanacname=XF_BRAS'
    Date = {
        'pageid': '1',
        'userId': '',
        'passwd': ''}

    test_user(el1, el2, statu1)
    user_list = get_user()

    Date['userId'] = user_list[0]
    Date['passwd'] = user_list[1]

    requests.post(url, Date, headrs)
    test()

