from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db

from models import Todo
from schema import TodoRequestSchema, TodoResponseSchema

router = APIRouter()


@router.get('/healthz', tags=['health'])
def health():
	return "OK"

@router.post("/todo", response_model=TodoResponseSchema)
def create_todo(todo: TodoRequestSchema):
    todo = Todo(title=todo.title)
    db.session.add(todo)
    db.session.commit()
    return todo

@router.get("/todos", response_model=list[TodoResponseSchema])
def get_all_todos():
    todos = db.session.query(Todo).all()
    return todos

@router.put("/todo/{id}", response_model=TodoResponseSchema)
def mark_as_complete(id: int):
    if not (
         todo := db.session.query(Todo).filter(Todo.id == id).one_or_none()
	):
         raise HTTPException(status_code=404, detail="Todo not found")
    todo.complete = True
    db.session.add(todo)
    db.session.commit()

    return todo

@router.delete("/todo/{id}")
def delete_todo(id: int):
    if not (
         todo := db.session.query(Todo).filter(Todo.id == id).one_or_none()
	):
         raise HTTPException(status_code=404, detail="Todo not found")

    db.session.delete(todo)
    db.session.commit()

    return "OK"
