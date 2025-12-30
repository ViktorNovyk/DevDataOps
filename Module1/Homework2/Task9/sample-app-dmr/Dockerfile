# Based on https://docs.streamlit.io/deploy/tutorials/docker
FROM python:3.9-slim

RUN pip install --no-cache-dir streamlit==1.50.0

WORKDIR /app
COPY app.py ./
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
