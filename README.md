# AI-Voice-Assistant-Chatbot
_This project is a chatbot assistant that can answer questions from speech input using EdgeGPT, a powerful natural language generation model. The chatbot can communicate in a creative and engaging way, and also use Bing search results to provide factual information. The chatbot uses the following technologies:_

## To run this project, you need to install the following library functions:

- **Pyttsx3** for text-to-speech synthesis. You can install it using the command `pip install pyttsx3`.
- **Vosk** for speech recognition. You can install it using the command `pip install vosk`. You also need to download the Vosk model for Indian English from [https://alphacephei.com/vosk/] and place it in your project folder.
- **PyAudio** for audio input stream. You can install it using the command `pip install pyaudio`.
- **Tkinter** for graphical user interface. You can install it using the command `pip install tk`.
- **PIL** for image manipulation. You can install it using the command `pip install pillow`.
- **Asyncio** is a Python library that enables you to write concurrent code with the async/await syntax. You can install it using the command `pip install asyncio`.
- **EdgeGPT** for natural language generation. You can install it using the command `pip install edgegpt`.
- **Re** is a Python library for working with regular expressions, which are patterns of characters that can be used to manipulate text. You can use re to create, search, replace, or split strings using various functions, methods, and special characters. You can install it using the command `pip install re`.

These are the library functions you need to install for this project. I hope this helps you. 😊

## The chatbot works as follows:

- When the program is run, a tkinter window is created with a title, a prompt, a microphone button, an exit button, and some labels.
- The chatbot speaks the prompt "Hello Sir ask you question" using pyttsx3 and waits for the user to tap the microphone button.
- When the user taps the microphone button, PyAudio starts recording the audio data from the microphone and passes it to Vosk for speech recognition.
- When Vosk recognizes the speech input, it returns a JSON string with the text of the input. The chatbot prints the input text on the console and uses it as a prompt for EdgeGPT.
- EdgeGPT generates a response based on the input text using its natural language generation model and also directly connected to web-results so the accuracy is much better. The response is a JSON string with a list of messages, each with an author and a text attribute. The chatbot filters out the messages with author "bot" and prints them on the console. It also removes any citation marks from the messages and speaks them out loud using pyttsx3.
- The chatbot then waits for another speech input from the user or an exit command from the exit button.
- When the user taps the exit button, PyAudio stops recording and closes the stream. The chatbot speaks "Good bye sir. If you have any other question feel free to ask me again" using pyttsx3 and closes the tkinter window.
