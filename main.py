from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

templates = Jinja2Templates(directory=".")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    lista =  [1, 2, 3, 4, 5, 6, 7, 8]
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hola profe", "X":lista})
