import openai
import pyttsx3

api_key = "sk-None-Xum7yGxo4Oc1fZN6l02YT3BlbkFJ7LBFdd1oYlGNmExPGOk1"
openai.api_key = api_key

# pyttsx3 setup
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

while True:
    def generate_text(messages):
        response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.6
    )
        return response.choices[0].message.content
    
    user_input = input("User: ")
    
    if "thank you" in user_input.lower():
        EndChat_message = "You are welcome! Have a great day!"
        print(f"Bot: {EndChat_message}")
        engine.say(EndChat_message)
        engine.runAndWait()
        break

    messages = []
    messages.append({"role": "user", "content": user_input})

    response_content = generate_text(messages)
    print(f"Bot: {response_content}")
    messages.append({"role": "assistant", "content": response_content})
    
    engine.say(response_content)
    engine.runAndWait()

    print("")