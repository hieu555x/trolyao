import pyttsx3

robot_mouth = pyttsx3.init()
voices = robot_mouth.getProperty('voices')
robot_mouth.setProperty('voice', voices[1].id)
robot_mouth.say("I will speak this text")
robot_mouth.runAndWait()
