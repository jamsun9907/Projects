from bs4 import BeautifulSoup
from requests import get
import time
from pymongo import MongoClient

def get_recipe_list(keyword='자취요리', page_num = 1):
    """
    keyword, page_num를 넣어주면 모두의 레시피에서 레시피 코드를 불러옴
    한 페이지에 레시피 40개
    """
    time.sleep(5) # 트래픽 부하를 막기 위해..

    # url 셋팅
    url = f'https://www.10000recipe.com/recipe/list.html?q={keyword}&order=reco&page={page_num}'
    html = get(url).content
    soup = BeautifulSoup(html, 'html.parser')


    # 이번엔 자취요리 레시피 코드를 가져온다. 자취요리 검색했을 때 나오는 레시피를 추천순으로 나열하여 데이터를 구한다.
    recipe_list = soup.find_all('a','common_sp_link',href=True)
    
    # 레시피의 개수(40개)
    recipe_num = len(recipe_list) 

    # 개별 코드 구하기
    recipe_code_list = []

    for i in range(recipe_num):
        tmp = recipe_list[i]['href'].rsplit('/', maxsplit=1)[1]
        try:
            int(tmp)
            recipe_code_list.append(tmp)
        except:
            pass

    return recipe_code_list

def recipe_finder(recipe_code):
    """
    레시피 코드를 입력하면 레시피명, 재료, 링크를 반환한다.
    """
    time.sleep(5) # 트래픽 부하를 막기 위해..

    # 기본 설정
    url = f'https://www.10000recipe.com/recipe/{recipe_code}'
    html = get(url).content
    soup = BeautifulSoup(html, 'html.parser')

    # 레시피 이름과 링크를 가져옴
    goods = soup.find(id = 'relationGoods')

    recipe_name = goods.find("div", 'best_tit').b.contents

    ingredients = soup.find(id = 'divConfirmedMaterialArea').find_all('ul')

    # 페이지의 필수 재료를 가져옴
    ingre_dict = {}

    for tb_num in range(len(ingredients)):
        # 테이블 마다 이름, 재료 가져옴
        tb_name = ingredients[tb_num].b.contents[0].replace('[','').replace(']','')
        ingre_list = [ingregient.contents[0].strip() for ingregient in ingredients[tb_num].find_all('li')] 

        ingre_dict[tb_name] = ingre_list # 딕셔너리 형태로 저장
    
    # 가져온 데이터를 dict 형태로 concatenate
    # 저장할 형태 지정 -> nosql로 저장할 예정
    recipe_info = {}

    # 저장
    recipe_info['recipe_name'] = recipe_name[0]
    recipe_info['url'] = url
    recipe_info['ingredients'] = ingre_dict

    return recipe_info

def save_to_mongoDB(recipe):
    """
    힘들게 구한 레시피 info를 mongoDB에 저장한다. reco
    """
    HOST = 'cluster0.1lslter.mongodb.net'
    USER = 'Sunyoung'
    PASSWORD = 'sun123'
    DATABASE_NAME = 'recipe_DB'
    COLLECTION_NAME = 'recipe_info'
    MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

    # 커넥션 접속 작업
    client = MongoClient(MONGO_URI) 
    db = client[DATABASE_NAME] # Connection
    collection = db[COLLECTION_NAME] # Creating table

    collection.insert_one(document = recipe)

    return None

# dddaf