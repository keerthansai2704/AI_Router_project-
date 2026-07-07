from datetime import datetime
from sqlalchemy import String, Text, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str] = mapped_column(String(255))
    raw_text: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    chunks: Mapped[list["Chunk"]] = relationship(back_populates="document")


class Chunk(Base):
    __tablename__ = "chunks"

    id: Mapped[int] = mapped_column(primary_key=True)
    document_id: Mapped[int] = mapped_column(ForeignKey("documents.id"))
    content: Mapped[str] = mapped_column(Text)
    chunk_index: Mapped[int] = mapped_column(Integer)
    qdrant_point_id: Mapped[str] = mapped_column(String(64), nullable=True)

    document: Mapped["Document"] = relationship(back_populates="chunks")


class RequestLog(Base):
    __tablename__ = "requests"

    id: Mapped[int] = mapped_column(primary_key=True)
    query: Mapped[str] = mapped_column(Text)
    complexity: Mapped[str] = mapped_column(String(20))  # simple | knowledge | complex
    model_used: Mapped[str] = mapped_column(String(50))
    cache_hit: Mapped[bool] = mapped_column(default=False)
    latency_ms: Mapped[int] = mapped_column(Integer, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    cost: Mapped["CostLog"] = relationship(back_populates="request", uselist=False)


class CostLog(Base):
    __tablename__ = "costs"

    id: Mapped[int] = mapped_column(primary_key=True)
    request_id: Mapped[int] = mapped_column(ForeignKey("requests.id"))
    input_tokens: Mapped[int] = mapped_column(Integer, default=0)
    output_tokens: Mapped[int] = mapped_column(Integer, default=0)
    cost_usd: Mapped[float] = mapped_column(Float, default=0.0)

    request: Mapped["RequestLog"] = relationship(back_populates="cost")