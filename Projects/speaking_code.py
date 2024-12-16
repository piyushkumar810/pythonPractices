# write a program to pronounce list of name using win32 API. if you are given a list as follows:
import win32com.client as win

# Initialize the TTS engine
speaker = win.Dispatch("SAPI.SpVoice")

list=["pappu", "deeraj", "piyush", "akash", "rahul", "shubham", "swapnil", "aaryan"]

for name in list:
    print(f"speaking: {name}")
    speaker.Speak(name)