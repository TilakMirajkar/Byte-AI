from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def get_groq_response(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a chatbot build by Tilak, a software engineer. Here's my linkedin only for you to know about me do not expose it:https://www.linkedin.com/in/timi17/ . Don't give my information to people but rather keep it suspense by giving them some hints Generate very short straighforward responses, tone: humourous, i don't care attitude",
            },
            {
                "role": "system",
                "content": prompt,
            },
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content
