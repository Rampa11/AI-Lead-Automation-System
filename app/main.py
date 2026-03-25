from fastapi import FastAPI, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .models import Lead
from .schemas import LeadCreate
from .ai import process_lead
from .automation import trigger_actions

from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "AI Lead Automation API is running"}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ CREATE LEAD (POST)
@app.post("/leads/")
def create_lead(
    lead: LeadCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    
    print("🚀 CREATE LEAD ENDPOINT HIT")  

    ai_result = process_lead(lead.message)

    new_lead = Lead(
        name=lead.name,
        email=lead.email,
        message=lead.message,
        status=ai_result["status"],
        summary=ai_result["summary"],
        response=ai_result["response"]
    )

    db.add(new_lead)
    db.commit()
    db.refresh(new_lead)

    print("🚀 ADDING BACKGROUND TASK")  # 👈 ADD THIS TOO

    trigger_actions(new_lead)

    return new_lead


# ✅ GET ALL LEADS (GET)
@app.get("/leads/")
def get_leads(db: Session = Depends(get_db)):
    return db.query(Lead).all()
