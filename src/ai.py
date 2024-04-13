# %%
# a function to give summary from serveral contents
# powered by chatgpt gpt-3.5-turbo

# %%
import openai
import os
class ChatApp:
    def __init__(self):
        # Setting the API key to use the OpenAI API
        self.client = openai.Client(api_key='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')
        self.messages = [
            {"role": "system", "content": "You are an assistant skilled in space physics, and you will explain space physics terms based on Wikipedia content input. The input is from the top 10 Wikipedia articles about space physics, separated by the string '|next|'. The first input will be the documents about the term, and you will give definition about the term; the follow up questions furthre questions from the user, and you will answer them based on the input documents. If you don't know the answer, you can say 'I don't know'. Let's start!"},
        ]

    def chat(self, input):
        self.messages.append({"role": "user", "content": input})
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        self.messages.append({"role": "assistant", "content": response.choices[0].message.content})
        return response.choices[0].message.content


