import csv
from bs4 import BeautifulSoup
import requests
import json

filepath = "C:\\Users\\Planning\\Desktop\\"
output_file_name = filepath + "노선별_경유정류장정보"
input_file_name = filepath + "대전_전체_노선별_노선정보"
k = csv.reader(open(input_file_name + ".csv", 'r'))
kk = csv.writer(open(output_file_name + ".csv", "w", newline="", encoding='utf-8'))
kk.writerow(["route_cd", "bus_stop_nm", "bus_node_id", "bus_stop_id", "x", "y"])

key = 'NcR9oUVZpWVq16HR%2F9Jih5C6wNEjp1ilDnz3ekuzrJFmKDpe0AmsEXrUp2s%2BbxyfEIoz%2FeGaKx9SWKp7fUtq%2FQ%3D%3D'
service_key = '&serviceKey='+key

for idk, j in enumerate(k):
    Line_ID = j[0]
    route_cd = 'busRouteId=' + Line_ID
    url = 'http://openapitraffic.daejeon.go.kr/api/rest/busRouteInfo/getStaionByRoute?' + route_cd + service_key
    req = requests.get(url)
    req.encoding = "UTF-8"

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    ROUTE_CD = soup.find_all('route_cd')
    BUS_STOP_NM = soup.find_all('busstop_nm')
    BUS_NODE_ID = soup.find_all('bus_node_id')
    BUS_ARS_ID = soup.find_all('bus_stop_id')
    y = soup.find_all('gps_lati')
    x = soup.find_all('gps_long')

    fin_data = {}   # 딕셔너리 만들기
    for idx, jj in enumerate(ROUTE_CD):
        fin_data[BUS_ARS_ID[idx].get_text()] = {"route_cd": ROUTE_CD[idx].get_text(),       # 필요한 정보 담기
                                              "busstop_nm": BUS_STOP_NM[idx].get_text(),
                                              "bus_node_id": BUS_NODE_ID[idx].get_text(),
                                              "bus_stop_id": BUS_ARS_ID[idx].get_text(),
                                              "gps_long": x[idx].get_text(),
                                              "gps_lati": y[idx].get_text()}

    #for key in fin_data:  # 잘담겼는지 확인
        #print(key, fin_data[key])
        #BUS_STOP_NM.replace("\xa0", "")

    for i in fin_data.items():
        A = i[1]["route_cd"]
        a = i[1]["busstop_nm"]
        b = i[1]["bus_node_id"]
        c = i[1]["bus_stop_id"]
        d = i[1]["gps_long"]
        e = i[1]["gps_lati"]
        fin = (A, a,  b, c, d, e)
        # print(len(fl),fl)
        # print(len(fin), fin)
        print(fin)
        kk.writerow(fin)