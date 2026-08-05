# Week 1 — LLM Basics

## What I learned

- **Tokens**: the smallest unit of text a model processes (often subwords,
  not full words). Korean text tends to use more tokens than English for
  the same meaning, which directly affects cost and context usage.
- **Context window**: the max number of tokens a model can "remember" in a
  single request (prompt + history + response combined).
- **Temperature / Top-p**: control output randomness. Low temperature →
  deterministic, good for code/data extraction. High temperature → more
  varied, good for creative writing.
- **Prompting vs. fine-tuning**: prompting adjusts input only (fast, cheap,
  iterative); fine-tuning retrains the model itself. Out of scope for this
  roadmap — prompting covers most real-world use cases.
- **System / User / Assistant roles**: how chat-based APIs structure
  conversation state and persona.

## What I built

- `curl_example.sh` — raw HTTP call to the Anthropic Messages API, no SDK,
  to understand the request/response structure directly.
- `basic_call.py` — minimal Python script (Anthropic SDK) that sends a
  question and prints the response plus token usage.

## Notes / gotchas

- Korean uses up to 2x more tokens than English for the same meaning
  (e.g. "Hello, how are you today?" = 15 tokens vs the Korean equivalent
  = 30 tokens). Matters for cost on Korean-language products.
- Concatenating text without spaces changes tokenization — worth
  remembering for chunking strategy later (Week 6).
- Used `count_tokens` endpoint instead of `tiktoken` — tiktoken is
  OpenAI's tokenizer, not Claude's, so it gives wrong numbers. Free,
  no credits used.

## Next

Day 3 — temperature/top-p experiment.
