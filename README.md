# 🩺 MedIntel – Medical Report Simplifier

**MedIntel** is an AI-powered Streamlit web app that simplifies complex medical reports into **clear, patient-friendly explanations** using Google’s **Gemini 2.5 Flash** model.

---

## 🌟 Features

- 📤 **Upload PDF Reports:** Upload any medical report in PDF format.  
- 🤖 **AI-Powered Summarization:** Uses Gemini AI to analyze and simplify medical content.  
- 💬 **Custom Instructions:** Ask the app to focus on specific sections (e.g., lab results, findings).  
- 🧠 **Patient-Friendly Explanations:** Converts medical jargon into simple, understandable text.  
- ⚠️ **Ethical Guardrails:** Does *not* provide diagnoses or treatment recommendations — purely educational.  
- 🎨 **Modern UI:** Beautiful Streamlit interface with custom styling and progress indicators.

---

## 🩹 Problem It Solves

Medical reports are often filled with **technical terms** that can be confusing for patients.  
**MedIntel** bridges this communication gap by:
- Simplifying complex medical language.  
- Helping patients better understand their health information.  
- Empowering users to have more informed conversations with their healthcare providers.

---

## 🧰 Tech Stack

- **Python 3.9+**  
- **Streamlit** (for the web interface)  
- **Google Generative AI (Gemini API)**  
- **PyPDF2** (for reading PDFs)  
- **dotenv** (for environment variable management)

---

## ⚙️ Setup Instructions

Follow these steps to run the project locally:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Hrishik03/MedIntel.git
cd MedIntel
2️⃣ Create a virtual environment
python -m venv venv

3️⃣ Activate the environment

Windows:

venv\Scripts\activate


macOS/Linux:

source venv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Set up your environment variables

Create a .env file in the project root and add your Gemini API key:

GEMINI_API_KEY=your_google_gemini_api_key_here

6️⃣ Run the app
streamlit run app.py

7️⃣ Open in browser

Once Streamlit starts, it will open automatically at:

http://localhost:8501

⚠️ Disclaimer

This application is for educational and informational purposes only.
It does not replace professional medical advice, diagnosis, or treatment.
Always consult your doctor for any health-related concerns.