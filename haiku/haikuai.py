import openai
import re
import sys

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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a prompt as an argument.")
        sys.exit(1)

    prompt = sys.argv[1]
    haiku = generate_haiku(prompt)

    print(haiku)
