# AI Assignment

This repository contains my solution for the AI Engineering Assignment. The project demonstrates token optimization, debugging practices, CI/CD automation, and a sample Python application with automated testing.

---

## Project Structure

```
ai-assignment/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── debugging/
│   └── debugging.md
│
├── token-optimization/
│   ├── optimization.py
│   ├── before.md
│   └── after.md
│
├── sample_app/
│   ├── app.py
│   ├── requirements.txt
│   └── tests/
│       └── test_app.py
│
├── README.md
├── pyproject.toml
├── .flake8
└── uv.lock
```

---

# Part 1 – Token Optimization

## Objective

Reduce unnecessary token usage while preserving response quality.

### Approach

- Removed redundant prompt context.
- Compressed repetitive instructions.
- Reduced unnecessary conversation history.
- Improved prompt efficiency.

### Result

| Metric | Value |
|---------|------:|
| Before | 100000 Tokens |
| After | 28000 Tokens |
| Reduction | **72%** |

---

# Part 2 – Debugging

The debugging section documents common issues encountered during development and how they were resolved.

Examples include:

- Import path issues
- Python module resolution
- Test execution failures
- Linting (Flake8) issues
- CI troubleshooting

Documentation is available in:

```
debugging/debugging.md
```

---

# Part 3 – CI/CD Pipeline

GitHub Actions is used to automate project validation.

Pipeline steps:

- Checkout repository
- Setup Python
- Install uv
- Install dependencies
- Run pytest
- Run Flake8
- Simulated deployment

Workflow location:

```
.github/workflows/ci-cd.yml
```

---

# Sample Python Application

A simple Python application is included for demonstration purposes.

Functions:

- add(a, b)
- subtract(a, b)

Example:

```python
print(add(10, 5))
print(subtract(10, 5))
```

---

# Running the Project

## Clone Repository

```bash
git clone https://github.com/Vibhu2002/ai-assignment.git
```

## Move into Project

```bash
cd ai-assignment
```

## Install Dependencies

```bash
uv sync
```

## Run Tests

```bash
uv run pytest
```

## Run Flake8

```bash
uv run flake8 sample_app
```

---

# Test Results

```
=====================
2 passed in 0.03s
=====================
```

---

# Technologies Used

- Python 3.13
- uv
- Pytest
- Flake8
- Git
- GitHub
- GitHub Actions

---

# Repository

GitHub:

https://github.com/Vibhu2002/ai-assignment

---

# Author

**Vibhanshu Shukla**

GitHub:
https://github.com/Vibhu2002

LinkedIn:
https://www.linkedin.com/in/vibhanshushukla2002/
