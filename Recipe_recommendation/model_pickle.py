from model import get_recipe, recommendation_model
import pickle

########### 흐름 ################
# 로컬 영역 
# 1. MongoDB 데이터를 가져와
# 2. 전처리해서 df로 바꾸고, 레시피는 local DB에 저장
# -> 웹에서 작동
# 3.0 피클링 : 저 위에꺼 다하는 클래스 객채(model)
# 3. 사용자 인풋 값 + 이미 있는 레시피 데이터 값으로 콘텐츠 기반 알고리즘 
# 4. 반환 값 출력(레시피 10개)

### 알고리즘 클레스로 구현하기

my_ingredients = '라면, 감자, 소금, 버터, 설탕, 고추장, 밥, 후추, 간장, 당근, 소면, 계란'

# recipe 불러오기
recipe = get_recipe()
df = recipe.just_get() # recipe dataframe

model = recommendation_model() # 모델

## 피클링
with open("model.pickle","wb") as fw:
    pickle.dump(model, fw)
 
# Load pickle
with open("model.pickle","rb") as fr:
    model = pickle.load(fr)

model.fit(df, my_ingredients)
recommedation = model.find_sim_recipe(30)
print(recommedation.iloc[0,0])

## Save recipe
# with open("recipe.pickle","wb") as fw:
#     pickle.dump(df, fw)
 
# # Load pickle
# with open("recipe.pickle","rb") as fr:
#     recipe = pickle.load(fr)
# print(recipe)

# print(recipe.iloc[ 0,0])

