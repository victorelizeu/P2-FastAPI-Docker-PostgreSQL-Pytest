from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"msg": "API rodando!"}


def test_create_asset():
    payload = {
        "nome": "Malha Base de Personagem",
        "categoria": "Character Asset",
        "data": "08/06/2026",
    }
    response = client.post("/assets/", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert data["nome"] == "Malha Base de Personagem"
    assert data["categoria"] == "Character Asset"

    assert "id" in data


def test_get_all_assets():
    response = client.get("/assets/")

    assert response.status_code == 200
    assert type(response.json()) == list


def test_get_asset_not_found():
    response = client.get("/assets/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Asset não encontrado!"


def test_update_asset():
    payload_criacao = {
        "nome": "Asset Antigo",
        "categoria": "Rascunho",
        "data": "2026-01-01",
    }
    response_criacao = client.post("/assets/", json=payload_criacao)
    asset_id = response_criacao.json()["id"]

    payload_atualizado = {
        "nome": "Asset Atualizado",
        "categoria": "Finalizado",
        "data": "2026-06-08",
    }
    response_update = client.put(f"/assets/{asset_id}", json=payload_atualizado)

    assert response_update.status_code == 200
    assert response_update.json()["nome"] == "Asset Atualizado"
    assert response_update.json()["categoria"] == "Finalizado"


def test_delete_asset():
    payload = {"nome": "Asset para Deletar", "categoria": "Lixo", "data": "2026-06-08"}
    response_criacao = client.post("/assets/", json=payload)
    asset_id = response_criacao.json()["id"]

    response_delete = client.delete(f"/assets/{asset_id}")

    assert response_delete.status_code == 200
    assert response_delete.json() == {"msg": "Asset deletado com sucesso!"}

    response_busca = client.get(f"/assets/{asset_id}")
    assert response_busca.status_code == 404
