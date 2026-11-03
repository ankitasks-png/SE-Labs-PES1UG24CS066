
import pytest

from ski_resort_pass import (
    process_resort_bookings,
    check_chairlift_anemometer,
)


def test_single_adult_full_day():
    groups = [{
        "is_active": True,
        "duration": "full_day",
        "skiers": [{"age": 30}],
    }]
    result = process_resort_bookings(groups, 15.0)
    assert result["total_revenue"] == 80.0
    assert result["status"] == "COMPLETED"


def test_season_pass():
    groups = [{
        "is_active": True,
        "duration": "season",
        "skiers": [{"age": 30}],
    }]
    result = process_resort_bookings(groups, 15.0)
    assert result["total_revenue"] == 300.0


def test_half_day_pass():
    groups = [{
        "is_active": True,
        "duration": "half_day",
        "skiers": [{"age": 30}],
    }]
    result = process_resort_bookings(groups, 15.0)
    assert result["total_revenue"] == 50.0


def test_child_discount():
    groups = [{
        "is_active": True,
        "duration": "full_day",
        "skiers": [{"age": 10}],
    }]
    result = process_resort_bookings(groups, 15.0)
    assert result["total_revenue"] == 48.0


def test_senior_discount():
    groups = [{
        "is_active": True,
        "duration": "full_day",
        "skiers": [{"age": 70}],
    }]
    result = process_resort_bookings(groups, 15.0)
    assert result["total_revenue"] == 56.0


def test_gear_rental():
    groups = [{
        "is_active": True,
        "duration": "full_day",
        "skiers": [{"age": 30, "gear_rental": True}],
    }]
    result = process_resort_bookings(groups, 15.0)
    assert result["total_revenue"] == 115.0


def test_lodge_locker():
    groups = [{
        "is_active": True,
        "duration": "full_day",
        "skiers": [{"age": 30}],
        "includes_lodge_locker": True,
    }]
    result = process_resort_bookings(groups, 20.0)
    assert result["total_revenue"] == 100.0


def test_inactive_group():
    groups = [{
        "is_active": False,
        "duration": "full_day",
        "skiers": [{"age": 30}],
    }]
    result = process_resort_bookings(groups, 15.0)
    assert result["status"] == "ZERO_SALES"


def test_invalid_duration():
    groups = [{
        "is_active": True,
        "duration": "weekly",
        "skiers": [{"age": 30}],
    }]
    result = process_resort_bookings(groups, 15.0)
    assert result["status"] == "ZERO_SALES"


def test_invalid_age():
    groups = [{
        "is_active": True,
        "duration": "full_day",
        "skiers": [{"age": 0}],
    }]
    result = process_resort_bookings(groups, 15.0)
    assert result["status"] == "ZERO_SALES"


def test_blackout_override():
    groups = [{
        "is_active": True,
        "duration": "full_day",
        "skiers": [{"age": 30, "blackout_override": True}],
    }]
    result = process_resort_bookings(groups, 15.0)
    assert result["total_revenue"] == 40.0


def test_half_day_blackout():
    groups = [{
        "is_active": True,
        "duration": "half_day",
        "skiers": [
            {"age": 30, "blackout_override": True},
            {"age": 30},
        ],
    }]
    result = process_resort_bookings(groups, 15.0)
    assert result["total_revenue"] == 0.0


def test_audit_review():
    groups = [{
        "is_active": True,
        "duration": "full_day",
        "skiers": [{"age": 0} for _ in range(5)],
    }]
    result = process_resort_bookings(groups, 15.0)
    assert result["status"] == "AUDIT_REVIEW"


def test_invalid_groups():
    with pytest.raises(ValueError):
        process_resort_bookings("invalid", 15.0)


def test_negative_facility_fee():
    with pytest.raises(ValueError):
        process_resort_bookings([], -1)


def test_no_wind_data():
    assert check_chairlift_anemometer([]) == "NO_DATA"


def test_safe_wind():
    assert check_chairlift_anemometer([[20, 30, 45]]) == "SAFE_OPERATION"


def test_high_wind():
    assert check_chairlift_anemometer([[46, 47]]) == "SUSPEND_LIFT"
