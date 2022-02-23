import json
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import os
import csv

# VWorld API의 Key
VWorld_APIkey = '59DEDA2D-924F-3AE5-B21B-17C05FC4E6E2'

# result는 EPSG:4326(경위도 좌표계)로 출력됨
def Geocorder(address, type='ROAD'):
    url = "http://api.vworld.kr/req/address?service=address&request=getCoord&type=" + str(type) + "&refine=false&key=%s&" % (VWorld_APIkey) + urlencode({quote_plus('address'):address}, encoding='UTF-8')

    request = Request(url)
    response = urlopen(request)
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read().decode('utf-8')

    else:
        print('error code:', rescode)

    jsonData = json.loads(response_body)

    lng = float(jsonData['response']['result']['point']['x'])
    lat = float(jsonData['response']['result']['point']['y'])

    return [lng, lat]

# 도로명주소 - 지번주소 순으로 검색 후, 좌표변환이 되지 않을 경우 경위도 값을 공백으로 출력
def GetCRS(address):
    try:
        result = Geocorder(address)
        print('{} => lng:{}, lat:{}'.format(address, result[0], result[1]))

    except:
        try:
            result = Geocorder(address, 'PARCEL')
            print('{} => lng:{}, lat:{}'.format(address, result[0], result[1]))

        except:
            result = ['', '']

    return result

# 1. 관광지POI DB에 대한 Geo_Cording
os.chdir('D:/2021/1. Works/7. 한국관광공사/관광공사_DB구축/2. 관광공사_동선DB/2-1. 관광지POI_DB/좌표변환대상')
Attraction_List = os.listdir()

for filename in Attraction_List:
    open_data = open(filename, 'r')
    data = csv.reader(open_data)

    write_data = open('[좌표추가]' + filename, 'w', newline='')
    csv_writer = csv.writer(write_data)

    for idx, line in enumerate(data):
        if idx > 0:
           Coord = GetCRS(line[3])
           csv_writer.writerow(line + Coord)

        else:
            csv_writer.writerow(line + ['경도', '위도'])

    write_data.close()
    open_data.close()

# 2. 대중교통POI DB에 대한 Geo_Cording
'''os.chdir('D:/2021/1. Works/7. 한국관광공사/관광공사_DB구축/대중교통POI_DB/')

open_data = open('대중교통POI_DB.csv', 'r')
data = csv.reader(open_data)

write_data = open('[좌표추가]대중교통POI_DB.csv', 'w', newline='')
csv_writer = csv.writer(write_data)

for idx, line in enumerate(data):
    if idx > 0:
        Coord = GetCRS(line[4])
        csv_writer.writerow(line + Coord)

    else:
        csv_writer.writerow(line + ['경도', '위도'])

write_data.close()
open_data.close()'''
