from flask import Flask, render_template, request
from bayes import predict_disease


app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")



@app.route("/predict", methods=["POST"])
def predict():


    name = request.form.get("name")

    age = request.form.get("age")

    gender = request.form.get("gender")


    symptoms = request.form.getlist("symptoms")



    disease, probabilities = predict_disease(symptoms)



    return render_template(
        "result.html",
        name=name,
        age=age,
        gender=gender,
        symptoms=symptoms,
        disease=disease,
        probabilities=probabilities
    )



if __name__ == "__main__":

    app.run(debug=True)