From python:3.9-slim
WORKDIR /app
COPY python1.py /app/
COPY paragraphs.txt /app/
RUN pip install nltk
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords
CMD ["python", "python1.py", "/app/paragraphs.txt"]