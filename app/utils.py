from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def get_groq_response(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content
