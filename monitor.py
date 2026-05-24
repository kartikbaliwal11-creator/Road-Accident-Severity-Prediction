import os

if os.path.exists("accident_model.pkl"):
    print("Model is available")
else:
    print("Model missing")