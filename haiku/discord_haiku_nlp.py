import discord
import openai
import re
import time
import spacy

# initialize the Discord client and OpenAI API key
client = discord.Client()
openai.api_key = "YOUR_API_KEY"

# load the spaCy English language model for NLP
nlp = spacy.load("en_core_web_sm")

# set configurable options for OpenAI API call
engine = "davinci"
temperature = 0.7
max_tokens = 25
top_p = 1
frequency_penalty = 0
presence_penalty = 0

# set a cooldown period between requests to prevent abuse
cooldown_seconds = 10
last_request_time = 0

# log in to Discord
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

# handle incoming messages
@client.event
async def on_message(message):
    global last_request_time

    # ignore messages from the bot itself
    if message.author == client.user:
        return

    # handle messages starting with "haiku "
    if message.content.startswith("haiku "):
        prompt = message.content[6:].strip()

        # validate user input
        if not prompt:
            await message.channel.send("Please provide a prompt for the haiku.")
            return

        # limit requests to once every cooldown period
        current_time = time.time()
        if current_time - last_request_time < cooldown_seconds:
            await message.channel.send("Please wait a few seconds before requesting another haiku.")
            return
        last_request_time = current_time

        try:
            # generate the haiku using the OpenAI API
            haiku = generate_haiku(prompt)
            await message.channel.send(haiku)
        except Exception as e:
            # handle errors gracefully
            await message.channel.send("An error occurred while generating the haiku.")

# generate a haiku using the OpenAI API
def generate_haiku(prompt):
    # use NLP to extract relevant keywords from the user's prompt
    doc = nlp(prompt)
    keywords = [token.text for token in doc if not token.is_stop and not token.is_punct and token.pos_ != "DET"]
    keyword_string = " ".join(keywords)

    # call the OpenAI API to generate a haiku based on the keywords
    response = openai.Completion.create(
        engine=engine,
        prompt=keyword_string,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )

    # clean up the generated haiku and return it
    haiku = response.choices[0].text.strip()
    haiku = re.sub('[^0-9a-zA-Z\n\.\?,!]+', ' ', haiku)
    haiku = re.sub(' +', ' ', haiku)
    haiku = haiku.replace("\n", " ")
    return haiku

# run the bot using your Discord bot token
client.run("YOUR_DISCORD_BOT_TOKEN")
