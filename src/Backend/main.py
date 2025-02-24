from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # Importa CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
import uvicorn
from uuid import uuid4
import firebase_admin
from firebase_admin import credentials, firestore

# Inicializar Firebase
cred = credentials.Certificate("proyectobiblioteca-adc3a-firebase-adminsdk-1p5lo-e37936d29e.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = FastAPI()

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permite solicitudes desde el frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

class Book(BaseModel):
    id: Optional[str] = None
    Autor: str
    NombreDelLibro: str
    Editorial: str
    LugarDeEditorial: str
    FechaDeEditorial: str
    CantidadDePaginas: int
    CodigoIsbn: str
    Tejure: str
    CategoriaDelLibro: str

@app.get("/books", response_model=List[Book])
async def get_books():
    books = []
    docs = db.collection('Libros').stream()
    for doc in docs:
        book_data = doc.to_dict()
        book_data['id'] = doc.id
        books.append(Book(**book_data))
    return books

@app.post("/books", response_model=Book)
async def create_book(book: Book):
    doc_ref = db.collection('Libros').document()
    book_dict = book.dict(exclude_unset=True, exclude={'id'})
    doc_ref.set(book_dict)
    book.id = doc_ref.id
    return book

@app.delete("/books/{isbn}")
async def delete_book(isbn: str):
    docs = db.collection('Libros').where('CodigoIsbn', '==', isbn).stream()
    for doc in docs:
        doc.reference.delete()
        return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books/search")
async def search_books(term: str):
    books = []
    docs = db.collection('Libros').stream()
    for doc in docs:
        book_data = doc.to_dict()
        book_data['id'] = doc.id
        book = Book(**book_data)
        if (term.lower() in book.NombreDelLibro.lower() or
            term.lower() in book.Autor.lower() or
            (book.CategoriaDelLibro and term.lower() in book.CategoriaDelLibro.lower()) or
            term.lower() in book.CodigoIsbn.lower()):
            books.append(book)
    return books

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)