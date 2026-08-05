# Week 1 Checklist — LLM Basics

> Goal: not just "understand tokens/context/temperature" but *see* them
> in action through small hands-on experiments. Each day ends with a
> commit.

---

## Day 1 (Tue) — Core concepts + first API call
- [x] Read: tokens, context window, temperature/top-p, prompting vs
      fine-tuning, system/user/assistant roles
- [x] Run: raw curl call to Anthropic Messages API
- [x] Run: `basic_call.py` (Python, <10 lines)
- [x] Commit: `Week 1 Day 1: basic API calls (curl + python)`

## Day 2 (Wed) — Tokenizer deep dive
- [ ] Install `tiktoken` (or equivalent tokenizer lib)
- [ ] Compare token count: same sentence in Korean vs English
- [ ] Compare token count: short sentence vs long paragraph
- [ ] Write up: 2-3 sentence observation (which surprised you, why)
- [ ] Commit: `Week 1 Day 2: tokenizer comparison (ko vs en)`

## Day 3 (Thu) — Temperature / Top-p experiment
- [ ] Same prompt, temperature = 0, 0.3, 0.7, 1.0, 5 calls each
- [ ] Check: how often does temp=0 return the identical output?
- [ ] Check: how varied are outputs at temp=1.0?
- [ ] Commit: `Week 1 Day 3: temperature/top-p experiment`

## Day 4 (Fri) — Context window limits
- [ ] Deliberately send a prompt that exceeds the context window
- [ ] Capture and read the actual error response
- [ ] Note: how would you handle this in production? (preview for Week 3)
- [ ] Commit: `Week 1 Day 4: context window overflow + error handling notes`

## Day 5 (Sat) — Cost calculator
- [ ] Look up current Anthropic pricing (input/output token rates)
- [ ] Write a function: `usage -> estimated cost ($)`
- [ ] Estimate: monthly cost for TickerBell's expected traffic (rough assumption ok)
- [ ] Commit: `Week 1 Day 5: cost calculator`

## Day 6 (Sun) — Mini integration + retro
- [ ] Build: small CLI chatbot combining the above (token count + running cost
      shown live, basic conversation history)
- [ ] Fill in `notes.md` with a real retrospective (what was harder than
      expected, what you'd do differently)
- [ ] Update Progress table in root `README.md` → Week 1 status to ✅
- [ ] Commit: `Week 1 Day 6: mini CLI chatbot + retro`

---

## Done when
- [ ] All 6 days committed separately (visible in git log)
- [ ] `notes.md` reflects actual experience, not just copied concepts
- [ ] You could explain "why Korean uses more tokens" and "temp 0 vs 1"
      to someone else without notes
