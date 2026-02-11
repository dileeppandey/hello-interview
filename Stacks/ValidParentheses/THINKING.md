# Valid Parentheses — First-Principles Thinking Guide

## 1. Understanding the Problem

**Restate**: I have a string of brackets. I need to check that every opening bracket has a matching closing bracket, and they're properly nested (no interleaving).

**Inputs**: String containing only `(){}[]`.
**Output**: Boolean — is the string valid?

**What "valid" means precisely**:
- `"{[]}"` — valid (properly nested)
- `"([)]"` — invalid (interleaved, not nested)
- `"((("` — invalid (unclosed)

## 2. Building Intuition

**Key property**: The most recently opened bracket must be closed first. This is **LIFO** (Last In, First Out) — the core property of a stack.

**Physical analogy**: Think of Russian nesting dolls. You must close the innermost doll before closing any outer ones. If you try to close an outer one while inner ones are still open, it's invalid.

## 3. Brute Force First

**Naive approach**: Repeatedly scan for adjacent matching pairs and remove them: `"([])"` → remove `"[]"` → `"()"` → remove `"()"` → `""` → valid.

**Complexity**: O(n²) — each scan is O(n), and we may need O(n) scans.

## 4. Identifying the Optimization

**Stack approach**: Process left to right. Push opening brackets. When hitting a closing bracket, check if it matches the most recent opening bracket (stack top). If yes, pop; if no, invalid.

**Why stack works**: The stack exactly models the nesting structure. "Most recent opening bracket" = stack top.

## 5. Building the Solution Step-by-Step

```
matching = {')': '(', '}': '{', ']': '['}
stack = []

For each char:
    If closing bracket:
        If stack empty or top doesn't match → False
        Pop the stack
    Else (opening bracket):
        Push to stack

Return stack is empty
```

**Dry-run**: `"{[]}"`
```
'{' → push. stack=['{']
'[' → push. stack=['{','[']
']' → closing, top='[', matches ']' → pop. stack=['{']
'}' → closing, top='{', matches '}' → pop. stack=[]
End: stack empty → True ✓
```

## 6. Complexity Analysis

**Time**: O(n) — single pass through the string.
**Space**: O(n) — stack can hold up to n/2 opening brackets.
