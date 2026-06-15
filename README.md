# 🩺 AI Blood Work Analyzer

An AI-powered healthcare application that analyzes blood test reports and provides easy-to-understand health insights along with personalized Indian diet recommendations.

## 🚀 Features

* 📄 Analyze blood work reports
* 🤖 AI-powered health summary generation
* 🥗 Personalized Indian diet recommendations
* ⚡ Instant report analysis using Google Gemini
* 🎨 Modern and interactive Streamlit dashboard
* 🔍 Detection of abnormal blood parameters (High / Low / Normal)

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Google Gemini 2.5 Flash
* Python Dotenv
* UV Package Manager

## 📸 Application Workflow

1. Paste the blood report into the application.
2. AI extracts all blood parameters and evaluates them against reference ranges.
3. Gemini generates a simplified health summary.
4. The application recommends an Indian diet plan based on the findings.

## 📂 Project Structure

```text
AI-Blood-Work-Analyzer/
│
├── streamlit_app/
│   └── app.py
│
├── .env
├── pyproject.toml
├── README.md
└── requirements.txt
```

## ⚙️ Setup Instructions

### Clone Repository

```bash
git clone https://github.com/your-username/AI-Blood-Work-Analyzer.git
cd AI-Blood-Work-Analyzer
```

### Create Environment File

Create a `.env` file and add:

```env
GOOGLE_API_KEY=your_google_api_key
```

### Install Dependencies

Using UV:

```bash
uv sync
```

### Run Application

```bash
streamlit run app.py
```

## 🎯 Use Cases

* Personal health monitoring
* Preliminary blood report interpretation
* Nutrition and diet planning
* Healthcare AI demonstrations
* Generative AI portfolio projects

## ⚠️ Disclaimer

This application is intended for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment.

## 👩‍💻 Author

**Ameesha Potnuru**

Built with ❤️ using Streamlit, LangChain, and Google Gemini AI.

