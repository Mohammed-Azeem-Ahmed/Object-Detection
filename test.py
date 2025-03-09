from ultralytics import YOLO
# from ultralytics.yolo.v7.detect.predict import DETECTIONPredictor
# import cv1

model = YOLO("yolov8n.pt")

results = model.predict(source="0",show=True)
type(results)

predict(results)