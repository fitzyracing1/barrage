# Barrage: documentation overview

Barrage is a plain-language document format (`.barrage`) that wraps real code in everyday explanations so that non-programmers can follow the idea, the flow and the purpose. The repo holds the spec and examples, with no code. (`docs/index.md` is the existing site page and has not been changed.)

| Path | Content |
|---|---|
| `SPEC.md` | Barrage Language Specification v1.0: purpose, goals, document structure, required rules, optional sections, file extension, versioning |
| `examples/reset-and-count.barrage`, `examples/pass-and-go-core.barrage` | examples |
| `docs/index.md` | site page |
| `CONTRIBUTING.md` | contributing |

## Document structure (SPEC.md §3)
`# Title`, then the sections Purpose, How it works (plain English), Key ideas, The actual code, Line-by-line translation, Decisions the program makes, What a person would notice, Current status, and Next possible steps.

## Validating
[barrage-checker](https://github.com/fitzyracing1/barrage-checker) provides `barrage-check file.barrage`.

The repo has no LICENSE file. Copyright (c) 2026 Joshua Almeida
