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

assignment/
├── model/
│ └── mobilenetv2_catsdogs.pth # Trained model weights
├── utils.py # Contains image transform function
├── app.py # Flask app
├── myenv/ # Virtual environment (optional)
└── README.md # Project documentation


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone 
cd cat-vs-dog-api
