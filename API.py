# Supporting file for API

import os
import anthropic
import apikey
from IPython.display import Markdown, display
from anthropic import HUMAN_PROMPT, AI_PROMPT


client = anthropic.Anthropic(
    api_key=apikey.api_key,
)

Prompt = "Write the Go code for the simple data analysis."
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": Prompt}
    ]
)

response_text = message.content[0].text

print(response_text)

