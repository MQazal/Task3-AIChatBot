from email import message
import openai
import whisper
import speech_recognition as sr

key = "sk-None-Xum7yGxo4Oc1fZN6l02YT3BlbkFJ7LBFdd1oYlGNmExPGOk1"
openai.api_key = key

model = whisper.load_model("tiny")

# speech recognition set-up
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)
r.dynamic_energy_threshold=False
r.energy_threshold = 300

while True:
    with mic as source:
        print("\nListening...")
        r.adjust_for_ambient_noise(source, duration=2)
        audio = r.listen(source)
        try:
            # Save the audio to a file
            with open("audio#1.wav", "wb") as f:
                f.write(audio.get_wav_data())

            # Use Whisper to transcribe the audio file
            result = model.transcribe("audio#1.wav", fp16=False)

            user_input = str(result.get('text', '')).strip()
            print(f"User: {user_input}")

        except Exception as e:
            print(f"Error: {e}")
            continue

    if "thank you" in user_input.lower():
        EndChat_message = "You're welcome! Have a great day!"
        print(f"Bot: {EndChat_message}")
        break

    messages = []
    messages.append({"role": "user", "content": user_input})

    response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.6
        )
    response_content = response.choices[0].message.content
    print(f"Bot: {response_content}")
    messages.append({"role": "assistant", "content": response_content})
