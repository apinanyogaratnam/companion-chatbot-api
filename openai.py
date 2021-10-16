import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

response = openai.Completion.create(
  engine="davinci",
  prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I feel sad\nAI: Does anything happen to you?\nHuman: yeah I love someone\nAI: What's the name of the person you love?\nHuman: Atlantaaaaaa\nAI: You like Atlanta?\nHuman: My bestieee\nAI: Does Atlanta love you?\nHuman: He didn't tell me yet lol\nAI: Do you think he will love you?\nHuman: \nAI: What do you want to tell him?\nHuman: ",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=["\n", " Human:", " AI:"]
)
