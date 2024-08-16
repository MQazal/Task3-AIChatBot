import openai

api_key = "sk-None-Xum7yGxo4Oc1fZN6l02YT3BlbkFJ7LBFdd1oYlGNmExPGOk1"
openai.api_key = api_key

chat_completion = openai.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "say test is success with emojis!?",
        }
    ],
    model="gpt-3.5-turbo",
)
print (chat_completion.choices[0].message.content)