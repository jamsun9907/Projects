from itertools import chain
from pymongo import MongoClient
import pymysql
import pandas as pd
import numpy as np


def load_Mongo_recipe():
    """
    MongoDB에 있는 모든 레시피를 불러와 리스트 형태로 반환한다.
    """
    # 커넥션 접속 작업
    HOST = 'cluster0.1lslter.mongodb.net'
    USER = 'Sunyoung'
    PASSWORD = 'sun123'
    DATABASE_NAME = 'recipe_DB'
    COLLECTION_NAME = 'recipe_info_v2'
    MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

    client = MongoClient(MONGO_URI) 
    db = client[DATABASE_NAME] # Connection
    collection = db[COLLECTION_NAME] # Creating table

    ## MongoDB 에서 데이터 불러오기
    data_list = [i for i in collection.find()]

    return data_list


def list_to_dataframe(data_list):
    """
    list를 넣어주면 더블리스트 풀고 df에 추가한다.
    Mongo DB에 있던 중복치 처리는 덤
    """
    # 데이터 프래임 생성
    df = pd.DataFrame(
    {'Recipe_name':[],
    'Hit_num':[],
    'Serves':[],
    'Cooking_time':[],
    'Level':[],
    'Url':[],
    'Ingredients':[]})

    for row in range(len(data_list)):
        # 재료의 더블 리스트롤 풀어준다
        dict_val = data_list[row]['ingredients'].values()
        ingredients = ','.join(s for s in list(chain(*dict_val))) # 리스트를 텍스트로 변환

        # 데이터 프레임에 추가 (id, name, url, ingredient 순서)
        df.loc[row] = [
            data_list[row]['recipe_name'], 
            data_list[row]['hit_num'],
            data_list[row]['serves'],
            data_list[row]['cooking_time'], 
            data_list[row]['level'],
            data_list[row]['url'], 
            ingredients]

    return df


def preprocessing(df):
    """
    깔끔하게 전처리를 완료하는 함수이다.
    """
    df_clean = df.copy()

    # 중복 제거 및 재정렬
    df_clean = df.copy()
    df_clean.drop_duplicates(subset='Url', inplace = True)
    df_clean.reset_index(inplace = True, drop = True)

    # 컬럼 형식 맞추기
    df_clean['Hit_num'] = df_clean['Hit_num'].str.replace(',','').astype(int)
    df_clean['Serves'] = df_clean['Serves'].str.extract(r'(\d+)').astype(int)
    df_clean['Cooking_time'] = df_clean['Cooking_time'].str.replace('2시간','120').str.extract(r'(\d+)').astype(int)

    return df_clean



##### 여기부터는 advanced #####
# 정제된 레시피 목록을 localDB에 저장한다.
def get_connection():

    HOST = 'localhost'
    USER = 'root'
    PASSWORD = '0000'
    DB_name='recipe'

    conn = pymysql.connect(host = HOST, user = USER, password = PASSWORD, db = DB_name, charset='utf8') 
    return conn

def init_table(conn):
    """
    recipe Table을 초기화
    """
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS recipe;")
    cur.execute("""CREATE TABLE recipe (
        id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Recipe_name VARCHAR(200),
        Hit_num INTEGER,
        Serves INTEGER,
        Cooking_time INTEGER,
        Level VARCHAR(200),
        Url VARCHAR(200),
        Ingredients VARCHAR(10000));""")
    
    conn.commit()
    pass


def df_to_sql(conn, df_clean):
    """
    레시피 데이터 프레임을 Mysql에 저장
    """
    cur = conn.cursor()
    query = "INSERT INTO recipe(Recipe_name, Hit_num, Serves, Cooking_time, Level, Url, Ingredients) VALUES (%s,%s,%s,%s,%s,%s,%s);"

    for row in range(len(df_clean)):
        data = df_clean.iloc[row, :].tolist()
        cur.execute(query, data)

    conn.commit()
    pass

## 저장
data_list = load_Mongo_recipe()
df = list_to_dataframe(data_list)
df_clean = preprocessing(df)
conn = get_connection()
init_table(conn)
df_to_sql(conn, df_clean)