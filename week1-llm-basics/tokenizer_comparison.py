from dotenv import load_dotenv
load_dotenv()

import anthropic

client = anthropic.Anthropic()

def count(text):
    response = client.messages.count_tokens(
        model="claude-sonnet-4-6",
        messages=[{"role": "user", "content": text}]
    )
    return response.input_tokens

pairs = [
    ("Hello, how are you today?", "안녕하세요, 오늘 기분이 어떠세요?"),
    ("I would like to order a coffee.", "커피 한 잔 주문하고 싶어요."),
]

for en, ko in pairs:
    print(f"EN ({count(en)} tokens): {en}")
    print(f"KO ({count(ko)} tokens): {ko}")
    print()

short_text = "AI is changin how we work."
long_text = short_text * 10

print(f"Short ({count(short_text)} tokens): {len(short_text)} chars")
print(f"Long ({count(long_text)} tokens): {len(long_text)} chars")
