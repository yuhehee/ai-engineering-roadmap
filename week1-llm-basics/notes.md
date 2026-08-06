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

- `raw_http_call.sh` — raw HTTP call to the Anthropic Messages API, no SDK,
  to understand the request/response structure directly.
- `sdk_call.py` — minimal Python script (Anthropic SDK) that sends a
  question and prints the response plus token usage.
- `tokenizer_comparison.py` — compares token counts (Korean vs English,
  short vs long text) using the `count_tokens` endpoint.
- `temperature_experiment.py` — same prompt run 5x at temperature 0, 0.3,
  0.7, 1.0, counts unique answers to see variance.

## Notes / gotchas

- Korean uses up to 2x more tokens than English for the same meaning
  (e.g. "Hello, how are you today?" = 15 tokens vs the Korean equivalent
  = 30 tokens). Matters for cost on Korean-language products.
- Concatenating text without spaces changes tokenization — worth
  remembering for chunking strategy later (Week 6).
- Used `count_tokens` endpoint instead of `tiktoken` — tiktoken is
  OpenAI's tokenizer, not Claude's, so it gives wrong numbers. Free,
  no credits used.

- Temperature controls how much low-probability candidates get picked.
  Barely visible when one answer dominates (e.g. "name an animal" → always
  "dog"), but clear when candidates are close in probability (e.g.
  "unusual pet" → hedgehog/axolotl/etc., unique answers went 2→4→5→5 as
  temp went 0→0.3→0.7→1.0).
- Even temperature=0 isn't 100% deterministic — parallel GPU processing
  causes occasional variation, especially between near-tied top candidates.

## Next

Day 4 — context window overflow + error handling.