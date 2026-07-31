# Barrage

**Barrage** is a plain-language format designed to make any code or unfinished program understandable to people who do not program.

It wraps real code with clear everyday explanations so that a complete non-programmer can still grasp the idea, the flow, and the purpose.

## Why Barrage exists

Most code is written only for other programmers.  
Barrage exists so that **anyone** can read and understand what a piece of code is trying to do.

## Quick Example

```barrage
# Reset and Count

> This small logic keeps a number from going too low and counts how many times the check has run.

## Purpose
Stop an important number from becoming invalid, and keep a running total of how many times the safety check has happened.

## How it works (plain English)
The program looks at a number called n.  
If that number is zero or lower, it forces the number back to exactly zero.  
After the check, it increases a separate counter by one.

## Key ideas
- Guard (a safety check that protects a value)
- Counter (a simple tally that goes up by one each time)

## The actual code
```
if (n <= 0) {
    n = 0;
}
i = i + 1;
```

## Line-by-line translation
1. `if (n <= 0)` → “Check whether the number is zero or negative.”
2. `n = 0;` → “If it is, set the number to zero.”
3. `i = i + 1;` → “Add one to the counter.”

## Decisions the program makes
- If n is zero or lower → force it to zero
- If n is already positive → leave it alone
- Always increase the counter after the check

## What a person would notice
The system quietly protects an important value and keeps a record of how many times it has done so.

## Current status
Unfinished core logic – ready for review or further development.

## Next possible steps
- Record the time of each reset
- Set a maximum limit on the counter
- Notify someone when a reset occurs
```

## Official Specification

See [SPEC.md](SPEC.md) for the complete language definition (v1.0).

## Tools

- `tools/check_barrage.py` — simple checker that validates a Barrage document structure

## Status

Barrage is at **Level 5 readiness**:
- Specification written
- Public repository structure ready
- Examples included
- Checker tool included
- Contribution guidelines included

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Barrage language specification and examples are released under the MIT License.
