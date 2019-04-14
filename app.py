import requests as rq
import re
import lxml
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool
import time

def get_urls(base_url, page_url):
    response = rq.get(page_url)
    response.encoding = response.apparent_encoding
    html_str = response.text

    """
    第一种方式 使用bs
    """
    soup = BeautifulSoup(html_str, 'html.parser')
    content_body = soup.find(class_='content')
    titles = content_body.find_all('a')

    """
    第二种方式 使用Xpath
    """

    url_lst = []
    for title in titles:
        url_lst.append(base_url+title['href'])
    return url_lst


def get_content(url):
    response = rq.get(url)
    response.encoding = response.apparent_encoding
    html_str = response.text
    content = re.search('class=content colSpan=3>(.*?)</td>', html_str, re.S).group(1)
    content = content.replace('<BR>', '\n').strip()
    return content


if __name__ == '__main__':
    chapter_lst = get_urls('http://www.dushu369.com', 'http://www.dushu369.com/gudianmingzhu/lzzy/')
    with open('聊斋.txt', 'w', encoding='utf-8') as f:
        start = time.time()
        pool = Pool(10)
        chapters = pool.map(get_content, chapter_lst)
        end = time.time()
        print(f'爬取总耗时{end - start}')
        for item in chapters:
            f.write(item)
    exit()