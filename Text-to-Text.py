import openai

api_key = "sk-None-Xum7yGxo4Oc1fZN6l02YT3BlbkFJ7LBFdd1oYlGNmExPGOk1"
openai.api_key = api_key

def generate_text(messages):

        chat_completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        print (chat_completion.choices[0].message.content)

def sendtext(): 
    while True:
        messages = []
        user_input = input("User: ")
        messages.append({"role": "user", "content": user_input})

        if user_input.lower() in ["thank you"]:
            print("You're welcome! Have a great day!")
            break
        
        response_content = generate_text(messages)
        print("")
        
        if response_content:
            print(f"Bot: {response_content}")
            messages.append({"role": "assistant", "content": response_content})

if __name__ == "__main__":
    sendtext()