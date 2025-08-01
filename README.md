# Offline-AI-Powered-Summarizer for HAL Intranet 🧠📄
⚙️ Offline AI-Powered Document Summarizer built for HAL's intranet system using Python, Flask, and NLP — supports PDF, DOCX, TXT files with a clean web UI and offline LLM integration.

This project is an offline document summarizer developed during industrial training at **Hindustan Aeronautics Limited (HAL), Avionics Division, Korwa**. It supports uploading `.pdf`, `.docx`, and `.txt` files, then generates intelligent summaries using a local LLM (DistilBART). The system runs entirely offline within HAL’s intranet environment.

---

## 🚀 Features
- 🔐 Offline LLM-based Summarization (DistilBART)
- 📁 Upload support for PDF, DOCX, TXT files
- 🧠 Intelligent chunking for large documents
- 🌗 Light/Dark Mode toggle
- 🖥️ Intuitive responsive frontend (HTML/CSS/JS)
- ⚙️ No internet/API dependency

---

## 🛠️ Tech Stack
- **Python**, **Flask**
- **Transformers (DistilBART)**
- **PyPDF2**, **python-docx**
- **HTML**, **CSS**, **JavaScript**

---

## 📸 UI Preview

![Screenshot](static/images/demo-preview.png)

---

## 📂 Folder Structure

├── app.py
├── utils.py
├── model/ # DistilBART model files
├── templates/
│ └── index.html
├── static/
│ └── images/
│ └── hal_logo.png
├── uploads/ # Temporary uploads
├── README.md

## 🧪 How to Run Locally

1. **Clone this repo**
```   
git clone https://github.com/yourusername/hal-offline-ai-summarizer.git
cd hal-offline-ai-summarizer
```

2. **Create a virtual environment (optional but recommended)**
```
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
```

3.Install dependencies

```
pip install -r requirements.txt
Run the app
```
4.Run the app
```
python app.py
```
App will be live at: http://localhost:5000

***📌 Notes***
The model (model/) is loaded locally; no internet or OpenAI API is used.

The project was developed under the guidance of Ankit Verma (DGM - IT & Lean) at HAL, Korwa.

Deployment was targeted for intranet environments with no external connectivity.


**🏢 Organization**
Hindustan Aeronautics Limited
Avionics Division, Korwa
Department: Information Technology (IT)
