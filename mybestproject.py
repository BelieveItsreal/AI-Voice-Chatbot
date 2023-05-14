import asyncio
import re
import pyttsx3
import vosk
import pyaudio
import json
import tkinter as tk
from PIL import Image, ImageTk
from EdgeGPT import Chatbot, ConversationStyle

# Initialize pyttsx3 for text-to-speech
text_speech = pyttsx3.init()
voices = text_speech.getProperty('voices')
text_speech.setProperty('voice', voices[0].id)

# Load the Vosk model for speech recognition
model = vosk.Model("vosk-model-en-in-0.5")
recognizer = vosk.KaldiRecognizer(model, 8000)

# Initialize PyAudio for audio input stream
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=8000, input=True, frames_per_buffer=8000)

async def main():
    bot = Chatbot(cookie_path='cookies.json')

    # Speak the prompt out loud
    print("Hello Sir ask you question")
    text_speech.say("Hello Sir ask you question")
    text_speech.runAndWait()

    # Listen for speech input
    while True:
        data = stream.read(8000)
        if len(data) == 0:
            break

        # Recognize speech and use it as input prompt for the chatbot
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result_dict = json.loads(result)
            text = result_dict["text"]
            print("you asked:", text)
            response = await bot.ask(prompt=text, conversation_style=ConversationStyle.creative)
            for message in response["item"]["messages"]:
                if message["author"] == "bot":
                    bot_response = message["text"]
                    bot_response2 = re.sub('\[\^\d+\^\]', '', bot_response)   #type: ignore
                    print("bot's response:", bot_response2)
                    text_speech.say(bot_response2)
                    text_speech.runAndWait()
            break

    await bot.close()

def exit_program():
    print("Good bye sir. If you have any other question feel free to ask me again")
    text_speech.say("Good bye sir. If you have any other question feel free to ask me again")
    text_speech.runAndWait()
    window.quit()

# create the tkinter window
window = tk.Tk()
window.title("Chatbot Assistant")
window.geometry("500x400")

# Set the background image
bg_image = ImageTk.PhotoImage(Image.open("D:\\coding\\python_in_hole\\python code\\bot png\\back.JPG"))
bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# create the UI elements
title_label = tk.Label(window, text="Welcome to Chatbot Assistant", font=("Arial", 20))
title_label.pack(pady=20)

prompt_label = tk.Label(window, text="Tap mic to ask question:", font=("Arial", 14))
prompt_label.pack()

mic_image = ImageTk.PhotoImage(Image.open("D:\\coding\\python_in_hole\\python code\\bot png\\mic.png").resize((50,50)))
ask_button = tk.Button(window, image=mic_image, command=lambda: asyncio.run(main()))
ask_button.pack(pady=10)

mic_label = tk.Label(window, text="Tap Mic To Ask Question", font=("Arial", 12))
mic_label.pack()

exit_image = ImageTk.PhotoImage(Image.open("D:\\coding\\python_in_hole\\python code\\bot png\\exit.png").resize((50,50)))
exit_button = tk.Button(window, image=exit_image, command=exit_program)
exit_button.pack(pady=30)

exit_label = tk.Label(window, text="Tap Icon To Close Bot", font=("Arial", 12))
exit_label.pack()

# run the tkinter event loop
window.mainloop()

# Clean up
stream.stop_stream()
stream.close()
p.terminate()
