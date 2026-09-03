# 🤖 AI Data Analysis Crew

An AI-powered **multi-agent data analysis system built with CrewAI** that uses Retrieval-Augmented Generation (RAG) to research customer purchasing behavior and transform retrieved information into a structured business analysis report.

## 🚀 Overview

This project demonstrates how multiple specialized AI agents can collaborate on a data analysis task.

The system uses a **Customer Behavior Data Researcher** to retrieve relevant information from a knowledge base using a RAG tool. A **Customer Behavior Reporting Analyst** then reviews those findings and produces a structured report containing key findings, purchasing patterns, business insights, and practical recommendations.

The workflow is designed to keep conclusions grounded in the information retrieved from the knowledge base rather than allowing the agents to invent unsupported facts.

## 🧠 How It Works

```text
┌──────────────────────────────────┐
│     Customer Behavior Data       │
│       customer_behavior.csv      │
└────────────────┬─────────────────┘
                 │
                 ▼
┌──────────────────────────────────┐
│       RAG Knowledge Base         │
│          dataset_info.txt        │
└────────────────┬─────────────────┘
                 │
                 ▼
┌──────────────────────────────────┐
│  🔎 Customer Behavior Data       │
│        Researcher Agent          │
│                                  │
│  Retrieves relevant information  │
│  and identifies patterns and     │
│  relationships                   │
└────────────────┬─────────────────┘
                 │
                 ▼
┌──────────────────────────────────┐
│  📊 Customer Behavior Reporting  │
│          Analyst Agent           │
│                                  │
│  Analyzes findings and produces  │
│  business insights &             │
│  recommendations                 │
└────────────────┬─────────────────┘
                 │
                 ▼
┌──────────────────────────────────┐
│          📄 report.md            │
│     Structured Analysis Report   │
└──────────────────────────────────┘
```

## 🤖 AI Agents

### 1. Customer Behavior Data Researcher

**Role:** Data Researcher

The researcher agent uses the RAG tool to retrieve relevant information from the customer behavior knowledge base.

Its responsibilities include:

* Retrieving relevant customer purchasing information
* Identifying important purchasing patterns
* Finding relevant factors and relationships
* Grounding findings in the available knowledge base
* Avoiding unsupported or invented facts

### 2. Customer Behavior Reporting Analyst

**Role:** Reporting Analyst

The reporting analyst receives the research findings and converts them into a clear business-oriented report.

Its responsibilities include:

* Reviewing the research findings
* Identifying key purchasing patterns
* Analyzing important factors
* Highlighting potential relationships between customer characteristics and behavior
* Developing business insights
* Providing practical recommendations
* Clearly distinguishing observations from recommendations

## 📋 Report Output

The final report is generated in Markdown format and contains:

1. **Executive Summary**
2. **Key Findings**
3. **Customer Purchasing Patterns**
4. **Important Factors**
5. **Business Insights**
6. **Recommendations**
7. **Conclusion**

The generated report is saved as:

```text
report.md
```

## 📂 Project Structure

```text
ai_data_analysis_crew/
│
├── knowledge/
│   ├── customer_behavior.csv
│   └── dataset_info.txt
│
├── src/
│   └── ai_data_analysis_crew/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       │
│       ├── tools/
│       │   ├── __init__.py
│       │   └── custom_tool.py
│       │
│       ├── crew.py
│       ├── main.py
│       └── __init__.py
│
├── tests/
├── AGENTS.md
├── pyproject.toml
├── report.md
├── uv.lock
├── .gitignore
└── README.md
```

## 🔧 Technologies

* **Python**
* **CrewAI**
* **Retrieval-Augmented Generation (RAG)**
* **YAML**
* **UV**
* **LLM API**
* **Git & GitHub**

## ⚙️ Installation

Make sure you have **Python 3.10 to 3.13** installed.

### 1. Clone the repository

```bash
git clone https://github.com/FabihaLaeeq/CrewAI-data-analysis.git
cd CrewAI-data-analysis
```

### 2. Install UV

If UV is not already installed:

```bash
pip install uv
```

### 3. Install project dependencies

```bash
crewai install
```

## 🔑 API Configuration

Create a `.env` file in the project root and add your API key:

```env
OPENAI_API_KEY=your_api_key_here
```

**Never commit your `.env` file or expose your API key publicly.**

## ▶️ Running the Project

From the project root, run:

```bash
crewai run
```

The CrewAI workflow will execute the configured agents and tasks.

After execution, the generated analysis can be found in:

```text
report.md
```

## 📚 Knowledge Base

The project contains a customer behavior dataset and supporting dataset information:

```text
knowledge/
├── customer_behavior.csv
└── dataset_info.txt
```

The RAG workflow uses the available knowledge to retrieve information relevant to customer purchasing behavior.

## 🎯 Key Learning Outcomes

This project demonstrates practical experience with:

* Multi-agent AI architecture
* CrewAI agent orchestration
* RAG-based information retrieval
* Agent roles and backstories
* Task-based AI workflows
* YAML configuration
* Knowledge bases
* Grounded AI analysis
* Automated business reporting
* AI-generated recommendations

## 🔄 Agent Workflow

The project follows a sequential workflow:

**Research → Analyze → Report**

The first agent focuses on retrieving and identifying relevant information. The second agent uses those findings to create a structured business report.

This separation of responsibilities demonstrates how specialized agents can work together rather than relying on a single general-purpose agent.

## 👩‍💻 Author

**Fabiha Laeeq**

A practical project exploring **Agentic AI, CrewAI, RAG, and AI-powered data analysis**.

## ⭐ Acknowledgements

Built using [CrewAI](https://crewai.com/), an open-source framework for orchestrating role-playing, autonomous AI agents.
