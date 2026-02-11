# Contributing to Hello, Interview!

Thank you for your interest in contributing to **Hello, Interview!** Our goal is to make this repository the gold standard for learning Data Structures and Algorithms (DSA).

By contributing, you are helping fellow developers master the art of problem-solving.

## Project Vision

We aim to provide:
1.  **Unique Conceptual Problems**: Not just a collection of every problem, but those that teach fundamental concepts.
2.  **Clean, Efficient Code**: Solutions that are easy to read and follow best practices — in any language.
3.  **Clear Explanations**: Problems should be accompanied by concise but thorough conceptual explanations.

## Repository Structure

The repo is organized by **topic**, then by **problem**. Each problem has its own directory containing a `README.md` and solution files in one or more languages.

```
<topic>/
├── <problem_name>/
│   ├── README.md          ← problem description, complexity, links
│   ├── solution.py
│   ├── solution.java
│   ├── solution.cpp
│   └── solution.go
└── Readme.md              ← category overview (list of problems)
```

## How to Contribute

### 1. Adding a Solution in a New Language

If a problem already exists but only has solutions in some languages:
- Navigate to the problem directory (e.g., `arrays_and_strings/four_sum/`).
- Add your solution file named `solution.<ext>` (see supported extensions below).
- Update the problem's `README.md` to add your language to the Solutions table.

### 2. Adding a New Problem

- **Directory**: Create a new folder in the appropriate category using `snake_case`, e.g., `arrays_and_strings/two_sum/`.
- **Solution file**: Name it `solution.<ext>` (e.g., `solution.py`, `solution.java`).
- **Problem README**: Create a `README.md` inside the problem folder using the template below.
- **Category README**: Update the category's `Readme.md` to list the new problem with a link.

### 3. Proposing a New Problem
If you have a unique problem that you think belongs here:
- Check if it's already in the repository.
- Create an issue to discuss the problem before implementation (optional but recommended).
- Ensure the problem has a clear title and a link to its source (e.g., LeetCode, HackerRank).

## Problem README Template

Each problem directory should have a `README.md` like this:

```markdown
# Problem Name

**Source**: [link to LeetCode/HackerRank/etc.](https://...)

## Problem Description

Concise description of the problem.

## Solutions

| Language   | File                           |
|------------|--------------------------------|
| Python     | [solution.py](solution.py)     |
| Java       | [solution.java](solution.java) |
| C++        | [solution.cpp](solution.cpp)   |
```

## Supported Languages & Conventions

| Language   | Extension | Style Guide |
|------------|-----------|-------------|
| Python     | `.py`     | PEP 8       |
| Java       | `.java`   | Google Java Style |
| C++        | `.cpp`    | Google C++ Style |
| Go         | `.go`     | `gofmt`     |
| JavaScript | `.js`     | Airbnb Style Guide |
| TypeScript | `.ts`     | Airbnb Style Guide |
| Rust       | `.rs`     | `rustfmt`   |
| C          | `.c`      | K&R Style   |
| Kotlin     | `.kt`     | Kotlin Coding Conventions |
| Swift      | `.swift`  | Swift API Design Guidelines |

> Other languages are welcome too — just use `solution.<ext>` as the filename.

## Coding Standards (All Languages)

- Include **time and space complexity** in comments at the top of the solution.
- Include a docstring/comment at the top with the **problem description and source link**.
- Prioritize **readability and conceptual clarity** over micro-optimizations.
- (Optional) Include driver/test code at the bottom for verification.

## Reporting Bugs

If you find a bug in a solution or an error in a description:
- Open an issue describing the problem.
- Or, even better, submit a PR with the fix!

---

Happy Coding! 🚀
