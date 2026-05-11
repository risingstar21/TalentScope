# 🎯 TalentScope — Job Market Intelligence Dashboard

An AI-powered dashboard that analyzes 1,23,000+ real LinkedIn job postings to reveal hiring trends, salary insights, and skill gaps — built to help job seekers make data-driven career decisions.

---

## 🚀 Live Demo

> Run locally using Streamlit (see setup below)

---

## 📊 Features

- **Top Cities by Job Count** — See where hiring is hottest across the US
- **Work Type Breakdown** — Full-time vs Contract vs Part-time market split
- **Most In-Demand Job Titles** — Top 15 roles with the highest postings
- **Experience Level Analysis** — Entry level vs Mid-Senior vs Director demand
- **Salary Insights** — Average salary benchmarks by experience level
- **🤖 AI Resume Gap Analyzer** — Paste your resume and get instant AI feedback on missing skills for Data Analyst, AI/ML, and Gen AI roles

---

## 🛠️ Tech Stack

| Layer | Tools Used |
|---|---|
| Data Processing | Python, Pandas, SQLite |
| Visualization | Plotly, Streamlit |
| AI/LLM Layer | OpenRouter API (LLM inference) |
| Dataset | LinkedIn Job Postings 2023-24 (Kaggle, 1.23L+ records) |

---

## ⚙️ Setup & Installation

```bash
# Clone the repository
git clone https://github.com/risingstar21/TalentScope.git
cd TalentScope

# Install dependencies
pip install pandas streamlit plotly openai python-dotenv

# Add your OpenRouter API key
echo "GEMINI_API_KEY=your_openrouter_key_here" > .env

# Run the dashboard
streamlit run app.py
```

---

## 💡 Key Insights from the Data

- **New York** leads with 2,700+ job postings — highest hiring city
- **79.8%** of all jobs are Full-time roles
- **Entry Level** has 36,000+ openings — strong market for freshers
- **Executive roles** average $138K salary vs $8K for internships

---

## 🤖 AI Resume Gap Analyzer

Paste any resume into the dashboard and the AI will instantly return:
- ✅ Top 5 skills you already have
- ❌ Top 5 skills missing based on current market demand
- 💡 One specific suggestion to improve your resume

---

## 📁 Project Structure

TalentScope/
├── app.py          # Main Streamlit dashboard
├── explore.py      # Data exploration scripts
├── .env            # API keys (not pushed to GitHub)
└── archive/        # Dataset files (postings.csv + SQLite DB)

---

## 👤 Author

**Ansh Agrawal**  
B.Tech CSE (Cybersecurity) — Ajeenkya DY Patil University  
[GitHub](https://github.com/risingstar21) | [LinkedIn](https://www.linkedin.com/in/ansh-agrawal2)