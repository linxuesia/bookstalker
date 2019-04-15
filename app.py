import requests as rq
import re
import lxml.html
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool
import time


def get_html(url):
    """
    通过链接地址获取页面的 html 源码
    :param url: 页面链接
    :return: 页面 html 源码 string 格式
    """
    response = rq.get(url)
    response.encoding = response.apparent_encoding
    html_str = response.text
    return html_str


def get_urls(base_url, page_url):
    """
    获取每个章节的 url 地址
    :param base_url: 网站根路径
    :param page_url: 页面链接
    :return: 返回每个章节的链接组成的列表
    """
    startt = time.time()
    html = get_html(page_url)
    url_lst = []

    # 第一种方式 使用bs
    # bss = time.time()
    # soup = BeautifulSoup(html, 'html.parser')
    # content_body = soup.find(class_='content')
    # titles = content_body.find_all('a')
    # for title in titles:
    #     url_lst.append(base_url+title['href'])
    # bse = time.time()
    # print(f'使用bs方法获取总共耗时{bse - bss}')

    # 第二种方式 使用Xpath 效率大概快了0.005秒
    xps = time.time()
    selector = lxml.html.fromstring(html)
    urls = selector.xpath('//td[@class="content"]/table/tr/td/a/@href')
    for title in urls:
        url_lst.append(base_url+title)
    xpe = time.time()
    print(f'使用xpath方法获取总共耗时{xpe - xps}')

    endt = time.time()
    print(f'获取页面所有的链接总共耗时{endt - startt}')
    return url_lst


def get_content(url):
    """
    通过链接获取每个章节的文本内容
    :param url: 页面的链接
    :return: 章节的文本 string 格式
    """
    # startt = time.time()
    html = get_html(url)

    content = re.search('class=content colSpan=3>(.*?)</td>', html, re.S).group(1)
    content = content.replace('<BR>', '\n').strip()
    # endt = time.time()
    # print(f'获取一个章节的内容耗时{endt - startt}')
    return content


if __name__ == '__main__':
    chapter_lst = get_urls('http://www.dushu369.com', 'http://www.dushu369.com/gudianmingzhu/lzzy/')
    with open('聊斋.txt', 'w', encoding='utf-8') as f:
        start = time.time()
        pool = Pool(10)
        chapters = pool.map(get_content, chapter_lst)
        end = time.time()
        print(f'爬取总耗时{end - start}， 总共章节数{len(chapter_lst)}')
        for item in chapters:
            f.write(item)
    exit()
