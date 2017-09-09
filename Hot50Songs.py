#输入歌手名，返回该歌手热门50单曲及单曲id

import requests
import bs4
import json


def get_html(url):
    headers = {
        'Referer': 'http://music.163.com/',
        'Host': 'music.163.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
        'Accept': 'text/html,application/xhml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return 'get_html error'


def get_content(url):
    try:
        songs = []
        html = get_html(url)
        soup = bs4.BeautifulSoup(html, 'lxml')
        allSongs = soup.find('ul', class_='f-hide')
        for song in allSongs.find_all('a'):
            details = {}
            details['name'] = song.text
            details['link'] = song['href']
            songs.append(details)
        return songs
    except:
        return 'get content error'


def get_artist_id(artist_name):
    try:
        headers = {
            'Referer': 'http://music.163.com/',
            'Host': 'music.163.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
            'Accept': 'text/html,application/xhml+xml,application/xml;q=0.9,*/*;q=0.8'
        }
        url = 'http://music.163.com/api/search/pc?s={}&offset=0&limit=100&type=100'.format(artist_name)
        r = requests.post(url, headers=headers)
        r.raise_for_status()
        r.encoding = 'utf-8'
        html = r.text

        jsons = json.loads(html)
        id = jsons['result']['artists'][0]['id']

        return id
    except:
        return 'get id error'


def print_content(url):
    songs = get_content(url)
    for song in songs:
        print('{} : {}'.format(song['name'], song['link']))




if __name__ == '__main__':
    artist_name = input('请输入歌手名: ')

    url = 'http://music.163.com/artist?id={}'.format(get_artist_id(artist_name))
    print_content(url)
    print('搜索完成！')
