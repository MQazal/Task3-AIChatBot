import openai
import whisper
import pyttsx3
import speech_recognition as sr

# Set up OpenAI API key
api_key = "sk-None-Xum7yGxo4Oc1fZN6l02YT3BlbkFJ7LBFdd1oYlGNmExPGOk1"
openai.api_key = api_key

# Load the Whisper model
model = whisper.load_model("tiny")

# Set up speech recognition
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)
r.dynamic_energy_threshold = False
r.energy_threshold = 300

# Set up text-to-speech with pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Choose input mode
mode = input("Type 't' for text input or 'v' for voice input: ").strip().lower()

def generate_text(messages):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.6
    )
    return response.choices[0].message.content

while True:
    if mode == 't':
        # Text input mode
        user_input = input("User: ").strip()
    elif mode == 'v':
        # Voice input mode
        with mic as source:
            print("\nListening...")
            r.adjust_for_ambient_noise(source, duration=2)
            audio = r.listen(source)
            try:
                # Save the audio to a file
                with open("audio#3.wav", "wb") as f:
                    f.write(audio.get_wav_data())

                # Use Whisper to transcribe the audio file
                result = model.transcribe("audio#3.wav", fp16=False)
                user_input = str(result.get('text', '')).strip()
                print(f"User: {user_input}")

            except Exception as e:
                print(f"Error: {e}")
                continue
    else:
        print("Invalid input. Please restart and choose 't' for text or 'v' for voice.")
        break

    if "thank you" in user_input.lower():
        EndChat_message = "You're welcome! Have a great day!"
        print(f"Bot: {EndChat_message}")
        engine.say(EndChat_message)
        engine.runAndWait()
        break

    messages = [{"role": "user", "content": user_input}]
    response_content = generate_text(messages)
    print(f"Bot: {response_content}")
    engine.say(response_content)
    engine.runAndWait()
    print("")
