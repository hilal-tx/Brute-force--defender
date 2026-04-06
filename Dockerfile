FROM python:3.9-slim
WORKDIR /app
COPY gereksinimler.txt .
RUN pip install --no-cache-dir -r gereksinimler.txt
COPY . .
CMD ["python", "kaynak/simulasyon.py"]
