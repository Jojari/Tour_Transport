import ast
import csv
import os

os.chdir('D:/2021/1. Works/7. 한국관광공사/관광공사_DB구축/2. 관광공사_동선DB/2-8. 관광지_to_관광지_동선_Output/')
Output_List = os.listdir()

BusInfo_Dict = {}
MetroInfo_Dict = {}

for filenum, file in enumerate(Output_List):
    District_Name = file.split('_')[0][7:]

    if District_Name not in BusInfo_Dict:
        BusInfo_Dict[District_Name] = {}

    '''if District_Name not in MetroInfo_Dict:
        MetroInfo_Dict[District_Name] = {}
        print(MetroInfo_Dict)'''

    Data = csv.reader(open(file, 'r'))

    for idx, line in enumerate(Data):
        if idx > 0:
            Stage_String = line[-1].split('%')
            Stage_List = []

            for level, Stage in enumerate(Stage_String):
                try:
                    Stage = ast.literal_eval(Stage)
                    Stage_List.append(Stage)

                except SyntaxError:
                    Stage_List.append(Stage)

            for level, Stage_Detail in enumerate(Stage_List):
                try:
                    if Stage_Detail[0] == '버스':
                        Bus_Stage = Stage_Detail

                        Bus_NumList = Bus_Stage[1]

                        Bus_Interval = Bus_Stage[3]
                        Bus_First = Bus_Stage[4]
                        Bus_Last = Bus_Stage[5]
                        Bus_Grade = Bus_Stage[6]

                        for count in range(len(Bus_NumList)):
                            # print(Bus_NumList[count])
                            if Bus_NumList[count] not in BusInfo_Dict[District_Name]:
                                BusInfo_Dict[District_Name][Bus_NumList[count]] = [Bus_Interval[count], Bus_First[count], Bus_Last[count], Bus_Grade[count]]
                            else:
                                pass

                    if Stage_Detail[0] == '지하철/철도':
                        Metro_Stage = Stage_Detail

                        Metro_Line = Metro_Stage[1]

                        if Metro_Line not in MetroInfo_Dict[District_Name]:
                            MetroInfo_Dict[District_Name][Metro_Line] = ['', '', '', '']
                        else:
                            pass

                    else:
                        pass
                except:
                    print('STAGEDETAIL')
                    print(Stage_Detail)
                    print('-----------------')
                    print('STAGELIST')
                    print(Stage_List)
                    print('-----------------')
                    print('LINE')
                    print(line)
                    pass
        else:
            pass

# print(BusInfo_Dict)
print(MetroInfo_Dict)

os.chdir('D:/2021/1. Works/7. 한국관광공사/관광공사_DB구축/2. 관광공사_동선DB/2-8. 관광지_to_관광지_동선_Output/')
csv_writer = csv.writer(open('한국관광공사_목포시_BusInfo_DB.csv', 'w', newline=''))

csv_writer.writerow(['도시명', '노선번호', '배차간격(회/분)', '첫차시간', '막차시간', '등급'])
# csv_writer.writerow(['도시명', '노선', '기준역', '배차횟수', '첫차시간', '막차시간'])


District_List = list(BusInfo_Dict.keys())

for i, District in enumerate(District_List):
    BusNum_List = list(BusInfo_Dict[District].keys())

    for j, BusNum in enumerate(BusNum_List):
        csv_writer.writerow([District, "'" + str(BusNum) + "'", "'" + str(BusInfo_Dict[District][BusNum][0]) + "'",
                             "'" + str(BusInfo_Dict[District][BusNum][1]) + "'",
                             "'" + str(BusInfo_Dict[District][BusNum][2]) + "'",
                             "'" + str(BusInfo_Dict[District][BusNum][3]) + "'"])

'''District_List = list(MetroInfo_Dict.keys())

for i, District in enumerate(District_List):
    MetroLine_List = list(MetroInfo_Dict[District].keys())
    print(MetroLine_List)
    print(District)

    for j, MetroLine in enumerate(MetroLine_List):
        csv_writer.writerow([District, "'" + str(MetroLine) + "'", "'" + str(MetroInfo_Dict[District][MetroLine][0]) + "'",
                             "'" + str(MetroInfo_Dict[District][MetroLine][1]) + "'",
                             "'" + str(MetroInfo_Dict[District][MetroLine][2]) + "'",
                             "'" + str(MetroInfo_Dict[District][MetroLine][3]) + "'"])'''




