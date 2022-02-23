from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

from bs4 import BeautifulSoup
import re



import csv
import time

delay = 1
fp = "C:\\Users\\Planning\\Desktop\\RouteSearch\\Selenium\\"

driver = webdriver.Chrome(fp + "chromedriver.exe")
driver.get("https://map.kakao.com/")

k = csv.reader(open(fp + "[최종]대중교통POI_DB.csv", 'r'))
kk = csv.reader(open(fp + "[최종]관광지POI_강릉시.csv", 'r'))

for idx, i in enumerate(k):
    if idx == 0:
        continue

    # 출발지
    KEYS = i[6] + "," + i[5] + "\n"

    for idx_2, j in enumerate(kk):
        if idx_2 == 0:
            continue

        # 도착지
        KEYS_2 = j[5] + "," + j[4] + "\n"
        WebDriverWait(driver, delay).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="local"]')))

        # 출발지 입력
        driver.refresh()
        driver.find_element_by_xpath('//*[@id="search.keyword.query"]').send_keys("\b"*30)
        driver.find_element_by_xpath('//*[@id="search.keyword.query"]').send_keys(KEYS)
        time.sleep(1.5)
        driver.find_element_by_xpath(
            '//*[@id="view.mapContainer"]/div[2]/div/div[6]/div[2]/div/div[2]/div[3]/div/div[2]/button').click()
        WebDriverWait(driver, delay).until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="view.mapContainer"]/div[2]/div/div[6]/div[2]/div/div[2]/div[3]/div/div[2]/div/button[1]')))
        driver.find_element_by_xpath('//*[@id="view.mapContainer"]/div[2]/div/div[6]/div[2]/div/div[2]/div[3]/div/div[2]/div/button[1]').click()
        driver.find_element_by_xpath('/html/body').click()
        time.sleep(0.5)

        # 도착지 입력
        driver.find_element_by_xpath('//*[@id="search.keyword.query"]').send_keys("\b"*30)
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="search.keyword.query"]').send_keys(KEYS_2)
        time.sleep(0.5)

        driver.find_element_by_xpath(
            '//*[@id="view.mapContainer"]/div[2]/div/div[6]/div[3]/div/div[2]/div[3]/div/div[2]/button').click()
        WebDriverWait(driver, delay).until(EC.visibility_of_element_located((
            By.XPATH, '//*[@id="view.mapContainer"]/div[2]/div/div[6]/div[3]/div/div[2]/div[3]/div/div[2]/div/button[3]')))
        driver.find_element_by_xpath(
            '//*[@id="view.mapContainer"]/div[2]/div/div[6]/div[3]/div/div[2]/div[3]/div/div[2]/div/button[3]').click()
        driver.find_element_by_xpath('/html/body').click()
        time.sleep(0.5)