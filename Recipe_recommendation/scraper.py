from api import get_recipe_list, recipe_finder, save_to_mongoDB

# 레시피 목록 가져오기 개수:1000개
# 레시피 긁어오기

for i in range(1,41):
    print(f'{i}번째 페이지 스크래핑 중...\n')
    recipe_list = get_recipe_list(keyword = '자취요리', page_num = i) # 자취요리 키워드로 40페이지까지 스크랩 완료...40개에 6분 걸림 # 일단 몽고디비에 저장....

    for recipe in recipe_list:
        try:
            recipe_info = recipe_finder(recipe)
            save_to_mongoDB(recipe_info)
        except:
            print(f'\n-----------------------\nError! Sth wrong happened in recipe_code : {recipe}')
            pass
            
    print(f"""
Result:
{i}번째 페이지 스크래핑 완료
MongoDB 예상 적재 데이터 : {40 * i}개
    --------------------------------------
    """)