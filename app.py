from flask import Flask, request, jsonify
from model import load_model, predict,CLASSES
from utility import get_transform, preprocess_image

app = Flask(__name__)

model = load_model()
transform = get_transform()

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "success": True,
        "content": "This is the home page of the Cat vs Dog Image Classification project"
    })

@app.route("/predict-image", methods=["POST"])
def predict_image_api():
    if "file" not in request.files:
        return jsonify({"success": False, "error": "No image file provided"}), 400

    file = request.files["file"]
    try:
        input_tensor = preprocess_image(file, transform)
        label_idx, confidence = predict(model, input_tensor)
        return jsonify({
            "success": True,
            "label": CLASSES[label_idx],
            "confidence": confidence
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
    

if __name__ == "__main__":
    app.run(debug=True)
