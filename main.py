from datetime import datetime
from uuid import uuid4

from aiofauna import ASGIServer, FaunaModel, Field
from mangum import Mangum


class Example(FaunaModel):
	id:str = Field(default_factory=lambda: str(uuid4()))
	created_at:datetime = Field(default_factory=datetime.utcnow)


app = ASGIServer()

@app.get("/")
async def index():
	return await Example.all()

@app.post("/")
async def create():
	return await Example().save()

@app.get("/{ref}")
async def get(ref:str):
	return await Example.get(ref)

@app.put("/{ref}")
async def update(ref:str):
	return await Example.update(ref, created_at=datetime.utcnow())

@app.delete("/{ref}")
async def delete(ref:str):
	return await Example.delete(ref)



handler = Mangum(app)