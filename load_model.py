from diet_model import DietModel

# Load the model
model = DietModel.load_model('diet_model.sav')

# Get user input
height_cm = float(input("Enter your height in centimeters: "))
weight_kg = float(input("Enter your weight in kilograms: "))
age = int(input("Enter your age: "))
gender = input("Enter your gender (M or F): ")
activity_level = float(input("Enter your activity level (1.2 for sedentary, 1.375 for lightly active, 1.55 for moderately active, 1.725 for very active, and 1.9 for extremely active): "))

# Calculate BMI
bmi = weight_kg / (height_cm / 100) ** 2
print(f"Your BMI is {bmi:.2f}")

# Calculate calorie intake
if gender == "M":
    bmr = 88.36 + (13.4 * weight_kg) + (4.8 * height_cm) - (5.7 * age)
else:
    bmr = 447.6 + (9.2 * weight_kg) + (3.1 * height_cm) - (4.3 * age)

calorie_intake = bmr * activity_level
print(f"Your daily calorie intake should be {calorie_intake:.2f} calories")

# Add suitable ingredients to input_ingredients array based on BMI
input_ingredients = []

if bmi < 18.5:
    input_ingredients = ['rice', 'eggs', 'beans', 'bananas', 'apples', 'carrots']
elif bmi < 25:
    input_ingredients = ['oats', 'chicken', 'yogurt', 'spinach', 'berries', 'nuts']
elif bmi < 30:
    input_ingredients = ['brown rice', 'salmon', 'sweet potato', 'quinoa', 'tomatoes', 'bell peppers']
else:
    input_ingredients = ['kale', 'tofu', 'broccoli', 'mushrooms', 'cauliflower', 'garlic']

print("Your recommended ingredients are:")
print(input_ingredients)

import random

# randomly choose 2 ingredients
input_ingredients = random.sample(input_ingredients, k=2)

print("Chosen ingredients:", input_ingredients)
input_nutrition = [250, 15, 2, 80, 150, 30, 5, 3, 20]
# Call recommend function to get recommended recipes
recommendation_dataframe = model.recommend(input_nutrition,input_ingredients)
output = model.output_recommended_recipes(recommendation_dataframe)

# Print output
if output is None:
    print("No recipes found.")
else:
    for recipe in output:
        print(f"Name: {recipe['Name']}")
        print(f"Ingredients: {recipe['RecipeIngredientParts']}")
        print(f"Instructions: {recipe['RecipeInstructions']}")
        print("--------")
