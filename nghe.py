import speech_recognition

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Robot: I'm Listening")
    audio = robot_ear.record(mic, duration=2)
    robot_ear.adjust_for_ambient_noise(mic)
try:
    you = robot_ear.recognize_google(audio)
except:
    you = ""

print("You : " + you)
