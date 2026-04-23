# agentic-day1# Agentic Day 1 – Context Handling in LLMs

## 📌 Overview
This project demonstrates a critical concept in building production AI systems:

> LLMs are stateless by default, and context must be explicitly passed.

We show:
- ❌ How naïve string-based invocation breaks context
- ✅ How structured messages fix the problem using conversation history

---

## 📂 Project Structure
agentic-day1/
├── .gitignore
├── requirements.txt
├── README.md
└── app.py



---

## ⚙️ Setup Instructions

1.Clone the repository
```bash
git clone https://github.com/<your-username>/agentic-day1.git
cd agentic-day1


2. Create virtual environment (Python 3.12)
    python3.12 -m venv venv
    source venv/bin/activate     # Windows: venv\Scripts\activate

3. Install dependencies 
    pip install -r requirements.txt 

4. Add environment variables 
Create a .env file: 
    GOOGLE_API_KEY=your_api_key_here


### ▶️ Run the Project 
    python app.py 


## 🧪 What This Demonstrates 
❌ Naïve Invocation (Context Break) 

    resp1 = llm.invoke("We are building an AI system...")
    resp2 = llm.invoke("What are the main risks?") 

    Each call is independent
    LLM does NOT remember previous input
    Leads to:
 

 ✅ Messages API Fix (Context Preserved) 

    messages = [
        SystemMessage(...),
        HumanMessage(...),
        HumanMessage(...)
    ]

    llm.invoke(messages) 

Full conversation history is passed
Model understands context
Produces consistent and relevant output 

**🧠 Key Learning**
    LLMs are stateless
    Context must be explicitly managed