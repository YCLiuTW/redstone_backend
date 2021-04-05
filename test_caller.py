import requests
import cv2, base64, json
from pydantic import BaseModel

def pass_image_caller():
  url = "http://127.0.0.1:8000/test2"
  token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuZXdqYXRlIiwiZXhwIjoxNjE3NDU0Mzc4fQ.DBFvs7X8HCCe0YT8SBHEF7zE3ji0_OlRZ_MhOF249f0'
  headers = {'Authorization' : "bearer "  + token}
  img = cv2.imread('1.jpg')
  _, img_encoded = cv2.imencode('.jpg', img)
  payload = json.dumps({'image' : str(base64.b64encode(img_encoded), encoding='utf-8')})
  response = requests.request("POST", url, headers = headers, data = payload)
  print(response.status_code)
  print(response.text)

if __name__ == '__main__':
  pass_image_caller()