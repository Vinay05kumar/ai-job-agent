# 🤖 AI Job Agent

AI Job Agent is an intelligent resume analysis and job-matching platform built using **Python, Streamlit, and Generative AI**. It helps job seekers evaluate their resumes against job descriptions, calculate ATS scores, identify missing skills, and receive AI-powered recommendations to improve their chances of getting shortlisted.

---

## 🚀 Features

### 📄 Resume Upload
- Upload resumes in PDF format
- Extract and process resume content automatically

### 📝 Job Description Analysis
- Paste any job description
- Compare resume with job requirements

### 📊 ATS Score Checker
- Calculate resume-job match percentage
- Evaluate ATS compatibility

### 🔍 Missing Skills Detection
- Identify missing keywords and skills
- Highlight areas for improvement

### 🤖 AI Resume Analysis
- Generate AI-powered recommendations
- Improve resume quality and relevance

### 📈 Career Insights
- Resume improvement suggestions
- Interview readiness assessment

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend Logic |
| Streamlit | Web Application UI |
| PyPDF | Resume PDF Processing |
| Google Gemini API | AI Analysis |
| Python Dotenv | Environment Variable Management |

---

## 📂 Project Structure

```bash
ai-job-agent/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── resumes/
│
├── outputs/
│
└── venv/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/ai-job-agent.git
cd ai-job-agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Get your API key from:

https://aistudio.google.com

---

## ▶️ Run Application

```bash
python -m streamlit run app.py
```

Application will start at:

```text
http://localhost:8501
```

---

## 📸 Application Workflow

### Step 1
Upload Resume PDF

### Step 2
Paste Job Description

### Step 3
Calculate ATS Match Score

### Step 4
View Missing Skills

### Step 5
Generate AI-Based Analysis

### Step 6
Improve Resume for Better Job Matching

---

## 🎯 Example Output

```text
ATS Score: 78%

Missing Skills:
- SQL
- Power BI
- Data Visualization

Resume Improvements:
- Add dashboard projects
- Highlight data cleaning experience

Interview Chances:
High
```

---

## 🔮 Future Enhancements

- AI Resume Rewriter
- Automatic Cover Letter Generator
- Resume Download Feature
- Job Application Tracker
- LinkedIn Job Search Integration
- Naukri Job Search Integration
- Auto Apply Agent using Playwright
- Multi-Agent Workflow using CrewAI
- LangGraph Integration
- Database Support (SQLite/PostgreSQL)

---

## 📚 Learning Outcomes

This project demonstrates:

- Resume Parsing
- ATS Optimization
- Prompt Engineering
- Generative AI Integration
- Streamlit Development
- PDF Processing
- Job Recommendation Systems

---

## 👨‍💻 Author

### Vinay Kumar

Final Year Computer Science Engineering Student

Aspiring Data Analyst | AI Enthusiast | Python Developer

---

## ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub and share it with others.

---

## 📄 License

This project is licensed under the MIT License.
