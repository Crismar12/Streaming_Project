# 🎬 Streaming Content Analytics Dashboard

> **A full-stack data analytics platform** that transforms streaming platform data into actionable insights through interactive visualizations and statistical analysis.

[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://hub.docker.com/r/francis133/dashboard-proyecto_streaming)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)

## 📊 Project Overview

This project demonstrates **end-to-end data engineering and analytics skills** by building a production-ready dashboard for streaming content analysis. It showcases data cleaning, exploratory data analysis (EDA), visualization design, and containerized deployment—key competencies for data analyst and data engineer roles.

### 🎯 Business Impact
- **Data-driven insights** into content performance across multiple streaming platforms
- **Geographic and temporal analysis** to identify market trends and content popularity
- **Interactive filtering system** enabling stakeholders to explore data independently
- **Scalable architecture** using Docker for seamless deployment across environments

---

## 🛠️ Technical Stack

| Category | Technologies |
|----------|-------------|
| **Frontend** | Streamlit (interactive dashboard) |
| **Data Processing** | Python, Pandas, NumPy |
| **Visualization** | Seaborn, Matplotlib, Plotly |
| **Data Formats** | CSV, Parquet (optimized storage) |
| **Containerization** | Docker |
| **Version Control** | Git, GitHub |
| **Data Analysis** | Jupyter Notebooks (EDA) |

---

## 🚀 Key Features

✅ **Multi-dimensional Filtering**: Dynamic filters by country, year, content type, and platform  
✅ **Statistical Analysis**: Descriptive statistics, distribution analysis, and correlation studies  
✅ **Visual Storytelling**: Professional charts and graphs with Seaborn/Matplotlib  
✅ **Performance Rankings**: Top-rated content, trending shows, and country-specific insights  
✅ **Production-Ready Deployment**: Dockerized application with one-command setup  
✅ **Clean Architecture**: Modular code structure with separation of concerns  

---

## 🐳 Quick Start with Docker

**Option 1: Pull from Docker Hub (Recommended)**
```bash
# 1. Pull the pre-built image
docker pull francis133/dashboard-proyecto_streaming:v1

# 2. Run the container
docker run -p 8501:8501 francis133/dashboard-proyecto_streaming:v1

# 3. Access the dashboard
# Open your browser and navigate to: http://localhost:8501
```

**Option 2: Build from Source**
```bash
# Clone and build locally
git clone https://github.com/Crismar12/Proyecto_Streaming.git
cd Proyecto_Streaming
docker build -t streaming-dashboard .
docker run -p 8501:8501 streaming-dashboard
```

---

## 💻 Local Development Setup

```bash
# 1. Clone the repository
git clone https://github.com/Crismar12/Proyecto_Streaming.git
cd Proyecto_Streaming

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Launch the application
streamlit run scripts/app.py
```

---

## 📁 Project Structure

```
Proyecto_Streaming/
├── 📂 data/                    # Raw and processed datasets
│   ├── *.csv                   # Raw data files
│   └── *.parquet               # Optimized data storage
├── 📂 notebooks/               # Jupyter notebooks
│   ├── data_cleaning.ipynb     # ETL processes
│   └── exploratory_analysis.ipynb  # EDA and insights
├── 📂 scripts/                 # Application code
│   ├── app.py                  # Main Streamlit dashboard
│   └── utils.py                # Helper functions and data processing
├── 📄 requirements.txt         # Python dependencies
├── 🐳 Dockerfile               # Container configuration
└── 📖 README.md                # Project documentation
```

---

## 🎓 Skills Demonstrated

### Data Engineering
- ETL pipeline design and implementation
- Data cleaning and normalization techniques
- Efficient data storage (Parquet format)
- Modular code architecture

### Data Analysis
- Exploratory Data Analysis (EDA)
- Statistical analysis and hypothesis testing
- Pattern recognition and trend identification
- Data storytelling through visualization

### Software Engineering
- Version control with Git/GitHub
- Containerization with Docker
- Application deployment and DevOps practices
- Clean code principles and documentation

### Business Intelligence
- Dashboard design and UX considerations
- KPI identification and tracking
- Stakeholder-focused reporting
- Data-driven decision support systems

---

## 📈 Sample Insights

The dashboard enables users to answer questions like:
- 📍 **Which countries have the most diverse content libraries?**
- 📅 **How has content production evolved over the years?**
- ⭐ **What are the highest-rated shows by genre and platform?**
- 🎭 **Which content types dominate different markets?**

---

## 🌟 Why This Project Stands Out

1. **Production-Ready**: Fully containerized with Docker for enterprise deployment
2. **Scalable Design**: Modular architecture supports easy feature additions
3. **Performance Optimized**: Uses Parquet format for efficient data loading
4. **Professional Documentation**: Clear setup instructions and code comments
5. **Best Practices**: Follows industry standards for project structure and version control

---

## 🔮 Future Enhancements

- [ ] Add machine learning models for content recommendation
- [ ] Integrate real-time data streaming from APIs
- [ ] Implement user authentication and personalized dashboards
- [ ] Deploy to cloud platforms (AWS, GCP, or Azure)
- [ ] Add automated testing and CI/CD pipeline

---

## 👨‍💻 About the Developer

**Francis** | Data Analyst & Systems Engineer

I'm passionate about transforming raw data into meaningful insights through elegant visualization and robust engineering practices. This project showcases my ability to handle the full data lifecycle—from collection and cleaning to analysis and deployment.

### 🔗 Connect With Me
- 💼 LinkedIn: [Your LinkedIn Profile]
- 🐙 GitHub: [@Crismar12](https://github.com/Crismar12)
- 📧 Email: [Your Email]

---

## 📄 License

This project is available for portfolio and educational purposes.

---

<div align="center">

**Built with ❤️ using Python, Streamlit, and Docker**

⭐ If you find this project interesting, please consider giving it a star!

</div>