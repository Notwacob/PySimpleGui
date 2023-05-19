import PySimpleGUI as sg
import subprocess

# Define the layout for the main window
layout = [[sg.Text("Click the button to run another PySimpleGUI program.")],
          [sg.Button("Converter", expand_x = True, size = (10, 1)), sg.Button("Calculator", expand_x = True, size = (10, 1))],
          [sg.Button("Stopwatch", expand_x = True, size = (10, 1)), sg.Button("Text Editor", expand_x = True, size = (10, 1))],
          [sg.Button("Snake", expand_x = True, size = (10, 1)), sg.Button("Graph App", expand_x = True, size = (10, 1))],
          [sg.Button("Image Editor", expand_x = True, size = (10, 1)), sg.Button("Music Player", expand_x = True, size = (10, 1))],
          [sg.Button("Weather App", expand_x = True, size = (10, 1)), sg.Button("Face Detector", expand_x = True, size = (10, 1))]]

# Create the main window
window = sg.Window("Run PySimpleGUI Programs", layout)

# Event loop for the main window
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Converter":
        # Run the Converter program
        subprocess.Popen(["python", "01_converter/app.py"])

    elif event == "Calculator":
        # Run the Calculator program
        subprocess.Popen(["python", "02_calculator/app.py"])
        
    elif event == "Stopwatch":
        # Run the Stopwatch program
        subprocess.Popen(["python", "03_stopwatch/app.py"])
        
    elif event == "Text Editor":
        # Run the Text Editor program
        subprocess.Popen(["python", "04_text_editor/app.py"])
        
    elif event == "Snake":
        # Run the Snake program
        subprocess.Popen(["python", "05_snake/app.py"])
        
    elif event == "Graph App":
        # Run the Graph App program
        subprocess.Popen(["python", "06_graph_app/app.py"])
    
    elif event == "Image Editor":
        # Run the Image Editor program
        subprocess.Popen(["python", "07_image_editor/app.py"])
        
    elif event == "Music Player":
        # Run the Music Player program
        subprocess.Popen(["python", "08_music_player/app.py"])
        
    elif event == "Weather App":
        # Run the Weather App program
        subprocess.Popen(["python", "09_weather_app/app.py"])
        
    elif event == "Face Detector":
        # Run the Face Detector program
        subprocess.Popen(["python", "10_face_detector/app.py"])

# Close the main window
window.close()
