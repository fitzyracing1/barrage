# Barrage Language Specification v1.0

**Status:** Stable  
**Date:** 2026-07-30

## 1. Purpose

Barrage is a plain-language markup format whose only job is to make any code or unfinished program understandable to people who do not program.

It never replaces the original code. It wraps the code with clear everyday explanations.

## 2. Design Goals

- Readable in under 30 seconds by a complete non-programmer
- Never hides or removes the original code
- Uses familiar visual structure (similar to Markdown)
- Forces every technical idea to be explained in ordinary words
- Short, concrete, and practical

## 3. Official Document Structure

A valid Barrage document must contain the following sections in order:

```barrage
# Title

> One-sentence summary written for anyone.

## Purpose
What this code is trying to achieve in everyday language.

## How it works (plain English)
Step-by-step description using only ordinary words.

## Key ideas
- Concept name (simple explanation in parentheses)
- Another concept (simple explanation)

## The actual code
```
[original code or pseudocode goes here exactly as written]
```

## Line-by-line translation
1. first important line → “What this line does in plain English”
2. next line → “What this line does in plain English”
…

## Decisions the program makes
- If this happens → the program does that
- Otherwise → the program does something else

## What a person would notice
How this affects a real person or real situation.

## Current status
Unfinished / Working / Needs review / Ready to share / etc.

## Next possible steps
What could be improved or added later.
```

## 4. Required Rules

1. The original code must always appear inside the “The actual code” section.
2. Every technical term must be explained the first time it appears.
3. Explanations must be written for someone who has never programmed.
4. Keep sections short and concrete — no filler.
5. The document must stand alone; a reader should not need any other context.

## 5. Optional Sections

These may be added when they improve clarity:

- `## Warnings` — things that could go wrong
- `## Who this helps` — the kind of person who benefits
- `## Simple analogy` — a real-world comparison

## 6. File Extension

Recommended file extension: `.barrage` or `.brg`

Plain `.md` is also acceptable when Barrage is embedded inside Markdown.

## 7. Versioning

This is version 1.0 of the Barrage language.  
Future versions will be numbered 1.1, 1.2, 2.0, etc.
