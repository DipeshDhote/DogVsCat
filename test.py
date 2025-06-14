import requests
import os

url = "http://127.0.0.1:5000/predict-image"

image_path = "test_data/th.jpg"  # Replace with your actual image path

print(os.path.exists(image_path))

# Open the image in binary mode
with open(image_path, 'rb') as img_file:
    files = {'file': img_file}
    response = requests.post(url=url, files=files)

# Print the response
print("Status Code:", response.status_code)
print("Response:", response.json())
