import json

from app.api import crud


def test_create_hero(test_app, monkeypatch):
    test_req_payload = {"name": "Вуди", "description": "Персонаж, представляющий собой образ типичного лесоруба"}
    test_res_payload = {"id": 1, "name": "Вуди",
                        "description": "Персонаж, представляющий собой образ типичного лесоруба"}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, "post", mock_post)

    res = test_app.post("/heroes/", content=json.dumps(test_req_payload))

    assert res.status_code == 201
    assert res.json() == test_res_payload


def test_create_invalid_hero(test_app):
    res = test_app.post("/heroes/", content=json.dumps({"name": "Вуди"}))
    assert res.status_code == 422


def test_get_hero(test_app, monkeypatch):
    test_data = {"id": 1, "name": "Уолтер", "description": "Эксклюзивный персонаж для Don't Starve Together."}

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    res = test_app.get("/heroes/1")
    assert res.status_code == 200
    assert res.json() == test_data


def test_get_all_heroes(test_app, monkeypatch):
    test_data = [
        {"name": "Вуди", "description": "Персонаж, представляющий собой образ типичного лесоруба", "id": 1},
        {"name": "Вортокс", "description": "Персонаж из платного дополнения к Don't Starve Together.", "id": 2}
    ]

    async def mock_get_all():
        return test_data

    monkeypatch.setattr(crud, "get_all", mock_get_all)

    res = test_app.get("/heroes")
    assert res.status_code == 200
    assert res.json() == test_data
