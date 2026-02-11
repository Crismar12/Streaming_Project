# 🎬 Streaming Content Analytics Dashboard
This project is an application developed with Streamlit (https://streamlit.io/) to analyze, visualize, and explore information from streaming platforms. It includes statistics, rankings by country, content types, and interactive navigation through customizable filters.

## 🚀 Main Features
- Interactive data visualization with filters by country, year, and type.

- Descriptive charts using Seaborn and Matplotlib.

- Exploration of rankings and ratings by content.

- App embedded in a Docker container for easy deployment.

## 🐳 How to run with Docker:
### 1. Get the image from Docker Hub
`docker pull francis133/dashboard-proyecto_streaming:v1`

### 2. Run the container
`docker run -p 8501:8501 francis133/dashboard-proyecto_streaming:v1`

### 3. Open the app
Visit http://localhost:8501 in your browser to explore the dashboard 📊

## Project Structure 📑
Proyecto_Streaming/
├── data/ # Datasets in CSV and Parquet formats
├── notebooks/ # Jupyter notebooks for data cleaning and exploratory analysis
├── scripts/ # Contains app.py and general functions applied to data cleaning
├── requirements.txt # Required Libraries
├── Dockerfile # Docker Image
└── README.md # This file

## ⚙️ Manual Installation (without Docker)
If you prefer to run the project locally:

```bash
# Clone this repository
git clone https://github.com/Crismar12/Proyecto_Streaming.git
cd Proyecto_Streaming

# Create a virtual environment and install dependencies
python -m venv venv
venv\Scripts\activate # On Windows
pip install -r requirements.txt

# Run the app
streamlit run scripts/app.py
```
## ✨ Author
Developed by Francis 🧠 With ❤️ for data visualization and systems and computer engineering.
