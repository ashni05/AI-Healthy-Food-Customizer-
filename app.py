from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        age = int(request.form["age"])
        goal = request.form["goal"]
        food = request.form["food"]

        if goal == "Weight Loss":
            suggestion = f"{food} + vegetables + fruits + plenty of water"
            calories = "Approx. 350–450 kcal"
            meal = "Healthy meal with vegetables and fruits"
            ingredients = f"{food}, vegetables, fruits"
            benefits = "Supports a balanced healthy lifestyle"
            water = "6–8 glasses per day"

        elif goal == "Weight Gain":
            suggestion = f"{food} + milk + nuts + eggs"
            calories = "Approx. 500–650 kcal"
            meal = "Protein-rich meal with milk and nuts"
            ingredients = f"{food}, milk, nuts, eggs"
            benefits = "Provides protein and energy"
            water = "6–8 glasses per day"

        else:
            suggestion = f"{food} + vegetables + fruits"
            calories = "Approx. 400–500 kcal"
            meal = "Balanced meal with vegetables and fruits"
            ingredients = f"{food}, vegetables, fruits"
            benefits = "Provides a balanced mix of nutrients"
            water = "6–8 glasses per day"

        result = {
            "suggestion": suggestion,
            "calories": calories,
            "meal": meal,
            "ingredients": ingredients,
            "benefits": benefits,
            "water": water
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
