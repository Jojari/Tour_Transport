from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import csv
import time

#######################################################################################
### 상이한 관광지DB의 중복 관광지 데이터를 제거하기 위한, 관광지 주소 검색 및 도로명주소 변환 코드 ###
#######################################################################################

def Find_Address(PlaceName):
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.ID, 'search.keyword.query')))
    Place_Search = driver.find_element_by_id('search.keyword.query')
    Place_Search.clear()

    Place_Search.send_keys(PlaceName)
    time.sleep(0.5)
    Place_Search.send_keys(Keys.ENTER)
    time.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    try:
        Address_Result = soup.find("p", {"data-id": 'address'})
        Address = Address_Result.get_text()

        SearchName_Result = soup.find("a", {"class": 'link_name'})
        SearchName = SearchName_Result.get_text()

    except:
        SearchName = '검색명없음'
        Address = '주소없음'


    print(PlaceName + str(':') + Address)

    return [SearchName, Address]

'''Region_List = ['인천광역시', '대전광역시', '부산광역시', '울산광역시', '대구광역시', '광주광역시', '세종특별자치시', '제주특별자치도',
               '수원시', '춘천시', '청주시', '태안군', '경주시', '창원시', '전주시', '여수시', '강릉시', '목포시', '천안시']'''

Region_List = ['천안시']

for Region in Region_List:
    write_data = open('D:/2021/1. Works/7. 한국관광공사/관광공사_DB구축/2. 관광공사_동선DB/2-1. 관광지POI_DB/' + Region + '.csv', 'w', newline="")
    csv_writer = csv.writer(write_data)

    csv_writer.writerow(['도시명', '관광지검색명', '관광지명', '상세주소'])

    driver = selenium.webdriver.Chrome('D:/chromedriver.exe')
    driver.maximize_window()

    URL = 'https://map.kakao.com/'
    driver.get(url=URL)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    os.chdir('D:/2021/1. Works/7. 한국관광공사/관광공사_DB구축/1. 관광지_기초DB/1-1. 관광공사_데이터랩_도시별데이터/관광공사_데이터랩_' + Region)
    Region_DataList = os.listdir()

    for Region_Data in Region_DataList:
        open_KTO_data = open(Region_Data, 'r')
        Data = csv.reader(open_KTO_data)

        for idx, line in enumerate(Data):
            if idx > 0:
                if line[4] not in ['버스터미널', '기차역', '공항']:
                    Input = Region + ' ' + line[1]

                    Address_Result = Find_Address(Input)

                    if Address_Result[1] == '':
                        Address_Result[1] = '주소없음'

                    if Address_Result[1] == '주소없음' or Address_Result[1][-1] in ['읍', '면', '리', '동']:
                        Address_Result[1] = line[2]

                    csv_writer.writerow([Region, Address_Result[0], line[1], Address_Result[1]])

        open_KTO_data.close()

    open_MCST_data = open('D:/2021/1. Works/7. 한국관광공사/관광공사_DB구축/1. 관광지_기초DB/1-2. 2019 주요관광지점 입장객통계/문체부_관광지식정보시스템_관광지목록.csv', 'r')
    Data = csv.reader(open_MCST_data)

    for idx, line in enumerate(Data):
        if idx > 0:
            if Region in ['인천광역시', '대전광역시', '부산광역시', '울산광역시', '대구광역시', '광주광역시', '세종특별자치시', '제주특별자치도']:
                if Region in line[0]:
                    Input = Region + ' ' + line[2]

                    Find_Address(Input)

                    Address_Result = Find_Address(Input)

                    if Address_Result[1] == '':
                        Address_Result[1] = '주소없음'

                    csv_writer.writerow([Region, Address_Result[0], line[2], Address_Result[1]])

            elif Region in ['수원시', '춘천시', '청주시', '태안군', '경주시', '창원시', '전주시', '여수시', '강릉시', '목포시', '천안시']:
                if Region in line[1]:
                    Input = Region + ' ' + line[2]

                    Find_Address(Input)

                    Address_Result = Find_Address(Input)

                    if Address_Result[1] == '':
                        Address_Result[1] = '주소없음'

                    csv_writer.writerow([Region, Address_Result[0], line[2], Address_Result[1]])

            else:
                pass

    open_MCST_data.close()

    driver.close()
    write_data.close()