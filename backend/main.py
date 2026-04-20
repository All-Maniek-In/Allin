from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Wykop Clone API", version="1.0.0")

# Pozwala frontendowi (z innego portu) odpytywać ten backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API działa! Witaj w backendzie naszego klonu Wykopu."}

@app.get("/api/posts")
def get_posts():
    # To jest tylko przykład. Później podepniemy tu bazę danych.
    return [
        {"id": 1, "title": "Pierwszy wpis na naszym nowym Wykopie!", "author": "koxum", "votes": 15},
        {"id": 2, "title": "Programowanie to super sprawa", "author": "Maniek", "votes": 8}
    ]

# Aby uruchomić: uvicorn main:app --reload
