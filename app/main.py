from fastapi import FastAPI

from app import db

app = FastAPI(title="MVP DataOps Docente")

@app.get("/")

def root():

 return {"message": "API MVP DataOps Docente activa"}

@app.get("/health")

def health():

 return {"status": "ok"}


@app.get("/db-health")

def check_db_health():

  return db.test_connection()


@app.get("/postulaciones-demo")

def get_postulaciones_endpoint(limit: int = 20):

  return db.get_postulaciones(limit=limit)


@app.get("/postulaciones-demo/stats")

def get_postulaciones_stats_endpoint():

  return db.get_postulaciones_stats()