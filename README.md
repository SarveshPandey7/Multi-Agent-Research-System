# 🔬 Multi-Agent Research System

An AI-powered research application that automates information gathering, web scraping, report generation, and content evaluation using multiple AI agents.

Built using **LangChain, LangGraph, Gemini, Tavily, BeautifulSoup, and Streamlit**.

## 🚀 Features

* **Search Agent:** Finds recent, reliable, and relevant information using web search.
* **Reader Agent:** Identifies relevant URLs and extracts detailed information from web pages.
* **Writer Chain:** Generates structured research reports using the collected information.
* **Critic Chain:** Reviews and evaluates the generated research report.
* **Interactive UI:** A clean Streamlit interface for submitting research topics and viewing results.
* **Report Export:** Download the generated research report.

## 🏗️ Architecture

```text
          User Input
               |
               ▼
         Search Agent
               |
               ▼
         Reader Agent
          (Web Scraping)
               |
               ▼
          Writer Chain
        (Report Generation)
               |
               ▼
          Critic Chain
          (Evaluation)
               |
               ▼
         Final Research
             Report
```

## 🛠️ Tech Stack

* **Language:** Python
* **LLM:** Google Gemini
* **Framework:** LangChain / LangGraph
* **Search:** Tavily API
* **Web Scraping:** BeautifulSoup, Requests
* **Frontend:** Streamlit
* **Environment Management:** Python-dotenv

## 📁 Project Structure

```text
Multi-Agent-Research-System/
│
├── agents.py
├── pipeline.py
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Multi-Agent-Research-System.git
```

### 2. Navigate to the project directory

```bash
cd Multi-Agent-Research-System
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API keys

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Use the environment variable names expected by your application.

### 6. Run the application

```bash
streamlit run app.py
```

## 🔑 API Requirements

This project requires API keys for:

* Google Gemini
* Tavily Search API

## 📌 Future Improvements

* Real-time agent execution status.
* Human-in-the-loop tool approval.
* Improved source verification and citation handling.
* Research report export in PDF format.
* Conversation history and persistent research sessions.

## 👨‍💻 Author

**Sarvesh Pandey**

B.Tech Computer Science Engineering Graduate | AI/ML & Data Science Enthusiast
