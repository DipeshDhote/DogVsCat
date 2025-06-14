import torch
from torchvision import models
import torch.nn as nn
import os
from dotenv import load_dotenv

load_dotenv()



DEVICE = "cuda" if os.environ.get("USE_CUDA") == "1" and torch.cuda.is_available() else "cpu"
CLASSES = ["cat", "dog"]
MODEL_PATH = os.environ.get("MODEL_PATH", "model/mobilenetv2_catsdogs.pth")

# Load the model
def load_model():
    model = models.mobilenet_v2(pretrained=False)
    model.classifier[1] = nn.Linear(model.last_channel, 1)
    model.load_state_dict(torch.load(MODEL_PATH,map_location=DEVICE))
    model = model.to(DEVICE)
    model.eval()

    return model

# Prediction
def predict(model,input_tensor):
    output = model(input_tensor.to(DEVICE))
    prob = torch.sigmoid(output)
    label = int((prob > 0.5).item())
    confidence = round(prob.item(), 4)

    return label, confidence

