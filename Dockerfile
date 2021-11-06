# To be filled by students
FROM python:3.8.2

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8501

CMD ["streamlit","run","app.py"]



