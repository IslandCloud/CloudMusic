from urllib import request
import os
import Hot50Songs
import re
import time


songID = '444323371'
mp3url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(songID)
path = r'C:\Users\dl201\desktop\music'
file_name = '木头的心.mp3'
dest_dir = os.path.join(path, file_name)


def downloadAllSongs(songIDlist):
    path = r'C:\Users\dl201\desktop\music'
    for song in songIDlist:
        url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(song['id'])
        name = song['name']
        file_name = '{}.mp3'.format(name)
        dest_dir = os.path.join(path, file_name)
        try:
            download_music(dest_dir, url)
            print('{} 下载完毕！'.format(name))
        except:
            print('{} 下载失败！'.format(name))
    print('全部歌曲下载完毕！')


def download_music(path, url):
    with request.urlopen(url) as web:
        with open(path, 'wb') as outfile:
            outfile.write(web.read())


def get_songID(link):
    pattern = r'id=([0-9]+)'
    id = re.search(pattern, link)
    return id.group(1)


def get_songIDlist(songs):
    songIDlist = []
    for song in songs:
        detail = {}
        name = song['name']
        link = song['link']
        id = get_songID(link)
        detail['name'] = name
        detail['id'] = id
        songIDlist.append(detail)
    return songIDlist

if __name__ == '__main__':
    #artist_name = input('请输入歌手名: ')

    t1 = time.time()

    url = 'http://music.163.com/artist?id={}'.format(Hot50Songs.get_artist_id('小缘'))
    songs = Hot50Songs.get_content(url)

    idlist = get_songIDlist(songs)
    downloadAllSongs(idlist)

    t2 = time.time()

    print(t2 - t1)