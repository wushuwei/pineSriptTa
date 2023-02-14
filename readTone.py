import openai
import os

# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define function to get tone of text
def get_tone(text):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=f"Classify the tone of the following text: '{text}'\nTone:",
      temperature=0.5,
      max_tokens=1,
      n = 1,
      stop=None
    )

    return response.choices[0].text.strip()

# Call the get_tone function with the text you want to analyze
text = "This is a positive message."
tone = get_tone(text)
print("The tone of the text is:", tone)
