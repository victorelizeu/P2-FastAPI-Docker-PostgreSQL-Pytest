from fastapi import FastAPI, Depends, HTTPException
from database import Base, engine, get_db
import models
from sqlalchemy.orm import Session
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def get():
    return {"msg": "API rodando!"}


@app.post("/assets/", response_model=schemas.Asset3DResponse)
def create(asset: schemas.Asset3DCreate, db: Session = Depends(get_db)):
    asset_novo = models.Asset3D(**asset.model_dump())

    db.add(asset_novo)

    db.commit()

    db.refresh(asset_novo)

    return asset_novo


@app.get("/assets/", response_model=list[schemas.Asset3DResponse])
def get_all(db: Session = Depends(get_db)):
    listar = db.query(models.Asset3D).all()

    return listar


@app.get("/assets/{asset_id}", response_model=schemas.Asset3DResponse)
def get_by_id(asset_id: int, db: Session = Depends(get_db)):
    achar = db.query(models.Asset3D).filter(models.Asset3D.id == asset_id).first()

    if achar is None:
        raise HTTPException(status_code=404, detail="Asset não encontrado!")
    return achar


@app.put("/assets/{asset_id}", response_model=schemas.Asset3DResponse)
def update(
    asset_atualizado: schemas.Asset3DCreate,
    asset_id: int,
    db: Session = Depends(get_db),
):
    achar = db.query(models.Asset3D).filter(models.Asset3D.id == asset_id).first()

    if achar is None:
        raise HTTPException(status_code=404, detail="Asset não encontrado!")
    achar.nome = asset_atualizado.nome
    achar.data = asset_atualizado.data
    achar.categoria = asset_atualizado.categoria

    db.commit()
    db.refresh(achar)

    return achar


@app.delete("/assets/{asset_id}")
def deletar(asset_id: int, db: Session = Depends(get_db)):
    achar = db.query(models.Asset3D).filter(models.Asset3D.id == asset_id).first()

    if achar is None:
        raise HTTPException(status_code=404, detail="Asset não encontrado!")
    db.delete(achar)

    db.commit()

    return {"msg": "Asset deletado com sucesso!"}
