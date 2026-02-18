from sqlalchemy import String, Integer, DateTime, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

class Device(Base):
    __tablename__ = "devices"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    serial_number: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    model: Mapped[str] = mapped_column(String(100))
    category: Mapped[str] = mapped_column(String(50))
    status: Mapped[str] = mapped_column(default="available")
    specs: Mapped[dict] = mapped_column(JSONB, nullable=True, default={})

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    target_model: Mapped[str] = mapped_column(String(50)) 
    target_id: Mapped[int] = mapped_column(Integer)
    action: Mapped[str] = mapped_column(String(20)) 
    changes: Mapped[dict] = mapped_column(JSONB)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now())