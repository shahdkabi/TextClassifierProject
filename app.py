from flask import Flask, request, jsonify
import pickle

# Load model, vectorizer, and clear category names
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)
with open("categories.pkl", "rb") as f:
    categories = pickle.load(f)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Flask ML API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    # Transform text and predict
    X = vectorizer.transform([text])
    prediction_index = model.predict(X)[0]  # numeric label
    category_name = categories[prediction_index]  # clear name

    return jsonify({
        "text": text,
        "category": category_name
    })

if __name__ == "__main__":
    app.run(debug=True)
