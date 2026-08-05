curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d '{
        "model": "claude-sonnet-4-6",
        "max_tokens": 200,
        "messages": [
            {"role": "user", "content": "Explain what a token is in one sentence."}
        ]
    }'
    