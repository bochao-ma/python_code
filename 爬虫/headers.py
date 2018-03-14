# -*- coding: utf-8 -*-
def headers(ty):
    """
    :param ty: string,类型（Android,Firefox,Chrome,IOS）
    :return: 返回头消息
    """
    headers = {}
    t = str(ty).lower()
    if (t == 'android'):
        headers[
            'User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19'
    elif (t == 'firefox'):
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0'
    elif (t == 'chrome'):
        headers[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
    elif (t == 'ios'):
        headers[
            'User-Agent'] = 'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
    else:
        print('输入错误，请检查输入类型（Android,Firefox,Chrome,IOS')
    return headers