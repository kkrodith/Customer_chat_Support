import os
from PIL import Image
import base64
import google.generativeai as genai

# Set your API key from environment variables
api_key = os.getenv("MY_API_KEY")
if not api_key:
    print("Error: API key not found. Please set 'MY_API_KEY' in your environment variables.")
    exit(1)
genai.configure(api_key=api_key)

def send_text_request(prompt):
    try:
        response = genai.generate_text(prompt=prompt)
        return response.text
    except Exception as e:
        return f"Error generating text: {e}"

def image_analysis_request(image_path):
    try:
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
        response = genai.generate_image_analysis(image=encoded_image)
        return response.text
    except FileNotFoundError:
        return "Error: File not found. Please provide a valid image path."
    except Exception as e:
        return f"Error analyzing image: {e}"

if __name__ == '__main__':
    print("Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif 'show image' in user_input.lower():
            image_path = input("Enter the path of the image file: ")
            output = image_analysis_request(image_path)
            print("Assistant:", output)
        else:
            output = send_text_request(user_input)
            print("Assistant:", output)
