import pyttsx3
import speech_recognition
from datetime import date, datetime
import wikipedia
import os
import time
# Khởi tạo các biến
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
# Đặt tốc độ giọng nói
robot_mouth.setProperty('rate', 115)
# Đặt lời phụ nữ
voices = robot_mouth.getProperty('voices')
robot_mouth.setProperty('voice', voices[1].id)
# Phần nghe
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.record(mic, duration=3)
        robot_ear.adjust_for_ambient_noise(mic)

    print("Robot:...")

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    # Phần hiểu
    print("You : " + you)

    if you == "hello" or you == "hi":
        robot_brain = "Hello Hieu"
    elif you == "":
        robot_brain = "I can't hear you, please try again"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B, %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "bye" in you or "end" in you:
        robot_brain = "Good bye"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    elif "american" in you or "president" in you:
        robot_brain = "Searching, please wait..."
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        robot_brain = wikipedia.summary("Donald Trump", sentences=2)
    elif "app" in you:
        print("Robot: Openning, please wait...")
        robot_mouth.say("Openning, please wait...")
        os.startfile(
            'C:\\Users\SPADE\AppData\Local\CocCoc\Browser\Application\browser.exe')
    elif "music" in you:
        robot_brain = "Openning... Please wait"
        music_dir = 'C:\\Users\SPADE\Downloads\Music'          # thư mục để nhạc
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
    elif "search" in you or "Wikipedia" in you:
        print("Robot: What are you looking for?")
        robot_mouth.say("What are you looking for")
        robot_mouth.runAndWait()
        with speech_recognition.Microphone() as mic:
            print("Robot: I'm Listening")
            audio = robot_ear.record(mic, duration=3)
            robot_ear.adjust_for_ambient_noise(mic)
        try:
            you = robot_ear.recognize_google(audio)
        except:
            you = ""
        print("You : " + you)
        robot_brain = "Searching, please wait..."
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        robot_brain = wikipedia.summary(you, sentences=2)
    elif "game" in you:
        print("Robot:Openning game, please wait")
        robot_mouth.say("Openning game, please wait")
        robot_mouth.runAndWait()
        os.startfile('"D:\\Games\Sekiro Shadows Die Twice\sekiro.exe"')
        break
    elif "Wait" in you:
        print("Robot:I'm waitting")
        robot_mouth.say("I'm waitting")
        robot_mouth.runAndWait()
        time.sleep(20)
    else:
        robot_brain = "I'm not understand, please try again"

    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
