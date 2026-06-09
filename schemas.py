from pydantic import BaseModel


class Asset3DCreate(BaseModel):
    nome: str
    categoria: str = "3D Model"
    data: str


class Asset3DResponse(Asset3DCreate):
    id: int

    model_config = {"from_attributes": True}
