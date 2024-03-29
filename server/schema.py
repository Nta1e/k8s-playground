from pydantic import BaseModel


class TodoRequestSchema(BaseModel):
	title: str


class TodoResponseSchema(BaseModel):
	id: int
	title: str
	complete: bool

	class Config:
		orm_mode = True
