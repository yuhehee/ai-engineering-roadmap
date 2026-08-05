from dotenv import load_dotenv
load_dotenv()

import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=200,
    messages=[
        {"role": "user", "content": "Enplain what a token is in one sentence."}
    ]
)

print(response.content[0].text)
print(f"Input tokens: {response.usage.input_tokens}, Output tokens: {response.usage.output_tokens}")
