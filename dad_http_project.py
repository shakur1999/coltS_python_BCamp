import requests
import random

# prompt input topic 
# take that input topic and search the web

input("Let me tell you a joke! Give me a topic: ")
int(input(f"I've got {user_iput} jokes about {user_input}. Here's one: "))

url = ("https://icanhazdadjoke.com/search")
res = requests.get(url,
                    headers= {"accepts": "application/json"},
                    params = {"term": "user_input", "limit": 20}
)