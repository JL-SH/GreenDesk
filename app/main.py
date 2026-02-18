from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from . import models, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="GreenDesk", version="1.0")

MODEL_MAP = {
    "devices": models.Device,
    "logs": models.AuditLog
}

@app.post("/devices/", response_model=schemas.DeviceOut, status_code=201)
def create_device(device: schemas.DeviceCreate, db: Session = Depends(get_db)):
    new_device = models.Device(**device.model_dump())
    db.add(new_device)
    db.commit()
    db.refresh(new_device)

    log = models.AuditLog(
        target_model="Device",
        target_id=new_device.id,
        action="create",
        changes={"new_state": device.model_dump()}
    )
    db.add(log)
    db.commit()
    
    return new_device

@app.get("/generic/{model_name}/{item_id}")
def get_any_model(model_name: str, item_id: int, db: Session = Depends(get_db)):
    model_class = MODEL_MAP.get(model_name.lower())
    
    if not model_class:
        raise HTTPException(status_code=404, detail="Modelo no registrado en la API genérica")

    item = db.query(model_class).filter(model_class.id == item_id).first()
    
    if not item:
        raise HTTPException(status_code=404, detail=f"No se encontró el item en {model_name}")
        
    return item