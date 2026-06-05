# Project 1: Rule-Based AI Chatbot (Deterministic Logic Engine)

## 📌 Project Overview

Welcome to the foundation phase of the DecodeLabs AI Engineering Internship (Batch: 2026).

This project implements a Rule-Based AI Chatbot using deterministic programming logic. Instead of machine learning or deep learning models, the chatbot relies on predefined rules and conditional statements to generate responses.

The project demonstrates the fundamentals of Artificial Intelligence by building a conversational system capable of understanding specific user inputs and responding appropriately.

---

## 🏗️ System Architecture (IPO Model)

### Input

* User enters text through the terminal.
* Input may contain uppercase letters, spaces, or different formatting styles.

### Process

1. Accept user input.
2. Normalize text using:

   * `.lower()`
   * `.strip()`
3. Compare input against predefined rules.
4. Identify user intent.
5. Generate the appropriate response.

### Output

* Greeting messages
* Information responses
* Fallback responses for unknown inputs
* Program termination upon exit command

---

## 🛠️ Technologies Used

* Python 3.x
* Conditional Statements
* Loops
* String Manipulation

---

## 🚀 Installation & Setup

### Prerequisites

Install Python 3.8 or higher.

Verify installation:

```bash
python --version
```

### Run the Project

Navigate to the project directory:

```bash
cd project1_chatbot
```

Execute the chatbot:

```bash
python chatbot.py
```

---

## 💻 Features

* Continuous conversation loop
* Input normalization
* Rule-based intent matching
* Unknown query handling
* Clean exit mechanism

---

## 🧪 Verification Test Cases

| Test Case             | Input             | Expected Result    |
| --------------------- | ----------------- | ------------------ |
| Greeting Test         | hello             | Greeting response  |
| Case Sensitivity Test | HeLLo             | Greeting response  |
| Whitespace Test       | hello             | Greeting response  |
| Unknown Query         | quantum computing | Fallback response  |
| Exit Command          | exit              | Program terminates |

---

## 📊 Expected Output

```text
You: hello
Bot: Hello! How can I help you?

You: what is AI?
Bot: Artificial Intelligence is the simulation of human intelligence by machines.

You: exit
Bot: Goodbye!
```

---

## 🎯 Learning Outcomes

This project demonstrates:

* Rule-Based Artificial Intelligence
* String Processing
* Conditional Logic
* Event Loops
* User Interaction Handling

---

## ✅ Requirements Achieved

* [x] Infinite Conversation Loop
* [x] Input Sanitization
* [x] Intent Recognition
* [x] Fallback Handling
* [x] Exit Functionality

---

Developed for DecodeLabs Industrial Training Program (Batch 2026)

Project Milestone 1: Rule-Based AI Chatbot
