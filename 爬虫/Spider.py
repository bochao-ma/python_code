# -*- coding- UTF-8 -*-
from urllib import request
import re


def find_charset(html):
    """
    :param html: string,网页内容
    :return: 返回网页的charset
    """
    charset = None
    m = re.compile(r'<meta .*(http-equiv="?Content-Type"?.*)?charset="?([a-zA-Z0-9_-]+)"?', re.I).search(html)
    if m and m.lastindex == 2:
        charset = m.group(2).lower()
    return charset


def load_page(url):
    """
    :param url: 爬取页面的网址
    :return: 网页的全部内容
    """
    # 写入User Agent信息
    header = {}
    header[
        'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
    # 创建request对象
    req = request.Request(url, headers=header)
    # 读取网页内容
    html = request.urlopen(req).read()
    # 获取网页的编码格式（charset）
    coding_type = find_charset(str(html))
    content = html.decode(coding_type)
    return content
