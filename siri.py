import pyttsx3
import speech_recognition
from datetime import date, datetime
import wikipedia
import os
import time
import webbrowser
from gtts import gTTS
import playsound

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
        print("Robot:Tôi đang nghe đây")
        audio = robot_ear.record(mic, duration=3)
        robot_ear.adjust_for_ambient_noise(mic)

    print("Robot:Chờ não load tý nha <3")

    try:
        you = robot_ear.recognize_google(audio,language="vi-VI")
    except:
        you = ""
    # Phần hiểu
    print("You : " + you)

    if "Chào" in you or "chào" in you:
        robot_mouth.setProperty('rate', 115)
        now = datetime.now()
        currentTime = int(now.strftime("%H"))
        if currentTime > 4 and currentTime <= 10:
            robot_brain = "Chào buổi sáng, tôi có thể giúp gì được cho bạn?"
        elif currentTime > 10 and currentTime <=15:
            robot_brain = "Chào buổi chiều, tôi có thể giúp gì được cho bạn?"
        else:
            robot_brain = "Chào buổi tối, tôi có thể giúp gì được cho bạn?"
    elif you == "":
        robot_brain = "Tôi không nghe gì hết á, bạn làm ơn có thể nói lại được không"
    elif "hôm" in you and "nay" in you:
        today = date.today()
        robot_brain = today.strftime("%B, %d, %Y")
    elif "giờ" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H {} %M {} %S {}")
        robot_brain = robot_brain.format("Giờ","Phút","Giây")
    elif "tạm biệt" in you or "Tạm biệt" in you:
        robot_brain = "Chào tạm biệt, chúc bạn một ngày tốt lành nha!!!"
        print("Robot: " + robot_brain)
        robot_brain = gTTS(robot_brain, lang="vi", slow=False)
        robot_brain.save("output.mp3")
        playsound.playsound("output.mp3", True)
        os.remove("output.mp3")
        break
    elif "tổng thống Mỹ" in you or "Tổng thống Mỹ" in you:
        robot_brain = "Đang tìm, chờ xíu nha"
        print("Robot: " + robot_brain)
        robot_brain = gTTS(robot_brain, lang="vi", slow=False)
        robot_brain.save("output.mp3")
        playsound.playsound("output.mp3", True)
        os.remove("output.mp3")
        robot_brain = str(wikipedia.summary("Donald Trump", sentences=2))
        print("Robot:"+robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        robot_brain = ""
    elif "trình duyệt" in you or "Trình duyệt" in you:
        print("Robot:Đang mở nè chờ xíu nha")
        robot_brain = gTTS("Đang mở nè chờ xíu nha", lang="vi", slow=False)
        robot_brain.save("output.mp3")
        playsound.playsound("output.mp3", True)
        os.startfile('C:\\Users\SPADER\Desktop\Coc Coc.lnk')
        os.remove("output.mp3")
        robot_brain = ""
    elif "mở nhạc" in you or "Mở nhạc" in you:
        print("Robot: Đang mở nè chờ chút đi")
        robot_brain = gTTS("Đang mở nè chờ chút đi", lang="vi", slow=False)
        robot_brain.save("output.mp3")
        playsound.playsound("output.mp3", True)
        music_dir = 'C:\\Users\SPADER\Downloads\Music'          # thư mục để nhạc
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
        os.remove("output.mp3")
        robot_brain = ""
    elif "tìm kiếm" in you or "Tìm kiếm" in you:
        print("Robot: Nói cho tôi biết bạn đang tìm kiếm gì")
        robot_brain = gTTS("Nói cho tôi biết bạn đang tìm kiếm gì", lang="vi", slow=False)
        robot_brain.save("output.mp3")
        playsound.playsound("output.mp3", True)
        os.remove("output.mp3")
        with speech_recognition.Microphone() as mic:
            print("Robot: Tôi đang nghe nè")
            audio = robot_ear.record(mic, duration=3)
            robot_ear.adjust_for_ambient_noise(mic)

        print("Robot:...")

        try:
            you = robot_ear.recognize_google(audio,language="vi-VI")
        except:
            you = ""

        print("You : " + you)
        robot_brain = "Đang tìm kiếm chờ chút nha"
        print("Robot: " + robot_brain)
        robot_brain = gTTS("Đang tìm kiếm chờ chút nha", lang="vi", slow=False)
        robot_brain.save("output.mp3")
        playsound.playsound("output.mp3", True)
        os.remove("output.mp3")
        try:
            robot_brain = wikipedia.summary(you, sentences=2)
            print("Robot:"+robot_brain)
            robot_mouth.say(robot_brain)
            robot_mouth.runAndWait()
        except:
            print("Robot:Không tìm thấy bạn ạ")
            robot_brain = gTTS("Không tìm thấy bạn ạ", lang="vi", slow=False)
            robot_brain.save("output.mp3")
            playsound.playsound("output.mp3", True)
            os.remove("output.mp3")
        robot_brain = ""
    elif "facebook" in you or "Facebook" in you:
        print("Robot: Đang mở nè, đợi xíu nha")
        robot_brain = gTTS("Đang mở nè đợi xíu nha", lang="vi", slow=False)
        robot_brain.save("output.mp3")
        playsound.playsound("output.mp3", True)
        os.remove("output.mp3")
        webbrowser.open("https://www.facebook.com/")
        break
    elif "dịch" in you or "Dịch" in you:
        print("Robot: Bạn muốn tôi dịch từ gì?")
        robot_brain = gTTS("Bạn muốn tôi dịch từ gì", lang="vi", slow=False)
        robot_brain.save("output.mp3")
        playsound.playsound("output.mp3", True)
        os.remove("output.mp3")
        with speech_recognition.Microphone() as mic:
            print("Robot: Tôi đang nghe này")
            audio = robot_ear.record(mic, duration=5)
            robot_ear.adjust_for_ambient_noise(mic)

        print("Robot...")

        try:
            you = robot_ear.recognize_google(audio)
        except:
            you = ""
        print("You:" + you)
        print("Robot: Đang dịch nè, đợi tôi xíu")
        robot_brain = gTTS("Đang dịch nè, đợi tôi xíu", lang="vi", slow=False)
        robot_brain.save("output.mp3")
        playsound.playsound("output.mp3", True)
        os.remove("output.mp3")
        Str = ""
        for i in range(0,len(you.split(" "))):
            Str = Str + you.split(" ")[i] + "%20"
        print("Robot: Kết quả nè")
        robot_brain = gTTS("Kết quả nè", lang="vi", slow=False)
        robot_brain.save("output.mp3")
        playsound.playsound("output.mp3", True)
        os.remove("output.mp3")
        webbrowser.open("https://translate.google.com/?hl=vi#view=home&op=translate&sl=auto&tl=vi&text="+Str)
        break
    elif "tìm nhạc" in you or "Tìm nhạc" in you:
        print("Robot: Tên bài hát bạn muốn tìm là gì, nói cho tôi biết được không")
        robot_brain = gTTS("Tên bài hát bạn muốn tìm là gì, nói cho tôi biết được không", lang="vi", slow=False)
        robot_brain.save("output.mp3")
        playsound.playsound("output.mp3", True)
        os.remove("output.mp3")
        with speech_recognition.Microphone() as mic:
            print("Robot: Đang tập trung nghe đây nói đi !!!")
            audio = robot_ear.record(mic, duration=5)
            robot_ear.adjust_for_ambient_noise(mic)

        print("Robot...")

        try:
            you = robot_ear.recognize_google(audio,language="vi-VI")
        except:
            you = ""
        print("You:" + you)
        print("Robot: Đang lục lọi tìm kiếm cho bạn nè, chờ chút đi")
        robot_brain = gTTS("Đang lục lọi tìm kiếm cho bạn nè, chờ chút đi", lang="vi", slow=False)
        robot_brain.save("output.mp3")
        playsound.playsound("output.mp3", True)
        os.remove("output.mp3")
        Str = ""
        for i in range(0, len(you.split(" "))):
            Str = Str + you.split(" ")[i] + "+"
        print("Robot: Xin lỗi đã bắt bạn đợi, kết quả đây nha")
        robot_brain = gTTS("Xin lỗi đã bắt bạn đợi, kết quả đây nha", lang="vi", slow=False)
        robot_brain.save("output.mp3")
        playsound.playsound("output.mp3", True)
        os.remove("output.mp3")
        webbrowser.open("https://zingmp3.vn/tim-kiem/bai-hat.html?q=" + Str)
        break
    elif "YouTube" in you or "youtube" in you:
        print("Robot: Tên cờ líp bạn muốn tìm là gì")
        robot_brain = gTTS("Tên cờ líp bạn muốn tìm là gì", lang="vi", slow=False)
        robot_brain.save("output.mp3")
        playsound.playsound("output.mp3", True)
        os.remove("output.mp3")
        with speech_recognition.Microphone() as mic:
            print("Robot: Nói đi nói đi đừng ngại ngần")
            audio = robot_ear.record(mic, duration=5)
            robot_ear.adjust_for_ambient_noise(mic)

        print("Robot...")

        try:
            you = robot_ear.recognize_google(audio,language="vi-VI")
        except:
            you = ""
        print("You:" + you)
        print("Robot: Đang tìm đang tìm, đang kiếm cho bạn nè")
        robot_brain = gTTS("Đang tìm đang tìm, đang kiếm cho bạn nè", lang="vi", slow=False)
        robot_brain.save("output.mp3")
        playsound.playsound("output.mp3", True)
        os.remove("output.mp3")
        Str = ""
        for i in range(0, len(you.split(" "))):
            Str = Str + you.split(" ")[i] + "+"
        print("Robot: Cảm ơn đã chờ đợi, kết quả của bạn sẽ được hiển thị trên web nha")
        robot_brain = gTTS("Cảm ơn đã chờ đợi, kết quả của bạn sẽ được hiển thị trên web nha", lang="vi", slow=False)
        robot_brain.save("output.mp3")
        playsound.playsound("output.mp3", True)
        os.remove("output.mp3")
        webbrowser.open("https://www.youtube.com/results?search_query=" + Str)
        break
    elif "thư điện tử" in you or "Thư điện tử" in you:
        print("Robot:Đang mở nè, làm gì mà hối thế")
        robot_brain = gTTS("Đang mở nè, làm gì mà hối thế", lang="vi", slow=False)
        robot_brain.save("output.mp3")
        playsound.playsound("output.mp3", True)
        os.remove("output.mp3")
        webbrowser.open("https://mail.google.com/")
        break
    else:
         robot_brain = "Tôi không hiểu bạn đang nói gì, làm ơn có thể nói lại được không"

    if robot_brain != "":
        print("Robot: " + str(robot_brain))
        output = gTTS(robot_brain, lang="vi", slow=False)
        output.save("output.mp3")
        playsound.playsound("output.mp3", True)
        os.remove("output.mp3")