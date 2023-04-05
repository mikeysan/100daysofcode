import discord
import openai
import re
import time
import spacy

client = discord.Client()
openai.api_key = "YOUR_API_KEY"
nlp = spacy.load("en_core_web_sm")

# configurable options
engine = "davinci"
temperature = 0.7
max_tokens = 25
top_p = 1
frequency_penalty = 0
presence_penalty = 0
cooldown_seconds = 10

last_request_time = 0

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    global last_request_time

    if message.author == client.user:
        return

    if message.content.startswith("haiku "):
        prompt = message.content[6:].strip()

        # input validation
        if not prompt:
            await message.channel.send("Please provide a prompt for the haiku.")
            return

        # rate limiting
        current_time = time.time()
        if current_time - last_request_time < cooldown_seconds:
            await message.channel.send("Please wait a few seconds before requesting another haiku.")
            return
        last_request_time = current_time

        try:
            haiku = generate_haiku(prompt)
            await message.channel.send(haiku)
        except Exception as e:
            await message.channel.send("An error occurred while generating the haiku.")

def generate_haiku(prompt):
    doc = nlp(prompt)
    keywords = [token.text for token in doc if not token.is_stop and not token.is_punct and token.pos_ != "DET"]
    keyword_string = " ".join(keywords)

    response = openai.Completion.create(
        engine=engine,
        prompt=keyword_string,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )

    haiku = response.choices[0].text.strip()
    haiku = re.sub('[^0-9a-zA-Z\n\.\?,!]+', ' ', haiku)
    haiku = re.sub(' +', ' ', haiku)
    haiku = haiku.replace("\n", " ")

    return haiku

client.run("YOUR_DISCORD_BOT_TOKEN")
