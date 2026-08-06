from dotenv import load_dotenv
load_dotenv()

import anthropic

client = anthropic.Anthropic()

prompt = "Suggest an unusual pet."
temperatures = [0, 0.3, 0.7, 1.0]

for temp in temperatures:
    print(f"--- temperature={temp} ---")
    outputs = []
    for _ in range(5):
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=20,
            temperature=temp,
            messages=[{"role": "user", "content": prompt}]
        )
        outputs.append(response.content[0].text.strip())
    for o in outputs:
        print(o)
    print(f"unique answers: {len(set(outputs))}/5")
    print()
    