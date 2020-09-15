from bs4 import BeautifulSoup
import requests
from scrap import scrap
from pprint import pprint

import json

header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Trident/7.0;rv:11.0) like Gecko"}

# 발라드
ballad_html = requests.get("https://www.melon.com/genre/song_list.htm?gnrCode=GN0100&steadyYn=Y", headers=header).text
ballad_bs = BeautifulSoup(ballad_html, "html.parser")
ballad50 = ballad_bs.select('tr')[1:]

# 댄스
dance_html = requests.get('https://www.melon.com/genre/song_list.htm?gnrCode=GN0200&steadyYn=Y', headers=header).text
dance_bs = BeautifulSoup(dance_html, "html.parser")
dance50 = dance_bs.select('tr')[1:]

# 랩/힙합
rap_html = requests.get('https://www.melon.com/genre/song_list.htm?gnrCode=GN0300&steadyYn=Y', headers=header).text
rap_bs = BeautifulSoup(rap_html, "html.parser")
rap50 = rap_bs.select('tr')[1:]

# rnb
rnb_html = requests.get('https://www.melon.com/genre/song_list.htm?gnrCode=GN0400&steadyYn=Y', headers=header).text
rnb_bs = BeautifulSoup(rnb_html, "html.parser")
rnb50 = rnb_bs.select('tr')[1:]

# indie
indie_html = requests.get('https://www.melon.com/genre/song_list.htm?gnrCode=GN0500&steadyYn=Y', headers=header).text
indie_bs = BeautifulSoup(indie_html, "html.parser")
indie50 = indie_bs.select('tr')[1:]

# rock
rock_html = requests.get('https://www.melon.com/genre/song_list.htm?gnrCode=GN0600&steadyYn=Y', headers=header).text
rock_bs = BeautifulSoup(rock_html, "html.parser")
rock50 = rock_bs.select('tr')[1:]

# trot
trot_html = requests.get('https://www.melon.com/genre/song_list.htm?gnrCode=GN0700&steadyYn=Y', headers=header).text
trot_bs = BeautifulSoup(trot_html, "html.parser")
trot50 = trot_bs.select('tr')[1:]

# folk
folk_html = requests.get('https://www.melon.com/genre/song_list.htm?gnrCode=GN0800&steadyYn=Y', headers=header).text
folk_bs = BeautifulSoup(folk_html, "html.parser")
folk50 = folk_bs.select('tr')[1:]

steady_seller_all = scrap(ballad50) + scrap(dance50) + scrap(rap50) + scrap(rnb50) \
                    + scrap(indie50) + scrap(rock50) + scrap(trot50) + scrap(folk50)


file = open("moviedata.json", "w+")
file.write(json.dumps(steady_seller_all))

print('finish')



