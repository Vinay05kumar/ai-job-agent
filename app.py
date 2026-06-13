import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)

st.title("🤖 AI Job Agent")

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

# Job Description
job_description = st.text_area(
    "Paste Job Description",
    height=200
)

if uploaded_file:

    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    st.success("Resume Uploaded Successfully!")

    if job_description:

        # ATS Score Calculation
        resume_words = set(resume_text.lower().split())
        jd_words = set(job_description.lower().split())

        if len(jd_words) > 0:

            matched_words = resume_words.intersection(jd_words)

            score = int(
                (len(matched_words) / len(jd_words)) * 100
            )

            st.subheader("ATS Match Score")
            st.metric("Match %", f"{score}%")

            missing_keywords = jd_words - resume_words

            st.subheader("Missing Keywords")
            st.write(list(missing_keywords)[:20])

        # AI Analysis Button
        if st.button("Analyze Resume"):

            prompt = f"""
You are an ATS Resume Expert.

Resume:
{resume_text}

Job Description:
{job_description}

Please provide:

1. ATS Score out of 100
2. Missing Skills
3. Resume Improvements
4. Improved Professional Summary
5. Interview Chances
"""

            try:

                # Try several Gemini models
                model_names = [
                    "gemini-2.5-flash",
                    "gemini-2.0-flash",
                    "gemini-pro"
                ]

                response = None

                for model_name in model_names:
                    try:
                        model = genai.GenerativeModel(model_name)
                        response = model.generate_content(prompt)
                        break
                    except:
                        pass

                st.subheader("AI Analysis")

                if response:
                    st.write(response.text)
                else:
                    st.warning(
                        "Gemini model not available. ATS Checker still works."
                    )

            except Exception as e:

                st.error(
                    f"Gemini Error: {str(e)}"
                )