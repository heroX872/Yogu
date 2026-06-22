# 🟡 Yogu Programming Language

**Yogu** is a simple interpreted programming language with its own unique syntax, built in Python.  
Created by [@ItsGabrieloo](https://github.com/ItsGabrieloo)

---

## 🚀 Getting Started

### Requirements
- Python 3.x

### Running Yogu

**Interactive mode (REPL):**
```
cd /storage/emulated/0/Download/.yg
```
python yogu.py
```

---

## 📖 Syntax

### 🖨️ Print — `TXT`
Displays text or a variable on the screen.

```
TXT /"Hello World"\
TXT /variableName\
```

---

### 📦 Declare a Variable — `Ph`
Creates a new variable.

```
Ph 'myVar'
```

---

### ⚙️ Assign / Operate — `Ht`
Assigns a value or performs an operation on a variable.

```
Ht 'myVar=10'
```

---

## ➕ Operators

Yogu uses its own set of operators — different from most languages by design:

| Symbol | Operation      |
|--------|----------------|
| `-`    | Addition       |
| `:`    | Subtraction    |
| `/`    | Multiplication |
| `\|`   | Division       |

### Examples:

```
Ph 'x'
Ht 'x=5-3'
TXT /x\
```
> Output: `8`  *(5 + 3)*

```
Ph 'y'
Ht 'y=10/2'
TXT /y\
```
> Output: `20`  *(10 × 2)*

---

## 💬 Comments

Use `##` to write comments. They are ignored by the interpreter.

```
## This is a comment
TXT /"Yogu is cool"\
```

---

## 📄 Full Example

```
## My first Yogu program

Ph 'num'
Ht 'num=4/5'
TXT /"Result:"\
TXT /num\
```

**Output:**
```
Result:
20
```

---

## 📁 File Extension

Yogu files use the `.yg` extension.

---

## 🛠️ Status

Yogu is in early development. More features coming soon:
- Conditionals
- Loops
- Functions

---

## 📜 License

MIT License — free to use and modify.

---

> Made with 💛 by [@ItsGabrieloo](https://github.com/ItsGabrieloo)
