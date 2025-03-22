from picamera2 import Picamera2, Preview
from time import sleep 

camera=Picamera2()
camera_config = camera.create_preview_configuration()
camera.configure(camera_config)
camera.start()
sleep(1)
camera.capture_file("/home/pi/cs326/final_proj/pic.jpg")
