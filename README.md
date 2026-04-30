# Python Hello World - DevOps Project

Un semplice progetto end-to-end per testare le basi della containerizzazione e del Continuous Deployment nel cloud.

**Live Demo:** [https://helloworldapp-ogip.onrender.com]

## Tecnologie Utilizzate
* **Sviluppo:** Python 3, Flask
* **Containerizzazione:** Docker
* **CI/CD & Hosting:** Render (PaaS)
* **Version Control:** Git, GitHub

## Descrizione del Progetto
Questo repository contiene una semplice applicazione web scritta in Python tramite il framework Flask.
L'obiettivo principale del progetto non è la complessità del codice, ma l'infrastruttura circostante. L'applicazione è interamente containerizzata tramite un `Dockerfile` ottimizzato.

Grazie all'integrazione tra GitHub e Render, ogni volta che viene effettuato un `git push` sul ramo `main`, la piattaforma intercetta la modifica, ricostruisce l'immagine Docker in automatico e pubblica la nuova versione online senza disservizi (Continuous Deployment).
