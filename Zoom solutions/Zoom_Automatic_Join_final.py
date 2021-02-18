import pyautogui
import time
import webbrowser

MeetingID = input("ID please:-")
Password = input("Password:-")
Time_of_join = input("Put the time u want to join in 24 hr format:-")
TimeRn = time.strftime("%H:%M:%S:-")

while (Time_of_join != TimeRn):
    print("Time is left "+ TimeRn)
    TimeRn = time.strftime("%H:%M:%S")
    time.sleep(1)

if (TimeRn == Time_of_join):
    print("Here we go")
    webbrowser.open("C:\\Users\\RITANKAR\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    time.sleep(13)
    pyautogui.press("Enter")
    time.sleep(4)
    pyautogui.typewrite(MeetingID)
    pyautogui.press("Enter")
    time.sleep(6)
    pyautogui.typewrite(Password)
    pyautogui.press("Enter")
    time.sleep(6)
    pyautogui.press("Enter")

    
    