FROM python:3.8.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY notebooks notebooks
COPY scripts scripts
COPY data data

EXPOSE 8501

CMD ["streamlit", "run", "scripts/app.py", "--server.port=8501", "--server.address=0.0.0.0"]

