import json
import datetime


date=datetime.datetime.today().strftime('%Y%m%d%H%M%S')#당일 날짜 시간 추출
year_month_day,times=date[:8],date[8:]
test_result_image_path=f"/mnt/sdb/AI/work/test_result_image/{year_month_day}/"#결과 이미지 파일 저장 위치

dict_nodule_maker_ids = dict()
for i in range(10):#제품군별
    dict_nodule_maker_ids[i]=dict()
    for j in range(10):##결절별
        dict_nodule_maker_ids[i][j]=[[0,0],[0,0],[0,0]]

with open(f"{test_result_image_path}/result.json","w") as file:
    json.dump(dict_nodule_maker_ids,file)
    