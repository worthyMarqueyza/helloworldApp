# Usa un'immagine Python ufficiale leggera
FROM python:3.10-slim

# Imposta la directory di lavoro nel container
WORKDIR /app

# Copia i file dei requisiti e installa le dipendenze
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto del codice dell'applicazione
COPY . .

# Esponi la porta su cui l'app è in ascolto
EXPOSE 80

# Comando per avviare l'applicazione
CMD ["python", "app.py"]
