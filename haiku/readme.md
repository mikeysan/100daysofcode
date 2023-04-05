# What is this about?

In this script, we use the OpenAI API to generate a haiku based on a prompt that you provide. 

We use the davinci language model (or newer) to generate the haiku, and we set some parameters to control the output.

##### Code explained

The `generate_haiku function` takes a prompt as input and returns a haiku as a string.

We also use regular expressions to clean up the haiku and remove any unwanted characters.

#### How to use

To use this script, you'll need to replace `YOUR_API_KEY` with your actual OpenAI API key.

You can get an API key by signing up for the OpenAI API at https://openai.com/signup/. 

Once you have your API key, you can run the script and provide a "prompt" to generate a haiku.

The prompt could be something like "Write a Haiku about fish".

##### On Windows 

Open a terminal and type `python haikuai.py "Write a haiku fish."`
 
