from api import get_recipe_list, recipe_finder, save_to_mongoDB

# 레시피 목록 가져오기 개수:1000개
# 레시피 긁어오기
recipe_list = get_recipe_list(page_num = 1)

for recipe in recipe_list:
    try:
        recipe_info = recipe_finder(recipe)
        save_to_mongoDB(recipe_info)
    except:
        print(f'\n-----------------------\nError! Sth wrong happened in recipe_code : {recipe}')
        pass