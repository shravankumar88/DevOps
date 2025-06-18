
# Python Basics Notes

---

## 🖥️ INTERPRETER

The **interpreter** uses the source language and converts the program **line by line**. The computer executes each command as it gets interpreted.

---

## ⚙️ Compiler vs Interpreter

| Feature         | Compiler                        | Interpreter                   |
| --------------- | ------------------------------- | ----------------------------- |
| Execution       | Converts entire program at once | Converts line by line         |
| Speed           | Generally faster                | Slower                        |
| Error Detection | After full program compilation  | Line-by-line during execution |
| Examples        | C, C++                          | Python, JavaScript            |

---

## ⚙️ Byte Code in Python

Although Python is called an interpreted language, it uses a **combination of compiling and interpreting**.

- Source code → Compiled to **Byte Code**
- Byte Code: Platform-independent low-level code
- Byte Code is not machine code
- It runs on **PVM (Python Virtual Machine)**

---

## 🚀 Python Features

- Free and open-source
- Easy to learn and code
- Object-Oriented Language
- GUI Programming support
- High-level and extensible
- Portable and integrated
- Dynamically typed
- Large standard library
- Easy to debug

---

## 🧾 Static vs Dynamic Typing

| Language Type     | Example             |
| ----------------- | ------------------- |
| Statically Typed  | `int x = 10;`     |
| Dynamically Typed | `x = 10` (Python) |

---

## 🧱 Core Python Concepts

### 🔁 Function / Method

- A reusable block of code
- Avoids repetition

### 📦 Module

- A Python file containing functions/methods

### 📦 Package

- A collection of modules

### 📚 Library

- A collection of packages

### 🏗 Framework

- A set of libraries with architecture (MVC, MVT)
- Examples: Django, Flask, FastAPI, Pyramid

---

## 🌐 Python Web Frameworks

- Django
- Flask
- FastAPI
- Pyramid
- Tornado
- Sanic
- Dash
- Web2py
- Falcon
- Bottle

---

## 💬 Comments in Python

| Type        | Syntax                         |
| ----------- | ------------------------------ |
| Single-line | `# comment`                  |
| Multi-line  | `'''...'''` or `"""..."""` |

---

## 📦 Variables

- Containers to store data
- Created when assigned for the first time
- Case-sensitive
- Rules:
  - Start with letter or underscore
  - Cannot start with a number
  - Only alphanumeric characters and underscores
  - Cannot use reserved keywords

### Naming Conventions

- `camelCase`
- `snake_case`
- `PascalCase`

---

## 🔠 Data Types

### Numbers

- `int` → 10
- `float` → 12.5
- `complex` → 2 + 3j

### Boolean

- `True`, `False`

### Set

- `{1, 2, 3}`

### Dictionary

- `{1: 'a', 2: 'b'}`

### Sequence Types

- String → `'Hello'`
- List → `[1, 'a', 3.14]`
- Tuple → `(1, 'b', 2.71)`

---

## 🔄 Type Conversions

### 1. Implicit Type Conversion

- Performed by Python automatically
- No data loss

### 2. Explicit Type Conversion (Typecasting)

- Done manually using functions like `int()`, `float()`, `str()`

---

## 📥 Input Function

- `input()` → Takes input as a **string** by default
- Example:
  ```python
  name = input("Enter your name: ")
  ```
