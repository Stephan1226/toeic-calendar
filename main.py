from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import Optional
from database import init_db, get_db, DayRecord

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request, db: Session = Depends(get_db)):
    records = db.query(DayRecord).order_by(DayRecord.day).all()
    days = {str(record.day): {
        "checked": record.checked,
        "source": record.source,
        "notion_link": record.notion_link
    } for record in records}
    return templates.TemplateResponse("index.html", {"request": request, "days": days})

@app.post("/update/{day}")
async def update_day(
    day: int,
    checked: Optional[str] = Form(None),
    source: str = Form(""),
    notion_link: str = Form(""),
    db: Session = Depends(get_db)
):
    record = db.query(DayRecord).filter(DayRecord.day == day).first()
    if record:
        record.checked = checked == "on"
        record.source = source
        record.notion_link = notion_link
        db.commit()
    return RedirectResponse(url="/", status_code=303)
