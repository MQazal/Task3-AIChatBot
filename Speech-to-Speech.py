from email import message
import openai
import whisper
import pyttsx3
import speech_recognition as sr

key = "sk-None-Xum7yGxo4Oc1fZN6l02YT3BlbkFJ7LBFdd1oYlGNmExPGOk1"
openai.api_key = key

model = whisper.load_model("tiny")

# pyttsx3 setup
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# speech recognition set-up
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)
r.dynamic_energy_threshold=False
r.energy_threshold = 300

while True:
    with mic as source:
        print("\nListening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            # Save the audio to a file
            with open("audio#2.wav", "wb") as f:
                f.write(audio.get_wav_data())

            # Use Whisper to transcribe the audio file
            result = model.transcribe("audio#2.wav", fp16=False)

            # Extract text from the result and ensure it's a string
            user_input = str(result.get('text', '')).strip()
            print(f"User: {user_input}")

        except Exception as e:
            print(f"Error: {e}")
            continue

    if "thank you" in user_input.lower():
        farewell_message = "You're welcome! Have a great day!"
        print(f"Bot: {farewell_message}")
        engine.say(farewell_message)
        engine.runAndWait()
        break

    messages = []
    messages.append({"role": "user", "content": user_input})

    chat_completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.6
        )
    response_content = chat_completion.choices[0].message.content
    print(f"Bot: {response_content}")
    messages.append({"role": "assistant", "content": response_content})

    engine.say(response_content)
    engine.runAndWait()