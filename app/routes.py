from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from config import SessionLocal
from schemas import BookSchema, RequestBook, Response
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
async def create_book_service(request: RequestBook, db: Session = Depends(get_db)):
    try:
        crud.create_book(db, book=request.parameter)
        return Response(status="Ok", code="200", message="Book created successfully").dict(exclude_none=True)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
async def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        books = crud.get_book(db, skip=skip, limit=limit)
        return Response(status="Ok", code="200", message="Success fetch all data", result=books)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/update")
async def update_book(request: RequestBook, db: Session = Depends(get_db)):
    if request.parameter.id is None:
        raise HTTPException(status_code=400, detail="Book ID is required")
    try:
        updated_book = crud.update_book(db, book_id=request.parameter.id, 
                                        title=request.parameter.title, 
                                        description=request.parameter.description)
        if not updated_book:
            raise HTTPException(status_code=404, detail="Book not found")
        return Response(status="Ok", code="200", message="Success update data", result=updated_book)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/delete")
async def delete_book(request: RequestBook, db: Session = Depends(get_db)):
    if request.parameter.id is None:
        raise HTTPException(status_code=400, detail="Book ID is required")
    try:
        result = crud.remove_book(db, book_id=request.parameter.id)
        if not result:
            raise HTTPException(status_code=404, detail="Book not found")
        return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
