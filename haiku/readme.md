## Discord Haiku Bot
This is a Discord bot that generates haikus based on user prompts using the OpenAI GPT-3 API. The bot extracts relevant keywords from the user's prompt using spaCy's natural language processing (NLP) library, and then calls the OpenAI API to generate a haiku based on those keywords.

### Requirements
To use this bot, you will need:

- A Discord account
- A Discord server where you have the "Manage Server" permission to add the bot
- An OpenAI API key (you can sign up for an API key at [https://beta.openai.com/signup/](https://beta.openai.com/signup/))
- Python 3.8 or higher
- The discord and openai Python packages (pip install discord openai)
- The spacy Python package and the en_core_web_sm spaCy model (pip install spacy && python -m spacy download en_core_web_sm)

### Setup
1. Clone this repository or download the code as a ZIP file and extract it to a folder on your computer.

2. In the folder containing the code, create a new file named `.env`.

3. Add the following lines to the `.env` file, replacing `YOUR_API_KEY` with your OpenAI API key and `YOUR_DISCORD_BOT_TOKEN` with your Discord bot token:

```py
OPENAI_API_KEY=YOUR_API_KEY
DISCORD_BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN
```

4. In your Discord server, create a new bot application and invite it to your server by following the steps in the [Discord documentation](https://discord.com/developers/docs/topics/oauth2#bots).

5. Copy the bot token from the "Bot" tab of your bot's application page, and paste it into the `.env` file as `DISCORD_BOT_TOKEN`

6. In the command prompt or terminal, navigate to the folder containing the code and run the following command to start the bot:

```py
python haiku_bot.py
```

7. The bot should now be running and ready to respond to user prompts!

### Usage

To generate a haiku using the bot, send a message in the format `haiku PROMPT` to any text channel where the bot is present, where `PROMPT` is a phrase or sentence that you would like the haiku to be based on. For example:

```py
haiku cherry blossom
```

The bot will extract relevant keywords from the prompt using spaCy, and then generate a haiku based on those keywords using the OpenAI API. The haiku will be posted in the same text channel where the `haiku` command was sent.

### Notes

- The bot will only respond to messages starting with the haiku command. Other messages will be ignored.
- The bot enforces a cooldown period between requests to prevent abuse. By default, the cooldown period is 10 seconds.
- The bot limits the length of the generated haiku to 25 tokens by default, but this can be adjusted by changing the max_tokens parameter in the code.
- The `temperature`, `top_p`, `frequency_penalty`, and `presence_penalty` parameters for the OpenAI API call can be adjusted in the code to fine-tune the quality of the generated haikus. Consult the [OpenAI API documentation](https://beta.openai.com/docs/api-reference/completions/create) for more information on these parameters.

