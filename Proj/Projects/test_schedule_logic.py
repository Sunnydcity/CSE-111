import pytest
from schedule_logic import create_schedule, validate_schedule, save_schedule, load_schedule

def test_create_schedule():
    subjects = ["Math", "Science"]
    times = ["09:00", "10:00"]
    schedule = create_schedule(subjects, times)
    assert schedule == {"09:00": "Math", "10:00": "Science"}

def test_validate_schedule():
    subjects = ["Math", "Science"]
    times = ["09:00", "09:00"]
    assert not validate_schedule(subjects, times)

def test_save_and_load_schedule(tmp_path):
    schedule = {"09:00": "Math", "10:00": "Science"}
    filename = tmp_path / "schedule.json"
    save_schedule(schedule, filename)
    loaded_schedule = load_schedule(filename)
    assert loaded_schedule == schedule
