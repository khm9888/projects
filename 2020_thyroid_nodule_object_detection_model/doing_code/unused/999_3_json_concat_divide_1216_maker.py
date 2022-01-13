import json
from sklearn.model_selection import train_test_split
import pandas as pd
import pymysql
import random
import os
import datetime

def createFolder(directory):#폴더 생성 함수
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


date=datetime.datetime.today().strftime('%Y%m%d%H%M%S')#당일 날짜 시간 추출
year_month_day,times=date[:8],date[8:]

load_csv="/mnt/sdb/AI/work/save_csv/"

ip = "192.168.1.17"
port = 13307
user = "acryl"
pw = "acryl00"
db = "MARKER"
tablename = 'THANQ'
charset="utf8"

json2 = "from_db.json"
# json2 = "from_db.json"
json4 = "train.json"
json5 = "val.json"
json6 = "test.json"

path = "/home/con/mmdetection/data/thyroid/annotations/"


create_json_path = f"/home/con/mmdetection/data/thyroid/annotations/{year_month_day[-4:]}"

filter_encrypt_id = ['O4xwh1VZhlRKZnYnmOSmQBf2x5iQxn02oOVlOTWbmqiPaJDwY/J7Yr7Vaf5pjuhuRCQPFNlVyhZrI4C3AWAQdw==', 'PpSsDkvJFVoTrgU0vadoDETwtnMpVmMZhWNpj+RomI1FCMSJjpNoiyU/4vhXuNbrqucde5OTOphDcCW41nOEOA==', 'by40d7wG9dLsLUXrjFB/OEYNV9y2FFXA3lSHh8OU6qaTUED2vpgo4G+VjNAkLTjzY2KHEx5A+My4/fvwt+l7aA==', 'vi7EiIiLpae1JASp8R75rR+CNMFjIo3GJSBcOnIJudun4HQm3YVVBqQRgDK7gHuIE0gIQ+hzscnegD1u9TpTFQ==', 'DNV6Lr6y1RqgKIdNzzJQyC14A0vEcpPISCJax9iQ+bjINWLlM/oPgAYairSJjLFhAYKjVi7lweMjFMi2pbcdGA==', 'jEMQvq0xp3gJYJM7YdKuBYwFAurCi2jNbYjEVZXnqgIgVWR8YR8b85NN2+UzoTSpuJKujorrAOXP0BZK0aFQrw==', 'ytypx7c75dkJFXqCbXV7b1ye+0m1Q1LP1ziSUVe+Rha6Jv1JT97/X3rxWckV8U7ZwA9UMVCt6OzRbtDHDQpKWw==', 'ZypW+vFjuhRGdKWCBa/lT3gJ1inEjI3XxeHNx0blrpArX9afsq79BPXy2SebbZmeKj/8IE7akJdWHpWKcHmqGQ==', 'iTR3lGkeZVAAmf+p/S+4YEF5cUoI8iPnr+IC3P579kDliSwMvgBHsJ+i+ALb5Ep7RHZEQOMFcje4jKiRO6nnNQ==', 'LFmQ0DdWBqTHpf4hMYVgVP8D4FvGV/wKE9PIR6IhCz0/W85S8GSjFJNWP7JOHZC6Py4Ekw7GhnN51j0+FY33eg==', 'B5eOX5ecWyUQugljntlGAeV6korWL9cjw0Vl3yXHdq0d7lehIHaaInlkMQ9w0PvFLJ23EPg0qMfTSgf7Fn/UEA==', 'uyjpf6hYdeyHE1PVoWXD1s80Ib+KUZl8N5Cyn/cis0kzl6vAkzsgEwB41gRiynDzLsKGqeoT3pbIhdAW6if5hQ==', 'B7JZA4zqRLz9+bVAVpwxTNrXuvx0IVKp9ok72H0mjZE4zuVfdxbz+JQfSwU4LwRSHAH1KpKdfvDpfrZRdCsTxg==', 'ojdhQYwnXZMyOlgYWbtDs+pwGDg6BRVKfazz9M6UlhxKReP0BbbulLAWEToCvdehP01t4f1RFjFGhH4WJm/5Ug==', 'z+VJ4MIETBonvfIZ8Gc6JmDBh1Kf+0vPRNQ5s17/WKX3IDYakbdjQzYORGkueiBSBAL+Qcb0Azmdq5im4Z0saw==', 'bQUXToqp47gmrlg95uO2oWJ7c7wSPBgQ6UxcS/xXF1kYn75o3sy0pWhImYVG/lNGKN9sOEFJ9LiK4JqO5FuAAQ==', 'kbCylpKkjoVZj7vWNpXHwAy9yuP9Oo9qQoe1cKUVIMQN+Oa6T+3HTBBOo9ucQQvfEyoIYetfaKvCnav1Ys2GLg==', 'ouINAQwSKwXbIoPIip459gY6RWYLM9FFR5aM1+7xr7s/Cp3r8IvTFMkMYpx7LvnPnvoToHHgCYDbjjRMgMqwnw==', '0hK67eNFAu6RaziMmlDRRfk6JFpPJniE/JCAlcCAZR2bbHpsWlOC5kq4frwvN49bns6Padh8EXlYJmSoyzXUkw==', '9hjmCqk36x0KFo8VJlJq0zU7IQmXHdnvCxfG/21R8uKH4Y2tcAKWrQa29rrtUFaG9X1MFEm7Oqf4tfIbK01ESw==', 'OZxWiXyPwU+Tp5DfJRm9Vtg1oIw1LL+4x9abMRLf6q+ockJkS27pYc7rxw2g/HiHC7pkMfcEOIn4umB0OG3nRQ==', 'D0t/hA6Bpp9PNbt2YIUSmNkxD+199IcwjHkaz2zOUZb6XtCJvkk3fD4klr0pMWG4jTX0ULsrXTsU5hzDNd4nrQ==', '85UMq3+Uo+Oxp3B7DYxZPpvNB5+ykscS+oNt2a83oi/06mZZj89o/sHws3pyWuGxeTICKBKnwQnw7FBoSJkcFQ==', '3U7yIX5TBdTDfAqEGM0y4EJM6qDAQorpqEtQjAK+C0MTsRHxe7IEJNSG1vvEX2SB1iGMNGoEQQIiJy0+Fy95YA==', 'hVubd1JbNaKiBwmwoHqDydVQM0g0BlidK4znt0McrxmsZH04cHdHR4IEMLAX1WxR1EMsk1EJ6usK9kzr+CbltA==', 'ttN1Ew5EBAeAbkOUPC9TUmtPKB2zBqkvr5cgQkDjCaFHxjzaTNhqgKLkzm/6TBVHKpqPCZ0yw37RlKUyzk2zkg==', 'XzAnXmwW9noGSiBq//FG4JZhV3dDsxJcPn0zHXNLuBy2SEM0TZRZAMMSUvZYeQh48GZHm9h1fwfPlYz6hvQzVg==', 'Ge26Wq+QASCE0kgUzKb3co0Y1Z6CzYdW1iiOGujhS9KYkR1zTNVAWk6Ub6Ee8WUg/4YR9EqQYj4X3KCvHcItzg==', '+Mh2XkaIWaeibEc0Gy+uur/nb5k0bVT9Ee1rTipYvQxkXmVWEX+RA2PmSy/Uyfz3cjy7Qwi1Mp8inoyTbbxCbQ==', 's3YtaTZa6QhSNFhT1sSeC93MoT1uBUofezihENOMZ2GI2prD1kcDJbTlUYFIYHEKFudl1YAQKSkv0HeeyMpopQ==', 'qQ2UPtYsJfgZjNVf4PPqPcLfIo1osxSBKYiKnpsTy6jtV1aBMKMSvu/QlqX//YgU67jPt7ZAkp9lYRe3BSOemA==', '0q4mL6WRRCPdmuMeKTGd6Du64zus7P1UuW+683W+L27bygF7zSWWAuOdkT2mAIwKpHYJ68vWsxoAVvE5NwXyYw==', 't1EAn0GUnKM5pFEQmvwIgYv2WTIKKGAt8/bTp3IqyJeide7k/O7t7Sj2hQm9OtQclvmchabYHUM6bLNT+zvjUw==', 'KZS/SWROCrfrF6cGbfm8x/3Bulajn0q34jiz6jk8an7nWLQvsx28b4bNiOYNnIR54XHhw678rRa2ff1h41VJgg==', 'LerlJIZfR20m2yt9TCQVPfV2tdIuM5OoX6weKcXqDIsiplUYeVyredVTzgA4n+9bYN87JZ9e8bkhvff5ikQvww==', 'J2gwDT1oe6qOqlO7czlcf+1vU93UwwFN2PEyO2ooL4PR0ar16nY6Y7JM/GHOEeIguWGlxWrXStrFTlCFMcob/Q==', 'dgvGGZg3mAH9mQt3nTUrGWAt9T2MmRK4xaCnjKwGeK0BSmTzu+IoumRM03468lUy8//h2OsCUjcOOpPKmrHFng==', 'iiYFIrq1QvLYZHDbdDJGYiNUqXWY4AVKfpxvrLFh/tdWapzhDcdz9C/tWvmzDRl8fqGWO3ygEeNqrsgB86WwRg==', '7PP/TQrBQ32KY4g7lswGk01un2FWe3y2voasl44s8xbefH/YbFZSfOmIvjzoBJ64YIyIl0QGzuhNGw0tDYgwkg==', 'MhaB4MKuz0Q4TEBDPf4Vl4iQs0JtT0f+KFwWYEF+QtPzea2gna2Hmhwijq6dHucMTHXbKGb/LoL27Xg9OudBFw==', 'c1ZpOf/81/Tf5GkD3e74WrDLWHv1tXVgBTCnvjgNS/R99N77rf42h/HOfaTdX11nUM/JIcCwnVdxpn9AjjEbng==', 'Cp2LgTy7VOZXTrSiIHdu8eKwpaIBzyGt77k7FwyarJYItqL1FnffdnbAXg4QsLGwW0zVJw9VYskHPMUjnJHBUw==', 'DLWS3TyDrqNGfA2pHD2aNdhIravxK8ikLu6YU+uu7e4/1WRyb9MIjgGryapUfDTTjNxBMTg4XlC5Zg+Ug9JGNQ==', 'mJCu3caNtytcTMnITT+32D5LDdFUcLw4BAq7whmOtY/QVnncH8RFWOXDkd2UkLmTH7T++qPkh7ABpeobzIolDA==', '5JZrlyoelg99p6Y7T6gRvDIva2eqrOwHi/JrKM3XJc1djl84dm9ukr+WfxVQi9BgzWBM/R6A30HwriXyGVkU9g==', 'VVMKdRmuMoH1qKXqFuEPbnzIa37zHiwNoFBiOqSweS9jZ/w21ce6glgSZY48ZSne5TBdqC/qvoixM+jB+ob6+Q==', 'Qqwgm58lVkdV2ofRI3vsW6RsyBsmw5Ip3LZ3PDRAfHxWAqofXkaYC7QhCLFUUTk8x3Vqwf0kkF7G2l+G9cZuxw==', 'pzbEZS0kIWyS8jFZh4tVAXVSoaKejsdxgNFYtyRJaHF4QDApiobZL40EOJX964b0SV5Ocf3MLk/HXXJY+2k0ig==', 'hs/0yym5XcO2GMDPxIljEvmMqK8Fz0NZw61d0Dsu1ItLHLJu2NfJcPY0W4pZlumMjB+ZApfs1Ltz/M+zfDRy7A==', 'WYrGtmH4WeX9dpL1qJZGR+GGtdu7FhtFMTk3kzpYXPq32LSD0x5yGZ0CyVepZ51EoPT2osUMyTTGgpZyzWs8xg==', 'fq6scckl8OClxg7E8gSuyvTjZASAkUD+qZkD04n6UXGRKrqDjBRuTTSIxeLCIIRfC8IkUtSm+R11uwKDr1kY7Q==', '5rXWgFD6jIDD7wxpuVRepS6WjfNrVTqVVCOb7SdJcLYxsLu6kzfaXL9c9fzG23IXlLSvjT5wWHquuxNdqtklhw==', 'agi23l8oiRL0UA4AC5lp8P3qjE+j2nwVRXqV3+Y6G1sgbZt2exwN5AdY+lZy9PhSHFuFgz71KsbMQGrArHef1A==', 'fXNGsHlGRKuDz2aUSEj6cpaG0Ylu9LYp/lWzynAnaYoJuHypMp0Cm9haA+KRH+7GOzvQmL/hl2qZYIIuz+BLAA==', 'JH55m5+nLn+AgtW8j6mXZAU4fFlPVfZyYULL1q6D5x7FQGKQX/FHkAoc4gNbtkjojCPr44OGsTjDo0PJ/LuVog==', 'Z47S1kjL6XrmzOcvP4hXBj30CwmaefFaB5yk4lBN0NBFjXmZMIXGSiiOpHJxpXRd+0qYJd4jpW0XsAjYN30rfA==', 'y21e7t2xHKIkSQCncmfTyqTOP2iQENvUtp1qrySrGman3Y+z+cS73aaquotPUWV7mfM7H8YBUwQHAszqh041wQ==']

origin_data = pd.read_csv(load_csv+"from_db.csv")

random_state=2

def divide(origin_data,devide_number,number,random_state=random_state):
    copy_data_2=origin_data.copy()
    copy_data_2["date_encrypt"]=copy_data_2["createdAt"].str[:10]+"-----"+copy_data_2["encrypt_id"]#생성일자와 암호키로 새로운 컬럼 추가한다.
    copy_data_2=copy_data_2.drop_duplicates(["date_encrypt"],keep="first")#중복 이미지 제거
    filter_csv=copy_data_2.groupby("encrypt_id").count()#암호키 기준으로 해서 개수를 샌다.
    indexes = filter_csv.index[1:]#정렬된 값의 암호키들을 인덱스로 추출
    encrypt_id = list(indexes)
    
    
    # copy_data_3 = origin_data.copy()
    # filter1 = copy_data_3.maker_id not in [1,2,] 
    
    #암호키만 추출,
    #maker_id는??
    
    print(f"총 환자번호 개수 : {len(encrypt_id)}")
    count_dict=dict()
    for index_o in encrypt_id:
        v=filter_csv.loc[index_o]
        encrypt_id=v["id"]
        if encrypt_id in count_dict:
            count_dict[encrypt_id].append(index_o)
        else:
            count_dict[encrypt_id]=[index_o]
            
    for encrypt_id_v in filter_encrypt_id:
        if encrypt_id_v in count_dict[1]:
            # print(True)
            count_dict[1].remove(encrypt_id_v)

    random.seed(random_state)
    random.shuffle(count_dict[1])
    count_dict[0]=list()
    
    print(f"하루 안에만 같은 환자번호 있는 경우 : {len(count_dict[1])}")
    
    copy_data = count_dict[1].copy()
    count_dict[1]=list()


  
    for i,c in enumerate(copy_data):
        if i%devide_number==number:
            count_dict[0].append(c)
        else:
            count_dict[1].append(c)
  
    # count_dict[0],count_dict[1]=count_dict[1][:100],count_dict[1][100:]

    return count_dict


devide_number = int(input("몇 개 셋트로 나눌래?"))
for number in range(devide_number):
    
    print(f'{"-"*20}{number}번째 시작 {"-"*20}')
    
    count_dict_1 = divide(origin_data,devide_number,number,random_state) #통틀어 하루만 등장한 환자 암호화키
    test_n=count_dict_1[0]
    train_n,val_n = train_test_split(count_dict_1[1],train_size=0.8,random_state=random_state) #10으로 나눴었음 #15프로 처참 #11
    # train_n,test_n = train_test_split(count_dict_1,train_size=0.8,random_state=random_state) #10으로 나눴었음 #15프로 처참 #11

    # val_n,test_n = train_test_split(test_n,train_size=0.6,random_state=random_state)#6:4
        #20:3:2

    with open(path+json2,"r") as file2 :
        data_db= json.load(file2)
            
    train_data = data_db.copy()
    val_data = data_db.copy()
    test_data = data_db.copy()

    train_list=list()#train
    val_list=list()#val
    test_list=list()#test


    check_duplication=[]

    for data in data_db["images"]:
        if data["encrypt_id"] in val_n:
            val_list.append(data)
        elif data["encrypt_id"] in test_n:
            if data["encrypt_id"] not in check_duplication:
                check_duplication.append(data["encrypt_id"])
                test_list.append(data)
        else:
            train_list.append(data)
            
        
    train_data["images"]=train_list
    val_data["images"]=val_list
    test_data["images"]=test_list

    total_count = len(train_list)+len(val_list)+len(test_list)
    # print(total_count)

    print(f'image_count : {len(data_db["images"])}')
    print(f'total_count : {total_count},필터링된 개수')
    print(f"train_size : {len(train_list)}, ({(len(train_list)/total_count)*100:.1f}%)")
    print(f"val_size : {len(val_list)}, ({(len(val_list)/total_count*100):.1f}%)")
    print(f"test_size : {len(test_list)}, ({(len(test_list)/total_count)*100:.1f}%), 중복환자번호 필터링")
    
    


    with open(f"{path}/{json4}","w") as file_w:
        json.dump(train_data,file_w)

    with open(f"{path}/{json5}","w") as file_w:
        json.dump(val_data,file_w)

    with open(f"{path}/{json6}","w") as file_w:
        json.dump(test_data,file_w)

    createFolder(f"{create_json_path}/#{number}")

    with open(f"{create_json_path}/#{number}/#{number}.txt","w") as file:
        file.write(f'image_count : {len(data_db["images"])}\n')
        file.write(f'total_count : {total_count},필터링된 개수\n')
        file.write(f"train_size : {len(train_list)}, ({(len(train_list)/total_count)*100:.1f}%)\n")
        file.write(f"val_size : {len(val_list)}, ({(len(val_list)/total_count*100):.1f}%)\n")
        file.write(f"test_size : {len(test_list)}, ({(len(test_list)/total_count)*100:.1f}%), 중복환자번호 필터링\n")

    with open(f"{create_json_path}/#{number}/{json4}","w") as file_w:
        json.dump(train_data,file_w)

    with open(f"{create_json_path}/#{number}/{json5}","w") as file_w:
        json.dump(val_data,file_w)

    with open(f"{create_json_path}/#{number}/{json6}","w") as file_w:
        json.dump(test_data,file_w)

