from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        age = int(request.form["age"])
        goal = request.form["goal"]
        food = request.form["food"]

        if goal == "Weight Loss":
            result = f"Healthy suggestion: {food} + vegetables + fruits + plenty of water"

        elif goal == "Weight Gain":
            result = f"Healthy suggestion: {food} + milk + nuts + eggs"

        else:
            result = f"Healthy suggestion: {food} + vegetables + fruits"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
