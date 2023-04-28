import asyncio
import re
import pyttsx3
import vosk
import pyaudio
import json
from EdgeGPT import Chatbot, ConversationStyle

# Initialize pyttsx3 for text-to-speech
text_speech = pyttsx3.init()
voices = text_speech.getProperty('voices')
text_speech.setProperty('voice', voices[0].id)

# Load the Vosk model for speech recognition
model = vosk.Model("D:\\vosk-model-en-in-0.5")
recognizer = vosk.KaldiRecognizer(model, 8000)

# Initialize PyAudio for audio input stream
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=8000, input=True, frames_per_buffer=8000)

async def main():
    bot = Chatbot(cookie_path='D:\\coding\\python_in_hole\\python code\\cookies.json')

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
                    bot_response2 = re.sub('\[\^\d+\^\]', '', bot_response)
                    print("bot's response:", bot_response2)
                    text_speech.say(bot_response2)
                    text_speech.runAndWait()
            break

    await bot.close()

assistant_is_on = True
while assistant_is_on:
    user_choice = input("\ntype 'Y' to ask question and 'exit' to exit the bot: ").lower()
    if user_choice == "y":
        asyncio.run(main())
    elif user_choice == "exit":
        print("Good bye sir. If u Have any other question feel free to ask me again")
        text_speech.say("Good bye sir. If u Have any other question feel free to ask me again")
        text_speech.runAndWait()
        assistant_is_on = False
    else:
        print("you have enetered a wrong input try again, type 'Y' to ask question and 'exit' to exit the bot")

# Clean up
stream.stop_stream()
stream.close()
p.terminate()