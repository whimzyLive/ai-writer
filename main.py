#!/usr/bin/env python3

import os
import openai
openai.api_type = "azure"
openai.api_base = "https://personal-blog-writer.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = os.getenv("OPENAI_API_KEY")

# defining a function to create the prompt from the system message and the messages
def create_prompt(system_message, messages):
    prompt = system_message
    message_template = "\n<|im_start|>{}\n{}\n<|im_end|>"
    for message in messages:
        prompt += message_template.format(message['sender'], message['text'])
    prompt += "\n<|im_start|>assistant\n"
    return prompt

# defining the system message
system_message_template = "<|im_start|>system\n{}\n<|im_end|>"
system_message = system_message_template.format("You are a computer science professor writing blogs to teach students and graduate developers about the new technologies and how to use them in simple terms with examples.")

# creating a list of messages to track the conversation
messages = [{"sender":"user","text":
             """Write a blog post on nextjs fundamentals
- use github flavoured markdown
- add code examples
- add charts/diagrams
- add detailed explanation on each technical topic
- add code examples
Include topics-
Page - used for based routing (page.js)  
Link - used to auto prefetch content and provide client side navigation with serverside routing  
Layout - Page and folder based layout sharing (layout.js)  
Fonts - Automatically hosts and serves fonts (load fonts from @next/font/{google|local})  
Style - Scopes the styles to nested page  
Global Style - global style need to be imported to global layout file  
Image - Built in size optimization, visual stability  
Static Data Fetching - Used for static site generation (default fetch api in next caches response)  
Dynamic Data Fetching - used with "cache - no-store" option on fetch api"""}]
response = openai.Completion.create(
  engine="test",
  prompt= create_prompt(system_message, messages),
  temperature=1,
  max_tokens=3200,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["<|im_end|>"])

f = open(".tmp/blog.md", 'w')

f.write(response.choices[0].text)
