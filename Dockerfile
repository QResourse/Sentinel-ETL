FROM python:3.8
# Adding trusting keys to apt for repositories
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "./main.py"]