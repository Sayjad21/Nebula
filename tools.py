import cv2
import base64
from groq import Groq
import config

def capture_image():
    """captures one image from the webcam.resize it and encode it as base64 jpeg(raw string) and returns it"""
    for idx in range(4):
        cap= cv2.VideoCapture(idx)
        if cap.isOpened():
            for _ in range(10):
                cap.read()  # skip the first 10 frames to allow camera to adjust
            ret, frame = cap.read()
            cap.release()
            if not ret:
                continue
            cv2.imwrite('temp.jpg', frame)
            ret, buf=cv2.imencode('.jpg', frame)
            if ret:
                base64_str = base64.b64encode(buf).decode('utf-8')
                return base64_str
    raise RuntimeError("No camera found or unable to capture image.")
            


def analyze_image(query:str)->str:
    """Expects a string with query.captures the image and sends query and then sends query and image to Groq vision chat api and returns the response"""
    
    image_base64 = capture_image()
    model="meta-llama/llama-4-maverick-17b-128e-instruct"
    if not query or not image_base64:
        raise ValueError("Query and image must be provided.")
    client = Groq(api_key=config.groq_api_key)
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_base64}",
                    },
                },
            ],
        }]
    chat_completion = client.chat.completions.create(
        model=model,
        messages=messages,
    )
    return chat_completion.choices[0].message.content
          
            
# Run the function
if __name__ == "__main__":
    query="how many people are there in the image?also describe the image"
    response = analyze_image(query)
    print("Response from Groq API:", response)