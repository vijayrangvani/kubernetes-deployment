from fastapi import FastAPI
import os 

app = FastAPI(title="Production Kubernetes API",
              version="1.0.0")

@app.get("/")
def root():
    return {
        "msg":"Fastapi application Kubernetes API running on Kubernetes v5",
        "environment":os.getenv("APP_ENV","development")
    }

@app.get("/health")
def status():
    return{
        "status":"healthy"
    }