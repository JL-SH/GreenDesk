from typing import Any, Dict, Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    username: str
    full_name: str

class UserOut(UserCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)

class DeviceBase(BaseModel):
    serial_number: str
    model: str
    category: str

class DeviceCreate(DeviceBase):
    pass

class DeviceOut(DeviceBase):
    id: int
    status: str
    return_date: Optional[datetime] = None
    owner_id: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)

class AuditLogOut(BaseModel):
    id: int
    target_model: str
    target_id: int
    action: str
    changes: Dict[str, Any]
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)