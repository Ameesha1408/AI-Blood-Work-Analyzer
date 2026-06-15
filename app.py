from dotenv import load_dotenv
import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# ---------------------------------------------------
# LOAD ENV
# ---------------------------------------------------
load_dotenv(
    r"C:\Users\ANEESHA\Desktop\AgenticAI-Tutorial\simple_llm_calling\.env"
)

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Blood Work Analyzer",
    page_icon="🩺",
    layout="wide"
)

# ---------------------------------------------------
# GEMINI MODEL
# ---------------------------------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #fef9ff 0%,
        #eff6ff 25%,
        #ecfeff 50%,
        #f0fdf4 75%,
        #fff7ed 100%
    );
}

/* Main Title */
.main-title{
    text-align:center;
    font-size:3.5rem;
    font-weight:900;
    background:linear-gradient(
        90deg,
        #2563eb,
        #06b6d4,
        #10b981,
        #f59e0b,
        #ec4899
    );
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:10px;
}

/* Subtitle */
.subtitle{
    text-align:center;
    color:#475569;
    font-size:1.05rem;
    margin-bottom:25px;
}

/* KPI Cards */
.metric-card{
    background:white;
    border-radius:20px;
    padding:20px;
    text-align:center;
    border:2px solid #e2e8f0;
    box-shadow:0px 10px 25px rgba(0,0,0,0.08);
}

/* Scroll Boxes */
.scroll-box{
    height:280px;
    overflow-y:auto;
    padding:18px;
    border-radius:18px;
    background:white;
    border:2px solid #dbeafe;
    color:#1e293b;
    font-size:15px;
    line-height:1.8;
    box-shadow:0px 10px 30px rgba(59,130,246,0.10);
}

/* Section Header */
.section-header{
    color:#2563eb;
    font-size:1.3rem;
    font-weight:700;
    margin-bottom:10px;
}

/* Text Area */
textarea{
    border-radius:15px !important;
    background:white !important;
    color:#0f172a !important;
}

/* Button */
.stButton > button{
    width:100%;
    height:60px;
    border:none;
    border-radius:14px;
    background:linear-gradient(
        90deg,
        #2563eb,
        #06b6d4,
        #10b981
    );
    color:white;
    font-size:18px;
    font-weight:700;
    box-shadow:0px 10px 25px rgba(37,99,235,0.25);
    transition:0.3s;
}

.stButton > button:hover{
    transform:translateY(-3px);
}

/* Footer */
.footer{
    text-align:center;
    color:#64748b;
    margin-top:30px;
    font-size:14px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.markdown(
    '<div class="main-title">🩺 AI Blood Work Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Upload your blood report and receive an AI-powered health summary
    with personalized Indian diet recommendations.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<div style="
background:linear-gradient(90deg,#2563eb,#06b6d4);
padding:18px;
border-radius:18px;
text-align:center;
color:white;
font-size:18px;
font-weight:600;
margin-bottom:25px;
">
🩺 AI-Powered Blood Report Analysis • Instant Health Insights • Personalized Indian Diet Recommendations
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="metric-card">
        <h3>🤖 AI Analysis</h3>
        <p>Gemini 2.5 Flash</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
        <h3>⚡ Instant Results</h3>
        <p>Fast Medical Insights</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card">
        <h3>🥗 Diet Planning</h3>
        <p>Indian Food Recommendations</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------
# MAIN LAYOUT
# ---------------------------------------------------
left_col, right_col = st.columns([1, 1])

with left_col:

    st.markdown(
        '<div class="section-header">📄 Blood Work Report</div>',
        unsafe_allow_html=True
    )

    blood_report = st.text_area(
        "Blood Report",
        height=500,
        placeholder="Paste your blood report here...",
        label_visibility="collapsed"
    )

    analyze_clicked = st.button(
        "🔍 Analyze Blood Report",
        use_container_width=True
    )

with right_col:

    st.markdown(
        '<div class="section-header">📋 Health Summary</div>',
        unsafe_allow_html=True
    )

    health_box = st.empty()
    health_box.markdown(
        '<div class="scroll-box"></div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="section-header">🥗 Suggested Diet Plan</div>',
        unsafe_allow_html=True
    )

    diet_box = st.empty()
    diet_box.markdown(
        '<div class="scroll-box"></div>',
        unsafe_allow_html=True
    )

# ---------------------------------------------------
# ANALYSIS
# ---------------------------------------------------
if analyze_clicked:

    if not blood_report.strip():
        st.warning("⚠️ Please paste a blood work report first.")

    else:

        with st.spinner("🧠 Gemini AI is analyzing your blood report..."):

            extraction_prompt = f"""
You are a medical data extraction assistant.

From the blood report below, extract ALL test values and classify each one as HIGH, LOW, or NORMAL based on the reference ranges provided.

Format:

- Test Name: value | Status: HIGH/LOW/NORMAL | Reference: range

Blood Report:
{blood_report}
"""

            extraction_response = llm.invoke(extraction_prompt)
            extracted_values = extraction_response.content

            diet_prompt = f"""
You are a clinical nutritionist specializing in Indian dietary habits.

Based on the blood work analysis below provide:

SECTION 1 - HEALTH SUMMARY

Explain the patient's condition in simple language.

SECTION 2 - INDIAN DIET PLAN

Suggest foods to eat and foods to avoid using common Indian foods such as:
dal, sabzi, roti, rice, fruits, nuts, sprouts, curd, etc.

Blood Work Analysis:
{extracted_values}
"""

            diet_response = llm.invoke(diet_prompt)
            full_response = diet_response.content

        if "SECTION 2" in full_response:

            parts = full_response.split("SECTION 2")

            health_summary = (
                parts[0]
                .replace("SECTION 1 - HEALTH SUMMARY:", "")
                .replace("SECTION 1", "")
                .strip()
            )

            diet_plan = (
                "SECTION 2" + parts[1]
            ).replace(
                "SECTION 2 - INDIAN DIET PLAN:",
                ""
            ).replace(
                "SECTION 2",
                ""
            ).strip()

        else:
            health_summary = full_response
            diet_plan = ""

        health_box.markdown(
            f'<div class="scroll-box">{health_summary}</div>',
            unsafe_allow_html=True
        )

        diet_box.markdown(
            f'<div class="scroll-box">{diet_plan if diet_plan else full_response}</div>',
            unsafe_allow_html=True
        )

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="footer">
        ❤️ Built with Streamlit • LangChain • Gemini AI
    </div>
    """,
    unsafe_allow_html=True
)

