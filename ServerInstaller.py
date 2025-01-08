import os
import requests
import time

platform = platform.name()

def commandLineInstaller():
  os.system('cls' if os.name == 'nt' else 'clear') # Clear Command Line
  print() # Some Text Art
  print("Welcome to IntelliClock!\nThis is the server installer")

# Using name IntelliClock, Not sure if i will keep it
if platform == "nt":
  import tkinter as tk
  from tkinter import ttk
  # Use GUI
  print("Using Tkinter GUI Installer")
  tk.Tk()
else:
  print("Other Platform, if your on windows this is an error. Defaulting to Command Line Installer")
  commandLineInstaller()
