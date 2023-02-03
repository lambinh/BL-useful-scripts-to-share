import os
import requests
import datetime

# Optain OpenAI Key: https://platform.openai.com/account/api-keys
# Read the API key from the .aiapikey file
api_key = open(".aiapikey", "r").read().strip()

# Set the headers for the API call
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Get the user input for the prompt
print("State-of-the-art image generation - powered by OpenAI")
prompt = input("Enter the description of a photo you want to generate': ")

# Set the data for the API call
data = {
    "prompt": prompt,
    "n": 1,
    "size": "1024x1024"
}

# Make the API call using the requests library
response = requests.post("https://api.openai.com/v1/images/generations", headers=headers, json=data)

# Check the status code of the response
if response.status_code == 200:
    # If the API call was successful, extract the URL of the generated image
    image_url = response.json()["data"][0]["url"]
    # Create a file name based on the current time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"image_{current_time}.png"

    # Download the image as a PNG file
    image_response = requests.get(image_url)
    with open(file_name, "wb") as image_file:
        image_file.write(image_response.content)
    print(f"Image saved as '{file_name}'")
else:
    # If the API call was not successful, print an error message
    print("Failed to generate image. Response code:", response.status_code)
