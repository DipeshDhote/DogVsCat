# 🐱🐶 Cat vs Dog Image Classification API

This project is a Flask-based REST API that classifies uploaded images as either a **cat** or a **dog** using a fine-tuned **MobileNetV2** model in **PyTorch**.

---

## 🚀 Features

- Binary image classification (Cat / Dog)
- RESTful API with Flask
- Torch model loading and prediction
- Preprocessing with torchvision transforms
- Returns predicted label and confidence score

---

## 🧠 Model Architecture

- **Base Model**: MobileNetV2 (pretrained=False)
- **Modified**: Final layer changed to `Linear(1280, 1)` for binary output
- **Activation**: Sigmoid for probability output
- **Trained On**: Dogs vs Cats dataset (Kaggle or custom)

---

## 🗂️ Project Structure
```
assignment/
├── model/
│ └── mobilenetv2_catsdogs.pth # Trained model weights
├── utils.py # Contains image transform function
├── app.py # Flask app
├── myenv/ # Virtual environment (optional)
└── README.md # Project documentation
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/DipeshDhote/DogVsCat.git
cd DogVsCat-api
```

## API Endpoints

1.Home
URL: /
Method: GET

Response:

json
Copy
Edit
{
  "success": true,
  "content": "This is the home page of the Cat vs Dog Image Classification project"
}

2. Predict Image
URL: /predict-image
Method: POST
Payload: multipart form with image file

Example using cURL:

bash
Copy
Edit
curl -X POST http://127.0.0.1:5000/predict-image \
     -F "file=@path_to_image.jpg"
Response:

json
Copy
Edit
{
  "success": true,
  "label": "dog",
  "confidence": 0.9823
}

