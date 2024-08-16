# Task3-AIChatBot

In this Assignment 3 of the Agile Methods exercise, I built a ChatBot AI with Python and the OpenAI API to help me talk to chatgpt locally in my development environment, so I made 6 models from it to do different tasks.

Firstly, I make sure that I have an activated virtual enviroment in Pyhton to install the necessary libraries for each task to be worked successfuly, and this is made by these 2 terminal commands:
#python -m venv VirtualEnviromentName to make it and #VirtualEnviromentName/Scripts/activate to activate it.

(print_text.py)
I start coding each task, so first one is about writing any string as normal sentence or question and run the code to print the goal from it and here I installed OpenAI library which is used in project to send the transcribed text to OpenAI’s language model (like GPT-3.5) for generating responses by #pip install openai, then I need to setup the API key to access to openai chatgpt service by
#setx OPENAI_API_KEY "keynumber".

(Text-to-Text.py)
The second one is about the serious starting with having a real chat with AI modle which is ("gpt-3.5-turbo") and here I didn't use any library, just define the model and how the text message will be sended
between User and Bot along with OpenAI library process.

(Text-to-Speech.py)
Third, I start by researching how to convert a user's text message into an AI-powered speech response, to do this task I installed pyttsx3 which is a text-to-speech conversion library by #pip install pyttsx3 along with OpenAI library process.

(Speech-to-Text.py)
This time I reversed the functionality by letting me talk to the bot and it responds to me via text message, so here I need to machine learning library which converts my voice along audio file to text
, so to achive this requirement, the Whisper AI is installed and it is an open-source automatic speech recognition (ASR) system developed by OpenAI to convert spoken language into written text, making it a powerful tool for transcription, voice-controlled application.
But here the process of installing it takes me a very long time because I installed other libraries with it:
1-OpenAI version: 1.40.2:
While not directly related to Whisper, the OpenAI library is used in your project to send the transcribed text to OpenAI’s language model (like GPT-3.5) for generating responses
2-PyTorch version: 2.2.0+cpu
It is a deep learning framework that is widely used for building and deploying machine learning models and Whisper is built on top of PyTorch to provide the necessary computational backend for running Whisper models like "tiny" model which I used in the code along with the +cpu indicates that you are using the CPU version of PyTorch, which means it's optimized to run on computer's CPU not GPU.
3-Chocolatey version: 2.3.0:
It was likely used to install FFmpeg or other dependencies on my Windows machine.
4-FFmpeg version: 7.0.2:
It is a versatile multimedia processing tool that can handle audio and video files, converting between different formats, and performing various transformations.
5- speech_recognition: This library is designed to recognize speech through user computer's microphone or from an audio file.

(Speech-to-Speech.py):
In this task, I used a speech recognition library to send a voice message from my side, and the pyttsx3 library will allow the robot to send a voice response.

(Speech-to-Text and Text-to-Speech integration) ==> (Tts-StT.py):
Here the same libraries are used but with the condition of determing which chat style is going to be used (text or voice).
