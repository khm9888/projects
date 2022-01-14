# -*- coding:utf-8 -*-
import pandas as pd
import pymysql


ip = "115.71.28.90"
port = 13304
user = "root"
pw = "acryl00"
db = "MARKER"
table = 'BURN_USER'
charset = "utf8"

choice = input("전체 모두 검색하시겠습니까?(y or yes/n)")


def select_data(table_name):  # DB 통해서, 값을 가져오는 함수
    conn = pymysql.connect(
        host=ip,
        user=user,
        passwd=pw,
        db=db,
        charset=charset,
        port=port
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = f'SELECT * FROM {table_name};'
    cursor.execute(sql)
    rows = cursor.fetchall()
    result = pd.DataFrame(rows)

    return result


origin_data = select_data(table_name=table)
print(origin_data)
