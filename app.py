import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.set_page_config(page_title="TalentScope", page_icon="🎯", layout="wide")
st.title("🎯 TalentScope — Job Market Intelligence Dashboard")
st.markdown("Real insights from 1,23,000+ LinkedIn job postings")

conn = sqlite3.connect("talentscope.db")

# --- Section 1: Top Cities ---
st.subheader("📍 Top 10 Cities by Job Count")
df_cities = pd.read_sql("""
    SELECT location, COUNT(*) as job_count 
    FROM jobs 
    WHERE location != 'United States'
    GROUP BY location 
    ORDER BY job_count DESC 
    LIMIT 10
""", conn)
fig1 = px.bar(df_cities, x='location', y='job_count', color='job_count',
              color_continuous_scale='Blues')
st.plotly_chart(fig1, use_container_width=True)

# --- Section 2: Work Type ---
st.subheader("💼 Full-time vs Contract vs Part-time")
df_work = pd.read_sql("""
    SELECT formatted_work_type as work_type, COUNT(*) as count
    FROM jobs
    WHERE formatted_work_type IS NOT NULL
    GROUP BY formatted_work_type
    ORDER BY count DESC
""", conn)
fig2 = px.pie(df_work, values='count', names='work_type',
              color_discrete_sequence=px.colors.sequential.Blues_r)
st.plotly_chart(fig2, use_container_width=True)

# --- Section 3: Top Job Titles ---
st.subheader("🏆 Top 15 Most In-Demand Job Titles")
df_titles = pd.read_sql("""
    SELECT title, COUNT(*) as job_count
    FROM jobs
    WHERE title IS NOT NULL
    GROUP BY title
    ORDER BY job_count DESC
    LIMIT 15
""", conn)
fig3 = px.bar(df_titles, x='job_count', y='title', orientation='h',
              color='job_count', color_continuous_scale='Teal')
fig3.update_layout(yaxis={'categoryorder': 'total ascending'})
st.plotly_chart(fig3, use_container_width=True)

# --- Section 4: Experience Level ---
st.subheader("📊 Jobs by Experience Level")
df_exp = pd.read_sql("""
    SELECT formatted_experience_level as experience, COUNT(*) as count
    FROM jobs
    WHERE formatted_experience_level IS NOT NULL
    GROUP BY formatted_experience_level
    ORDER BY count DESC
""", conn)
fig4 = px.bar(df_exp, x='experience', y='count', color='count',
              color_continuous_scale='Purples')
st.plotly_chart(fig4, use_container_width=True)

# --- Section 5: Salary Insights ---
st.subheader("💰 Average Salary by Experience Level")
df_salary = pd.read_sql("""
    SELECT formatted_experience_level as experience,
           ROUND(AVG(med_salary), 0) as avg_salary
    FROM jobs
    WHERE med_salary IS NOT NULL
    AND formatted_experience_level IS NOT NULL
    GROUP BY formatted_experience_level
    ORDER BY avg_salary DESC
""", conn)
fig5 = px.bar(df_salary, x='experience', y='avg_salary', color='avg_salary',
              color_continuous_scale='Greens')
st.plotly_chart(fig5, use_container_width=True)

conn.close()

# --- Section 6: AI Resume Gap Analyzer ---
st.divider()
st.subheader("🤖 AI Resume Gap Analyzer")
st.markdown("Apna resume paste karo — AI batayega job market ke hisaab se kya missing hai!")

resume_text = st.text_area("Resume yahan paste karo:", height=300,
                            placeholder="Paste your resume text here...")

if st.button("🔍 Analyze My Resume"):
    if resume_text.strip() == "":
        st.warning("Pehle resume paste karo!")
    else:
        with st.spinner("AI analyze kar raha hai..."):
            client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=os.getenv("GEMINI_API_KEY"),
            )
            prompt = f"""
You are a job market expert. Analyze this resume and tell:
1. Top 5 skills this person has
2. Top 5 skills MISSING based on current job market demand (Data Analyst, AI/ML, Gen AI roles)
3. One specific suggestion to improve this resume

Keep response concise and actionable. Use bullet points.

Resume:
{resume_text}
"""
            response = client.chat.completions.create(
                model="openrouter/auto",
                messages=[{"role": "user", "content": prompt}]
            )
            st.markdown("### 📋 AI Analysis:")
            st.markdown(response.choices[0].message.content)