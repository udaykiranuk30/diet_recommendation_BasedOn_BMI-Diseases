from flask import Flask, render_template, request
from diet_model import DietModel
import datetime
import ast
import requests
from bs4 import BeautifulSoup

Not_found_link='data:image/png;base64,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'

def get_images_links(searchTerm):
    try:
        searchUrl = "https://www.google.com/search?q={}&site=webhp&tbm=isch".format(searchTerm)
        d = requests.get(searchUrl).text
        soup = BeautifulSoup(d, 'html.parser')

        img_tags = soup.find_all('img')

        imgs_urls = []
        for img in img_tags:
            if img['src'].startswith("http"):
                imgs_urls.append(img['src'])

        return(imgs_urls[0])
    except:
        return Not_found_link


app = Flask(__name__)

# Load the model
model = DietModel.load_model('diet_model.sav')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/dietrecommend',methods=['POST','GET'])
def dietrecommend():
    return render_template('index.html');

@app.route('/generated', methods=['POST', 'GET'])
def generated():
     # Get the chosen ingredients from the form data
    chosen_ingredients = request.form.getlist('chosenIngredients')

    # Convert the string representation of the ingredients to a Python list
    input_ingredients = ast.literal_eval(chosen_ingredients[0])

    # Get the user details from the form
    user_details = {
        'height': request.form.get('height'),
        'weight': request.form.get('weight'),
        'age': request.form.get('age'),
        'gender': request.form.get('gender'),
        # Add other user details as needed
    }

    # Prepare input nutrition and ingredients
    input_nutrition = [250, 15, 2, 80, 150, 30, 5, 3, 20]  # Adjust the values as per your requirement

    # Check if input ingredients are provided
    if input_ingredients:
        recommendation_dataframe = model.recommend(input_nutrition,input_ingredients)
        output = model.output_recommended_recipes(recommendation_dataframe)

        # Prepare the output and pass it back to generated.html
        if output is None:
            output_text = "No recipes found."
        else:
            output_text = []

            timestamp = datetime.datetime.now()  # Get the current timestamp

          

            for recipe in output:
                recipe_text = f"<div class='recipe'>"

                # Add the image to the recipe
                image_url = get_images_links(recipe['Name'])  # Retrieve image URL based on recipe name
                recipe_text += f"<img src='{image_url}' alt='Recipe Image' class='recipe-image'>"

                recipe_text += "<div class='recipe-content'>"
                recipe_text += f"<h2>{recipe['Name']}</h2>"

                if recipe['RecipeIngredientParts']:
                    recipe_text += "<h3>Ingredients:</h3>"
                    recipe_text += "<ul>"
                    for ingredient in recipe['RecipeIngredientParts']:
                        if ingredient in input_ingredients:
                            recipe_text += f"<li>{ingredient}</li>"
                        else:
                            recipe_text += f"<li>{ingredient}</li>"
                    recipe_text += "</ul>"
                else:
                    recipe_text += "<p class='empty-placeholder'>No ingredients available</p>"

                if recipe['RecipeInstructions']:
                    recipe_text += "<h3>Instructions:</h3>"
                    recipe_text += "<ol>"
                    for instruction in recipe['RecipeInstructions']:
                        recipe_text += f"<li>{instruction}</li>"
                    recipe_text += "</ol>"
                else:
                    recipe_text += "<p class='empty-placeholder'>No instructions available</p>"

                recipe_text += "</div>"
                recipe_text += "</div>"
                output_text.append(recipe_text)

            output_text = "".join(output_text)
    else:
        output_text = "No ingredients selected."

    return render_template('results.html', chosenIngredients=input_ingredients, output_text=output_text)
 

@app.route('/disease',methods=['POST','GET'])
def disease():
    return render_template('disease.html')

@app.route('/diseaseprediction', methods=['POST', 'GET'])
def diseaseprediction():
    # Get the chosen ingredients from the form data
    chosen_ingredients = request.form.getlist('chosenIngredients')

    # Convert the string representation of the ingredients to a Python list
    input_ingredients = ast.literal_eval(chosen_ingredients[0])

    input_nutrition=ast.literal_eval(request.form['recommendedPreferences'])


    # Check if input ingredients are provided
    if input_ingredients:
        recommendation_dataframe = model.recommend(input_nutrition,input_ingredients)
        output = model.output_recommended_recipes(recommendation_dataframe)

        # Prepare the output and pass it back to generated.html
        if output is None:
            output_text = "No recipes found."
        else:
            output_text = []

            timestamp = datetime.datetime.now()  # Get the current timestamp

            for recipe in output:
                recipe_text = f"<div class='recipe'>"

                # Add the image to the recipe
                image_url = get_images_links(recipe['Name'])  # Retrieve image URL based on recipe name
                recipe_text += f"<img src='{image_url}' alt='Recipe Image' class='recipe-image'>"

                recipe_text += "<div class='recipe-content'>"
                recipe_text += f"<h2>{recipe['Name']}</h2>"

                if recipe['RecipeIngredientParts']:
                    recipe_text += "<h3>Ingredients:</h3>"
                    recipe_text += "<ul>"
                    for ingredient in recipe['RecipeIngredientParts']:
                        if ingredient in input_ingredients:
                            recipe_text += f"<li>{ingredient}</li>"
                        else:
                            recipe_text += f"<li>{ingredient}</li>"
                    recipe_text += "</ul>"
                else:
                    recipe_text += "<p class='empty-placeholder'>No ingredients available</p>"

                if recipe['RecipeInstructions']:
                    recipe_text += "<h3>Instructions:</h3>"
                    recipe_text += "<ol>"
                    for instruction in recipe['RecipeInstructions']:
                        if instruction.strip():
                            recipe_text += f"<li>{instruction.strip()}</li>"
                    recipe_text += "</ol>"
                else:
                    recipe_text += "<p class='empty-placeholder'>No instructions available</p>"

                recipe_text += "</div>"
                recipe_text += "</div>"
                output_text.append(recipe_text)

            output_text = "".join(output_text)
    else:
        output_text = "No ingredients selected."

    return render_template('generated.html', chosenIngredients=input_ingredients, output_text=output_text)


 

if __name__ == '__main__':
    app.run()
