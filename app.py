import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import PyPDF2


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
if not api_key:
    st.error("Missing GEMINI_API_KEY in .env file")
else:
    genai.configure(api_key=api_key)

# Page configuration
st.set_page_config(
    page_title="MedIntel - Report Simplifier",
    page_icon="⚕️",
    layout="centered"
)

# --- CSS styling ---
st.markdown("""
    <style>
    .main {
        background-color: #f4f6fb;
        border-radius: 12px;
        padding: 1.5rem;
    }
    .stTextArea textarea {
        border: 1px solid #5A5AFB;
        border-radius: 8px;
    }
    .stButton>button {
        background-color: #5A5AFB;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        border: none;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #4949e3;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

#Header 

st.title("🩺 MedIntel - Medical Report Simplifier")
st.caption("Transform complex medical reports into clear, patient-friendly explanations.")
st.markdown("---")


uploaded_file = st.file_uploader("📤 Upload your medical report (PDF)", type=["pdf"])

if uploaded_file is not None:
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""

        # extracted preview in expander
        with st.expander("View Extracted Report Text (Preview)"):
            st.write(text[:100] + ("..." if len(text) > 100 else ""))

        st.markdown("---")

        # User Input
        st.markdown("### 💬 What would you like to understand?")
        user_instruction = st.text_area(
            "Optional: Specify your question or focus area",
            placeholder="e.g., Summarize the key findings or explain the lab results section.",
            help="You can leave this blank for a general explanation of the report."
        )

        
        if st.button("✨ Simplify Report"):
            with st.spinner("🔍 Analyzing and simplifying your report..."):
                progress_bar = st.progress(0)
                for pct in range(0, 100, 10):
                    progress_bar.progress(pct)
                
                model = genai.GenerativeModel("gemini-2.5-flash")

                if user_instruction.strip():
                    prompt = f"""
                    You are a friendly medical assistant explaining a medical report to a patient.
                    Task: {user_instruction}
                    Use simple, clear, and calm language suitable for a non-medical person.
                    DO NOT provide diagnosis, treatment, or medical advice.

                    Report:
                    {text}
                    """
                else:
                    prompt = f"""
                    You are a friendly medical assistant explaining a medical report to a patient.
                    Use simple, clear, and calm language suitable for a non-medical person.
                    DO NOT provide diagnosis, treatment, or medical advice.

                    Report:
                    {text}
                    """
                response = model.generate_content(prompt)
                explanation = response.text

                progress_bar.progress(100)

            # --- Display Output ---
            st.success("✅ Simplified Explanation Ready!")
            st.subheader("📘 Simplified Explanation")
            st.write(explanation)

            st.markdown("---")
            st.info("⚠️ *Disclaimer: This summary is for educational purposes only and is **not a substitute for professional medical advice.***")

    except Exception as e:
        st.error(f"❌ Failed to process the file: {e}")
else:
    st.info("📎 Please upload a PDF report to begin.")
