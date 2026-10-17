import pytest
from main import add_task, update_task, change_completed, delete_task, load_tasks, tasks
import json


@pytest.fixture
def clean_tasks():
    tasks.clear()
    yield
    tasks.clear()


def test_add_task(clean_tasks):
    add_task("Learn Python")

    assert tasks[0]["title"] == "Learn Python"
    assert tasks[0]["id"] == 1
    assert tasks[0]["completed"] is False


def test_add_multiple_tasks(clean_tasks):
    add_task("Learn Python")
    add_task("Learn AI")

    assert len(tasks) == 2
    assert tasks[0]["id"] == 1
    assert tasks[1]["id"] == 2


def test_update_task(clean_tasks):
    add_task("Learn Python")
    result = update_task(1, "Learn AI")
    assert result is True
    assert tasks[0]["title"] == "Learn AI"


def test_update_task_not_found(clean_tasks):
    add_task("Learn Python")
    result = update_task(10, "Learn AI")
    assert result is False


def test_change_completed(clean_tasks):
    add_task("Learn Python")
    result = change_completed(1)
    assert result is True
    assert tasks[0]["completed"] is True


def test_change_completed_not_found(clean_tasks):
    add_task("Learn Python")
    result = change_completed(10)
    assert result is False


def test_delete_task(clean_tasks):
    add_task("Learn Python")
    result = delete_task(1)
    assert result is True
    assert len(tasks) == 0


def test_delete_task_not_found(clean_tasks):
    add_task("Learn Python")
    result = delete_task(10)
    assert result is False
    assert len(tasks) == 1


def test_load_tasks(tmp_path):
    tasks = [{
        "id": 1,
        "title": "Learn Python",
        "completed": False
    }]
    file_path = tmp_path / "tasks.json"
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)

    loaded_tasks = load_tasks(file_path)
    assert isinstance(loaded_tasks, list)
    assert len(loaded_tasks) == 1
    assert loaded_tasks[0]["title"] == "Learn Python"
    assert loaded_tasks[0]["id"] == 1


def test_load_empty_tasks(tmp_path):
    file_path = tmp_path / "tasks.json"
    file_path.write_text("[]", encoding="utf-8")

    loaded_tasks = load_tasks(file_path)

    assert loaded_tasks == []


def test_load_invalid_json(tmp_path, capsys):
    file_path = tmp_path / "tasks.json"
    file_path.write_text("{invalid json}", encoding="utf-8")

    loaded_tasks = load_tasks(file_path)

    assert loaded_tasks == []

    captured = capsys.readouterr()
    assert "Invalid tasks data" in captured.out


def test_load_invalid_structure(tmp_path, capsys):
    file_path = tmp_path / "tasks.json"
    file_path.write_text(
        '{"id": 1, "title": "Learn Python", "completed": false}',
        encoding="utf-8"
    )

    loaded_tasks = load_tasks(file_path)

    assert loaded_tasks == []

    captured = capsys.readouterr()
    assert "Invalid tasks data" in captured.out
