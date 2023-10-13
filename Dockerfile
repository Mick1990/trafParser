FROM python:3.10
WORKDIR /testTaskMikhail/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
