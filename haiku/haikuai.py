import openai
import re

openai.api_key = "YOUR_API_KEY"

def generate_haiku(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=25,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    haiku = response.choices[0].text.strip()
    haiku = re.sub('[^0-9a-zA-Z\n\.\?,!]+', ' ', haiku)
    haiku = re.sub(' +', ' ', haiku)
    haiku = haiku.replace("\n", " ")

    return haiku

prompt = "Write a haiku about the ocean."
haiku = generate_haiku(prompt)

print(haiku)
