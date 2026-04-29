# 🚖 Ride Analytics Platform

An end-to-end data analytics platform that simulates ride data, processes it using an ETL pipeline, stores it in PostgreSQL, and visualizes insights through an interactive dashboard.

This project demonstrates real-world data engineering and analytics workflows with Docker-based deployment.

---

## 🚀 Features

- 🔄 End-to-End ETL Pipeline (Data Generation → Processing → Storage)
- 🗄 PostgreSQL Database Integration
- 📊 Interactive Dashboard using Streamlit
- 🔍 Filters (City & Date)
- 🔄 Data Refresh Button
- 🐳 Dockerized Multi-Container Architecture

---

## 🧱 Tech Stack

- Python  
- Pandas  
- SQLAlchemy  
- PostgreSQL  
- Streamlit  
- Docker & Docker Compose  

---

## 📊 Dashboard Preview

### Main Dashboard
![Dashboard](attached screenshots in assets folder)

---

## ⚙️ Project Architecture
Data Generation → Data Processing → PostgreSQL → Streamlit Dashboard → Docker

---

## ▶️ How to Run (Docker - Recommended)

### 1. Clone Repository
git clone https://github.com/Vraj-2011/ride-analytics-platform.git

cd ride-analytics-platform

---

### 2. Start Docker
docker-compose up --build

---

### 3. Load Data (IMPORTANT)

Open a new terminal:
docker exec -it ride_app python scripts/load_data.py

---

### 4. Open Dashboard
http://localhost:8501/

---

## 💻 Run Locally (Without Docker)

### Install dependencies
pip install -r requirements.txt

---

### Run pipeline
python scripts/generate_data.py
python scripts/process_data.py
python scripts/load_data.py

---

### Run dashboard
python -m streamlit run dashboard/app.py

---

## 🧠 Key Learnings

- Built a complete ETL pipeline from scratch  
- Integrated PostgreSQL for structured data storage  
- Designed an interactive dashboard with filtering  
- Implemented Docker-based multi-container system  
- Solved real-world issues like database connectivity and container networking  

---

## 💼 Resume Highlight

Built a containerized ride analytics platform using Python, PostgreSQL, and Docker with an end-to-end ETL pipeline and interactive dashboard.

---

## 🚀 Future Improvements

- Add real-time streaming using Kafka  
- Deploy application on cloud (AWS/GCP)  
- Add authentication & user roles  
- Integrate Airflow for scheduling  

---

## 📬 Contact

www.linkedin.com/in/vraj-shah-9600b4238
