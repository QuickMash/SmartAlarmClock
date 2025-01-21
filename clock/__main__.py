import requests
import time
import datetime
import flask
import os
import json
import speech_recognition as sr


def main():
  time = json.loads(requests.get("http://worldtimeapi.org/api"))
  print(time)
  print("Formatting...")
  print(time["time"])

def recognize():
  print("TALK")
  
if __name__ == "__main__":
  main()
else:
  sys.exit(f"{__name__} must be ran directly")
