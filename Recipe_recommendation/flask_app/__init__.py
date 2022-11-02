from flask import Flask, render_template, request
from flask_app.routes.main_route import bp as main_bp
import pickle

app = Flask(__name__) 

with open(r"C:\Users\Sunyoung_Jang\Documents\GitHub\Projects\Recipe_recommendation\flask_app\recipe.pickle","rb") as fr:
    recipe = pickle.load(fr)
with open(r"C:\Users\Sunyoung_Jang\Documents\GitHub\Projects\Recipe_recommendation\flask_app\model.pickle","rb") as fr:
    model = pickle.load(fr)

########## test
# Load pickle
# my_ingredients = '라면, 감자, 소금, 버터, 설탕, 고추장, 밥, 후추, 간장, 당근, 소면, 계란'


# model.fit(recipe, my_ingredients)
# recommedation = model.find_sim_recipe(30)
# print(recommedation.iloc[0,0])

###########3

@app.route('/', methods=['GET', 'POST']) 
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        try:
            ###### model 학습 존
            # input
            try:
                my_ingredients = str(request.form['ingre']) # ''안에 ,로 구분된 입력값을 받는다. (str)
                cooking_time = float(request.form['time'])
                print(type(my_ingredients), type(cooking_time)) ## test

            except:
                my_ingredients = '물, 식용유, 밥, 소금, 설탕'
                cooking_time = 180
            
            # training
            model.fit(recipe, my_ingredients)
            pred = model.find_sim_recipe(cooking_time)

            # output = pred[['Recipe_name','Url']].set_index('Recipe_name').to_html()
            output = pred[['Recipe_name','Url']].values.tolist()
            # for i in output:
            #     print(i)

            return render_template("index.html", recipes=output)

        except :
            return render_template("404.html")


@app.route('/tmp', methods=['GET','POST'])
def tmp():

    return render_template('index_temp.html')

if __name__ == "__main__":
    app.run(debug=True)