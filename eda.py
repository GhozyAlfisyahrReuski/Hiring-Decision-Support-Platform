import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import shap
from scipy.stats import ttest_ind, chi2_contingency

# Load your dataset
df_raw = pd.read_csv("your_dataset.csv")
df_copy = df_raw.copy()

# ===== QUESTION FUNCTIONS =====
def q1_hired_vs_not_hired():
    counts = df_raw['HiringDecision'].value_counts().sort_index()
    labels = ['Not Hired', 'Hired']
    colors = ['#F44336', '#4CAF50']
    fig, ax = plt.subplots(figsize=(6,6))
    ax.pie(counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90,
           wedgeprops=dict(width=0.4), textprops={'fontsize': 12})
    ax.set_title('Applicants Hired vs Not Hired', fontsize=14)
    st.pyplot(fig)

def q2_avg_candidate_value():
    labels = ["Interview Score", "Skill Score", "Personality Score", "Experience Years", "EducationLevel"]
    stats = [51, 51, 49, 8, 2]
    max_values = [100, 100, 100, 15, 4]
    stats = [s / m * 100 for s, m in zip(stats, max_values)]
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    stats += stats[:1]
    angles += angles[:1]
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, stats, color="blue", linewidth=2)
    ax.fill(angles, stats, color="skyblue", alpha=0.4)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(["20", "40", "60", "80", "100"])
    st.pyplot(fig)

def q3_feature_importance():
    # Assume best_xgb and X are available
    explainer = shap.Explainer(best_xgb, X)
    shap_values = explainer(X)
    shap.summary_plot(shap_values, X)
    st.pyplot(bbox_inches='tight')

def q4_demographics():
    df_copy['Age'] = pd.to_numeric(df_copy['Age'], errors='coerce')
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    sns.boxplot(x="HiringDecision", y="Age", data=df_copy, ax=axes[0])
    gender_prop = pd.crosstab(df_copy['HiringDecision'], df_copy['Gender'], normalize='index')
    gender_prop.plot(kind='bar', stacked=True, color=["#66c2a5", "#fc8d62"], ax=axes[1])
    st.pyplot(fig)

def q5_technical_scores():
    tech_cols = ['SkillScore', 'PersonalityScore', 'InterviewScore']
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))
    for i, col in enumerate(tech_cols):
        if col in df_copy.columns:
            sns.boxplot(data=df_copy, x='HiringDecision', y=col, ax=axs[i])
            axs[i].set_title(f'{col} by Hiring Status')
    st.pyplot(fig)

def q6_recruitment_strategy():
    recruitment_summary = df_copy.groupby('RecruitmentStrategy')['HiringDecision'].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=recruitment_summary.index, y=recruitment_summary.values, ax=ax)
    ax.set_title('Hiring Rate by Recruitment Strategy')
    st.pyplot(fig)

# ===== STREAMLIT APP =====
st.title("Exploratory Data Analysis")

question_map = {
    "1. How many applicants are hired?": q1_hired_vs_not_hired,
    "2. What is the Average candidate value?": q2_avg_candidate_value,
    "3. Which characteristics are most relevant for decision-making?": q3_feature_importance,
    "4. Does applicants demographic status play a role?": q4_demographics,
    "5. How do technical assessment scores differ?": q5_technical_scores,
    "6. Are there recruitment strategies with higher hiring rates?": q6_recruitment_strategy
}

selected_question = st.selectbox("Select an EDA question", list(question_map.keys()))
question_map[selected_question]()  # Run the selected question's function
