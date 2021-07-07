import requests
import json
import time
from lxml import etree

cookie = input('请输入cookie：')
head = {
    'cookie': cookie,
    'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/90.0.4430.93Safari/537.36'
}


# 获取评论信息(小冰机器人)
def pl(title):
    url = 'https://ux-plus-bing.xiaoice.com/s_api/game/getresponse?workflow=AIBeingsBingBFChat'
    headers = {
        'Host': 'ux-plus-bing.xiaoice.com',
        'Connection': 'keep-alive',
        'Content-Length': '118',
        'sec-ch-ua': '"NotA;Brand";v="99","Chromium";v="90","GoogleChrome";v="90"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/90.0.4430.93Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': '*/*',
        'Origin': 'https://ux-plus-bing.xiaoice.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ux-plus-bing.xiaoice.com/BingVirtualBF?authcode=86982F42D8E17BD3B6305BA785B12871',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'pname=bingaibeings;uxplusaffinity=1620711950.636.2592.823106;subpid=virtualbf;afuidcode=p0RmgubOOQr8EEh4NGgfV3hgpt_adf5wn5SrQklsH1Q7I6PfGze795nUKQQKSodgDAwSlK2uA8pGraIaMngeLWU;cpid=061b9211b53da5682799fb25cdca933f;salt=4D72C7D82759E28FC6D65A89CA308B85;logInfo=%7B%22pageName%22%3A%22builtinvirtualchat%22%2C%22tid%22%3A%22f1c853057c44668be27e4d3f5c89dd8f%22%7D;.AspNetCore.Session=CfDJ8IIWMkvtK0NDrI%2FS5O3WxfijFh4cWgUcUQR%2F2KJYNXl%2BK9JSZKg0FtFKFTMp6%2BQxbi%2FQybOcIWm1TUuoKTKWuM1oBLTtw2laoDjiV98%2BBAd0T8xIvjQg%2BclzWIf%2Fgsl0JgUTH3MmBMQB27OWmOOrgfONInYzGevKUTeMGXkDmOPg;apieid=49dd6b628c4d43e1b54bdf9e93bdcab0'
    }
    data = json.dumps({"TraceId": "55cb3f3ae06b22bdbf38359d257a0b38",
                       "Content": {"Text": title, "Metadata": {}}})
    for i in range(2):
        rep = requests.post(url=url, headers=headers, data=data).json()
        con = rep[0]['Content']['Text']
        print(con)
        if len(con) >= 4:
            return con
    return pl2()


# 获取评论信息（诗词歌赋网）
def pl2():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'
    }
    url = 'https://v2.jinrishici.com/one.json'
    param = {
        'client': 'browser-sdk/1.2',
        'X-User-Token': 'fxdY7KCt5G+IXQIBWXx7Xr2GxAugPX2j'
    }
    response = requests.get(url=url, headers=headers, params=param).json()
    # 读取json并赋值
    js_rep = json.dumps(response)
    # 获取status
    state = json.loads(js_rep)['status']
    # 获取content
    content = json.loads(js_rep)['data']['content']
    if state == 'success':
        return content
    else:
        return False


# 获取更新的帖子
def gx():
    li = ('Hmily', 'Okxxx', '烟99', 'blackwhite001', 'LCG', '皈依我佛', 'Godfather.Cr', '稀鸿绝鳞')
    href_li = []
    headers = {
        'Cookie': head['cookie'],
        'User-Agent': head['User-Agent']
    }
    url = 'https://www.52pojie.cn/forum-10-1.html'
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    # 获取所有tbody 并且封装成list
    tbody_li = tree.xpath('//*[@id="threadlisttableid"]/tbody')
    # 遍历tbody，取出所有tbody的name和href
    for tbody in tbody_li:
        name = tbody.xpath('./tr/td[@class="by"][1]/cite/a/text()')
        href = tbody.xpath('./tr/td[@class="icn"]/a/@href')
        title = tbody.xpath('./tr/th/a[2]/text()')
        # 如果不是空列表，那么执行下一步
        if name:
            # 如果不存在于li（排除列表）中，那么执行
            if name[0] not in li:
                href_li.append(href[0] + '|' + title[0])
    # 判断取出帖子列表是否为空，不是则返回所有的帖子
    if href_li:
        return href_li
    else:
        return False


# 回复
def hf(href):
    url = 'https://www.52pojie.cn/forum.php'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '448',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': head['cookie'],
        'User-Agent': head['User-Agent'],
        'sec-ch-ua': '"NotA;Brand";v="99","Chromium";v="90","GoogleChrome";v="90"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'iframe',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1'
    }
    for h in href:
        hh = h.split('|')
        content = pl(hh[1])
        param = {
            'mod': 'post',
            'infloat': 'yes',
            'action': 'reply',
            'fid': '10',
            'extra': 'page=1',
            'tid': h[7:14],
            'replysubmit': 'yes',
            'inajax': '1'
        }
        data = {
            'formhash': '67900684',
            'handlekey': 'reply',
            'noticeauthor': '1fefRIR5k10L/baQfn6n+H+KkcdMyocIOS8Szp/Jdw/IDVFWLQ',
            'noticetrimstr': '',
            'noticeauthormsg': '(unabletodecodevalue)',
            'usesig': '1',
            'reppid': '38432997',
            'reppost': '38432997',
            'subject': '',
            'message': content.encode('GBK')
        }
        response = requests.post(url=url, data=data, headers=headers, params=param).text
        if '非常感谢，回复发布成功' in response:
            now = str(time.strftime("%H:%M  ", time.localtime()))
            print(now + 'Q：' + hh[1] + '  A：' + content + '  url：' + hh[0])
        else:
            print(response)
        time.sleep(361)


def qd():
    while True:
        href = gx()
        if not href:
            print('程序错误')
            break
        hf(href)


qd()
