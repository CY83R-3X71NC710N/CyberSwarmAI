

#!/usr/bin/env python
# CY83R-3X71NC710N © 2023

# Import Statements
import os
import sys
import time
import random
import string
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier

# Main Code
# This code will use a combination of Machine Learning models and Natural Language Processing to detect malicious behaviour and flag risks.

# First, we will create a dataset of malicious and non-malicious behaviour.
# We will use a combination of real-world data and simulated data.
# The data will be stored in a CSV file.

# Create a list of malicious behaviour
malicious_behaviour = ["Unauthorized access", "Data theft", "Unauthorized modification", "Unauthorized deletion", "Unauthorized use of resources", "Unauthorized installation of software", "Unauthorized use of system privileges", "Unauthorized use of user accounts", "Unauthorized use of network resources", "Unauthorized use of system services"]

# Create a list of non-malicious behaviour
non_malicious_behaviour = ["Authorized access", "Data sharing", "Authorized modification", "Authorized deletion", "Authorized use of resources", "Authorized installation of software", "Authorized use of system privileges", "Authorized use of user accounts", "Authorized use of network resources", "Authorized use of system services"]

# Create a list of labels
labels = ["Malicious", "Non-Malicious"]

# Create a dataframe with the data
data = {'Behaviour': malicious_behaviour + non_malicious_behaviour, 'Label': labels * 10}
df = pd.DataFrame(data)

# Split the data into training and testing sets
X = df['Behaviour']
y = df['Label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

# Create a list of Machine Learning models
models = [RandomForestClassifier(), SVC(), KNeighborsClassifier(), GaussianNB(), DecisionTreeClassifier(), LogisticRegression(), MLPClassifier()]

# Train the models
for model in models:
    model.fit(X_train, y_train)

# Make predictions
predictions = []
for model in models:
    predictions.append(model.predict(X_test))

# Evaluate the models
for i in range(len(models)):
    print("Model:", models[i])
    print("Accuracy:", accuracy_score(y_test, predictions[i]))
    print("Confusion Matrix:\n", confusion_matrix(y_test, predictions[i]))
    print("Classification Report:\n", classification_report(y_test, predictions[i]))
    print("\n")

# GUI Development
# Create a GUI for the program using Tkinter
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("CyberSwarmAI")
window.geometry("400x400")

# Create a label
label = tk.Label(window, text="Welcome to CyberSwarmAI!")
label.pack()

# Create a text entry box
entry = tk.Entry(window)
entry.pack()

# Create a button
def clicked():
    behaviour = entry.get()
    for model in models:
        prediction = model.predict([behaviour])
        if prediction[0] == "Malicious":
            label.configure(text="Malicious behaviour detected!")
        else:
            label.configure(text="No malicious behaviour detected.")

button = tk.Button(window, text="Check", command=clicked)
button.pack()

# Finishing Touches
# Add a loop to keep the window open
window.mainloop()
