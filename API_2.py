import csv
from bs4 import BeautifulSoup
import requests
import os

filepath = "C:\\Users\\Planning\\Desktop\\"
input_file_name = filepath + 'route_NO'
output_file_name = filepath + "구례군_버스노선번호목록"
k = csv.reader(open(input_file_name + ".csv", "r"))
kk = csv.writer(open(output_file_name + ".csv", "w", newline="", encoding="utf-8"))
kk.writerow(["NUM", "ROUTE_ID", "ROUTE_NO"])

key = 'ekg8wIqj7G4ny7g4dGQmDTMnqDaECx3VuQxM663Rm9A248QmvwSgL%2F%2FQvC2fAaN3jCy6MsaXS9XoL4VzfIydcg%3D%3D'
service_key = 'serviceKey=' + key
'''
n = 0
for idx, j in enumerate(k):
    if idx != 0:
        Line_ID = 'routeNo=' + j[0]
        #city = '35050' #남원
        #city = '35340' #장수
        #city = '35350' #임실
        #city = '35360' #순창
        #city = '36320' #곡성
        #city = '38380' #함양
        #city = '38360' #하동
        #city = '36330' #구례
        url = 'http://openapi.tago.go.kr/openapi/service/BusRouteInfoInqireService/getRouteNoList?' + \
              service_key + '&cityCode=36320&' + Line_ID

        req = requests.get(url)
        req.encoding = "UTF-8"
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        ROUTE_ID = soup.find_all('routeid')
        ROUTE_NO = soup.find_all('routeno')

        fin_data = {}
        for idy, jj in enumerate(ROUTE_ID):
            fin_data[ROUTE_ID[idy].get_text()] = {"routeid": ROUTE_ID[idy].get_text(), "routeno": ROUTE_NO[idy].get_text()}

        for i in fin_data.items():
            n += 1
            fin = n, i[1]["routeno"], i[1]["routeid"]
            print(fin)
            kk.writerow(fin)
'''

url = 'http://openapi.tago.go.kr/openapi/service/BusRouteInfoInqireService/getRouteNoList?' + \
      service_key + '&cityCode=36330&' + 'routeNo=구례-남원'

req = requests.get(url)
req.encoding = "UTF-8"
print(url)

html = req.text
soup = BeautifulSoup(html, 'html.parser')

ROUTE_ID = soup.find_all('routeid')
ROUTE_NO = soup.find_all('routeno')

fin_data = {}
for idy, jj in enumerate(ROUTE_ID):
    fin_data[ROUTE_ID[idy].get_text()] = {"routeid": ROUTE_ID[idy].get_text(), "routeno": ROUTE_NO[idy].get_text()}

for i in fin_data.items():
    fin = i[1]["routeno"], i[1]["routeid"]
    print(fin)
    kk.writerow(fin)