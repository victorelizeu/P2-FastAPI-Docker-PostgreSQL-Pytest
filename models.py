from database import Base
from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped


class Asset3D(Base):
    __tablename__ = "models"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    nome: Mapped[str] = mapped_column(String, nullable=False, index=True)

    categoria: Mapped[str] = mapped_column(String, nullable=False)

    data: Mapped[str] = mapped_column(String, nullable=True)