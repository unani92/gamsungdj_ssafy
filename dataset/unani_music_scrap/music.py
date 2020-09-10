from bs4 import BeautifulSoup
import requests
import re
import json

header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Trident/7.0;rv:11.0) like Gecko"}
html = requests.get("https://www.melon.com/chart/index.htm", headers=header).text
bs = BeautifulSoup(html, "html.parser")
top100 = bs.select('tr')[1:]

song_lst = []

for idx, song in enumerate(top100):
    song_dict = dict()
    song_no = song.attrs['data-song-no']
    song_res = requests.get(f'https://www.melon.com/song/detail.htm?songId={int(song_no)}', headers=header).text
    bs = BeautifulSoup(song_res, 'html.parser')

    name_artist = bs.select('.info div')
    song_dict['song_id'] = int(song_no)
    song_dict['song_name'] = re.sub(r"\s+", " ", name_artist[0].text.rstrip())[4:]
    song_dict['artist_id'] = int(name_artist[1].select('a')[0].attrs['href'][38:-3])
    song_dict['artist_name'] = name_artist[1].select('a span')[0].text

    album_release_genre = bs.select('.list dd')
    song_dict['album_id'] = int(album_release_genre[0].select('a')[0].attrs['href'][37:-3])
    song_dict['album_name'] = album_release_genre[0].text
    song_dict['release_date'] = album_release_genre[1].text
    song_dict['song_genre'] = album_release_genre[2].text

    lyric = re.sub(r"\s+", " ", bs.select('.lyric')[0].text)
    song_dict['lyric'] = lyric

    like_res = requests.get(
        f'https://www.melon.com/commonlike/getSongLike.json?contsIds={int(song_no)}',
        headers = header
    ).json()
    like = like_res['contsLike'][0]["SUMMCNT"]
    song_dict['song_like'] = like

    song_lst.append(song_dict)
    if not idx % 10:
        print(f'{idx} % proceed')

file = open("moviedata.json", "w+")
file.write(json.dumps(song_lst))